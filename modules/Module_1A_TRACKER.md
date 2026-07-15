# Module 1A: Chronic SCI Lesion Architecture — Corpus Building Tracker

## Overview

This tracker monitors the systematic population of mSCIdblit with experiment-level evidence describing the gross anatomical architecture of chronic spinal cord injury lesions.

**Target Corpus**: 30–60 primary research papers + 8–15 reviews + human pathology papers

---

## Search Strategy Log

### Search Query Template

| Search ID | Query | Database | Date Executed | Papers Retrieved | Papers Already In Corpus | New Papers | Status | Notes |
|-----------|-------|----------|---|---|---|---|---|---|
| S001 | `chronic spinal cord injury lesion architecture` | PubMed | 2026-07-15 | 9 | 0 | 9 | COMPLETE | Initial broad search; all PubMed hits retained for screening |
| S002 | `thoracic contusion chronic histopathology` | PubMed | 2026-07-15 | 75 | 0 | 75 | COMPLETE | Species: mouse, rat, guinea pig; top 25 PMID window retained |
| S003 | `glial scar anatomy spinal cord injury` | PubMed | 2026-07-15 | 1138 | 0 | 1138 | COMPLETE | Focus: astrocytic border; top 25 PMID window retained |
| S004 | `fibrotic scar spinal cord injury chronic` | PubMed | 2026-07-15 | 28 | 0 | 28 | COMPLETE | Focus: fibrotic compartment; top 25 PMID window retained |
| S005 | `pericyte spinal cord scar fibrosis` | PubMed | 2026-07-15 | 28 | 0 | 28 | COMPLETE | Focus: mesenchymal border; top 25 PMID window retained |
| S006 | `astrocytic border spinal cord injury` | PubMed | 2026-07-15 | 90 | 0 | 90 | COMPLETE | Focus: border architecture; top 25 PMID window retained |
| S007 | `human chronic spinal cord injury pathology` | PubMed | 2026-07-15 | 1457 | 0 | 1457 | COMPLETE | Human tissue data; top 25 PMID window retained |
| S008 | `MRI chronic spinal cord injury lesion volume` | PubMed | 2026-07-15 | 23 | 0 | 23 | COMPLETE | Imaging correlates; all PubMed hits retained for screening |
| S009 | `scar resection spinal cord injury surgery` | PubMed | 2026-07-15 | 26 | 0 | 26 | COMPLETE | Surgical intervention; top 25 PMID window retained |
| S010 | `cavity formation spinal cord injury chronic` | PubMed | 2026-07-15 | 74 | 0 | 74 | COMPLETE | Cystic cavitation; top 25 PMID window retained |
| S011 | `white matter sparing spinal cord injury` | PubMed | 2026-07-15 | 365 | 0 | 365 | COMPLETE | Spared tissue; top 25 PMID window retained |
| S012 | `gray matter loss spinal cord injury chronic` | PubMed | 2026-07-15 | 44 | 0 | 44 | COMPLETE | Gray matter compartment; top 25 PMID window retained |
| S013 | Citation forward/backward from anchor papers | — | — | — | — | — | PENDING | See Anchor Paper List |

---

### Search Saturation Assessment

| Phase | Date | Cumulative Papers | New Unique Papers This Phase | Repeat Rate (%) | Saturation Indicator |
|-------|------|---|---|---|---|
| Phase 1 (S001–S004) | 2026-07-15 | 84 screened PMIDs | 84 | 0.0 | Broad anatomy/scar searches still discovery-rich |
| Phase 2 (S005–S009) | 2026-07-15 | 200 screened PMIDs | 116 | 5.7 | Pericyte, human, MRI, and scar-resection searches added many new candidates |
| Phase 3 (S010–S012) | 2026-07-15 | 266 screened PMIDs | 66 | 12.0 | Cavitation/white-gray matter searches remain below saturation threshold |
| Phase 4 (Citation chains) | — | — | — | — | — |
| Phase 5 (Review mining) | — | — | — | — | — |

**Saturation Threshold**: When >70% of retrieved papers are already in corpus across 2 consecutive searches, document and move to consensus phase.

---

## Paper Inventory by Lesion Compartment

### 1. Lesion Core Architecture

| Paper ID | First Author | Year | Title | Species | Injury Model | Status | Notes |
|----------|--------------|------|-------|---------|--------------|--------|-------|
| M1A-P001 | Zhang SX | 2011 | Histological repair of damaged spinal cord tissue from chronic contusion injury of rat: a LM observation | Rat | Chronic contusion | QUEUED PASS -1 | Candidate for lesion core/cavity histology |
| M1A-P002 | Hu R | 2010 | Glial scar and neuroregeneration: histological, functional, and magnetic resonance imaging analysis in chronic spinal cord injury | Rat | Chronic SCI | QUEUED PASS -1 | Candidate for lesion architecture plus MRI |

### 2. Astrocytic Border

| Paper ID | First Author | Year | Title | Species | Injury Model | Status | Notes |
|----------|--------------|------|-------|---------|--------------|--------|-------|
| M1A-P003 | Tamaru T | 2023 | Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury | Mouse/rat | SCI | QUEUED PASS -1 | Anchor for chronic astrocytic scar persistence |
| M1A-P004 | Gong L | 2023 | Spatiotemporal dynamics of the molecular expression pattern and intercellular interactions in the glial scar response to spinal cord injury | Mouse | SCI | QUEUED PASS -1 | Candidate for border cell interactions |
| M1A-P005 | Rasouli A | 2009 | Resection of glial scar following spinal cord injury | Rat | SCI with scar resection | QUEUED PASS -1 | Also relevant to scar resection anatomy |

### 3. Reactive Surrounding Neural Tissue

| Paper ID | First Author | Year | Title | Species | Injury Model | Status | Notes |
|----------|--------------|------|-------|---------|--------------|--------|-------|
| M1A-P006 | Li Y | 2020 | Delayed microglial depletion after spinal cord injury reduces chronic inflammation and neurodegeneration in the brain and improves neurological recovery in male mice | Mouse | SCI | QUEUED PASS -1 | Candidate for chronic inflammatory/neurodegenerative tissue context |

### 4. Fibrotic Scar

| Paper ID | First Author | Year | Title | Species | Injury Model | Status | Notes |
|----------|--------------|------|-------|---------|--------------|--------|-------|
| M1A-P007 | Cooper JG | 2018 | Fibronectin EDA forms the chronic fibrotic scar after contusive spinal cord injury | Mouse | Contusion | PASS 3 COMPLETE | Anchor for chronic fibrotic compartment |
| M1A-P008 | Soderblom C | 2013 | Perivascular fibroblasts form the fibrotic scar after contusive spinal cord injury | Mouse | Contusion | QUEUED PASS -1 | Candidate for fibroblast source/cell identity |
| M1A-P009 | Dias DO | 2018 | Reducing pericyte-derived scarring promotes recovery after spinal cord injury | Mouse | SCI | QUEUED PASS -1 | Candidate for pericyte-derived scar |
| M1A-P010 | Yokota K | 2017 | Periostin promotes scar formation through the interaction between pericytes and infiltrating monocytes/macrophages after spinal cord injury | Mouse | SCI | QUEUED PASS -1 | Candidate for pericyte/macrophage scar mechanism |

### 5. Cystic Cavitation

| Paper ID | First Author | Year | Title | Species | Injury Model | Status | Notes |
|----------|--------------|------|-------|---------|--------------|--------|-------|
| M1A-P011 | Radojicic M | 2005 | Septations in chronic spinal cord injury cavities contain axons | Rat | Chronic SCI cavity | QUEUED PASS -1 | Candidate for cavity internal architecture |
| M1A-P012 | Wang N | 2018 | Collagen scaffold combined with human umbilical cord-derived mesenchymal stem cells promote functional recovery after scar resection in rats with chronic spinal cord injury | Rat | Chronic SCI with scar resection | QUEUED PASS -1 | Candidate for cavity/resection anatomy |

### 6. White Matter Sparing

| Paper ID | First Author | Year | Title | Species | Injury Model | Status | Notes |
|----------|--------------|------|-------|---------|--------------|--------|-------|
| M1A-P013 | Rosenberg LJ | 2005 | Chronic alterations in the cellular composition of spinal cord white matter following contusion injury | Rat | Contusion | QUEUED PASS -1 | Anchor for chronic white matter pathology |
| M1A-P014 | McCallum S | 2026 | Lesion-remote astrocytes govern microglia-mediated white matter repair | Mouse | SCI | QUEUED PASS -1 | Candidate for lesion-remote spared white matter |

### 7. Gray Matter Loss

| Paper ID | First Author | Year | Title | Species | Injury Model | Status | Notes |
|----------|--------------|------|-------|---------|--------------|--------|-------|
| M1A-P015 | Collazos-Castro JE | 2005 | Motoneuron loss associated with chronic locomotion impairments after spinal cord contusion in the rat | Rat | Contusion | QUEUED PASS -1 | Candidate for gray matter/motoneuron loss |

### 8. Lesion Geometry

| Paper ID | First Author | Year | Title | Species | Injury Model | Status | Notes |
|----------|--------------|------|-------|---------|--------------|--------|-------|
| M1A-P016 | Emmenegger TM | 2024 | Longitudinal motor system changes from acute to chronic spinal cord injury | Human | SCI | QUEUED PASS -1 | Candidate for longitudinal lesion geometry/imaging context |
| M1A-P017 | Burks JD | 2019 | Imaging characteristics of chronic spinal cord injury identified during screening for a cell transplantation clinical trial | Human | Chronic SCI | QUEUED PASS -1 | Candidate for chronic lesion imaging morphology |

### 9. Human Chronic Pathology

| Paper ID | First Author | Year | Title | Tissue Source | Status | Notes |
|----------|--------------|------|-------|---|--------|-------|
| M1A-P018 | Tuszynski MH | 1999 | Human spinal cord retains substantial structural mass in chronic stages after injury | Human spinal cord | QUEUED PASS -1 | Anchor for human chronic structural preservation |
| M1A-P019 | Grumbles RM | 2017 | Motoneuron death after human spinal cord injury | Human spinal cord | QUEUED PASS -1 | Candidate for human gray matter/motoneuron pathology |
| M1A-P020 | Tator CH | 1997 | Vascular mechanisms in the pathophysiology of human spinal cord injury | Human spinal cord | QUEUED PASS -1 | Candidate for vascular pathology context |

### 10. Species Differences

| Paper ID | First Author | Year | Title | Species Compared | Status | Notes |
|----------|--------------|------|-------|---|--------|-------|
| M1A-P021 | Xue X | 2024 | Heterogeneous fibroblasts contribute to fibrotic scar formation after spinal cord injury in mice and monkeys | Mouse, monkey | QUEUED PASS -1 | Candidate for cross-species fibrotic scar architecture |

### 11. Scar Resection Anatomy

| Paper ID | First Author | Year | Title | Species | Intervention | Status | Notes |
|----------|--------------|------|-------|---------|---|--------|-------|
| M1A-P005 | Rasouli A | 2009 | Resection of glial scar following spinal cord injury | Rat | Scar resection | QUEUED PASS -1 | Resection anatomy anchor |
| M1A-P022 | Xiao Z | 2016 | One-year clinical study of NeuroRegen scaffold implantation following scar resection in complete chronic spinal cord injury patients | Human | Scar resection + scaffold | QUEUED PASS -1 | Candidate for human chronic scar resection |
| M1A-P023 | Estrada V | 2014 | Long-lasting significant functional improvement in chronic severe spinal cord injury following scar resection and polyethylene glycol implantation | Human | Scar resection + PEG | QUEUED PASS -1 | Candidate for surgical anatomy |

### 12. Three-Dimensional Lesion Organization

| Paper ID | First Author | Year | Title | Species | Imaging/Reconstruction Method | Status | Notes |
|----------|--------------|------|-------|---------|---|--------|-------|
| M1A-P024 | Scholtes F | 2011 | Post-mortem assessment of rat spinal cord injury and white matter sparing using inversion recovery-supported proton density magnetic resonance imaging | Rat | MRI plus post-mortem tissue | QUEUED PASS -1 | Candidate for 3D/imaging-to-histology linkage |
| M1A-P025 | Zhao C | 2018 | Diffusion tensor imaging of spinal cord parenchyma lesion in rat with chronic spinal cord injury | Rat | DTI | QUEUED PASS -1 | Candidate for chronic parenchymal lesion geometry |

---

## Anchor Paper List

**Anchor papers** are foundational publications that define modern understanding of chronic SCI lesion architecture. Prioritize for extraction.

| Paper ID | First Author | Year | Title | Lesion Compartment Focus | Extraction Status |
|----------|--------------|------|-------|---|---|
| ANCHOR001 | Rosenberg LJ | 2005 | Chronic alterations in the cellular composition of spinal cord white matter following contusion injury | White matter sparing / chronic contusion histopathology | QUEUED PASS -1 |
| ANCHOR002 | Cooper JG | 2018 | Fibronectin EDA forms the chronic fibrotic scar after contusive spinal cord injury | Chronic fibrotic scar | QUEUED PASS -1 |
| ANCHOR003 | Tamaru T | 2023 | Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury | Astrocytic scar persistence | QUEUED PASS -1 |
| ANCHOR004 | Tuszynski MH | 1999 | Human spinal cord retains substantial structural mass in chronic stages after injury | Human chronic pathology | QUEUED PASS -1 |
| ANCHOR005 | Rasouli A | 2009 | Resection of glial scar following spinal cord injury | Scar resection anatomy | QUEUED PASS -1 |

**Instructions for Anchor Paper Identification**:
1. Search: "chronic spinal cord injury lesion architecture" + "anatomy" + "histopathology"
2. Look for papers with 500+ citations
3. Check if cited in multiple major reviews
4. Verify: Contains detailed anatomical characterization AND quantitative data

---

## Extraction Pipeline Progress

### Pass -1: Full Text Verification

| Paper ID | Full Text Available | Figures Available | Figure Legends Available | Methods Accessible | Results Section Present | Status |
|----------|---|---|---|---|---|---|
| M1A-P007 | YES | YES | YES | YES | YES | PASS |

**BLOCKED papers**: Log separately for future retrieval attempts

---

### Pass 0: Paper Registration

| Paper ID | Title | Authors | Year | Journal | Volume | Issue | Pages | DOI | PMID | URL | Registered |
|----------|-------|---------|------|---------|--------|-------|-------|-----|------|-----|---|
| M1A-P007 | Fibronectin EDA forms the chronic fibrotic scar after contusive spinal cord injury | John G. Cooper; Su Ji Jeong; Tammy L. McGuire; Sripadh Sharma; Wenxia Wang; Swati Bhattacharyya; John Varga; John A. Kessler | 2018 | Neurobiology of Disease | 116 | — | 60-68 | 10.1016/j.nbd.2018.04.014 | 29705186 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5995671/ | YES |

---

### Pass 1: Research Questions Identified

| Paper ID | Question ID | Research Question Text | Hypothesis Direction | Keywords | Question Extracted |
|----------|-------------|---|---|---|---|
| M1A-P007 | M1A-P007-RQ001 | Does eliminating the fibronectin Extra Domain A isoform reduce fibrotic scarring and improve recovery after contusive spinal cord injury in mice? | positive | FnEDA; fibronectin matrix; fibrotic scar; contusion SCI; chronic lesion | YES |

---

### Pass 2: Experimental Paradigms Identified

| Paper ID | Paradigm ID | Paradigm Name | Description | Methodology | Paradigm Extracted |
|----------|-------------|---|---|---|---|
| M1A-P007 | M1A-P007-P001 | FnEDA-null versus wildtype mouse contusion SCI | Compare FnEDA-null mice with littermate wildtype controls after T11 contusion SCI, measuring fibronectin isoforms, lesion/fibrotic scar anatomy, fibronectin matrix stability, axonal density, and locomotor recovery across acute, subacute, and chronic time points. | Infinite Horizons impactor, 70 kdyn force, 60 s dwell; 8-10 week male/female FnEDA-null and littermate wildtype mice for genotype comparisons; 8 week female C57BL/6 mice for FnEDA mRNA/protein time course; IHC, western blot, qPCR, DOC digestion, BMS/mBBB scoring. | YES |

---

### Pass 3: Experiments Extracted

| Paper ID | Experiment ID | Figure Ref | Species | Strain | Sex | Injury Model | Injury Device | Injury Severity | Vertebral Level | Chronicity (DPI) | Control Type | Intervention Type | Methods Summary | Experiment Extracted |
|----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M1A-P007 | M1A-P007-E001 | Fig 1A-G | Mus musculus | C57BL/6 | Female | Contusion SCI | Infinite Horizons IH-0400 | 70 kdyn, 60 s dwell | T11 | uninjured, 3, 7, 21, 90 DPI / 13 weeks | Uninjured spinal cord | Injury time course | Lesion tissue harvested for qPCR and western blot quantification of FnEDA/FnEDB/total fibronectin. | YES |
| M1A-P007 | M1A-P007-E002 | Fig 2A-I | Mus musculus | FnEDA-null and littermate WT | Male and female | Contusion SCI | Infinite Horizons IH-0400 | 70 kdyn, 60 s dwell | T11 | 7, 21, 90 DPI | Wildtype littermate injured mice | FnEDA domain deletion | Western blot and 20 um mid-sagittal IHC sections quantified for total fibronectin, GFAP-defined lesion core/rim, lesion area, and GFAP response. | YES |
| M1A-P007 | M1A-P007-E003 | Fig 3A-F | Mus musculus | FnEDA-null and littermate WT | Male and female | Contusion SCI | Infinite Horizons IH-0400 | 70 kdyn, 60 s dwell | T11 | 7, 21, 90 DPI | Wildtype littermate injured mice | FnEDA domain deletion | DOC/SDS biochemical fractionation separated soluble fibronectin from insoluble matrix-assembled fibronectin in 4 mm lesion-containing cord tissue. | YES |
| M1A-P007 | M1A-P007-E004 | Fig 4A-C | Mus musculus | FnEDA-null and littermate WT | Male and female | Contusion SCI | Infinite Horizons IH-0400 | 70 kdyn, 60 s dwell | T11 | 90 DPI | Wildtype littermate injured mice | FnEDA domain deletion | 20 um mid-sagittal sections stained for SMI-312; axonal staining intensity quantified across distances from lesion center and normalized to 2 mm rostral tissue. | YES |
| M1A-P007 | M1A-P007-E005 | Fig 5A-D | Mus musculus | FnEDA-null and littermate WT | Male and female | Contusion SCI | Infinite Horizons IH-0400 | 70 kdyn, 60 s dwell | T11 | weekly after SCI through final behavioral week | Wildtype littermate injured mice | FnEDA domain deletion | Blinded open-field locomotor scoring using BMS and modified BBB; mice with combined 24 h BMS >1 excluded as improperly injured. | YES |

---

### Pass 4: Observations Extracted

| Paper ID | Observation ID | Experiment ID | Figure Ref | Evidence Type | Observation Value | Unit | Quantitative | Statistics Reported | Observation Extracted |
|----------|---|---|---|---|---|---|---|---|---|
| — | O001 | E001 | Fig 2A | Histological measurement | — | — | YES/NO | YES/NO | YES/NO |

---

### Pass 5: Author Claims Extracted

| Paper ID | Claim ID | Claim Text | Claim Type | Confidence Level | Supporting Observation IDs | Claim Extracted |
|----------|----------|---|---|---|---|---|
| — | C001 | — | interpretation/conclusion/speculation | high/medium/low | O001, O002 | YES/NO |

---

## Overall Extraction Status

| Pass | Total Papers | Completed | In Progress | Blocked | Pending | Completion % |
|------|---|---|---|---|---|---|
| -1 (Verify) | 27 | 1 | 0 | 0 | 26 | 4% |
| 0 (Register) | 27 | 1 | 0 | 0 | 26 | 4% |
| 1 (Questions) | 27 | 1 | 0 | 0 | 26 | 4% |
| 2 (Paradigms) | 27 | 1 | 0 | 0 | 26 | 4% |
| 3 (Experiments) | 27 | 1 paper / 5 experiments | 0 | 0 | 26 papers | 4% papers |
| 4 (Observations) | 27 | 0 | 0 | 0 | 27 | 0% |
| 5 (Claims) | 27 | 0 | 0 | 0 | 27 | 0% |

---

## Contradictions & Conflicts Identified

Log papers that report conflicting findings on the same anatomical compartment or measurement.

| Topic | Paper 1 ID | Finding 1 | Paper 2 ID | Finding 2 | Conflict Type | Resolution Status |
|-------|---|---|---|---|---|---|
| Example: Cavity volume at 8 weeks | P001 | "30% volume" | P002 | "15% volume" | Quantitative divergence | UNRESOLVED |
| — | — | — | — | — | — | — |

---

## Controlled Vocabulary Updates Required

### Species (ControlledVocabulary_Species)

| Species Name | NCBI Taxonomy ID | Represented in Corpus | Status |
|---|---|---|---|
| Mus musculus | 10090 | YES | REPRESENTED |
| Rattus norvegicus | 10116 | — | — |
| Cavia porcellus | 10141 | — | — |
| Canis lupus familiaris | 9615 | — | — |
| Sus scrofa | 9823 | — | — |
| Homo sapiens | 9606 | — | — |

### Injury Models (ControlledVocabulary_InjuryModel)

| Model Name | Anatomical Target | Species | Represented in Corpus | Status |
|---|---|---|---|---|
| Thoracic contusion | T9–T10 | Mouse, rat | YES | REPRESENTED |
| Dorsal hemisection | Thoracic | Mouse, rat | — | — |
| Lateral hemisection | Thoracic | Mouse, rat | — | — |
| Complete transection | Thoracic | Mouse, rat | — | — |
| Compression | T10 | Mouse, rat | — | — |
| Human traumatic lesion | Variable | Human | — | — |

### Lesion Compartments (ControlledVocabulary_LesionCompartment)

| Compartment Name | Description | Primary/Secondary | Status |
|---|---|---|---|
| Lesion core | Central zone of tissue destruction | PRIMARY | — |
| Fibrotic core | Fibroblast-rich central region | PRIMARY | REPRESENTED |
| Astrocytic border | Glial scar boundary | PRIMARY | REPRESENTED |
| Reactive neural tissue | Altered but intact tissue surrounding lesion | PRIMARY | — |
| Spared white matter | Preserved WM tracts at periphery | PRIMARY | — |
| Spared gray matter | Preserved GM at lesion periphery | PRIMARY | — |
| Cystic cavity | Fluid-filled void within lesion | PRIMARY | — |
| Pericyte border | Mesenchymal cell zone | SECONDARY | — |
| Meningeal fibrosis | Dural involvement | SECONDARY | — |
| Remote spinal cord | Tissue rostral/caudal to lesion | SECONDARY | — |

### Evidence Types (ControlledVocabulary_EvidenceType)

| Evidence Type | Description | Represented in Corpus |
|---|---|---|
| Histological measurement | Quantitative measurement from tissue sections | YES |
| Immunohistochemistry | Labeled cellular/molecular identification | YES |
| Electron microscopy | Ultrastructural observation | — |
| MRI measurement | Imaging-based quantification | — |
| CT imaging | Imaging-based quantification | — |
| Two-photon imaging | Live tissue visualization | — |
| Confocal microscopy | High-resolution cellular imaging | — |
| Serial section reconstruction | 3D computational reconstruction | — |
| Qualitative histology | Descriptive anatomical characterization | — |
| Human tissue examination | Autopsy or surgical specimen | — |

### Assays (ControlledVocabulary_Assay)

| Assay Name | Assay Type | Measured Compartment | Represented in Corpus |
|---|---|---|---|
| Lesion area measurement | Histological | Lesion core | YES |
| Cavity volume quantification | Histological | Cystic cavity | — |
| GFAP immunostaining | Immunohistochemistry | Astrocytic border | YES |
| Collagen staining (Masson's trichrome) | Histological | Fibrotic scar | — |
| White matter sparing quantification | Histological | Spared WM | — |
| Gray matter loss quantification | Histological | Gray matter | — |
| MRI T2-weighted lesion volume | MRI | Overall lesion | — |
| Voxel-based morphometry | MRI analysis | Tissue loss | — |
| Eriochrome cyanine stain | Histological | Myelinated axons | — |
| Cellularity assessment | Immunohistochemistry | Cell density | — |

### Outcome Types (ControlledVocabulary_OutcomeType)

| Outcome Type | Measurement Unit | Relevant Compartment | Represented in Corpus |
|---|---|---|---|
| Lesion area | mm² | Lesion core | YES |
| Lesion length | mm | Lesion core | — |
| Lesion volume | mm³ | Lesion core | — |
| Cavity volume | mm³ or % of lesion | Cystic cavity | — |
| White matter sparing | mm² or % | Spared WM | — |
| Gray matter loss | mm² or % | Gray matter | — |
| Lesion width | mm | Lesion geometry | — |
| Rostral extension | mm | Lesion extent | — |
| Caudal extension | mm | Lesion extent | — |

---

## Reference Queue

Papers identified but not yet processed:

| DOI / PMID | First Author | Year | Title | Reason Identified | Date Added | Status |
|---|---|---|---|---|---|---|
| 10.1002/glia.20096 | Rosenberg LJ | 2005 | Chronic alterations in the cellular composition of spinal cord white matter following contusion injury | S002; anchor for chronic contusion white matter pathology | 2026-07-15 | QUEUED PASS -1 |
| 10.1016/j.nbd.2018.04.014 | Cooper JG | 2018 | Fibronectin EDA forms the chronic fibrotic scar after contusive spinal cord injury | S004; anchor for chronic fibrotic scar | 2026-07-15 | PASS 3 COMPLETE |
| 10.1016/j.expneurol.2022.114264 | Tamaru T | 2023 | Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury | S003; anchor for chronic astrocytic scar | 2026-07-15 | QUEUED PASS -1 |
| PMID:10391368 | Tuszynski MH | 1999 | Human spinal cord retains substantial structural mass in chronic stages after injury | S007; anchor for human chronic pathology | 2026-07-15 | QUEUED PASS -1 |
| 10.1002/jor.20793 | Rasouli A | 2009 | Resection of glial scar following spinal cord injury | S003/S009; anchor for scar resection anatomy | 2026-07-15 | QUEUED PASS -1 |
| 10.14670/HH-26.45 | Zhang SX | 2011 | Histological repair of damaged spinal cord tissue from chronic contusion injury of rat: a LM observation | S004/S010; lesion core and cavity histology | 2026-07-15 | QUEUED PASS -1 |
| 10.3171/2010.3.SPINE09190 | Hu R | 2010 | Glial scar and neuroregeneration: histological, functional, and magnetic resonance imaging analysis in chronic spinal cord injury | S010; histology plus MRI candidate | 2026-07-15 | QUEUED PASS -1 |
| 10.1523/JNEUROSCI.2524-13.2013 | Soderblom C | 2013 | Perivascular fibroblasts form the fibrotic scar after contusive spinal cord injury | S005; fibrotic scar cell-source candidate | 2026-07-15 | QUEUED PASS -1 |
| 10.1016/j.cell.2018.02.004 | Dias DO | 2018 | Reducing pericyte-derived scarring promotes recovery after spinal cord injury | S005; pericyte-derived scar candidate | 2026-07-15 | QUEUED PASS -1 |
| 10.1016/j.ajpath.2016.11.010 | Yokota K | 2017 | Periostin promotes scar formation through the interaction between pericytes and infiltrating monocytes/macrophages after spinal cord injury | S005; pericyte/macrophage scar mechanism | 2026-07-15 | QUEUED PASS -1 |
| 10.1016/j.expneurol.2005.08.009 | Radojicic M | 2005 | Septations in chronic spinal cord injury cavities contain axons | S010; cavity internal architecture | 2026-07-15 | QUEUED PASS -1 |
| 10.1002/term.2450 | Wang N | 2018 | Collagen scaffold combined with human umbilical cord-derived mesenchymal stem cells promote functional recovery after scar resection in rats with chronic spinal cord injury | S009/S010; chronic scar resection/cavity anatomy | 2026-07-15 | QUEUED PASS -1 |
| 10.1089/neu.2015.4374 | Grumbles RM | 2017 | Motoneuron death after human spinal cord injury | S002/S007; human gray matter pathology | 2026-07-15 | QUEUED PASS -1 |
| 10.3171/jns.1997.86.3.0483 | Tator CH | 1997 | Vascular mechanisms in the pathophysiology of human spinal cord injury | S012; human vascular pathology context | 2026-07-15 | QUEUED PASS -1 |
| 10.1089/neu.2005.22.544 | Collazos-Castro JE | 2005 | Motoneuron loss associated with chronic locomotion impairments after spinal cord contusion in the rat | S012; gray matter/motoneuron loss | 2026-07-15 | QUEUED PASS -1 |
| 10.1038/s41586-025-09887-y | McCallum S | 2026 | Lesion-remote astrocytes govern microglia-mediated white matter repair | S011; lesion-remote white matter repair | 2026-07-15 | QUEUED PASS -1 |
| 10.1007/s12264-022-00897-8 | Gong L | 2023 | Spatiotemporal dynamics of the molecular expression pattern and intercellular interactions in the glial scar response to spinal cord injury | S003; glial scar spatiotemporal organization | 2026-07-15 | QUEUED PASS -1 |
| 10.1096/fj.202200463R | Hou J | 2022 | Heterogeneity analysis of astrocytes following spinal cord injury at single-cell resolution | S003; astrocyte heterogeneity candidate | 2026-07-15 | QUEUED PASS -1 |
| 10.1038/s41467-024-50564-x | Xue X | 2024 | Heterogeneous fibroblasts contribute to fibrotic scar formation after spinal cord injury in mice and monkeys | S005; cross-species fibrotic scar candidate | 2026-07-15 | QUEUED PASS -1 |
| 10.1016/j.jmbbm.2020.103953 | Baumann HJ | 2020 | Softening of the chronic hemi-section spinal cord injury scar parallels dysregulation of cellular and extracellular matrix content | S004; chronic scar mechanics/ECM | 2026-07-15 | QUEUED PASS -1 |
| 10.1089/neu.2019.6540 | Cooper JG | 2020 | Spinal cord injury results in chronic mechanical stiffening | S004; chronic scar/tissue stiffness | 2026-07-15 | QUEUED PASS -1 |
| 10.1038/s41393-022-00770-5 | Faro SH | 2022 | DTI of chronic spinal cord injury in children without MRI abnormalities and with pathology on MRI and comparison to severity of motor impairment | S007/S008; human imaging pathology | 2026-07-15 | QUEUED PASS -1 |
| 10.3171/2018.12.FOCUS18593 | Burks JD | 2019 | Imaging characteristics of chronic spinal cord injury identified during screening for a cell transplantation clinical trial | S008; chronic lesion imaging morphology | 2026-07-15 | QUEUED PASS -1 |
| 10.1007/s11427-016-5080-z | Xiao Z | 2016 | One-year clinical study of NeuroRegen scaffold implantation following scar resection in complete chronic spinal cord injury patients | S009; human scar resection candidate | 2026-07-15 | QUEUED PASS -1 |
| 10.1016/j.nbd.2014.03.018 | Estrada V | 2014 | Long-lasting significant functional improvement in chronic severe spinal cord injury following scar resection and polyethylene glycol implantation | S009; chronic scar resection candidate | 2026-07-15 | QUEUED PASS -1 |
| 10.1038/sc.2010.129 | Scholtes F | 2011 | Post-mortem assessment of rat spinal cord injury and white matter sparing using inversion recovery-supported proton density magnetic resonance imaging | S008/S011; MRI-to-histology white matter sparing | 2026-07-15 | QUEUED PASS -1 |
| 10.1016/j.mri.2017.11.009 | Zhao C | 2018 | Diffusion tensor imaging of spinal cord parenchyma lesion in rat with chronic spinal cord injury | S010; chronic parenchymal lesion DTI | 2026-07-15 | QUEUED PASS -1 |

---

## Module 1A Completion Checklist

- [ ] **Search Saturation Documented**: All 13 search queries completed; >70% repeat rate across final 2 phases; forward/backward citation chains exhausted
- [ ] **Anchor Papers Extracted**: ≥3 foundational papers fully processed through all 5 passes
- [ ] **Lesion Compartments Represented**: All 12 anatomical topics have ≥3 primary papers each
- [ ] **Human Pathology Included**: ≥2 human autopsy/surgical pathology papers extracted
- [ ] **Species Representation**: Mouse, rat, and large-animal studies represented
- [ ] **Contradictions Identified & Logged**: Conflicting findings documented in Contradictions table
- [ ] **Controlled Vocabulary Finalized**: All reference tables populated (Species, Injury Models, Lesion Compartments, Evidence Types, Assays, Outcome Types)
- [ ] **Corpus Size Achieved**: ≥30 primary research papers + ≥8 review articles
- [ ] **Database Population Complete**: All 5 passes completed for all papers in corpus
  - [ ] Pass 0: Paper table populated
  - [ ] Pass 1: ResearchQuestion table populated
  - [ ] Pass 2: ExperimentalParadigm table populated
  - [ ] Pass 3: Experiment table populated
  - [ ] Pass 4: Observation table populated
  - [ ] Pass 5: AuthorClaim table populated
- [ ] **EvidenceLink Complete**: All author claims linked to supporting observations
- [ ] **Search Log Finalized**: All search strategies documented with retrieval counts
- [ ] **Contradiction Map Complete**: All conflicting findings identified
- [ ] **No Synthesis Performed**: Zero consensus statements generated; zero hypotheses generated

---

## Sign-Off

**Module 1A Curator**: ___________________  
**Date Initiated**: 2026-07-15
**Date Completed**: ___________________  
**Total Papers Extracted**: 1 through Pass 3
**Total Experiments**: 5
**Total Observations**: _____  
**Total Claims**: _____  
**Contradictions Found**: _____  

**Notes**:

---

**Next Phase**: Module 1B (Consensus Generation) — begins only after all completion criteria met.
