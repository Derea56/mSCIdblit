# Module 2A: Biomaterials and Scaffold Repair in SCI — Corpus Building Tracker

## Overview

This tracker monitors systematic population of mSCIdblit with experiment-level evidence on biomaterials, scaffolds, hydrogels, conduits, matrices, and scaffold-supported repair after spinal cord injury.

**Target Corpus**: 30-60 primary research papers + 8-15 reviews, with emphasis on scaffold material, injury model, cargo/cell combination, lesion context, and repair outcome.

## Scope

| Include | Exclude or Defer |
|---|---|
| Scaffold-only and scaffold-plus-cell SCI experiments | Peripheral nerve-only studies unless directly used in SCI |
| Hydrogels, collagen, chitosan, fibrin, PEG, PLGA, decellularized ECM, NeuroRegen, aligned conduits | Pure drug delivery without a material scaffold unless delivery matrix is central |
| Acute, subacute, and chronic SCI when scaffold repair is measured | General biomaterials chemistry without SCI in vivo/in vitro injury relevance |
| Human scaffold/scar-resection studies | Reviews only after primary search phases establish the map |

## Search Strategy Log

| Search ID | Query | Database | Date Executed | Papers Retrieved | Unique Candidate PMIDs | Status | Notes |
|---|---|---|---:|---:|---:|---|---|
| S001 | `spinal cord injury scaffold biomaterial repair` | PubMed | 2026-07-15 | 329 | 20 retained | COMPLETE PHASE 1A | Broad scaffold-repair entry search |
| S002 | `spinal cord injury hydrogel scaffold axon regeneration` | PubMed | 2026-07-15 | 108 | 20 retained | COMPLETE PHASE 1A | Hydrogel and axon-growth focus |
| S003 | `chronic spinal cord injury scar resection scaffold` | PubMed | 2026-07-15 | 7 | 7 retained | COMPLETE PHASE 1A | Chronic cavity/scar-resection bridge to Module 1A |
| S004 | `spinal cord injury collagen scaffold NeuroRegen` | PubMed | 2026-07-15 | — | — | QUEUED PHASE 1B | Rate-limited during first batch; retry slowly |
| S005 | `spinal cord injury decellularized matrix scaffold` | PubMed | 2026-07-15 | — | — | QUEUED PHASE 1B | Rate-limited during first batch; retry slowly |
| S006 | `spinal cord injury chitosan fibrin scaffold` | PubMed | 2026-07-15 | — | — | QUEUED PHASE 1B | Rate-limited during first batch; retry slowly |
| S007 | `spinal cord injury biomaterial scaffold stem cells` | PubMed | 2026-07-15 | — | — | QUEUED PHASE 1B | Rate-limited during first batch; retry slowly |
| S008 | `spinal cord injury aligned scaffold regeneration` | PubMed | 2026-07-15 | — | — | QUEUED PHASE 1B | Rate-limited during first batch; retry slowly |

## Search Saturation Assessment

| Phase | Date | Cumulative Screened PMIDs | New Unique Papers This Phase | Repeat Rate (%) | Saturation Indicator |
|---|---|---:|---:|---:|---|
| Phase 1A | 2026-07-15 | 46 top-window PMIDs | 46 before dedup against future phases | 0.0 within module search window | Early scaffold searches are discovery-rich; not saturated |

## Paper Inventory

| Paper ID | First Author | Year | Title | Species / System | Scaffold or Material | Status | Notes |
|---|---|---:|---|---|---|---|---|
| M2A-P001 | Xiao Z | 2016 | One-year clinical study of NeuroRegen scaffold implantation following scar resection in complete chronic spinal cord injury patients | Human | NeuroRegen collagen scaffold + BMMC | CARRIED FROM M1A | Clinical chronic scar-resection scaffold anchor |
| M2A-P002 | Wang N | 2018 | Collagen scaffold combined with human umbilical cord-derived mesenchymal stem cells promote functional recovery after scar resection in rats with chronic spinal cord injury | Rat | Collagen scaffold + hUC-MSC | CARRIED FROM M1A | Chronic scar-resection scaffold anchor |
| M2A-P003 | Ito K | 2024 | Histological effects of combined therapy involving scar resection, decellularized scaffolds, and human iPSC-NS/PCs transplantation in chronic complete spinal cord injury | Rodent model context | Decellularized scaffold + hNS/PC | CARRIED FROM M1A | Chronic complete SCI scaffold/cell anchor |
| M2A-P004 | Koffler J | 2019 | Biomimetic 3D-printed scaffolds for spinal cord injury repair | Rat | 3D-printed biomimetic scaffold | PHASE 1A CANDIDATE | High-yield scaffold architecture anchor |
| M2A-P005 | Dumont CM | 2019 | Aligned hydrogel tubes guide regeneration following spinal cord injury | Rodent model context | Aligned hydrogel tubes | PHASE 1A CANDIDATE | Alignment/guidance scaffold anchor |
| M2A-P006 | Huang L | 2020 | Anisotropic Alginate Hydrogels Promote Axonal Growth across Chronic Spinal Cord Transections after Scar Removal | Chronic transection model | Anisotropic alginate hydrogel | PHASE 1A CANDIDATE | Chronic scar-removal scaffold bridge |
| M2A-P007 | Liu X | 2022 | A functionalized collagen-I scaffold delivers microRNA 21-loaded exosomes for spinal cord injury repair | Rodent model context | Functionalized collagen-I scaffold | PHASE 1A CANDIDATE | Scaffold cargo-delivery anchor |
| M2A-P008 | Nguyen LH | 2017 | Three-dimensional aligned nanofibers-hydrogel scaffold for controlled non-viral drug/gene delivery to direct axon regeneration in spinal cord injury treatment | Rodent model context | Aligned nanofiber-hydrogel scaffold | PHASE 1A CANDIDATE | Gene/drug delivery plus alignment |
| M2A-P009 | Zhao Y | 2017 | Clinical Study of NeuroRegen Scaffold Combined With Human Mesenchymal Stem Cells for the Repair of Chronic Complete Spinal Cord Injury | Human | NeuroRegen collagen scaffold + hUCB-MSC | PASS 3 ABSTRACT-LEVEL | Human chronic complete SCI scaffold-cell clinical anchor |

## Extraction Pipeline Progress

| Pass | Description | Status |
|---|---|---|
| Pass -1 | Full-text verification | STARTED |
| Pass 0 | Paper registration | STARTED |
| Pass 1 | Research question extraction | STARTED |
| Pass 2 | Experimental paradigm extraction | STARTED |
| Pass 3 | Experiment-level extraction | STARTED |

### Pass -1: Full Text Verification

| Paper ID | Full Text Available | Figures Available | Figure Legends Available | Methods Accessible | Results Section Present | Status |
|---|---|---|---|---|---|---|
| M2A-P001 | SOURCE PAGE / CARRIED FROM M1A | YES | YES | ABSTRACT + source page | ABSTRACT + source page | PASS 3 CARRIED |
| M2A-P002 | NO | NO | NO | ABSTRACT ONLY | ABSTRACT ONLY | PASS 3 ABSTRACT-LEVEL |
| M2A-P003 | SOURCE PAGE / CARRIED FROM M1A | YES | YES | ABSTRACT + source page | ABSTRACT + source page | PASS 3 CARRIED |
| M2A-P004 | PMC AVAILABLE | YES | YES | YES | YES | QUEUED FULL-TEXT UPGRADE; PASS 3 ABSTRACT-LEVEL FOR NOW |
| M2A-P005 | PMC AVAILABLE | YES | YES | YES | YES | QUEUED FULL-TEXT UPGRADE; PASS 3 ABSTRACT-LEVEL FOR NOW |
| M2A-P006 | NO | NO | NO | ABSTRACT ONLY | ABSTRACT ONLY | PASS 3 ABSTRACT-LEVEL |
| M2A-P007 | NO | NO | NO | ABSTRACT ONLY | ABSTRACT ONLY | PASS 3 ABSTRACT-LEVEL |
| M2A-P008 | PMC AVAILABLE | YES | YES | YES | YES | QUEUED FULL-TEXT UPGRADE; PASS 3 ABSTRACT-LEVEL FOR NOW |
| M2A-P009 | PMC AVAILABLE | YES | YES | YES | YES | QUEUED FULL-TEXT UPGRADE; PASS 3 ABSTRACT-LEVEL FOR NOW |

### Pass 1: Research Questions Identified

| Paper ID | Question ID | Research Question Text | Hypothesis Direction | Keywords | Question Extracted |
|---|---|---|---|---|---|
| M2A-P001 | M2A-P001-RQ001 | Is electrophysiology-guided scar resection followed by NeuroRegen scaffold plus autologous BMMC implantation safe and feasible in complete chronic human SCI? | positive | NeuroRegen; scar resection; BMMC; chronic complete SCI; SSEP; MEP | YES |
| M2A-P002 | M2A-P002-RQ001 | Does NeuroRegen collagen scaffold plus hUC-MSC implantation after chronic scar resection improve locomotor, electrophysiological, and histological outcomes in rats? | positive | chronic SCI; scar resection; collagen scaffold; hUC-MSC; evoked potentials; remyelination | YES |
| M2A-P003 | M2A-P003-RQ001 | Does combined scar resection, kidney-derived dECM hydrogel scaffolding, and hNS/PC transplantation improve histological repair in chronic complete SCI? | positive histology / negative function | chronic complete SCI; dECM hydrogel; hNS/PC; scar resection; angiogenesis; host axons | YES |
| M2A-P004 | M2A-P004-RQ001 | Can biomimetic 3D-printed hydrogel scaffolds loaded with neural progenitor cells guide host and graft axons across complete SCI and improve function? | positive | 3D printing; biomimetic scaffold; NPC; neural relay; complete SCI; axon regeneration | YES (abstract-level) |
| M2A-P005 | M2A-P005-RQ001 | Can modular aligned hydrogel tubes integrate into SCI lesions, reduce scarring, guide axon growth, and improve functional recovery? | positive | aligned hydrogel tubes; porosity; axon guidance; glial scar; myelination; recovery | YES (abstract-level) |
| M2A-P006 | M2A-P006-RQ001 | Do anisotropic alginate hydrogels implanted after scar removal support axonal growth, electrophysiological conduction, and locomotor recovery in chronic complete transection SCI? | positive | anisotropic alginate hydrogel; chronic transection; scar removal; raphaespinal axons; propriospinal axons; locomotion | YES (abstract-level) |
| M2A-P007 | M2A-P007-RQ001 | Can collagen-I scaffolds tether engineered miR21-loaded exosomes to improve local retention, sustained release, and SCI repair? | positive | collagen-I scaffold; exosomes; miR21; collagen-binding domain; sustained release; SCI repair | YES (abstract-level) |
| M2A-P008 | M2A-P008-RQ001 | Can a three-dimensional aligned nanofiber-hydrogel scaffold provide sustained nonviral delivery and contact guidance for axon regeneration after cervical hemi-incision SCI? | positive | aligned nanofibers; hydrogel; nonviral delivery; cervical hemi-incision; axon regeneration; scar | YES (abstract-level) |
| M2A-P009 | M2A-P009-RQ001 | Is NeuroRegen scaffold plus human umbilical cord MSC implantation safe and potentially efficacious after scar resection in chronic complete human SCI? | positive | NeuroRegen; hUCB-MSC; chronic complete SCI; scar resection; MEP; sensory recovery | YES (abstract-level) |

### Pass 2: Experimental Paradigms Identified

| Paper ID | Paradigm ID | Paradigm Name | Description | Methodology | Paradigm Extracted |
|---|---|---|---|---|---|
| M2A-P001 | M2A-P001-P001 | Human scar resection and NeuroRegen scaffold implantation | Assess feasibility and safety of electrophysiology-guided scar resection followed by NeuroRegen scaffold plus autologous BMMC implantation. | Five complete chronic traumatic SCI patients; MRI localization, intraoperative SSEP/MEP scar-boundary mapping, scar excision, BMMC-loaded NeuroRegen scaffold implantation, and 12-month follow-up. | YES |
| M2A-P001 | M2A-P001-P002 | Resected human scar tissue characterization | Confirm that excised tissue represented scar rather than preserved neural tissue. | Resected scar samples were formalin-fixed and immunostained for CSPGs, vimentin, NF, nestin, Tuj-1, and S100. | YES |
| M2A-P002 | M2A-P002-P001 | Chronic scar resection safety | Test whether surgical scar resection affects locomotor function after chronic rat SCI. | Adult rats with 12-week chronic SCI underwent scar tissue resection from the lesion area and locomotor outcome was assessed. | YES (abstract-level) |
| M2A-P002 | M2A-P002-P002 | NeuroRegen scaffold plus hUC-MSC implantation | Test whether collagen scaffold plus hUC-MSCs repair the resected chronic cavity. | NeuroRegen collagen scaffold and hUC-MSCs were implanted into the resected cavity; locomotion, motor/somatosensory evoked potentials, and histological repair were assessed. | YES (abstract-level) |
| M2A-P003 | M2A-P003-P001 | Chronic scar resection plus dECM scaffold histology | Evaluate histological repair after scar resection and decellularized scaffold filling of chronic complete SCI cavities. | Chronic complete SCI model; scar resection and dECM hydrogel scaffold were used to address cavitary lesions and tissue support. | YES |
| M2A-P003 | M2A-P003-P002 | hNS/PC transplantation in scaffold-supported chronic lesion | Test whether hNS/PC transplantation combined with scaffold support alters histological repair after chronic scar resection. | Human iPSC-derived neural stem/progenitor cells were combined with scar resection and dECM scaffold support; source page/abstract emphasized histological effects. | YES |
| M2A-P004 | M2A-P004-P001 | 3D-printed biomimetic scaffold fabrication and scaling | Create rodent-tailored and human-scalable biomimetic CNS scaffold architectures using microscale continuous projection printing. | uCPP hydrogel scaffold printing tailored to rodent spinal cord dimensions and scalable to human lesion geometries. | YES (abstract-level) |
| M2A-P004 | M2A-P004-P002 | NPC-loaded biomimetic scaffold repair after complete SCI | Test whether NPC-loaded 3D-printed scaffolds support host axon entry, graft axon exit, synaptic relay formation, and functional recovery. | Complete rodent SCI; NPC-loaded biomimetic hydrogel scaffold implantation; axon regeneration, host-graft synapses, synaptic transmission, and functional outcomes assessed. | YES (abstract-level) |
| M2A-P005 | M2A-P005-P001 | Porous aligned hydrogel tube implantation | Test whether modular hydrogel tubes conform to SCI defects, integrate with host tissue, and guide axon growth. | Porous hydrogel tubes with 66.5% porosity assembled in an SCI lesion; host integration, immune infiltration, glial scar, and axon growth assessed against gelfoam control. | YES (abstract-level) |
| M2A-P005 | M2A-P005-P002 | Hydrogel tube axon density and functional recovery | Quantify axon density, myelination, and functional recovery after aligned hydrogel tube implantation. | Axon density and myelination within tubes were quantified; functional recovery was compared with control. | YES (abstract-level) |
| M2A-P006 | M2A-P006-P001 | Chronic transection scar resection plus alginate hydrogel engraftment | Test whether anisotropic alginate hydrogels improve conduction and locomotion after scar removal in chronic complete transection SCI. | Chronic thoracic transection; scar resection 4 weeks post-injury; anisotropic alginate hydrogel implantation; electrophysiology and locomotor function assessed up to 3 months. | YES (abstract-level) |
| M2A-P006 | M2A-P006-P002 | Tract-specific axon regeneration through alginate scaffold | Determine which descending and ascending projections regenerate through anisotropic alginate hydrogel channels after chronic SCI. | Histology assessed host cell migration, fibroglial scarring, corticospinal, raphaespinal, propriospinal, and sensory axons within and beyond the scaffold. | YES (abstract-level) |
| M2A-P007 | M2A-P007-P001 | Engineered exosome-collagen scaffold construction | Generate CBD-modified miR21-loaded exosomes and tether them to collagen-I scaffold for local retention and sustained delivery. | CBD-Lamp2b and miR21 were overexpressed in HEK293T cells; engineered exosomes were bound to collagen-I scaffold and evaluated for retention/release logic. | YES (abstract-level) |
| M2A-P007 | M2A-P007-P002 | Functionalized collagen-I scaffold SCI repair | Test whether CBD-LP-miR21-exosome collagen scaffold benefits SCI repair. | Functionalized collagen-I scaffold enriched with miR21-loaded exosomes was applied to SCI repair and assessed for repair benefit according to PubMed abstract. | YES (abstract-level) |
| M2A-P008 | M2A-P008-P001 | Aligned nanofiber-hydrogel scaffold in cervical hemi-incision SCI | Test whether aligned nanofiber-hydrogel scaffold provides contact guidance and sustained nonviral delivery after rat cervical hemi-incision SCI. | Rat C5 hemi-incision model; 3D aligned nanofiber-hydrogel scaffold; nonviral protein/nucleic-acid delivery; early aligned axon regeneration assessed. | YES (abstract-level) |
| M2A-P008 | M2A-P008-P002 | Scaffold inflammatory and scar response | Determine whether aligned nanofiber-hydrogel scaffold triggers excessive inflammation or scar formation. | Inflammatory response and scar tissue formation were assessed after scaffold implantation according to PubMed abstract. | YES (abstract-level) |
| M2A-P009 | M2A-P009-P001 | Human NeuroRegen plus hUCB-MSC clinical implantation | Assess safety and possible efficacy of NeuroRegen scaffold loaded with hUCB-MSCs after scar resection in chronic complete SCI patients. | Eight chronic complete SCI patients; intraoperative neurophysiological scar identification and resection; NeuroRegen scaffold loaded with hUCB-MSC implantation; 1-year safety and neurological follow-up. | YES (abstract-level) |

### Pass 3: Experiments Extracted

| Paper ID | Experiment ID | Figure Ref | Species | Strain | Sex | Injury Model | Injury Device | Injury Severity | Vertebral Level | Chronicity (DPI/WPI) | Control Type | Intervention Type | Methods Summary | Experiment Extracted |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M2A-P001 | M2A-P001-E001 | Clinical source page / M1A carried | Homo sapiens | N/A | Mixed | Complete chronic traumatic SCI | Clinical SCI / surgical scar resection | Complete chronic SCI | Variable | Chronic; 12-month follow-up | Preoperative baseline / intraoperative electrophysiology | Scar resection + NeuroRegen scaffold + autologous BMMC | Five patients underwent MRI localization, intraoperative SSEP/MEP-guided scar excision, BMMC-loaded NeuroRegen scaffold implantation, and 12-month safety/electrophysiology follow-up. | YES |
| M2A-P001 | M2A-P001-E002 | Clinical source page / M1A carried | Homo sapiens | N/A | Mixed | Complete chronic traumatic SCI | Surgical scar resection | Resected scar tissue | Variable | Chronic | Preserved neural tissue marker comparison | Scar tissue histology | Resected human scar tissue was immunostained for CSPGs, vimentin, NF, nestin, Tuj-1, and S100 to verify scar identity. | YES |
| M2A-P002 | M2A-P002-E001 | Abstract | Rattus norvegicus | Adult rats | UNKNOWN | Chronic SCI with scar resection | Surgical resection | 12-week chronic SCI | UNKNOWN | 12 WPI scar resection | Chronic SCI before implantation | Scar resection | Locomotor function after surgical scar resection was assessed to evaluate safety. | YES (abstract-level) |
| M2A-P002 | M2A-P002-E002 | Abstract | Rattus norvegicus | Adult rats | UNKNOWN | Chronic SCI with scar resection and scaffold/cell implantation | Surgical resection + NeuroRegen scaffold | 12-week chronic SCI | UNKNOWN | Chronic post-resection implantation | Resection/scaffold comparison | Collagen scaffold plus hUC-MSC implantation | NeuroRegen collagen scaffold and hUC-MSCs implanted into the resected cavity were assessed by locomotion, motor/somatosensory evoked potentials, and histological repair outcomes. | YES (abstract-level) |
| M2A-P003 | M2A-P003-E001 | Abstract/source page / M1A carried | Rodent chronic complete SCI model | UNKNOWN | UNKNOWN | Chronic complete SCI with cavitary lesion | Surgical scar resection | Complete chronic lesion | UNKNOWN | Chronic phase | Scar resection/scaffold comparisons | dECM scaffold after scar resection | Histology assessed cavitary lesion filling, vascular endothelial cell migration, microenvironment changes, and tissue repair after scar resection plus kidney-derived dECM hydrogel scaffold. | YES |
| M2A-P003 | M2A-P003-E002 | Abstract/source page / M1A carried | Rodent chronic complete SCI model | UNKNOWN | UNKNOWN | Chronic complete SCI with cavitary lesion | Surgical scar resection + transplantation | Complete chronic lesion | UNKNOWN | Chronic phase | Scaffold/no-cell comparisons | hNS/PC transplantation with scaffold support | Human iPSC-derived NS/PC transplantation was combined with scaffold-supported scar resection to assess graft survival, host axon regeneration, histological repair, and lack of functional recovery. | YES |
| M2A-P004 | M2A-P004-E001 | Abstract | Rodent model / scalable human geometry | N/A | N/A | Complete SCI geometry modeling | uCPP scaffold fabrication | Complete SCI scaffold design | Spinal cord | N/A | Native spinal cord geometry | 3D-printed biomimetic hydrogel scaffold | Microscale continuous projection printing produced biomimetic CNS hydrogel scaffolds tailored to rodent spinal cord dimensions and scalable to human lesion geometries. | YES (abstract-level) |
| M2A-P004 | M2A-P004-E002 | Abstract | Rodent | UNKNOWN | UNKNOWN | Complete SCI | Complete spinal cord injury | Complete SCI | UNKNOWN | Post-implant repair interval UNKNOWN | Injured scaffold/graft comparisons | NPC-loaded 3D-printed scaffold implantation | NPC-loaded biomimetic scaffolds were implanted into complete SCI sites to assess host axon regeneration into the device, NPC axon extension into host cord, synaptic relay formation, synaptic transmission, and functional improvement. | YES (abstract-level) |
| M2A-P005 | M2A-P005-E001 | Abstract | Rodent model context | UNKNOWN | UNKNOWN | SCI defect | Experimental SCI | Lesion defect filled with tubes | UNKNOWN | 1-2 WPI immune/scar assessment | Gelfoam control | Porous aligned hydrogel tube implantation | Modular porous hydrogel tubes were assembled to fill the injury, integrate with host tissue by cell infiltration, and compare immune infiltration and glial scar response against gelfoam. | YES (abstract-level) |
| M2A-P005 | M2A-P005-E002 | Abstract | Rodent model context | UNKNOWN | UNKNOWN | SCI defect | Experimental SCI | Lesion defect filled with tubes | UNKNOWN | Recovery phase UNKNOWN | Gelfoam control | Hydrogel tube axon-guidance scaffold | Hydrogel tubes guided robust axon growth along inner and outer tube surfaces, increased axon density within tubes, supported myelination of a subset of axons, and enhanced functional recovery. | YES (abstract-level) |
| M2A-P006 | M2A-P006-E001 | Abstract | Rattus norvegicus | UNKNOWN | UNKNOWN | Chronic complete thoracic transection SCI | Thoracic transection + scar resection | Complete chronic transection | Thoracic | Scar resection 4 WPI; outcomes up to 3 months after engraftment | Scar resection without hydrogel / pre-engraftment baseline | Anisotropic alginate hydrogel engraftment | After scar resection, anisotropic alginate hydrogels were implanted into the chronic transection cavity and assessed for electrophysiological conductivity and locomotor function. | YES (abstract-level) |
| M2A-P006 | M2A-P006-E002 | Abstract | Rattus norvegicus | UNKNOWN | UNKNOWN | Chronic complete thoracic transection SCI | Thoracic transection + scar resection | Complete chronic transection | Thoracic | Up to 3 months after engraftment | Scar resection comparison | Anisotropic alginate hydrogel channels | Histology assessed host-cell migration, fibroglial scarring, and regeneration of corticospinal, raphaespinal, propriospinal, and ascending sensory axons through and beyond hydrogel channels. | YES (abstract-level) |
| M2A-P007 | M2A-P007-E001 | Abstract | HEK293T cells / scaffold system | HEK293T | N/A | In vitro scaffold delivery model | N/A | N/A | N/A | In vitro | Untethered exosome/scaffold logic | CBD-LP-miR21 exosome collagen tethering | CBD-Lamp2b and miR21 were overexpressed in HEK293T cells to produce engineered exosomes that tether to collagen-I scaffold and support sustained miR21 release. | YES (abstract-level) |
| M2A-P007 | M2A-P007-E002 | Abstract | SCI model context | UNKNOWN | UNKNOWN | SCI | Experimental SCI | UNKNOWN | UNKNOWN | Post-injury repair interval UNKNOWN | Nonfunctionalized scaffold/exosome comparisons | Functionalized collagen-I scaffold with miR21-loaded exosomes | A collagen-I scaffold enriched with CBD-LP-miR21 exosomes was applied to SCI repair to improve exosome retention, sustained release, and repair outcomes. | YES (abstract-level) |
| M2A-P008 | M2A-P008-E001 | Abstract | Rattus norvegicus | UNKNOWN | UNKNOWN | Cervical hemi-incision SCI | Hemi-incision | C5 hemi-incision | C5 | 1 WPI early axon assessment | Injury/scaffold comparison | 3D aligned nanofiber-hydrogel scaffold with nonviral delivery | A 3D aligned nanofiber-hydrogel scaffold provided sustained nonviral delivery of proteins and small noncoding RNAs plus contact guidance after C5 hemi-incision, with aligned axon regeneration observed by 1 WPI. | YES (abstract-level) |
| M2A-P008 | M2A-P008-E002 | Abstract | Rattus norvegicus | UNKNOWN | UNKNOWN | Cervical hemi-incision SCI | Hemi-incision | C5 hemi-incision | C5 | Post-implant response interval UNKNOWN | Injury/scaffold comparison | 3D aligned nanofiber-hydrogel scaffold | Inflammatory response and scar tissue formation were assessed after scaffold implantation, with no excessive inflammatory response or scar formation reported in the abstract. | YES (abstract-level) |
| M2A-P009 | M2A-P009-E001 | Abstract | Homo sapiens | N/A | Mixed/UNKNOWN | Chronic complete SCI | Clinical SCI + surgical scar resection | Chronic complete SCI | Variable | Chronic; 1-year follow-up | Preoperative baseline / safety monitoring | NeuroRegen scaffold + hUCB-MSC implantation | Eight chronic complete SCI patients underwent neurophysiology-guided scar resection and implantation of hUCB-MSC-loaded NeuroRegen scaffold, with adverse events and neurological/electrophysiological outcomes tracked for 1 year. | YES (abstract-level) |

## Module 2A Current Count

**Total papers with experiment-level extraction**: 9

**Total experiments extracted**: 17

**Extraction confidence mix**: 6 carried/source-page experiments from Module 1A-aligned anchors; 11 abstract-level experiments queued for full-text upgrade where possible.
