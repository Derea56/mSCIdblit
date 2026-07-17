# Module 6B: Human Chronic SCI Pathology and Translational Imaging - Evidence Consolidation and Consensus Readiness

## Overview

This tracker records the post-saturation phase for Module 6A. Module 6B converts the frozen human pathology and translational imaging corpus into atomic observations, author claims, evidence links, boundary conditions, and consensus-ready profiles.

**Boundary condition**: Module 6B may prepare consensus profiles, but project-level `Consensus` records should only be created after observations and author claims are linked to source evidence. Full SQL materialization should wait until first-pass evidence links are complete and low-confidence abstract/source-page rows are upgraded where needed.

**Input corpus**: Module 6A saturation corpus, 36 paper/cohort rows plus 8 review/map anchors.

**Module 6 first-pass curation freeze**: 2026-07-16. Status: Module 6A corpus is saturated/frozen first pass; Module 6B evidence consolidation is consensus-ready first pass.

---

## Module 6B Goals

| Goal ID | Goal | Output Table / Artifact | Status |
|---|---|---|---|
| M6B-G001 | Extract atomic empirical observations from Module 6A cohort rows | Observation | COMPLETE FIRST PASS |
| M6B-G002 | Extract author interpretations separately from observations | AuthorClaim | COMPLETE FIRST PASS |
| M6B-G003 | Link each claim to supporting or contextual observations | EvidenceLink | COMPLETE FIRST PASS |
| M6B-G004 | Cluster evidence by human pathology or imaging axis | Consensus-ready evidence profiles | COMPLETE FIRST PASS |
| M6B-G005 | Mark modality, timing, anatomy, endpoint, and confidence boundaries | Boundary / contradiction map | COMPLETE FIRST PASS |
| M6B-G006 | Draft consensus statements only after linked evidence exists | Consensus | CONSENSUS-READY FIRST PASS |

---

## Evidence Topic Map

| Topic ID | Consensus-Ready Topic | Primary Papers | Evidence Need | Status |
|---|---|---|---|---|
| M6B-T001 | Chronic human lesion architecture includes preserved tissue, focal cystic loss, scar-resection anatomy, and syrinx/cyst complications | M6A-P001, P003, P018-P019 | Preserve chronicity, surgical anatomy, and cyst/syrinx boundaries | CONSENSUS-READY FIRST PASS |
| M6B-T002 | Human autopsy/pathology shows ventral-root, myelin, vascular, and cystic compartments not captured by MRI alone | M6A-P002, P017-P019 | Separate tissue pathology from imaging biomarkers | CONSENSUS-READY FIRST PASS |
| M6B-T003 | DTI and tract-specific diffusion can reveal injury beyond conventional MRI and correlate with impairment | M6A-P004, P006-P007, P022 | Preserve pediatric/adult, complete/incomplete, and tract-specific boundaries | CONSENSUS-READY FIRST PASS |
| M6B-T004 | Tissue bridges and lesion geometry are prognostic human MRI biomarkers | M6A-P005, P008-P009, P035 | Preserve level, etiology, timing, and endpoint boundaries | CONSENSUS-READY FIRST PASS |
| M6B-T005 | qMRI, MRS, cord atrophy, and remote degeneration track chronic system-level pathology | M6A-P010-P012, P016, P021, P027-P032 | Separate spinal, supraspinal, metabolic, microstructural, and clinical endpoints | CONSENSUS-READY FIRST PASS |
| M6B-T006 | fMRI and cortical reorganization evidence supports remote plasticity but is indirect for lesion-bed anatomy | M6A-P013-P015, P023-P026 | Preserve lesion/tract linkage before using in consensus | CONSENSUS-READY FIRST PASS |
| M6B-T007 | Trial screening and surgical translation evidence supports stratification and feasibility rather than repair efficacy by itself | M6A-P003, P020, P029-P036 | Separate screening, review-map, and direct cohort evidence | CONSENSUS-READY FIRST PASS |
| M6B-T008 | Module 6 synthesis must remain modality-specific and confidence-labeled | M6A-P001-P036, M6A-R001-R008 | Preserve abstract/source-page limits and human-to-animal translation boundaries | CONSENSUS-READY FIRST PASS |

---

## Pass 4A: Atomic Observations Extracted

| Observation ID | Topic ID | Paper ID | Experiment ID | Figure Ref | Evidence Type | Outcome Type | Observation Value | Normalized Value | Unit | Quantitative | Statistics Reported | Source Section | Extraction Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M6B-O001 | M6B-T001 | M6A-P001 | M6A-P001-E001 | Fig 1; Table 1 | Chronic MRI stereology | Lesion architecture | Focal cystic atrophy was largely restricted to the impact site, with substantial adjacent rostral/caudal cord mass preserved except in late syrinx cases. | chronic SCI can preserve adjacent cord mass despite focal cystic loss | cord area/anatomy | YES | source/full-text carried | M1A carried | high | Human structural preservation anchor. |
| M6B-O002 | M6B-T002 | M6A-P002 | M6A-P002-E001 | Fig 1-Fig 5 | Ventral-root pathology | Axon and myelin pathology | Human SCI caused large-diameter ventral-root axon loss at/near lesion levels and thin myelin in surviving large fibers. | chronic SCI includes ventral-root axon loss and thin-myelin pathology | axon count/myelin | YES | source/full-text carried | M1A carried | high | Tissue pathology not captured by MRI alone. |
| M6B-O003 | M6B-T001 | M6A-P003 | M6A-P003-E001 | Clinical source | Surgical anatomy/trial | Scar resection and implantation | Five patients underwent MRI/electrophysiology-guided chronic scar resection and scaffold-cell implantation. | chronic scar-resection anatomy can be mapped for human scaffold implantation | feasibility/anatomy | YES | source-page level | Source page | high | Human reconstructive anatomy precedent. |
| M6B-O004 | M6B-T003 | M6A-P004 | M6A-P004-E001 | Abstract/source | Pediatric DTI | MRI-normal cord abnormality | Pediatric SCI groups showed abnormal FA/RD in adjacent MRI-normal-appearing cord segments, with FA patterns related to AIS severity. | DTI detects pediatric SCI abnormalities beyond conventional MRI | FA/RD/AIS | YES | abstract-level | Abstract/source page | medium | Pediatric and MRI-normal boundary. |
| M6B-O005 | M6B-T004 | M6A-P005 | M6A-P005-E001 | Abstract/source | Longitudinal qMRI | Lesion and motor-system change | Lesion size contracted early, tissue bridges emerged, remote cord/CST degeneration progressed, and lesion/myelin metrics predicted long-term motor and SCIM recovery. | acute-to-chronic MRI tracks lesion contraction, bridges, degeneration, and recovery prediction | lesion/qMRI/recovery | YES | source-page level | Abstract/source page | high | Strong longitudinal imaging anchor. |
| M6B-O006 | M6B-T003 | M6A-P006 | M6A-P006-E001 | Abstract/PMC | Chronic DTI | Whole-cord diffusion | Chronic SCI showed elevated lesion diffusion, lower FA at lesion, completeness-dependent FA, and altered upper-cervical diffusion. | chronic SCI alters lesion and remote DTI metrics | FA/diffusion | YES | abstract-level | Abstract/PMC | medium | Whole-cord DTI anchor. |
| M6B-O007 | M6B-T003 | M6A-P007 | M6A-P007-E001 | Abstract/PMC | Subject-specific DTI | Impairment association | Subject-specific injury-region DTI metrics were associated with residual motor and sensory impairment. | subject-specific DTI metrics relate to motor/sensory impairment | DTI/ISNCSCI | YES | abstract-level | Abstract/PMC | medium | Tractography-region boundary. |
| M6B-O008 | M6B-T004 | M6A-P008 | M6A-P008-E001 | Abstract/PMC | Thoracic tissue bridge MRI | Recovery prediction | Wider midsagittal tissue bridges at 1 month were associated with better lower-extremity motor and pinprick recovery at 1 year. | thoracic tissue bridges predict lower-extremity motor and pinprick recovery | bridge width/recovery | YES | abstract-level | Abstract/PMC | medium | Thoracic traumatic/ischemic boundary. |
| M6B-O009 | M6B-T004 | M6A-P009 | M6A-P009-E001 | Abstract/PMC | Cervical tissue bridge MRI | Prognosis/stratification | Cervical tissue bridge measures supported recovery-specific stratification and trial prognostication. | cervical tissue bridges support recovery prognostication | bridge metrics/recovery | YES | abstract-level | Abstract/PMC | medium | Multicentre cervical anchor. |
| M6B-O010 | M6B-T005 | M6A-P010 | M6A-P010-E001 | Abstract/source | Cervical cord MRS | Metabolic alteration | Chronic SCI showed lower tNAA/mI and tCho/mI ratios at C2, associated with atrophy, tissue bridge severity, and worse sensory/motor outcomes. | cervical MRS detects supralesional metabolic change linked to impairment | metabolite ratios | YES | abstract-level | Abstract/source page | medium | Metabolic spinal cord biomarker. |
| M6B-O011 | M6B-T005 | M6A-P011 | M6A-P011-E001 | Abstract/PubMed | Longitudinal brain/CST MRI | Remote degeneration | Longitudinal MRI detected degeneration above lesion in cranial CST and sensorimotor cortices with clinical outcome relevance. | SCI causes remote CST and sensorimotor cortical degeneration | volume/morphometry | YES | abstract-level | PubMed | low | Full text upgrade needed. |
| M6B-O012 | M6B-T005 | M6A-P012 | M6A-P012-E001 | Abstract/PubMed | qMRI prediction | Functional recovery | Early rostral cord and brain volume/microstructural changes predicted functional recovery. | early qMRI rostral cord/brain metrics predict recovery | qMRI/recovery | YES | abstract-level | PubMed | medium | Prediction anchor. |
| M6B-O013 | M6B-T006 | M6A-P013 | M6A-P013-E001 | Abstract/PubMed | Multimodal MRI/fMRI | Cortical reorganization | CST microstructural integrity related to spinal cord area and sensorimotor cortical reorganization. | axonal integrity links spinal structure to cortical reorganization | CST/cortex | YES | abstract-level | PubMed | medium | Tract-plasticity linkage. |
| M6B-O014 | M6B-T006 | M6A-P014 | M6A-P014-E001 | Abstract/PMC | Structural MRI/fMRI | Atrophy and disability | Cord and cortical atrophy were associated with sensorimotor cortical reorganization and disability. | cord/cortical atrophy associates with reorganization and disability | atrophy/fMRI | YES | abstract-level | Abstract/PMC | medium | Brain-spine linkage. |
| M6B-O015 | M6B-T006 | M6A-P015 | M6A-P015-E001 | Abstract/PubMed | fMRI | Cortical representation | Paraplegic patients showed altered cortical representation of non-affected upper limb movements. | chronic SCI alters motor cortical representation | fMRI activation | YES | abstract-level | PubMed | low | Indirect for lesion anatomy. |
| M6B-O016 | M6B-T005 | M6A-P016 | M6A-P016-E001 | Abstract/PMC | qMRI tract degeneration | Progressive remote degeneration | Remote CST and dorsal column degeneration formed progressive spatial gradients after SCI. | major spinal pathways degenerate progressively after SCI | tract qMRI | YES | abstract-level | Abstract/PMC | medium | Tract-gradient anchor. |
| M6B-O017 | M6B-T002 | M6A-P017 | M6A-P017-E001 | M1A carried | Autopsy vascular pathology | Vascular and secondary tissue damage | Human SCI vascular pathology included hemorrhage, white-matter degeneration, venous occlusion, cavitation, and remote infarct-like lesions. | human SCI includes vascular pathology and remote infarct-like lesions | histology/microangiography | YES | source/full-text carried | M1A carried | high | Vascular compartment anchor. |
| M6B-O018 | M6B-T001 | M6A-P018 | M6A-P018-E001 | Abstract/source | Syrinx autopsy pathology | Chronic cyst complication | Syrinx occurred in partially damaged segments and drainage did not yield satisfactory symptom relief despite radiographic drainage. | post-traumatic syrinx can persist as chronic structural pathology | syrinx/function | YES | abstract-level | Abstract/source page | medium | Cyst/syrinx boundary. |
| M6B-O019 | M6B-T001 | M6A-P019 | M6A-P019-E001 | Abstract/source | Late syrinx precedent | Chronic complication | Progressive late post-traumatic syringomyelia was identified as a chronic structural complication after SCI. | late post-traumatic syringomyelia is a chronic SCI complication | syrinx | NO | abstract-level | Abstract/source page | low | Legacy row. |
| M6B-O020 | M6B-T007 | M6A-P020 | M6A-P020-E001 | Review/source | Trial imaging framework | Screening/outcome framework | MRI anatomy is positioned as a clinical trial screening and outcome-measure tool. | MRI supports SCI trial screening and endpoint selection | trial framework | NO | review-level | Review/source | medium | Map anchor, not primary cohort. |
| M6B-O021 | M6B-T005 | M6A-P021 | M6A-P021-E001 | Abstract | Cord atrophy MRI | Motor/sensory deficits | Independent spinal cord atrophy measures correlated with motor and sensory deficits. | cord atrophy metrics correlate with impairment | atrophy/deficits | YES | abstract-level | Abstract | low | Full text upgrade needed. |
| M6B-O022 | M6B-T003 | M6A-P022 | M6A-P022-E001 | Abstract/PMC ref | Tract-specific diffusion MRI | Motor output | Lateral corticospinal tract damage correlated with motor output in incomplete SCI. | lateral CST damage correlates with motor output | CST diffusion/motor | YES | abstract-level | Abstract/PMC reference | medium | Tract-specific motor anchor. |
| M6B-O023 | M6B-T006 | M6A-P023 | M6A-P023-E001 | Abstract | Brain morphometry | Supraspinal atrophy | Specific brain regions showed atrophy after cervical SCI. | cervical SCI is associated with brain-region atrophy | brain volume | YES | abstract-level | Abstract | low | Secondary to spinal anatomy. |
| M6B-O024 | M6B-T006 | M6A-P024 | M6A-P024-E001 | Abstract | Longitudinal fMRI | Recovery plasticity | Sensorimotor cortical plasticity changed during recovery following SCI. | sensorimotor cortical plasticity changes during recovery | fMRI/recovery | YES | abstract-level | Abstract | low | Full text upgrade needed. |
| M6B-O025 | M6B-T006 | M6A-P025 | M6A-P025-E001 | Abstract | fMRI cortical plasticity | Motor cortex reorganization | Human motor cortex plasticity was observed after cervical SCI. | cervical SCI is associated with motor cortex plasticity | fMRI | YES | abstract-level | Abstract | low | Early fMRI anchor. |
| M6B-O026 | M6B-T006 | M6A-P026 | M6A-P026-E001 | Abstract | fMRI activation | Force association | Motor cortex activation related to squeezing force after SCI. | motor cortex activation relates to residual force | fMRI/force | YES | abstract-level | Abstract | low | Functional endpoint boundary. |
| M6B-O027 | M6B-T005 | M6A-P027 | M6A-P027-E001 | Abstract | Sensory pathway MRI | Sensory atrophy/outcome | Sensory system atrophy was tracked and linked to outcome prediction. | sensory pathway atrophy can support outcome prediction | sensory MRI/outcome | YES | abstract-level | Abstract | low | Full text upgrade needed. |
| M6B-O028 | M6B-T005 | M6A-P028 | M6A-P028-E001 | Abstract | Neurodegeneration imaging | Above-lesion degeneration | Neurodegeneration above the level of SCI was tracked longitudinally. | above-lesion neurodegeneration progresses after SCI | neuroimaging | YES | abstract-level | Abstract | low | Remote degeneration context. |
| M6B-O029 | M6B-T007 | M6A-P029 | M6A-P029-E001 | Review/map | Traumatic/nontraumatic synthesis | Pathology boundary | Neuroimaging can reveal pathological similarities and boundaries across traumatic and nontraumatic SCI. | traumatic and nontraumatic SCI need separate imaging-pathology boundaries | synthesis | NO | review-level | Review/map | medium | Etiology boundary. |
| M6B-O030 | M6B-T008 | M6A-P030 | M6A-P030-E001 | Methods/map | qMRI interpretation | Modality boundary | qMRI metrics require cautious interpretation as indirect markers of myelin, iron, and tissue structure. | qMRI markers are indirect and histology-informed | methods boundary | NO | methods-level | Methods/map | medium | Prevents overinterpretation. |
| M6B-O031 | M6B-T005 | M6A-P031 | M6A-P031-E001 | Abstract/source | Chronic complete qMRI | Brainstem/dorsal column change | Chronic complete SCI showed supraspinal qMRI changes mainly as caudal brainstem volume reduction consistent with dorsal column Wallerian degeneration. | complete SCI qMRI changes localize mainly to caudal brainstem volume reduction | qMRI volume | YES | abstract-level | Abstract/source page | medium | Complete-SCI boundary. |
| M6B-O032 | M6B-T005 | M6A-P032 | M6A-P032-E001 | Abstract/source | Supraspinal MRS | Metabolic change | Complete SCI showed altered metabolites in pons/cerebellum with correlations to clinical scores. | supraspinal MRS detects metabolic changes linked to clinical scores | MRS/metabolites | YES | abstract-level | Abstract/source page | medium | Supraspinal metabolic anchor. |
| M6B-O033 | M6B-T007 | M6A-P033 | M6A-P033-E001 | Review/map | Biomarker readiness | Diagnostic workup | Imaging biomarkers are part of a broader diagnostic workup after traumatic SCI. | imaging is one component of SCI biomarker workup | biomarker framework | NO | review-level | Review/map | medium | Review-map only. |
| M6B-O034 | M6B-T007 | M6A-P034 | M6A-P034-E001 | Review/map | Neuroimaging synthesis | Imaging category map | Neuroimaging tracks structural, microstructural, metabolic, and functional consequences of SCI. | SCI neuroimaging spans structural, microstructural, metabolic, and functional domains | synthesis | NO | review-level | Review/map | medium | Modality map. |
| M6B-O035 | M6B-T004 | M6A-P035 | M6A-P035-E001 | Abstract/PMC | Tissue bridge MRI | Walking ability | Tissue bridge ratio was associated with 6-minute walk distance in incomplete SCI. | midsagittal tissue bridge ratio associates with walking ability | bridge ratio/6MWD | YES | abstract-level | Abstract/PMC | medium | Incomplete SCI case-series anchor. |
| M6B-O036 | M6B-T007 | M6A-P036 | M6A-P036-E001 | Review/map | Trial readiness | Screening/stratification | Trial-readiness literature frames imaging as screening and stratification rather than direct repair evidence. | imaging trial readiness is screening/stratification evidence | trial framework | NO | review-level | Review/map | low | Review-map boundary. |

---

## Pass 5A: Author Claims Extracted

| Claim ID | Topic ID | Paper ID | Claim Text | Claim Type | Confidence Level | Source Section | Extraction Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| M6B-C001 | M6B-T001 | M6A-P001, P018-P019 | Chronic human SCI lesion architecture can preserve adjacent cord tissue while focal cystic loss and syrinx/cyst pathology remain important compartments. | synthesis | high | Tracker/source rows | medium | Architecture claim. |
| M6B-C002 | M6B-T002 | M6A-P002 | Ventral-root axon loss and thin-myelin pathology are human chronic SCI compartments relevant to motor output and remyelination boundaries. | conclusion | high | M1A carried | high | Tissue pathology. |
| M6B-C003 | M6B-T001 | M6A-P003 | Chronic scar resection and scaffold-cell implantation can be anatomically planned with MRI and electrophysiologic boundary mapping in humans. | conclusion | high | Source page | high | Feasibility, not efficacy. |
| M6B-C004 | M6B-T002 | M6A-P017 | Vascular pathology is part of human SCI lesion evolution and can include hemorrhage, venous occlusion, cavitation, and remote infarct-like lesions. | conclusion | high | M1A carried | high | Autopsy anchor. |
| M6B-C005 | M6B-T001 | M6A-P018-P019 | Post-traumatic syrinx and cystic complications should be preserved as distinct chronic structural complications. | conclusion | medium | Abstract/source page | medium | Legacy/full-text upgrade boundary. |
| M6B-C006 | M6B-T003 | M6A-P004, P006-P007 | DTI can detect abnormalities beyond conventional MRI-visible lesion morphology. | synthesis | medium | Abstract/PMC | medium | Modality-specific. |
| M6B-C007 | M6B-T003 | M6A-P007, P022 | Subject-specific or tract-specific diffusion metrics relate to motor and sensory impairment after SCI. | synthesis | medium | Abstract/PMC | medium | Tract metric claim. |
| M6B-C008 | M6B-T004 | M6A-P005, P008-P009, P035 | Tissue bridge and lesion-geometry metrics are clinically meaningful prognostic MRI biomarkers. | synthesis | high | Abstract/PMC/source | medium | Prognostic biomarker. |
| M6B-C009 | M6B-T004 | M6A-P008-P009, P035 | Tissue bridge interpretation should preserve level, timing, etiology, completeness, and endpoint boundaries. | boundary condition | high | Module 6A tracker | high | Prevents overgeneralization. |
| M6B-C010 | M6B-T005 | M6A-P010, P032 | MRS can capture spinal or supraspinal metabolic changes related to impairment or clinical scores. | synthesis | medium | Abstract/source page | medium | Metabolic biomarkers. |
| M6B-C011 | M6B-T005 | M6A-P005, P011-P012, P016, P027-P031 | qMRI and longitudinal neuroimaging track remote degeneration and recovery predictors after SCI. | synthesis | medium | Abstract/source page | medium | Remote degeneration. |
| M6B-C012 | M6B-T005 | M6A-P011, P016, P028, P031 | CST and dorsal column degeneration can occur above the lesion over time. | synthesis | medium | Abstract/PMC/source | medium | Tract degeneration. |
| M6B-C013 | M6B-T006 | M6A-P013-P015, P024-P026 | fMRI and cortical reorganization studies indicate remote plasticity after SCI. | synthesis | medium | Abstract/source page | low | Indirect evidence. |
| M6B-C014 | M6B-T006 | M6A-P013-P014, P023-P026 | Cortical reorganization claims should be linked to spinal lesion severity, tract integrity, or clinical impairment before consensus use. | boundary condition | high | Module 6A tracker | high | Brain-only caution. |
| M6B-C015 | M6B-T005 | M6A-P021, P023, P027-P028 | Cord, sensory-system, and brain atrophy metrics are clinically relevant but indirect. | synthesis | medium | Abstract/source page | low | Full-text upgrade queue. |
| M6B-C016 | M6B-T007 | M6A-P020, P036 | Imaging supports trial screening, endpoint selection, and stratification. | synthesis | medium | Review/source | medium | Trial readiness. |
| M6B-C017 | M6B-T008 | M6A-P004, P008-P009, P029, P031-P035 | Pediatric, traumatic, ischemic, nontraumatic, complete, and incomplete SCI should not be collapsed without preserving cohort boundaries. | boundary condition | high | Module 6A tracker | high | Cohort ontology. |
| M6B-C018 | M6B-T008 | M6A-P001-P010, P017-P019 | MRI evidence and autopsy pathology are complementary but not interchangeable. | boundary condition | high | Module 6A tracker | high | Modality boundary. |
| M6B-C019 | M6B-T008 | M6A-P004, P006-P016, P021-P032 | DTI, qMRI, MRS, and fMRI are indirect biomarkers that require modality-specific confidence labels. | boundary condition | high | Module 6A tracker | high | Interpretation boundary. |
| M6B-C020 | M6B-T007 | M6A-P003, P020, P036 | Surgical reconstruction and trial screening anatomy are feasibility or stratification evidence unless linked to repair outcomes. | boundary condition | high | Module 6A tracker | high | Surgical/trial boundary. |
| M6B-C021 | M6B-T007 | M6A-P020, P029-P034, P036 | Review and method rows should guide interpretation but should not replace primary cohort extraction. | boundary condition | high | Module 6A tracker | high | Review-map boundary. |
| M6B-C022 | M6B-T008 | M6A-P001-P036 | Human pathology and imaging evidence define translation constraints for animal and biomaterial modules. | synthesis | high | Module 6A tracker | high | Cross-module role. |
| M6B-C023 | M6B-T001 | M6A-P001, P003 | Preserved human tissue and surgical scar-resection anatomy may support reconstruction feasibility but do not prove regenerative permissiveness. | boundary condition | high | Module 6A tracker | high | Feasibility versus mechanism. |
| M6B-C024 | M6B-T002 | M6A-P002 | Ventral-root and myelin pathology links Module 6 to remyelination/white-matter repair, but remains human pathology evidence rather than intervention evidence. | boundary condition | high | Module 6A tracker | high | Cross-module boundary. |
| M6B-C025 | M6B-T002 | M6A-P017-P019 | Vascular and syrinx pathology link lesion architecture to chronic secondary structural damage. | synthesis | medium | M1A/abstract rows | medium | Pathology architecture. |
| M6B-C026 | M6B-T005 | M6A-P005, P011-P012, P016, P027-P032 | Remote motor-system and sensory-system degeneration should be treated as active chronic pathology rather than only downstream disability. | synthesis | medium | Abstract/source page | medium | Systems pathology. |
| M6B-C027 | M6B-T003 | M6A-P004 | Pediatric SCIWOMR highlights the limitation of conventional MRI for detecting clinically relevant cord pathology. | conclusion | medium | Abstract/source page | medium | Pediatric boundary. |
| M6B-C028 | M6B-T003 | M6A-P008-P009, P022, P035 | Lateral CST and tissue bridge metrics can support motor recovery stratification. | synthesis | medium | Abstract/PMC/source | medium | Tract plus lesion geometry. |
| M6B-C029 | M6B-T005 | M6A-P010, P032 | Metabolic imaging adds nonstructural clinical readouts to human SCI pathology assessment. | synthesis | medium | Abstract/source page | medium | MRS claim. |
| M6B-C030 | M6B-T006 | M6A-P015, P024-P026 | fMRI activation findings are lower-directness evidence for lesion anatomy unless tied to spinal metrics or outcomes. | boundary condition | high | Module 6A tracker | high | Directness boundary. |
| M6B-C031 | M6B-T007 | M6A-P020, P033-P036 | Clinical trial imaging should be used as screening and stratification evidence before being treated as mechanistic repair evidence. | boundary condition | high | Review/map | medium | Trial interpretation. |
| M6B-C032 | M6B-T008 | M6A-P001-P036 | Module 6 consensus should stratify by modality, timing, injury level, etiology, completeness, and confidence. | synthesis | high | Module 6A tracker | high | Ontology claim. |
| M6B-C033 | M6B-T008 | M6A-P006-P036 | Low-confidence abstract/source-page rows require full-text upgrade before strong numeric or mechanistic claims. | boundary condition | high | Module 6A tracker | high | Evidence quality. |
| M6B-C034 | M6B-T008 | M6A-P004, P006-P016, P021-P032 | Chronic SCI imaging is not equivalent to histologic cell-state evidence. | boundary condition | high | Module 6A tracker | high | Imaging-to-cell-state caution. |
| M6B-C035 | M6B-T008 | M6A-P001-P036 | Human evidence can set translational boundaries for implant, graft, and reconstruction planning. | synthesis | high | Module 6A tracker | high | Cross-module translation. |
| M6B-C036 | M6B-T008 | M6A-P001-P036 | Module 6B should preserve human evidence type and not mix animal imaging into human pathology consensus statements. | boundary condition | high | Module 6A tracker | high | Species boundary. |

---

## Pass 6: Evidence Links Drafted

| Link ID | Claim ID | Observation ID | Link Type | Strength | Notes |
|---|---|---|---|---|---|
| M6B-L001 | M6B-C001 | M6B-O001 | supports | high | MRI stereology preservation |
| M6B-L002 | M6B-C001 | M6B-O018 | supports | medium | Syrinx pathology |
| M6B-L003 | M6B-C001 | M6B-O019 | supports | low | Late syrinx precedent |
| M6B-L004 | M6B-C002 | M6B-O002 | supports | high | Ventral-root pathology |
| M6B-L005 | M6B-C003 | M6B-O003 | supports | high | Scar-resection anatomy |
| M6B-L006 | M6B-C004 | M6B-O017 | supports | high | Vascular autopsy pathology |
| M6B-L007 | M6B-C005 | M6B-O018 | supports | medium | Syrinx autopsy row |
| M6B-L008 | M6B-C005 | M6B-O019 | supports | low | Late syrinx row |
| M6B-L009 | M6B-C006 | M6B-O004 | supports | medium | Pediatric DTI |
| M6B-L010 | M6B-C006 | M6B-O006 | supports | medium | Chronic whole-cord DTI |
| M6B-L011 | M6B-C006 | M6B-O007 | supports | medium | Subject-specific DTI |
| M6B-L012 | M6B-C007 | M6B-O007 | supports | medium | Impairment association |
| M6B-L013 | M6B-C007 | M6B-O022 | supports | medium | CST motor output |
| M6B-L014 | M6B-C008 | M6B-O005 | supports | high | Longitudinal lesion/tissue bridge |
| M6B-L015 | M6B-C008 | M6B-O008 | supports | medium | Thoracic tissue bridge |
| M6B-L016 | M6B-C008 | M6B-O009 | supports | medium | Cervical multicentre bridge |
| M6B-L017 | M6B-C008 | M6B-O035 | supports | medium | Walking association |
| M6B-L018 | M6B-C009 | M6B-O008 | contextual_support | medium | Thoracic traumatic/ischemic |
| M6B-L019 | M6B-C009 | M6B-O009 | contextual_support | medium | Cervical cohort |
| M6B-L020 | M6B-C009 | M6B-O035 | contextual_support | medium | Incomplete SCI walking |
| M6B-L021 | M6B-C010 | M6B-O010 | supports | medium | Cervical cord MRS |
| M6B-L022 | M6B-C010 | M6B-O032 | supports | medium | Supraspinal MRS |
| M6B-L023 | M6B-C011 | M6B-O005 | supports | high | Longitudinal qMRI |
| M6B-L024 | M6B-C011 | M6B-O011 | supports | low | CST/cortex degeneration |
| M6B-L025 | M6B-C011 | M6B-O012 | supports | medium | qMRI recovery prediction |
| M6B-L026 | M6B-C011 | M6B-O016 | supports | medium | Tract degeneration gradients |
| M6B-L027 | M6B-C011 | M6B-O027 | contextual_support | low | Sensory atrophy |
| M6B-L028 | M6B-C011 | M6B-O028 | contextual_support | low | Above-lesion degeneration |
| M6B-L029 | M6B-C012 | M6B-O011 | supports | low | Cranial CST degeneration |
| M6B-L030 | M6B-C012 | M6B-O016 | supports | medium | CST/dorsal column gradients |
| M6B-L031 | M6B-C012 | M6B-O031 | supports | medium | Dorsal column Wallerian degeneration |
| M6B-L032 | M6B-C013 | M6B-O013 | supports | medium | Axonal integrity/cortical reorganization |
| M6B-L033 | M6B-C013 | M6B-O014 | supports | medium | Atrophy and cortical reorganization |
| M6B-L034 | M6B-C013 | M6B-O015 | supports | low | Upper-limb representation |
| M6B-L035 | M6B-C013 | M6B-O024 | supports | low | Recovery plasticity |
| M6B-L036 | M6B-C013 | M6B-O025 | supports | low | Motor cortex plasticity |
| M6B-L037 | M6B-C013 | M6B-O026 | supports | low | Motor activation/force |
| M6B-L038 | M6B-C014 | M6B-O013 | contextual_support | medium | Has tract linkage |
| M6B-L039 | M6B-C014 | M6B-O014 | contextual_support | medium | Has disability linkage |
| M6B-L040 | M6B-C014 | M6B-O023 | contextual_support | low | Brain-only atrophy caution |
| M6B-L041 | M6B-C015 | M6B-O021 | supports | low | Cord atrophy deficits |
| M6B-L042 | M6B-C015 | M6B-O023 | supports | low | Brain atrophy |
| M6B-L043 | M6B-C015 | M6B-O027 | supports | low | Sensory atrophy |
| M6B-L044 | M6B-C015 | M6B-O028 | supports | low | Neurodegeneration above lesion |
| M6B-L045 | M6B-C016 | M6B-O020 | supports | medium | MRI trial framework |
| M6B-L046 | M6B-C016 | M6B-O036 | supports | low | Trial-readiness review |
| M6B-L047 | M6B-C017 | M6B-O004 | contextual_support | medium | Pediatric SCIWOMR |
| M6B-L048 | M6B-C017 | M6B-O008 | contextual_support | medium | Traumatic/ischemic thoracic |
| M6B-L049 | M6B-C017 | M6B-O031 | contextual_support | medium | Complete SCI |
| M6B-L050 | M6B-C017 | M6B-O035 | contextual_support | medium | Incomplete SCI |
| M6B-L051 | M6B-C018 | M6B-O001 | contextual_support | high | MRI anatomy |
| M6B-L052 | M6B-C018 | M6B-O002 | contextual_support | high | Autopsy/ventral-root pathology |
| M6B-L053 | M6B-C018 | M6B-O017 | contextual_support | high | Autopsy vascular pathology |
| M6B-L054 | M6B-C018 | M6B-O018 | contextual_support | medium | Syrinx autopsy pathology |
| M6B-L055 | M6B-C019 | M6B-O004 | contextual_support | medium | DTI |
| M6B-L056 | M6B-C019 | M6B-O010 | contextual_support | medium | MRS |
| M6B-L057 | M6B-C019 | M6B-O012 | contextual_support | medium | qMRI |
| M6B-L058 | M6B-C019 | M6B-O013 | contextual_support | medium | multimodal/fMRI |
| M6B-L059 | M6B-C020 | M6B-O003 | supports | high | Surgery feasibility |
| M6B-L060 | M6B-C020 | M6B-O020 | contextual_support | medium | Trial framework |
| M6B-L061 | M6B-C020 | M6B-O036 | contextual_support | low | Trial readiness |
| M6B-L062 | M6B-C021 | M6B-O029 | contextual_support | medium | Review/map |
| M6B-L063 | M6B-C021 | M6B-O030 | contextual_support | medium | Methods/map |
| M6B-L064 | M6B-C021 | M6B-O033 | contextual_support | medium | Biomarker review |
| M6B-L065 | M6B-C021 | M6B-O034 | contextual_support | medium | Neuroimaging review |
| M6B-L066 | M6B-C022 | M6B-O001 | supports | high | Human preserved tissue |
| M6B-L067 | M6B-C022 | M6B-O017 | supports | high | Human vascular pathology |
| M6B-L068 | M6B-C023 | M6B-O001 | supports | high | Preserved tissue |
| M6B-L069 | M6B-C023 | M6B-O003 | supports | high | Scar resection |
| M6B-L070 | M6B-C024 | M6B-O002 | supports | high | Ventral root/myelin |
| M6B-L071 | M6B-C025 | M6B-O017 | supports | high | Vascular pathology |
| M6B-L072 | M6B-C025 | M6B-O018 | supports | medium | Syrinx pathology |
| M6B-L073 | M6B-C026 | M6B-O005 | supports | high | Motor-system longitudinal |
| M6B-L074 | M6B-C026 | M6B-O016 | supports | medium | Major pathway degeneration |
| M6B-L075 | M6B-C026 | M6B-O027 | contextual_support | low | Sensory system atrophy |
| M6B-L076 | M6B-C026 | M6B-O032 | contextual_support | medium | Supraspinal metabolism |
| M6B-L077 | M6B-C027 | M6B-O004 | supports | medium | Pediatric MRI-normal DTI abnormality |
| M6B-L078 | M6B-C028 | M6B-O008 | supports | medium | Tissue bridge recovery |
| M6B-L079 | M6B-C028 | M6B-O022 | supports | medium | Lateral CST motor output |
| M6B-L080 | M6B-C028 | M6B-O035 | supports | medium | Walking bridge ratio |
| M6B-L081 | M6B-C029 | M6B-O010 | supports | medium | Spinal MRS |
| M6B-L082 | M6B-C029 | M6B-O032 | supports | medium | Supraspinal MRS |
| M6B-L083 | M6B-C030 | M6B-O015 | supports | low | fMRI indirectness |
| M6B-L084 | M6B-C030 | M6B-O024 | supports | low | Cortical plasticity |
| M6B-L085 | M6B-C030 | M6B-O026 | supports | low | Activation/force |
| M6B-L086 | M6B-C031 | M6B-O020 | supports | medium | Clinical trial MRI |
| M6B-L087 | M6B-C031 | M6B-O033 | contextual_support | medium | Biomarker workup |
| M6B-L088 | M6B-C031 | M6B-O036 | supports | low | Trial readiness |
| M6B-L089 | M6B-C032 | M6B-O004 | contextual_support | medium | pediatric and DTI |
| M6B-L090 | M6B-C032 | M6B-O008 | contextual_support | medium | level/etiology/timing |
| M6B-L091 | M6B-C032 | M6B-O031 | contextual_support | medium | completeness |
| M6B-L092 | M6B-C032 | M6B-O035 | contextual_support | medium | endpoint/incomplete SCI |
| M6B-L093 | M6B-C033 | M6B-O011 | contextual_support | low | abstract-level row |
| M6B-L094 | M6B-C033 | M6B-O021 | contextual_support | low | abstract-level row |
| M6B-L095 | M6B-C033 | M6B-O024 | contextual_support | low | abstract-level row |
| M6B-L096 | M6B-C033 | M6B-O026 | contextual_support | low | abstract-level row |
| M6B-L097 | M6B-C034 | M6B-O006 | contextual_support | medium | diffusion metric caution |
| M6B-L098 | M6B-C034 | M6B-O010 | contextual_support | medium | metabolite caution |
| M6B-L099 | M6B-C034 | M6B-O030 | supports | medium | qMRI methods boundary |
| M6B-L100 | M6B-C035 | M6B-O001 | supports | high | human lesion architecture |
| M6B-L101 | M6B-C035 | M6B-O003 | supports | high | reconstructive anatomy |
| M6B-L102 | M6B-C035 | M6B-O008 | supports | medium | prognostic stratification |
| M6B-L103 | M6B-C036 | M6B-O001 | contextual_support | high | human-only evidence |
| M6B-L104 | M6B-C036 | M6B-O017 | contextual_support | high | human autopsy evidence |

---

## Boundary Conditions Draft

| Boundary ID | Boundary Statement | Observation IDs | Claim IDs | Status |
|---|---|---|---|---|
| M6B-B001 | Human lesion anatomy is multi-compartmental: focal cystic atrophy, preserved adjacent cord, tissue bridges, syrinx/cyst pathology, vascular pathology, ventral-root loss, and remote tract degeneration should not be collapsed into one lesion metric. | M6B-O001-O019, O035 | M6B-C001-C005, C008-C012, C025-C026 | ACTIVE |
| M6B-B002 | MRI, DTI, qMRI, MRS, fMRI, and autopsy pathology are complementary but not interchangeable; imaging-visible changes do not specify cell type or matrix composition without tissue evidence. | M6B-O001-O034 | M6B-C018-C019, C034 | ACTIVE |
| M6B-B003 | DTI, qMRI, MRS, and fMRI are indirect biomarkers and must retain modality-specific confidence labels, especially for abstract/source-page rows. | M6B-O004, O006-O016, O021-O032 | M6B-C006-C015, C019, C033-C034 | ACTIVE |
| M6B-B004 | Brain and supraspinal changes should be linked back to spinal lesion severity, tract integrity, or clinical impairment before they are used as human lesion-architecture consensus evidence. | M6B-O011-O016, O023-O032 | M6B-C011-C015, C026, C030 | ACTIVE |
| M6B-B005 | Surgical reconstruction and clinical trial screening anatomy are feasibility and stratification evidence unless linked to pathology, repair, or outcome evidence. | M6B-O003, O020, O033-O036 | M6B-C003, C016, C020-C021, C031 | ACTIVE |
| M6B-B006 | Pediatric SCIWOMR, traumatic adult SCI, ischemic SCI, nontraumatic SCI, complete SCI, and incomplete SCI should preserve age, etiology, level, and completeness boundaries. | M6B-O004, O008-O009, O031, O035 | M6B-C009, C017, C028, C032 | ACTIVE |
| M6B-B007 | Low-confidence abstract/source-page rows are acceptable for first-pass consensus readiness but require full-text upgrade before strong numeric, dose-like, or mechanism-specific SQL materialization. | M6B-O006-O036 | M6B-C021, C033 | ACTIVE |
| M6B-B008 | Human pathology/imaging evidence sets translational constraints for reconstruction modules but does not by itself prove animal mechanism, implant compatibility, or regenerative permissiveness. | M6B-O001-O036 | M6B-C022-C024, C032, C035-C036 | ACTIVE |

---

## Consensus Draft Queue

| Consensus Draft ID | Topic ID | Draft Statement | Supporting Observations | Supporting Claims | Boundary Records | Readiness Status | Notes |
|---|---|---|---|---|---|---|---|
| M6B-S001 | M6B-T001 | Human chronic SCI lesion architecture includes preserved adjacent tissue, focal cystic loss, scar-resection anatomy, and chronic syrinx/cyst complications; these compartments should be tracked separately. | M6B-O001, O003, O018-O019 | M6B-C001, C003, C005, C023 | M6B-B001, M6B-B005, M6B-B008 | CONSENSUS-READY FIRST PASS | Architecture statement. |
| M6B-S002 | M6B-T002 | Human tissue pathology shows ventral-root axon/myelin injury and vascular/cystic compartments that are not reducible to MRI-visible lesion geometry. | M6B-O002, O017-O018 | M6B-C002, C004, C018, C024-C025 | M6B-B001, M6B-B002 | CONSENSUS-READY FIRST PASS | Autopsy/pathology statement. |
| M6B-S003 | M6B-T003 | DTI and tract-specific diffusion measures can reveal clinically relevant injury beyond conventional MRI and can relate to motor or sensory impairment. | M6B-O004, O006-O007, O022 | M6B-C006-C007, C027-C028 | M6B-B002, M6B-B003, M6B-B006 | CONSENSUS-READY FIRST PASS | Diffusion/tract statement. |
| M6B-S004 | M6B-T004 | Tissue bridges and lesion-geometry measures are promising prognostic MRI biomarkers for recovery and walking ability, but interpretation must preserve level, etiology, timing, completeness, and endpoint boundaries. | M6B-O005, O008-O009, O035 | M6B-C008-C009, C028, C032 | M6B-B001, M6B-B006 | CONSENSUS-READY FIRST PASS | Tissue bridge statement. |
| M6B-S005 | M6B-T005 | qMRI, MRS, atrophy, and longitudinal neuroimaging support a model of chronic system-level pathology involving remote spinal, sensory, motor, brainstem, and metabolic changes. | M6B-O010-O012, O016, O021, O027-O032 | M6B-C010-C012, C015, C026, C029 | M6B-B003, M6B-B004, M6B-B007 | CONSENSUS-READY FIRST PASS | Remote degeneration statement. |
| M6B-S006 | M6B-T006 | fMRI and cortical reorganization studies support remote plasticity after SCI, but they are indirect lesion-bed evidence unless paired with spinal lesion, tract, or clinical impairment measures. | M6B-O013-O015, O023-O026 | M6B-C013-C014, C030 | M6B-B003, M6B-B004 | CONSENSUS-READY FIRST PASS | Cortical plasticity statement. |
| M6B-S007 | M6B-T007 | Human imaging can support surgical planning, trial screening, and stratification, but review and trial-readiness rows should not be treated as direct repair efficacy evidence. | M6B-O003, O020, O029, O033-O036 | M6B-C016, C020-C021, C031 | M6B-B005, M6B-B007, M6B-B008 | CONSENSUS-READY FIRST PASS | Translation/trial statement. |
| M6B-S008 | M6B-T008 | Module 6 consensus should remain human-specific, modality-stratified, confidence-labeled, and bounded by timing, injury level, etiology, completeness, and evidence directness. | M6B-O001-O036 | M6B-C017-C019, C022, C032-C036 | all boundary records | CONSENSUS-READY FIRST PASS | Cross-module guardrail. |

## Module 6B Completion Checklist

| Requirement | Status | Notes |
|---|---|---|
| Atomic observations extracted from saturated 6A corpus | MET FOR ALL FIRST-PASS TOPICS | 36 observations from 36 cohort/paper rows |
| Author claims separated from observations | MET FOR ALL FIRST-PASS TOPICS | 36 claims with confidence labels |
| Claims linked to observations | MET FOR ALL FIRST-PASS TOPICS | 104 evidence links |
| Boundaries and contradictions recorded | MET FOR ALL FIRST-PASS TOPICS | 8 boundary records |
| Consensus statements drafted only after links | MET FOR ALL FIRST-PASS TOPICS | 8 consensus-ready statements |
| Confidence labels retained | MET FOR ALL FIRST-PASS TOPICS | Abstract/source-page rows retained as low or medium confidence |

## Module 6B Freeze Note

Module 6B reached consensus-ready first pass on 2026-07-16 by converting the saturated Module 6A human pathology and translational imaging corpus into linked observations, author claims, evidence links, boundaries, and consensus drafts. The next step is full-text upgrade of low-confidence rows and optional SQL materialization after the tracker-level evidence bundle validates.
