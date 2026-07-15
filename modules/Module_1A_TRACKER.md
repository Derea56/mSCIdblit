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
| M1A-P003 | Tamaru T | 2023 | Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury | Mouse | Contusion SCI / astrocyte culture / astrocyte transplantation | PASS 3 COMPLETE | Anchor for chronic astrocytic scar persistence |
| M1A-P004 | Gong L | 2023 | Spatiotemporal dynamics of the molecular expression pattern and intercellular interactions in the glial scar response to spinal cord injury | Mouse | Lateral hemisection | PASS 3 COMPLETE | Spatial transcriptomic atlas of scar compartments and cell interactions |
| M1A-P005 | Rasouli A | 2009 | Resection of glial scar following spinal cord injury | Rat | SCI with scar resection | PASS 3 COMPLETE | Glial scar resection comparison in contusion and hemisection |

### 3. Reactive Surrounding Neural Tissue

| Paper ID | First Author | Year | Title | Species | Injury Model | Status | Notes |
|----------|--------------|------|-------|---------|--------------|--------|-------|
| M1A-P006 | Li Y | 2020 | Delayed microglial depletion after spinal cord injury reduces chronic inflammation and neurodegeneration in the brain and improves neurological recovery in male mice | Mouse | SCI | QUEUED PASS -1 | Candidate for chronic inflammatory/neurodegenerative tissue context |

### 4. Fibrotic Scar

| Paper ID | First Author | Year | Title | Species | Injury Model | Status | Notes |
|----------|--------------|------|-------|---------|--------------|--------|-------|
| M1A-P007 | Cooper JG | 2018 | Fibronectin EDA forms the chronic fibrotic scar after contusive spinal cord injury | Mouse | Contusion | PASS 3 COMPLETE | Anchor for chronic fibrotic compartment |
| M1A-P008 | Soderblom C | 2013 | Perivascular fibroblasts form the fibrotic scar after contusive spinal cord injury | Mouse | Contusion | PASS 3 COMPLETE | Anchor for perivascular fibroblast source/cell identity |
| M1A-P009 | Dias DO | 2018 | Reducing pericyte-derived scarring promotes recovery after spinal cord injury | Mouse | Dorsal hemisection / dorsal funiculus incision | PASS 3 COMPLETE | Anchor for type A pericyte-derived scar modulation |
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
| M1A-P014 | McCallum S | 2026 | Lesion-remote astrocytes govern microglia-mediated white matter repair | Mouse | Incomplete hemisection / crush SCI | PASS 3 COMPLETE | Lesion-remote white matter astrocyte-microglia repair state |

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
| M1A-P021 | Xue X | 2024 | Heterogeneous fibroblasts contribute to fibrotic scar formation after spinal cord injury in mice and monkeys | Mouse, monkey | PASS 3 COMPLETE | Cross-species fibrotic scar heterogeneity and fibroblast origins |

### 11. Scar Resection Anatomy

| Paper ID | First Author | Year | Title | Species | Intervention | Status | Notes |
|----------|--------------|------|-------|---------|---|--------|-------|
| M1A-P005 | Rasouli A | 2009 | Resection of glial scar following spinal cord injury | Rat | Scar resection | PASS 3 COMPLETE | Resection anatomy anchor |
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
| ANCHOR003 | Tamaru T | 2023 | Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury | Astrocytic scar persistence | PASS 3 COMPLETE |
| ANCHOR004 | Tuszynski MH | 1999 | Human spinal cord retains substantial structural mass in chronic stages after injury | Human chronic pathology | QUEUED PASS -1 |
| ANCHOR005 | Rasouli A | 2009 | Resection of glial scar following spinal cord injury | Scar resection anatomy | PASS 3 COMPLETE |

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
| M1A-P003 | YES | YES | YES | YES | YES | PASS |
| M1A-P004 | YES | YES | YES | YES | YES | PASS |
| M1A-P005 | YES | YES | YES | YES | YES | PASS |
| M1A-P007 | YES | YES | YES | YES | YES | PASS |
| M1A-P008 | YES | YES | YES | YES | YES | PASS |
| M1A-P009 | YES | YES | YES | YES | YES | PASS |
| M1A-P014 | YES | YES | YES | YES | YES | PASS |
| M1A-P021 | YES | YES | YES | YES | YES | PASS |

**BLOCKED papers**: Log separately for future retrieval attempts

---

### Pass 0: Paper Registration

| Paper ID | Title | Authors | Year | Journal | Volume | Issue | Pages | DOI | PMID | URL | Registered |
|----------|-------|---------|------|---------|--------|-------|-------|-----|------|-----|---|
| M1A-P003 | Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury | Tetsuya Tamaru; Kazu Kobayakawa; Hirokazu Saiwai; Daijiro Konno; Ken Kijima; Shingo Yoshizaki; Kazuhiro Hata; Hirotaka Iura; Gentaro Ono; Yohei Haruta; Kazuki Kitade; Kei-Ichiro Iida; Ken-Ichi Kawaguchi; Yoshihiro Matsumoto; Kensuke Kubota; Takeshi Maeda; Seiji Okada; Yasuharu Nakashima | 2023 | Experimental Neurology | 359 | — | 114264 | 10.1016/j.expneurol.2022.114264 | 36336030 | https://catalog.lib.kyushu-u.ac.jp/opac_download_md/6787512/med3703.pdf | YES |
| M1A-P004 | Spatiotemporal Dynamics of the Molecular Expression Pattern and Intercellular Interactions in the Glial Scar Response to Spinal Cord Injury | Leilei Gong; Yun Gu; Xiaoxiao Han; Chengcheng Luan; Chang Liu; Xinghui Wang; Yufeng Sun; Mengru Zheng; Mengya Fang; Shuhai Yang; Lai Xu; Hualin Sun; Bin Yu; Xiaosong Gu; Songlin Zhou | 2023 | Neuroscience Bulletin | 39 | 2 | 213-244 | 10.1007/s12264-022-00897-8 | 35788904 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9905408/ | YES |
| M1A-P005 | Resection of glial scar following spinal cord injury | Alexandre Rasouli; Nitin Bhatia; Paul Dinh; Kim Cahill; Sourabh Suryadevara; Ranjan Gupta | 2009 | Journal of Orthopaedic Research | 27 | 7 | 931-936 | 10.1002/jor.20793 | 19062171 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2696557/ | YES |
| M1A-P007 | Fibronectin EDA forms the chronic fibrotic scar after contusive spinal cord injury | John G. Cooper; Su Ji Jeong; Tammy L. McGuire; Sripadh Sharma; Wenxia Wang; Swati Bhattacharyya; John Varga; John A. Kessler | 2018 | Neurobiology of Disease | 116 | — | 60-68 | 10.1016/j.nbd.2018.04.014 | 29705186 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5995671/ | YES |
| M1A-P008 | Perivascular Fibroblasts Form the Fibrotic Scar after Contusive Spinal Cord Injury | Cynthia Soderblom; Xueting Luo; Ezra Blumenthal; Eric Bray; Kirill Lyapichev; Jose Ramos; Vidhya Krishnan; Catherine Lai-Hsu; Kevin K Park; Pantelis Tsoulfas; Jae K Lee | 2013 | The Journal of Neuroscience | 33 | 34 | 13882-13887 | 10.1523/JNEUROSCI.2524-13.2013 | 23966707 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3755723/ | YES |
| M1A-P009 | Reducing Pericyte-Derived Scarring Promotes Recovery after Spinal Cord Injury | David Oliveira Dias; Hoseok Kim; Daniel Holl; Beata Werne Solnestam; Joakim Lundeberg; Marie Carlen; Christian Goritz; Jonas Frisen | 2018 | Cell | 173 | 1 | 153-165.e22 | 10.1016/j.cell.2018.02.004 | 29502968 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5871719/ | YES |
| M1A-P014 | Lesion-remote astrocytes govern microglia-mediated white matter repair | Sarah McCallum; Keshav B Suresh; Timothy S Islam; Manish K Tripathi; Ann W Saustad; Oksana Shelest; Aditya Patil; David Lee; Brandon Kwon; Katherine Leitholf; Inga Yenokian; Sophia E Shaka; Connor H Beveridge; Palak Manchandra; Caitlin E Randolph; Gordon P Meares; Ranjan Dutta; Jasmine Plummer; Vinicius F Calsavara; Riki Kawaguchi; Simon R V Knott; Gaurav Chopra; Joshua E Burda | 2026 | Nature | 649 | 8098 | 959-970 | 10.1038/s41586-025-09887-y | 41407858 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12823418/ | YES |
| M1A-P021 | Heterogeneous fibroblasts contribute to fibrotic scar formation after spinal cord injury in mice and monkeys | Xiaoyu Xue; Xianming Wu; Yongheng Fan; Shuyu Han; Haipeng Zhang; Yuting Sun; Yanyun Yin; Man Yin; Bing Chen; Zheng Sun; Shuaijing Zhao; Qi Zhang; Weiyuan Liu; Jiaojiao Zhang; Jiayin Li; Ya Shi; Zhifeng Xiao; Jianwu Dai; Yannan Zhao | 2024 | Nature Communications | 15 | 1 | 6321 | 10.1038/s41467-024-50564-x | 39060269 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11282111/ | YES |

---

### Pass 1: Research Questions Identified

| Paper ID | Question ID | Research Question Text | Hypothesis Direction | Keywords | Question Extracted |
|----------|-------------|---|---|---|---|
| M1A-P003 | M1A-P003-RQ001 | Do scar-forming astrocytes persist into the chronic phase after SCI, retain scar-forming autonomy, and recruit surrounding astrocytes through beta1-integrin/N-cadherin signaling? | exploratory | chronic phase; glial scar; scar-forming astrocyte; beta1-integrin; N-cadherin; astrocyte plasticity | YES |
| M1A-P004 | M1A-P004-RQ001 | How do spatial gene-expression patterns, scar-resident cell states, ligand-receptor interactions, and pharmacologic CD36 inhibition change across mouse glial scar maturation after SCI? | exploratory | spatial transcriptomics; glial scar; fibroblast; microglia; astrocyte; salvianolic acid B; CD36 | YES |
| M1A-P005 | M1A-P005-RQ001 | Does surgical glial scar resection improve axonal regeneration or functional recovery after rat contusion or dorsal hemisection SCI? | negative/mixed | glial scar resection; contusion; dorsal hemisection; BBB score; BDA tracing | YES |
| M1A-P007 | M1A-P007-RQ001 | Does eliminating the fibronectin Extra Domain A isoform reduce fibrotic scarring and improve recovery after contusive spinal cord injury in mice? | positive | FnEDA; fibronectin matrix; fibrotic scar; contusion SCI; chronic lesion | YES |
| M1A-P008 | M1A-P008-RQ001 | Do Col1alpha1-expressing perivascular fibroblasts enter and form the fibrotic scar after contusive SCI with intact dura, and are they distinct from NG2-positive pericytes? | exploratory | Col1alpha1-GFP; perivascular fibroblast; fibrotic scar; contusion SCI; NG2 lineage tracing; PDGFR-beta | YES |
| M1A-P009 | M1A-P009-RQ001 | Does attenuating type A pericyte-derived fibrotic scarring reduce ECM deposition and permit axonal regeneration, circuit integration, and functional recovery after mouse SCI? | positive | type A pericyte; Glast-Rasless; fibrotic scar; dorsal hemisection; CST; 5-HT; optogenetics | YES |
| M1A-P014 | M1A-P014-RQ001 | Do lesion-remote astrocyte reactivity states, particularly CCN1-expressing white matter astrocytes, govern microglial debris clearance and white matter repair after SCI? | positive | lesion-remote astrocyte; CCN1; microglia; white matter degeneration; debris clearance; lipid metabolism | YES |
| M1A-P021 | M1A-P021-RQ001 | What fibroblast lineages and functional subtypes form fibrotic scars after SCI in mice and rhesus macaques, and how do penetrating and non-penetrating injuries differ? | exploratory | fibrotic scar heterogeneity; meningeal fibroblast; perivascular fibroblast; transection; crush; monkey | YES |

---

### Pass 2: Experimental Paradigms Identified

| Paper ID | Paradigm ID | Paradigm Name | Description | Methodology | Paradigm Extracted |
|----------|-------------|---|---|---|---|
| M1A-P003 | M1A-P003-P001 | Astrocyte phenotype time course after mouse contusion SCI | Compare naive astrocytes, reactive astrocytes, subacute scar-forming astrocytes, and chronic-phase astrocytes after SCI. | T9 70 kdyn Infinite Horizons contusion SCI; GFAP/N-cadherin immunostaining; LMD isolation of GFAP-positive astrocytes; RT-PCR/qPCR for scar-associated genes. | YES |
| M1A-P003 | M1A-P003-P002 | In vitro astrocyte phenotype manipulation | Generate IL-6 reactive astrocytes and collagen-I-grown scar-forming astrocytes, then test whether removing collagen signaling or blocking beta1-integrin/N-cadherin reverts scar-forming astrocytes. | Primary astrocytes from P1-P3 C57BL/6J mice; IL-6 plus soluble IL-6 receptor; type I collagen-coated dishes; Poly-D-lysine reseeding; anti-beta1 integrin and anti-N-cadherin antibodies; immunostaining and qPCR. | YES |
| M1A-P003 | M1A-P003-P003 | Scar-forming astrocyte transplantation and beta1-integrin blockade | Test whether transplanted scar-forming astrocytes maintain scar phenotype, recruit host astrocytes, and whether beta1-integrin blockade reduces recruitment after transplantation or SCI. | EGFP-positive Col-I-SAs from CAG-EGFP neonatal mice transplanted into naive spinal cord; anti-beta1 integrin antibody after transplantation or after SCI; GFAP/N-cadherin/GAP43 immunostaining and LMD/qPCR. | YES |
| M1A-P004 | M1A-P004-P001 | Mouse glial scar spatial transcriptomic time course | Build a spatiotemporal atlas of mouse glial scar maturation after T10 right lateral hemisection. | Sixty 8-week-old female C57BL/6J mice; T10 right lateral hemisection; 10x Genomics Visium spatial transcriptomics and H&E at 3, 7, 14, and 28 DPI; Seurat clustering, GSVA, pseudotime, WGCNA, ligand-receptor analysis. | YES |
| M1A-P004 | M1A-P004-P002 | Scar cell-state and interaction mapping | Identify spatially resolved fibroblast, macrophage, microglia, astrocyte, oligodendrocyte, endothelial, and other scar-resident states and infer their interactions. | Spatial transcriptomic deconvolution, cell-type marker mapping, pseudotime trajectories, SCENIC, CellPhoneDB-style ligand-receptor analysis, and scar-boundary marker mapping. | YES |
| M1A-P004 | M1A-P004-P003 | Salvianolic acid B scar modulation | Test whether CD36 inhibition with salvianolic acid B modifies fibrotic scar signatures after SCI. | SAB administered after T10 lateral hemisection; spatial transcriptomic and scar marker analyses focused on CD36/fibrosis-associated compartments. | YES |
| M1A-P005 | M1A-P005-P001 | Contusion SCI glial scar resection | Test whether delayed surgical glial scar resection improves outcome after rat contusion SCI. | Adult female Sprague-Dawley rats received moderate contusion SCI; at 1 WPI, 2 mm of glial scar was excised or sham exposed; BBB scoring and BDA corticospinal/ascending tract tracing were performed. | YES |
| M1A-P005 | M1A-P005-P002 | Dorsal hemisection glial scar resection | Test whether delayed surgical glial scar resection improves outcome after rat dorsal hemisection SCI. | Adult female Sprague-Dawley rats received dorsal hemisection SCI; at 1 WPI, 2 mm of glial scar was excised or sham exposed; BBB scoring and BDA tract tracing were performed. | YES |
| M1A-P007 | M1A-P007-P001 | FnEDA-null versus wildtype mouse contusion SCI | Compare FnEDA-null mice with littermate wildtype controls after T11 contusion SCI, measuring fibronectin isoforms, lesion/fibrotic scar anatomy, fibronectin matrix stability, axonal density, and locomotor recovery across acute, subacute, and chronic time points. | Infinite Horizons impactor, 70 kdyn force, 60 s dwell; 8-10 week male/female FnEDA-null and littermate wildtype mice for genotype comparisons; 8 week female C57BL/6 mice for FnEDA mRNA/protein time course; IHC, western blot, qPCR, DOC digestion, BMS/mBBB scoring. | YES |
| M1A-P008 | M1A-P008-P001 | Uninjured Col1alpha1-positive perivascular fibroblast identity | Map Col1alpha1-GFP-positive cells in uninjured spinal cord and determine whether they resemble perivascular fibroblasts rather than pericytes, endothelial cells, immune cells, or neural lineage cells. | Col1alpha1-GFP mouse spinal cord; light-sheet fluorescence microscopy with LEL-labeled vasculature; sagittal cryosections; immunostaining for CD13, PDGFR-beta, NG2, nestin, alphaSMA, CD45, GFAP, Olig2, PECAM, and related markers. | YES |
| M1A-P008 | M1A-P008-P002 | Contusive SCI fibrotic scar time course | Track entry, expansion, organization, and persistence of Col1alpha1-GFP-positive cells after closed-dura contusive SCI. | Seven- to 9-week-old female Col1alpha1-GFP mice received T8 75 kdyn Infinite Horizon contusion; tissue examined at 0, 3, 4, 5, 7, 14, 28, and 56 DPI by immunohistochemistry, cell density counts, GFAP border analysis, ECM staining, 5-HT axon staining, and LSFM. | YES |
| M1A-P008 | M1A-P008-P003 | Contusion versus dorsal hemisection fibrotic scar geometry | Compare fibrotic scar organization after contusive SCI with intact dura versus dorsal hemisection with dural disruption. | Col1alpha1-GFP mice underwent T8 contusion or dorsal hemisection; 3 and 14 DPI sections were assessed for Col1alpha1-GFP distribution, laminin, fibronectin, GFAP boundary organization, and continuity with meninges. | YES |
| M1A-P008 | M1A-P008-P004 | NG2 lineage tracing for pericyte distinction | Test whether NG2-positive pericytes contribute substantially to the Col1alpha1-positive fibrotic scar after contusive SCI. | Col1alpha1-GFP; NG2-CreER; Rosa26-tdTomato mice received tamoxifen before T8 contusion; 7 and 14 DPI tissue was assessed for spatial overlap between Col1alpha1-GFP-positive fibroblasts, tdTomato-positive NG2-lineage cells, and Glut1-positive vessels. | YES |
| M1A-P009 | M1A-P009-P001 | Type A pericyte-derived scar attenuation | Reduce generation of type A pericyte progeny and measure fibrotic scar/ECM consequences after mouse SCI. | Glast-CreER/R26R-YFP/Rasless C57BL/6J mice, tamoxifen or vehicle, dorsal funiculus incision or dorsal hemisection; PDGFRbeta/YFP lineage tracing, EdU, RNA-seq, qPCR, western blot, and IHC at 5 DPI and 2-4 WPI. | YES |
| M1A-P009 | M1A-P009-P002 | Axonal regeneration after reduced pericyte scarring | Determine whether reduced pericyte-derived scarring permits CST and raphespinal axons to cross or extend caudal to lesion. | Dorsal hemisection in Glast-Rasless mice; BDA/ChR2-GFP tracing of corticospinal projections and 5-HT staining of raphespinal fibers through 18 WPI. | YES |
| M1A-P009 | M1A-P009-P003 | Optogenetic circuit integration after scar attenuation | Test whether regenerated CST axons form functional connections caudal to SCI. | AAV9-CAG-ChR2-GFP or GFP transduction in sensorimotor cortex; in vivo photostimulation and spinal/cortical recordings in vehicle and tamoxifen-treated Glast-Rasless mice at chronic post-injury time points. | YES |
| M1A-P009 | M1A-P009-P004 | Behavioral recovery after reduced pericyte scarring | Evaluate sensorimotor recovery and relation to regenerated axon density after attenuated fibrotic scarring. | Horizontal ladder, CatWalk gait analysis, ChR2-assisted behavioral testing, CST/5-HT axon quantification, and correlation analyses through 18 WPI. | YES |
| M1A-P014 | M1A-P014-P001 | Lesion-remote astrocyte molecular time course | Define LRA transcriptional states in spared tissue rostral and caudal to incomplete SCI. | Young adult male/female mice; T12 unilateral incomplete hemisection; RiboTag astrocyte RNA-seq, whole-tissue RNA-seq, snRNA-seq, and spatial transcriptomics across 3, 7, 14, and 28 DPI. | YES |
| M1A-P014 | M1A-P014-P002 | White matter LRA-microglia niche mapping | Identify lesion-remote white matter astrocyte and microglial states associated with Wallerian degeneration. | Spatial transcriptomic deconvolution and NMF identified WM3/4 astrocytes and Mg2/5 microglia enriched in ipsilesional white matter. | YES |
| M1A-P014 | M1A-P014-P003 | Astrocyte Ccn1 deletion after SCI | Test whether astrocyte-derived CCN1 controls microglial debris handling and recovery. | Aldh1l1-CreERT2;Ccn1-loxP mice with tamoxifen clearance; T12 iSCI; FluoroMyelin/SMI32/IBA1 3D reconstructions, debris clearance assays, and neurological recovery assays through chronic time points. | YES |
| M1A-P014 | M1A-P014-P004 | CCN1 microglial lipid metabolism mechanism | Test whether CCN1 directly reprograms microglial lipid metabolism. | Primary microglia treated with recombinant CCN1 versus vehicle; RNA-seq, cholesterol efflux, lipid droplet and lipid metabolism readouts. | YES |
| M1A-P014 | M1A-P014-P005 | Myelin-damage induction of Ccn1-positive astrocytes | Determine whether myelin damage is sufficient to induce Ccn1-positive astrocytes and whether this state appears in demyelinating disorders. | Intraspinal CFSE-myelin or lysolecithin injections, saporin models, EAE, and human/mouse disorder tissue comparisons. | YES |
| M1A-P021 | M1A-P021-P001 | PDGFRbeta-lineage scar recruitment after transection versus crush SCI | Compare recruitment of PDGFRbeta-positive cells into fibrotic scars after penetrating and non-penetrating SCI. | PDGFRbeta-CreER::R26-TdT mice; T10 complete transection or forceps crush; immunostaining for PDGFRbeta/TdT/CD31/GFAP and time points including 5 DPI, 14 DPI, and 1 MPI. | YES |
| M1A-P021 | M1A-P021-P002 | Mouse fibroblast/pericyte scRNA-seq and lineage tracing | Distinguish fibroblasts, dividing fibroblasts, pericytes/vSMCs, and myofibroblasts after SCI. | PDGFRbeta-CreER::R26-TdT sorted cells from 4 mm lesion-centered tissue at 0, 5, and 14 DPI; 10x scRNA-seq plus Myh11-, NG2-, Col1a2-, and Crabp2-CreER lineage tracing. | YES |
| M1A-P021 | M1A-P021-P003 | CE-F versus LA-F spatial organization in mouse scars | Map meningeal Crabp2/Emb fibroblasts and perivascular/pial Lama1/Lama2 fibroblasts in fibrotic scar subregions. | Immunostaining and lineage tracing after T10 transection and crush SCI; quantification of Emb/Lama1 and Crabp2/Lama2 spatial compartments at 14 DPI. | YES |
| M1A-P021 | M1A-P021-P004 | Rhesus macaque fibrotic scar comparison | Test whether monkey SCI shows fibroblast subtypes and spatial organization similar to mouse scars. | Female rhesus macaques underwent T9 complete transection; lesion core and edge samples at 0, 7, 14, 30 DPI, and 6 MPI were analyzed by scRNA-seq/snRNA-seq and immunostaining. | YES |
| M1A-P021 | M1A-P021-P005 | Fibroblast subtype function assays | Compare CE-F and LA-F functions in lipid metabolism and angiogenesis. | Mouse/monkey scRNA-seq pathway analyses, Bodipy lipid droplet staining, in vitro myelin uptake, RT-qPCR, endothelial tube formation co-culture, and ligand-receptor interaction analysis. | YES |

---

### Pass 3: Experiments Extracted

| Paper ID | Experiment ID | Figure Ref | Species | Strain | Sex | Injury Model | Injury Device | Injury Severity | Vertebral Level | Chronicity (DPI/WPI) | Control Type | Intervention Type | Methods Summary | Experiment Extracted |
|----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M1A-P003 | M1A-P003-E001 | Fig 1A-E | Mus musculus | C57BL/6J | UNKNOWN | Contusion SCI | Infinite Horizons impactor | 70 kdyn | T9 | naive, 1, 2, 12 WPI | Naive spinal cord / earlier post-injury astrocyte states | Injury time course | GFAP/Hoechst histology quantified GFAP-positive area and astrocyte process overlap; GFAP-positive astrocytes isolated by LMD for qPCR of scar-associated genes. | YES |
| M1A-P003 | M1A-P003-E002 | Fig 2A-F | Mus musculus | C57BL/6J primary astrocytes | UNKNOWN | In vitro astrocyte culture | N/A | N/A | N/A | 48 h culture/reseed interval | Primary astrocytes / IL-6 reactive astrocytes / Col-I-SAs on collagen | Removal of type I collagen signaling by reseeding Col-I-SAs onto Poly-D-lysine | P1-P3 primary astrocytes were converted to IL-6-RAs with IL-6/sIL-6R, then to Col-I-SAs on type I collagen; morphology, N-cadherin, GFAP, and SA-marker qPCR were assessed before/after reseeding. | YES |
| M1A-P003 | M1A-P003-E003 | Fig 3A-D | Mus musculus | C57BL/6J primary astrocytes | UNKNOWN | In vitro astrocyte culture | N/A | N/A | N/A | 24 h antibody exposure | Control antibody / control IgG treated Col-I-SAs | Anti-beta1 integrin antibody or anti-N-cadherin neutralizing antibody | Col-I-SAs were treated with beta1-integrin or N-cadherin blocking antibodies and assessed by GFAP/N-cadherin/Hoechst immunostaining and SA-marker qPCR. | YES |
| M1A-P003 | M1A-P003-E004 | Fig 4A-F | Mus musculus | Donor CAG-EGFP; host wildtype C57BL/6J | UNKNOWN | Naive spinal cord astrocyte transplantation | Glass tip stereotaxic injector | 1 x 10^5 Col-I-SAs at 0.5 ul/min | Spinal cord, exact level UNKNOWN | 0, 4, 7, 14, 28 days post-transplantation | Day 0 transplanted SAs / surrounding host astrocytes | EGFP-positive Col-I-SA transplantation into naive spinal cord | EGFP-positive Col-I-SAs were transplanted into naive spinal cord; transplanted SAs and neighboring host astrocytes were examined by GFAP/N-cadherin/Hoechst staining and LMD/qPCR. | YES |
| M1A-P003 | M1A-P003-E005 | Fig 5A-C | Mus musculus | Donor CAG-EGFP; host wildtype C57BL/6J | UNKNOWN | Naive spinal cord astrocyte transplantation | Stereotaxic injector | 1 ug anti-beta1 integrin antibody every 2 days from 2-12 days post-transplantation | Transplant site, exact level UNKNOWN | 14 days post-transplantation | Isotype control antibody | Anti-beta1 integrin antibody after Col-I-SA transplantation | After EGFP-positive Col-I-SA transplantation, anti-beta1 integrin antibody was injected at the transplant site; host EGFP-negative/GFAP-positive/N-cadherin-positive astrocyte recruitment was quantified. | YES |
| M1A-P003 | M1A-P003-E006 | Fig 5D-H | Mus musculus | C57BL/6J | UNKNOWN | Contusion SCI | Infinite Horizons impactor | 70 kdyn | T9 | antibody dosing 14-26 DPI; assessment 28 DPI | Isotype control antibody | Anti-beta1 integrin antibody after SCI | Anti-beta1 integrin antibody was injected into the spinal cord epicenter every 2 days from 14-26 DPI; GFAP/N-cadherin-positive chronic astrocytes and GAP43-positive area were quantified. | YES |
| M1A-P004 | M1A-P004-E001 | Fig 1A-L | Mus musculus | C57BL/6J | Female | Right lateral hemisection SCI | Optimum knife after T10 laminectomy | Right lateral hemisection, ventral/lateral tissue not spared | T10 | 3, 7, 14, 28 DPI | Uninjured / earlier and later post-injury stages | Injury time course spatial transcriptomics | 10x Visium ST and H&E were used to profile tissue-wide gene-expression patterns and scar maturation stages after T10 right lateral hemisection. | YES |
| M1A-P004 | M1A-P004-E002 | Fig 2-Fig 8 | Mus musculus | C57BL/6J | Female | Right lateral hemisection SCI | Optimum knife after T10 laminectomy | Right lateral hemisection | T10 | 3, 7, 14, 28 DPI | Spatial clusters and time-matched scar regions | Cell-state mapping after SCI | ST deconvolution, marker mapping, trajectory analysis, and ligand-receptor analyses were used to describe fibroblast, macrophage, microglia, astrocyte, oligodendrocyte, and endothelial scar-resident states. | YES |
| M1A-P004 | M1A-P004-E003 | Fig 9A-H | Mus musculus | C57BL/6J | Female | Right lateral hemisection SCI | Optimum knife after T10 laminectomy | Right lateral hemisection | T10 | 3, 7, 14, 28 DPI | Earlier post-injury spatial modules | Scar gene-network maturation | WGCNA and co-expression module analyses identified time-correlated scar modules, including ECM-receptor and lysosome-associated modules. | YES |
| M1A-P004 | M1A-P004-E004 | Fig 10A-G | Mus musculus | C57BL/6J | Female | Right lateral hemisection SCI | Optimum knife after T10 laminectomy | Right lateral hemisection | T10 | 3, 7, 14, 28 DPI | Immunostained scar markers / ST scar-marker maps | Scar boundary visualization and phase model | Tissue transparency, laminin/fibronectin/collagen IV immunostaining, and ST maps were used to define scar boundaries and cell fractions across scar maturation phases. | YES |
| M1A-P005 | M1A-P005-E001 | Fig 1-Fig 4 | Rattus norvegicus | Sprague-Dawley | Female | Contusion SCI with delayed glial scar resection | Contusion device UNKNOWN | Moderate contusion; 2 mm scar excision at 1 WPI | Thoracic level UNKNOWN | resection at 1 WPI; behavioral follow-up weekly; histology after BDA survival interval | Contusion SCI sham re-exposure without scar resection | Surgical glial scar resection | Adult female rats received moderate contusion SCI; 1 week later 2 mm of gross glial scar was excised or sham exposed, then BBB locomotor score and BDA tract tracing assessed functional and axonal outcomes. | YES |
| M1A-P005 | M1A-P005-E002 | Fig 1-Fig 4 | Rattus norvegicus | Sprague-Dawley | Female | Dorsal hemisection SCI with delayed glial scar resection | Microsurgical hemisection | Dorsal hemisection; 2 mm scar excision at 1 WPI | Thoracic level UNKNOWN | resection at 1 WPI; behavioral follow-up weekly; histology after BDA survival interval | Dorsal hemisection sham re-exposure without scar resection | Surgical glial scar resection | Adult female rats received dorsal hemisection SCI; 1 week later 2 mm of glial scar was excised or sham exposed, then BBB locomotor score and BDA tracing assessed recovery and axonal labeling. | YES |
| M1A-P007 | M1A-P007-E001 | Fig 1A-G | Mus musculus | C57BL/6 | Female | Contusion SCI | Infinite Horizons IH-0400 | 70 kdyn, 60 s dwell | T11 | uninjured, 3, 7, 21, 90 DPI / 13 weeks | Uninjured spinal cord | Injury time course | Lesion tissue harvested for qPCR and western blot quantification of FnEDA/FnEDB/total fibronectin. | YES |
| M1A-P007 | M1A-P007-E002 | Fig 2A-I | Mus musculus | FnEDA-null and littermate WT | Male and female | Contusion SCI | Infinite Horizons IH-0400 | 70 kdyn, 60 s dwell | T11 | 7, 21, 90 DPI | Wildtype littermate injured mice | FnEDA domain deletion | Western blot and 20 um mid-sagittal IHC sections quantified for total fibronectin, GFAP-defined lesion core/rim, lesion area, and GFAP response. | YES |
| M1A-P007 | M1A-P007-E003 | Fig 3A-F | Mus musculus | FnEDA-null and littermate WT | Male and female | Contusion SCI | Infinite Horizons IH-0400 | 70 kdyn, 60 s dwell | T11 | 7, 21, 90 DPI | Wildtype littermate injured mice | FnEDA domain deletion | DOC/SDS biochemical fractionation separated soluble fibronectin from insoluble matrix-assembled fibronectin in 4 mm lesion-containing cord tissue. | YES |
| M1A-P007 | M1A-P007-E004 | Fig 4A-C | Mus musculus | FnEDA-null and littermate WT | Male and female | Contusion SCI | Infinite Horizons IH-0400 | 70 kdyn, 60 s dwell | T11 | 90 DPI | Wildtype littermate injured mice | FnEDA domain deletion | 20 um mid-sagittal sections stained for SMI-312; axonal staining intensity quantified across distances from lesion center and normalized to 2 mm rostral tissue. | YES |
| M1A-P007 | M1A-P007-E005 | Fig 5A-D | Mus musculus | FnEDA-null and littermate WT | Male and female | Contusion SCI | Infinite Horizons IH-0400 | 70 kdyn, 60 s dwell | T11 | weekly after SCI through final behavioral week | Wildtype littermate injured mice | FnEDA domain deletion | Blinded open-field locomotor scoring using BMS and modified BBB; mice with combined 24 h BMS >1 excluded as improperly injured. | YES |
| M1A-P008 | M1A-P008-E001 | Fig 1A-L | Mus musculus | Col1alpha1-GFP, C57BL/6 background | UNKNOWN | Uninjured spinal cord | N/A | N/A | Spinal cord, exact level UNKNOWN | Uninjured baseline | Marker-negative nonfibroblast lineages / vascular context | Baseline anatomical mapping | Uninjured Col1alpha1-GFP spinal cord was analyzed by LSFM and immunostaining; Col1alpha1-positive cells localized to larger blood vessels, expressed CD13 and PDGFR-beta, and lacked NG2, nestin, alphaSMA, immune, endothelial, astrocyte, oligodendrocyte, and fibrocyte markers. | YES |
| M1A-P008 | M1A-P008-E002 | Fig 2A-H, K-V | Mus musculus | Col1alpha1-GFP, C57BL/6 background | Female | Contusion SCI | Infinite Horizon impactor | 75 kdyn | T8 | 0, 3, 4, 5, 7, 14, 28, 56 DPI | Uninjured spinal cord / earlier post-injury time points | Injury time course | Col1alpha1-GFP mice underwent T8 contusion; sagittal sections and LSFM were used to quantify Col1alpha1-positive cell entry, peak density, chronic persistence, fibrotic scar apposition to GFAP-positive astrocytic border, ECM deposition, vascular association, and 5-HT axon exclusion. | YES |
| M1A-P008 | M1A-P008-E003 | Fig 3A-O | Mus musculus | Col1alpha1-GFP, C57BL/6 background | Female | Contusion SCI | Infinite Horizon impactor | 75 kdyn | T8 | 5, 7, 14 DPI; chronic time points included in text | Uninjured Col1alpha1-positive cell marker profile | Injury-induced marker time course | Col1alpha1-GFP-positive cells in the contusion scar were immunophenotyped for PDGFR-beta, CD13, alphaSMA, and nonfibroblast lineage markers; PDGFR-beta remained broadly expressed, CD13 decreased by 14 DPI, and alphaSMA was transient. | YES |
| M1A-P008 | M1A-P008-E004 | Fig 2I-J, O-V; Fig 3P-T | Mus musculus | Col1alpha1-GFP, C57BL/6 background | Female | Dorsal hemisection SCI | Microsurgical dorsal hemisection | Penetrating injury with dural disruption | T8 | 3, 14 DPI | T8 contusion SCI with intact dura | Dorsal hemisection injury model | Col1alpha1-GFP distribution after dorsal hemisection was compared with contusion; dorsal hemisection produced a Col1alpha1-positive scar continuous with dura, with different laminin/fibronectin organization and similar acute alphaSMA expression. | YES |
| M1A-P008 | M1A-P008-E005 | Fig 4A-L | Mus musculus | Col1alpha1-GFP; NG2-CreER; Rosa26-tdTomato, C57BL/6 background | Female | Contusion SCI | Infinite Horizon impactor | 75 kdyn | T8 | 7 DPI data noted; 14 DPI shown | Uninjured Col1alpha1/NG2 vascular organization | NG2-lineage tracing after contusion | Tamoxifen-induced NG2-CreER lineage tracing labeled NG2-positive pericytes and OPCs before T8 contusion; 14 DPI tissue showed Col1alpha1-positive fibroblasts concentrated at the injury epicenter and NG2-lineage cells largely outside it, with rare overlap. | YES |
| M1A-P009 | M1A-P009-E001 | Fig 1A-G; Fig S1-S2 | Mus musculus | Glast-Rasless-YFP, C57BL/6J background | Male and female | Dorsal funiculus incision / dorsal hemisection SCI | Microsurgical incision/scissors | Dorsal funiculus cut 0.8 mm deep or dorsal hemisection | Mid-thoracic | 5 DPI; 2 WPI | Vehicle-treated Glast-Rasless-YFP mice | Tamoxifen-induced Rasless recombination reducing type A pericyte progeny | Type A pericyte lineage tracing and Rasless recombination were used to reduce PDGFRbeta-positive stromal scar occupancy and fibrosis-associated ECM gene/protein expression after SCI. | YES |
| M1A-P009 | M1A-P009-E002 | Fig S3; Fig 2-Fig 4 | Mus musculus | Glast-Rasless-YFP, C57BL/6J background | Male and female | Dorsal hemisection SCI | Microsurgical hemisection | Dorsal hemisection | Mid-thoracic | 2, 4, 18 WPI | Vehicle-treated injured mice with dense fibrotic scar | Reduced pericyte-derived scarring | IHC and axon tracing assessed CD68 inflammation, GFAP glial border, OPCs, CST and 5-HT axons in animals with dense versus attenuated fibrotic scarring. | YES |
| M1A-P009 | M1A-P009-E003 | Fig 5-Fig 6; Fig S6 | Mus musculus | Glast-Rasless-YFP, C57BL/6J background | Male and female | Dorsal hemisection SCI | Microsurgical hemisection | Dorsal hemisection | Mid-thoracic | 18 WPI | Vehicle-treated injured mice / AAV-GFP controls | ChR2-assisted assessment of regenerated CST function after scar attenuation | AAV9-CAG-ChR2-GFP transduction and in vivo photostimulation with spinal recordings tested whether regenerated CST terminals caudal to lesion evoked postsynaptic activity. | YES |
| M1A-P009 | M1A-P009-E004 | Fig 7A-H; Fig S7 | Mus musculus | Glast-Rasless-YFP, C57BL/6J background | Male and female | Dorsal hemisection SCI | Microsurgical hemisection | Dorsal hemisection | Mid-thoracic | weekly through 18 WPI | Vehicle-treated injured mice | Reduced pericyte-derived scarring | Horizontal ladder, CatWalk, ChR2-assisted behavior, CST/5-HT axon density, and correlation analyses assessed sensorimotor recovery after scar attenuation. | YES |
| M1A-P014 | M1A-P014-E001 | Fig 1; Extended Data Fig 1-3 | Mus musculus | RiboTag and related C57BL/6 background lines | Male and female | Incomplete SCI | Microknife unilateral hemisection | Unilateral T12 incomplete hemisection | T12 | 3, 7, 14, 28 DPI | Healthy spinal cord astrocytes / border-forming astrocytes | Injury time course of lesion-remote astrocytes | RiboTag astrocyte RNA-seq, whole-tissue RNA-seq, snRNA-seq, and spatial transcriptomics profiled LRA states in spared tissue rostral and caudal to lesion. | YES |
| M1A-P014 | M1A-P014-E002 | Fig 2; Extended Data Fig 4-6 | Mus musculus | C57BL/6 background transgenic lines | Male and female | Incomplete SCI | Microknife unilateral hemisection | Unilateral T12 incomplete hemisection | T12 | acute through chronic post-injury time points | Healthy and non-white-matter spatial states | White matter LRA-microglia niche after SCI | NMF and spatial transcriptomic deconvolution identified WM3/4 lesion-remote astrocytes co-localized with Mg2/Mg5 debris-associated microglia in ipsilesional white matter. | YES |
| M1A-P014 | M1A-P014-E003 | Fig 3; Extended Data Fig 7 | Mus musculus | Aldh1l1-CreERT2; Ccn1-loxP | Male and female | Incomplete SCI | Microknife unilateral hemisection | Unilateral T12 incomplete hemisection | T12 | 7, 28, 90 DPI | Wildtype or Ccn1-intact injured mice | Astrocyte-specific Ccn1 deletion | FluoroMyelin, SMI32, and IBA1 3D reconstructions quantified microglial internalized myelin/axon debris, debris clearance, and recovery after astrocyte Ccn1 loss. | YES |
| M1A-P014 | M1A-P014-E004 | Fig 4; Extended Data Fig 8 | Mus musculus | Primary microglia culture | UNKNOWN | In vitro microglia culture | N/A | N/A | N/A | acute culture exposure | Vehicle/BSA-treated microglia | Recombinant CCN1 treatment | Primary microglia RNA-seq, cholesterol efflux, lipid droplet, and lipid metabolism assays tested direct CCN1 effects on microglial lipid handling. | YES |
| M1A-P014 | M1A-P014-E005 | Fig 5; Extended Data Fig 9 | Mus musculus; Homo sapiens tissue comparison | C57BL/6 and disease-model mice; human disorder tissue | Male and female / human sex variable | Myelin injection / lysolecithin / saporin / EAE / human demyelinating pathology | Intraspinal microinjection or disease model | CFSE-myelin, lysolecithin, saporin, or EAE | T12 lateral white matter for injections | 3 days post-myelin; 3, 10, 25 days post-lysolecithin; additional model-specific time points | PBS vehicle or non-demyelinating controls | Myelin damage and demyelinating disease contexts | Myelin debris injection and demyelinating disorder comparisons tested whether Ccn1-positive astrocytes are induced by local myelin damage and conserved across disease contexts. | YES |
| M1A-P021 | M1A-P021-E001 | Fig 1A-I | Mus musculus | PDGFRbeta-CreER::R26-TdT | Male and female | Transection or crush SCI | Microsurgical scissors or forceps | T10 complete transection or 5 s bilateral forceps crush with intact dura | T10 | 0, 5, 14 DPI; 1 MPI | Uninjured spinal cord / 0 DPI | Injury model comparison | PDGFRbeta-lineage tracing and immunostaining compared recruitment of PDGFRbeta-positive cells to lesion cores after penetrating transection versus non-penetrating crush SCI. | YES |
| M1A-P021 | M1A-P021-E002 | Fig 2-Fig 3 | Mus musculus | PDGFRbeta-, Myh11-, NG2-, Col1a2-CreER::R26-TdT | Male and female | Transection SCI with lineage comparisons | Microsurgical scissors | T10 complete transection | T10 | 0, 5, 14 DPI | Pericyte/vSMC lineages and uninjured tissue | Fibroblast lineage/scRNA-seq mapping | FACS-enriched TdT-positive lesion cells were profiled by 10x scRNA-seq and lineage tracing to distinguish fibroblasts, dividing fibroblasts, pericytes/vSMCs, and ECM-producing myofibroblasts. | YES |
| M1A-P021 | M1A-P021-E003 | Fig 4A-E | Mus musculus | PDGFRbeta-CreER; Col1a2-CreER; Crabp2-CreER reporters | Male and female | Transection or crush SCI | Microsurgical scissors or forceps | T10 complete transection or 5 s crush | T10 | 14 DPI | Uninjured fibroblast spatial markers | CE-F versus LA-F scar spatial mapping | Emb/Crabp2 and Lama1/Lama2 immunostaining and lineage tracing mapped meningeal CE-F cells in central scar regions and LA-F cells in peripheral/perivascular scar regions. | YES |
| M1A-P021 | M1A-P021-E004 | Fig 6A-H | Macaca mulatta | Rhesus macaque | Female | Complete transection SCI | Surgical resection/transection | T9 laminectomy with 8 mm spinal cord tissue removed | T9 | 0, 7, 14, 30 DPI; 6 MPI | Uninjured monkey spinal cord / lesion edge versus core | Cross-species scar fibroblast profiling | Monkey lesion core/edge tissue was analyzed by scRNA-seq/snRNA-seq and immunostaining to compare CE-F and LA-F-like fibroblast organization with mouse scars. | YES |
| M1A-P021 | M1A-P021-E005 | Fig 7-Fig 8 | Mus musculus; Macaca mulatta | Mouse fibroblast subtypes and rhesus macaque tissue | Mixed / female monkey | SCI-derived fibroblast analysis plus in vitro assays | N/A for in vitro components | N/A for in vitro components | N/A for in vitro components | SCI time points plus culture assays | CE-F subtype / endothelial cells alone | LA-F lipid transport and angiogenesis function assays | Bodipy lipid droplet staining, myelin uptake, RT-qPCR, GO analysis, endothelial co-culture tube formation, and ligand-receptor analysis compared LA-F and CE-F functional programs. | YES |

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
| -1 (Verify) | 27 | 8 | 0 | 0 | 19 | 30% |
| 0 (Register) | 27 | 8 | 0 | 0 | 19 | 30% |
| 1 (Questions) | 27 | 8 | 0 | 0 | 19 | 30% |
| 2 (Paradigms) | 27 | 8 | 0 | 0 | 19 | 30% |
| 3 (Experiments) | 27 | 8 papers / 36 experiments | 0 | 0 | 19 papers | 30% papers |
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
| Rattus norvegicus | 10116 | YES | REPRESENTED |
| Cavia porcellus | 10141 | — | — |
| Canis lupus familiaris | 9615 | — | — |
| Sus scrofa | 9823 | — | — |
| Macaca mulatta | 9544 | YES | REPRESENTED |
| Homo sapiens | 9606 | YES | REPRESENTED |

### Injury Models (ControlledVocabulary_InjuryModel)

| Model Name | Anatomical Target | Species | Represented in Corpus | Status |
|---|---|---|---|---|
| Thoracic contusion | T8–T11 | Mouse, rat | YES | REPRESENTED |
| Dorsal hemisection | Thoracic | Mouse, rat | YES | REPRESENTED |
| Lateral hemisection | Thoracic | Mouse, rat | YES | REPRESENTED |
| Complete transection | Thoracic | Mouse, rat, monkey | YES | REPRESENTED |
| Crush | Thoracic | Mouse | YES | REPRESENTED |
| Dorsal funiculus incision | Thoracic | Mouse | YES | REPRESENTED |
| Compression | T10 | Mouse, rat | — | — |
| Human traumatic lesion | Variable | Human | — | — |

### Lesion Compartments (ControlledVocabulary_LesionCompartment)

| Compartment Name | Description | Primary/Secondary | Status |
|---|---|---|---|
| Lesion core | Central zone of tissue destruction | PRIMARY | REPRESENTED |
| Fibrotic core | Fibroblast-rich central region | PRIMARY | REPRESENTED |
| Astrocytic border | Glial scar boundary | PRIMARY | REPRESENTED |
| Reactive neural tissue | Altered but intact tissue surrounding lesion | PRIMARY | REPRESENTED |
| Spared white matter | Preserved WM tracts at periphery | PRIMARY | REPRESENTED |
| Spared gray matter | Preserved GM at lesion periphery | PRIMARY | — |
| Cystic cavity | Fluid-filled void within lesion | PRIMARY | — |
| Pericyte border | Mesenchymal cell zone | SECONDARY | REPRESENTED |
| Meningeal fibrosis | Dural involvement | SECONDARY | REPRESENTED |
| Remote spinal cord | Tissue rostral/caudal to lesion | SECONDARY | REPRESENTED |

### Evidence Types (ControlledVocabulary_EvidenceType)

| Evidence Type | Description | Represented in Corpus |
|---|---|---|
| Histological measurement | Quantitative measurement from tissue sections | YES |
| Immunohistochemistry | Labeled cellular/molecular identification | YES |
| Electron microscopy | Ultrastructural observation | — |
| MRI measurement | Imaging-based quantification | — |
| CT imaging | Imaging-based quantification | — |
| Two-photon imaging | Live tissue visualization | — |
| Confocal microscopy | High-resolution cellular imaging | YES |
| Serial section reconstruction | 3D computational reconstruction | — |
| Qualitative histology | Descriptive anatomical characterization | YES |
| Human tissue examination | Autopsy or surgical specimen | — |

### Assays (ControlledVocabulary_Assay)

| Assay Name | Assay Type | Measured Compartment | Represented in Corpus |
|---|---|---|---|
| Lesion area measurement | Histological | Lesion core | YES |
| Cavity volume quantification | Histological | Cystic cavity | — |
| GFAP immunostaining | Immunohistochemistry | Astrocytic border | YES |
| N-cadherin immunostaining | Immunohistochemistry | Astrocytic border | YES |
| GAP43 immunostaining | Immunohistochemistry | Axonal growth near lesion | YES |
| Astrocyte LMD qPCR | Molecular assay | Astrocytic border | YES |
| Collagen staining (Masson's trichrome) | Histological | Fibrotic scar | — |
| Col1alpha1-GFP reporter imaging | Reporter histology | Fibrotic scar / perivascular fibroblasts | YES |
| NG2-CreER lineage tracing | Genetic lineage tracing | Pericyte border / fibrotic scar | YES |
| Light-sheet fluorescence microscopy | 3D imaging | Vascular-associated fibrotic scar | YES |
| Spatial transcriptomics | Spatial omics | Glial scar / lesion border / remote tissue | YES |
| Single-cell RNA-seq | Transcriptomics | Fibrotic scar / scar-resident cells | YES |
| RiboTag RNA-seq | Cell-type transcriptomics | Lesion-remote astrocytes | YES |
| BDA axon tracing | Tract tracing | Axons near lesion | YES |
| BBB locomotor scoring | Behavioral assay | Functional recovery | YES |
| Optogenetic stimulation/recording | Functional circuit assay | Regenerated CST circuitry | YES |
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
| White matter sparing | mm² or % | Spared WM | YES |
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
| 10.1016/j.expneurol.2022.114264 | Tamaru T | 2023 | Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury | S003; anchor for chronic astrocytic scar | 2026-07-15 | PASS 3 COMPLETE |
| PMID:10391368 | Tuszynski MH | 1999 | Human spinal cord retains substantial structural mass in chronic stages after injury | S007; anchor for human chronic pathology | 2026-07-15 | QUEUED PASS -1 |
| 10.1002/jor.20793 | Rasouli A | 2009 | Resection of glial scar following spinal cord injury | S003/S009; anchor for scar resection anatomy | 2026-07-15 | PASS 3 COMPLETE |
| 10.14670/HH-26.45 | Zhang SX | 2011 | Histological repair of damaged spinal cord tissue from chronic contusion injury of rat: a LM observation | S004/S010; lesion core and cavity histology | 2026-07-15 | QUEUED PASS -1 |
| 10.3171/2010.3.SPINE09190 | Hu R | 2010 | Glial scar and neuroregeneration: histological, functional, and magnetic resonance imaging analysis in chronic spinal cord injury | S010; histology plus MRI candidate | 2026-07-15 | QUEUED PASS -1 |
| 10.1523/JNEUROSCI.2524-13.2013 | Soderblom C | 2013 | Perivascular fibroblasts form the fibrotic scar after contusive spinal cord injury | S005; fibrotic scar cell-source candidate | 2026-07-15 | PASS 3 COMPLETE |
| 10.1016/j.cell.2018.02.004 | Dias DO | 2018 | Reducing pericyte-derived scarring promotes recovery after spinal cord injury | S005; pericyte-derived scar candidate | 2026-07-15 | PASS 3 COMPLETE |
| 10.1016/j.ajpath.2016.11.010 | Yokota K | 2017 | Periostin promotes scar formation through the interaction between pericytes and infiltrating monocytes/macrophages after spinal cord injury | S005; pericyte/macrophage scar mechanism | 2026-07-15 | QUEUED PASS -1 |
| 10.1016/j.expneurol.2005.08.009 | Radojicic M | 2005 | Septations in chronic spinal cord injury cavities contain axons | S010; cavity internal architecture | 2026-07-15 | QUEUED PASS -1 |
| 10.1002/term.2450 | Wang N | 2018 | Collagen scaffold combined with human umbilical cord-derived mesenchymal stem cells promote functional recovery after scar resection in rats with chronic spinal cord injury | S009/S010; chronic scar resection/cavity anatomy | 2026-07-15 | QUEUED PASS -1 |
| 10.1089/neu.2015.4374 | Grumbles RM | 2017 | Motoneuron death after human spinal cord injury | S002/S007; human gray matter pathology | 2026-07-15 | QUEUED PASS -1 |
| 10.3171/jns.1997.86.3.0483 | Tator CH | 1997 | Vascular mechanisms in the pathophysiology of human spinal cord injury | S012; human vascular pathology context | 2026-07-15 | QUEUED PASS -1 |
| 10.1089/neu.2005.22.544 | Collazos-Castro JE | 2005 | Motoneuron loss associated with chronic locomotion impairments after spinal cord contusion in the rat | S012; gray matter/motoneuron loss | 2026-07-15 | QUEUED PASS -1 |
| 10.1038/s41586-025-09887-y | McCallum S | 2026 | Lesion-remote astrocytes govern microglia-mediated white matter repair | S011; lesion-remote white matter repair | 2026-07-15 | PASS 3 COMPLETE |
| 10.1007/s12264-022-00897-8 | Gong L | 2023 | Spatiotemporal dynamics of the molecular expression pattern and intercellular interactions in the glial scar response to spinal cord injury | S003; glial scar spatiotemporal organization | 2026-07-15 | PASS 3 COMPLETE |
| 10.1096/fj.202200463R | Hou J | 2022 | Heterogeneity analysis of astrocytes following spinal cord injury at single-cell resolution | S003; astrocyte heterogeneity candidate | 2026-07-15 | QUEUED PASS -1 |
| 10.1038/s41467-024-50564-x | Xue X | 2024 | Heterogeneous fibroblasts contribute to fibrotic scar formation after spinal cord injury in mice and monkeys | S005; cross-species fibrotic scar candidate | 2026-07-15 | PASS 3 COMPLETE |
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
**Total Papers Extracted**: 8 through Pass 3
**Total Experiments**: 36
**Total Observations**: _____  
**Total Claims**: _____  
**Contradictions Found**: _____  

**Notes**:

- 2026-07-15: Tamaru 2023 was first routed through local Ollama (`qwen2.5-coder:32b`) for a second-pass experiment extraction. The model recovered the broad figure-level experiment families but incorrectly propagated in vivo SCI device/model fields into in vitro and transplantation rows. Final tracker rows were manually curated from the open Kyushu University PDF text and kept consistent with the Cooper 2018 granularity standard.
- 2026-07-15: Soderblom 2013 was manually curated from the PubMed Central article text without Ollama because the source text was compact enough for direct extraction. The paper adds perivascular fibroblast identity, T8 contusion fibrotic scar time course, dorsal hemisection comparison, and NG2-lineage distinction experiments.
- 2026-07-15: Five additional full-text papers were curated through Pass 3 from PubMed Central text: Gong 2023, Rasouli 2009, Dias 2018, McCallum 2026, and Xue 2024. Immediate queue papers without accessible full text through current routes (Yokota 2017, Radojicic 2005, Wang 2018, Rosenberg 2005) remain queued for later retrieval rather than abstract-only extraction.

---

**Next Phase**: Module 1B (Consensus Generation) — begins only after all completion criteria met.
