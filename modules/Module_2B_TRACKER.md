# Module 2B: Biomaterials and Scaffold Repair in SCI — Evidence Consolidation and Consensus Readiness

## Overview

This tracker records the post-saturation phase for Module 2A. Module 2B converts the Module 2A scaffold-repair corpus into atomic observations, author claims, evidence links, boundary conditions, and consensus-ready profiles.

**Boundary condition**: Module 2B may prepare consensus profiles, but project-level `Consensus` records should only be created after observations and author claims are linked to source evidence. Full SQL materialization should wait until the first-pass evidence links are complete.

**Input corpus**: Module 2A saturation corpus, 43 experiment-level papers / 84 extracted experiments plus 8 review/map anchors.

**Module 2 first-pass curation freeze**: 2026-07-16. Status: Module 2A corpus is saturated/frozen first pass; Module 2B evidence consolidation started.

---

## Module 2B Goals

| Goal ID | Goal | Output Table / Artifact | Status |
|---|---|---|---|
| M2B-G001 | Extract atomic empirical observations from Module 2A experiments | Observation | STARTED |
| M2B-G002 | Extract author interpretations separately from observations | AuthorClaim | STARTED |
| M2B-G003 | Link each claim to supporting or contradicting observations | EvidenceLink | STARTED |
| M2B-G004 | Cluster evidence by scaffold-repair topic | Consensus-ready evidence profiles | STARTED |
| M2B-G005 | Mark contradictions, material-specific boundaries, and translational limitations | Boundary / contradiction map | STARTED |
| M2B-G006 | Draft consensus statements only after linked evidence exists | Consensus | DEFERRED UNTIL FIRST-PASS LINKS COMPLETE |

---

## Evidence Topic Map

| Topic ID | Consensus-Ready Topic | Primary Papers | Evidence Need | Status |
|---|---|---|---|---|
| M2B-T001 | Scaffold architecture and physical guidance can organize axon/cell growth across SCI lesions | M2A-P004, P005, P008, P010, P011, P018, P021, P035, P037, P039, P040, P042, P043 | Extract channel/alignment/3D-printing observations and distinguish in vitro guidance from in vivo repair | STARTED |
| M2B-T002 | Scaffold-plus-cell combinations improve cell retention and lesion bridging but confound material versus cell effects | M2A-P001, P002, P003, P009, P012, P013, P015, P016, P018, P020, P022, P023, P024, P033, P035, P041, P042 | Extract cell-source, scaffold-carrier, graft survival, differentiation, and functional outcomes | STARTED |
| M2B-T003 | Controlled cargo delivery from scaffolds can modulate inflammation, trophic support, and regeneration | M2A-P007, P013, P025, P026, P027, P028, P030, P031, P036, P037, P038, P040 | Extract cargo identity, release logic, inflammatory/trophic outcome, and functional endpoints | STARTED |
| M2B-T004 | Natural and decellularized ECM scaffolds provide tissue-like microenvironments but produce context-dependent immune and repair effects | M2A-P003, P014, P016, P020, P022, P032 | Extract ECM source, integration, angiogenesis, axon ingrowth, immune reaction, and cell-support outcomes | STARTED |
| M2B-T005 | Chronic scar-resection scaffold strategies are translationally important but depend on lesion completeness and scar/neural-tissue separation | M2A-P001, P002, P003, P006, P009, P015 | Extract chronic lesion preparation, scar/cavity removal, scaffold filling, safety, electrophysiology, and functional outcomes | STARTED |
| M2B-T006 | Large-animal, primate, and human scaffold studies support feasibility more strongly than efficacy | M2A-P001, P009, P015, P017, P029, P030, P033 | Extract safety, species/model, follow-up, adverse events, locomotor/electrophysiology, and endpoint limitations | STARTED |
| M2B-T007 | Conductive/electrical and surface-patch scaffold strategies expand the intervention space beyond passive bridging | M2A-P019, P024, P034, P038, P039 | Extract conductivity, electrical stimulation, patch/surface application, macrophage/neuron response, and functional outcomes | STARTED |
| M2B-T008 | Scaffold repair evidence is mostly positive but limited by abstract-level extraction, combination therapies, and model heterogeneity | M2A-P004-P043; M2A-R001-R008 | Extract boundary conditions, negative/neutral findings, review-map cautions, and places where mechanism exceeds data | STARTED |

---

## Extraction Priority

| Priority | Paper Set | Rationale | Status |
|---|---|---|---|
| 1 | Translational anchors: P001, P009, P015, P017, P029, P030, P033 | Human, canine, and non-human primate studies determine translational boundary conditions | STARTED |
| 2 | Architecture/guidance anchors: P004, P005, P008, P010, P011, P018, P035, P039, P040, P042, P043 | Needed to separate scaffold structure from cargo/cell effects | STARTED |
| 3 | Cargo and release anchors: P007, P025, P026, P027, P028, P030, P031, P036, P037, P038 | Needed for trophic, anti-inflammatory, and timed-release claims | STARTED |
| 4 | ECM/hydrogel anchors: P003, P014, P016, P020, P022, P032 | Needed for material microenvironment and immune-response claims | STARTED |
| 5 | Remaining abstract-level combinatorial papers | Fill topic coverage conservatively; queue full-text upgrades where PMC is available | QUEUED |

---

## Pass 4: Observation Extraction Tracker

| Topic ID | Paper ID | Experiment IDs | Target Observation Types | Status | Notes |
|---|---|---|---|---|---|
| M2B-T006 | M2A-P001, P009, P017, P033 | clinical scaffold/cell experiments | safety, feasibility, electrophysiology, sensory/motor outcomes | STARTED | Human clinical evidence should remain feasibility-oriented |
| M2B-T006 | M2A-P015, P029, P030 | large-animal/primate experiments | locomotor recovery, tissue remodeling, conduction, histology | STARTED | Cross-species bridge between rodent and human claims |
| M2B-T001 | M2A-P004, P005, P008, P010, P011 | scaffold architecture experiments | channels, alignment, 3D printing, hydrogel tubes, axon guidance | STARTED | Core physical-guidance evidence profile |
| M2B-T001 | M2A-P018, P021, P035, P039, P040, P042, P043 | advanced guidance experiments | aligned collagen, magnetic alignment, GelMA channels, conductive fibers, agarose channels, OEC scaffold boundary | STARTED | Includes boundary condition where functional recovery may not track axon regeneration |
| M2B-T002 | M2A-P002, P003, P012, P013, P016, P020, P022, P023, P024, P041, P042 | scaffold-plus-cell experiments | graft survival, differentiation, retention, myelination, repair | STARTED | Combination therapy makes causal attribution difficult |
| M2B-T003 | M2A-P007, P025, P026, P027, P028, P030, P031, P036, P037, P038 | cargo/release experiments | NT-3, bFGF, BDNF/VEGF, steroid, exosomes, timed release | STARTED | Separate scaffold carrier effect from bioactive cargo effect |
| M2B-T004 | M2A-P014, P016, P020, P022, P032 | ECM scaffold experiments | integration, neovascularization, axon ingrowth, immune response, cell support | STARTED | Material source matters: spinal cord, urinary bladder, peripheral nerve, brain, astrocyte ECM |
| M2B-T005 | M2A-P001, P002, P003, P006, P009, P015 | chronic scar/cavity experiments | scar resection, cavity filling, chronicity, safety, function | STARTED | Direct bridge to Module 1 lesion-architecture findings |
| M2B-T007 | M2A-P019, P024, P034, P038, P039 | conductive/electrical/patch experiments | conductivity, electrical stimulation, surface patch, macrophage polarization, axonal response | STARTED | Emerging intervention family |
| M2B-T008 | M2A-R001-R008; P043 | review/boundary records | translational cautions, model heterogeneity, combination-therapy confounding | STARTED | Prevent overclaiming from positive abstract-level studies |

---

## Pass 4A: Atomic Observations Extracted

These rows are tracker-level Observation candidates. They preserve intended database fields while remaining reviewable before materialization into SQL.

| Observation ID | Topic ID | Paper ID | Experiment ID | Figure Ref | Evidence Type | Outcome Type | Observation Value | Normalized Value | Unit | Quantitative | Statistics Reported | Source Section | Extraction Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M2B-O001 | M2B-T006 | M2A-P001 | M2A-P001-E001 | Clinical source page / M1A carried | Clinical intervention | Safety / feasibility | Five complete chronic traumatic SCI patients underwent SSEP/MEP-guided scar excision, autologous BMMC-loaded NeuroRegen scaffold implantation, and 12-month follow-up. | chronic complete human scaffold implantation feasible in small cohort | patients / months | YES | small cohort; adverse-event detail requires full source review | Abstract + source page | medium | Feasibility signal only; not efficacy proof. |
| M2B-O002 | M2B-T006 | M2A-P009 | M2A-P009-E001 | Abstract | Clinical intervention | Safety / neurological outcome | Eight chronic complete SCI patients received hUCB-MSC-loaded NeuroRegen scaffold after neurophysiology-guided scar resection and were followed for one year. | chronic complete human NeuroRegen/hUCB-MSC feasibility cohort | patients / year | YES | abstract-level; exact outcome statistics not yet extracted | Abstract | medium | Similar intervention family as M2A-P001 but different cell source. |
| M2B-O003 | M2B-T006 | M2A-P029 | M2A-P029-E001-E002 | Abstract | Non-human primate intervention | Locomotor recovery / tissue remodeling | Porous PLGA/poly-l-lysine scaffolds implanted after thoracic lateral hemisection improved locomotor recovery in fully hemisected monkeys compared with non-implanted controls and showed appositional healing/tissue remodeling at 12 weeks. | primate scaffold implantation improved locomotion and remodeling | weeks post injury | YES | significant improvement reported in abstract | Abstract | medium | Strong translational bridge but still abstract-level here. |
| M2B-O004 | M2B-T001 | M2A-P004 | M2A-P004-E001-E002 | Abstract | 3D printing / graft scaffold | Axon guidance / relay formation | Biomimetic 3D-printed scaffolds loaded with neural progenitor cells supported host axon entry, graft axon extension into host cord, synaptic relay formation, synaptic transmission, and functional improvement after complete SCI. | 3D printed architecture plus NPCs supports bridge/relay repair | qualitative | YES | statistics not extracted from abstract | Abstract | medium | Architecture and cell effects are bundled. |
| M2B-O005 | M2B-T001 | M2A-P005 | M2A-P005-E001-E002 | Abstract | Aligned hydrogel scaffold | Axon growth / integration | Porous aligned hydrogel tubes integrated with host tissue, reduced scarring relative to gelfoam, guided axon growth along tube surfaces, supported myelination of some axons, and enhanced functional recovery. | aligned hydrogel tubes support tissue integration and axon guidance | qualitative | YES | abstract-level; exact values not extracted | Abstract | medium | Important scaffold-only guidance anchor. |
| M2B-O006 | M2B-T001 | M2A-P010 | M2A-P010-E001-E002 | Abstract | Scaffold fabrication / platform | Channel architecture | PLGA 85:15 scaffolds were fabricated with parallel channels to enable testing of scaffold architecture, transplanted cells, and local molecular agents for axon regeneration. | multi-channel PLGA scaffold as combinatorial repair platform | qualitative | NO | not applicable | Abstract | medium | Primarily platform/architecture evidence, not direct functional outcome. |
| M2B-O007 | M2B-T001 | M2A-P011 | M2A-P011-E001-E002 | Abstract | Peptide nanofiber scaffold | Host ingrowth | Self-assembling peptide nanofiber scaffold with neural progenitor and Schwann cells supported host-cell migration, blood-vessel growth, and axonal ingrowth into rat dorsal-column transection sites. | SAPNS creates permissive 3D ingrowth environment | qualitative | YES | exact values not extracted | Abstract | medium | Early peptide scaffold bridge anchor. |
| M2B-O008 | M2B-T001 | M2A-P039 | M2A-P039-E001-E002 | Abstract | Conductive aligned hydrogel / electrical stimulation | Axon regeneration / recovery | Aligned CNT/GelMA hydrogel fibers mimicked axon-like conductive aligned structure; combined with electrical stimulation they promoted neural-cell alignment/differentiation in vitro and were tested for SCI recovery in vivo. | conductive aligned scaffold plus ES promotes neural alignment and repair | qualitative | YES | exact values not extracted | Abstract | medium | Advanced guidance/electrical interface anchor. |
| M2B-O009 | M2B-T002 | M2A-P012 | M2A-P012-E001-E002 | Abstract | PLGA scaffold plus hMSC | Locomotor / electrophysiology | hMSC-seeded PLGA scaffolds implanted into 2-mm complete rat spinal cord defects improved BBB scores and MEP amplitudes relative to scaffold-only controls. | PLGA+hMSC improved function/electrophysiology vs scaffold-only | BBB / MEP | YES | abstract reports approximate BBB 5 vs 2 and MEP 200-300 uV | Abstract | medium | Useful because scaffold-only comparator is present. |
| M2B-O010 | M2B-T002 | M2A-P016 | M2A-P016-E001-E002 | Abstract | dPN matrix plus Schwann cells | Myelinated axons / locomotion | Schwann cells in injectable decellularized peripheral nerve matrix produced larger implants and about twice as many Schwann-cell-myelinated axons as Matrigel grafts while performing similarly in BBB locomotor testing. | iPN improves graft/axon histology vs Matrigel without clear BBB superiority | relative axon count / BBB | YES | "twice as many" reported in abstract | Abstract | medium | Separates histological benefit from locomotor equivalence. |
| M2B-O011 | M2B-T002 | M2A-P041 | M2A-P041-E001-E002 | Abstract | Gelatin scaffold plus engineered cells | Myelination / regeneration | Gelatin sponge scaffold with NT-3-overexpressing Schwann cells and TrkC-overexpressing NSCs enhanced myelination and repair after rat T10 complete transection. | engineered cell/scaffold network promotes myelination | qualitative | YES | exact values not extracted | Abstract | medium | Combination mechanism is highly bundled. |
| M2B-O012 | M2B-T003 | M2A-P025 | M2A-P025-E001-E002 | Abstract | Fibrin scaffold controlled release | Axonal sprouting / function | NT-3 released from fibrin scaffolds increased neuronal fiber growth into adult rat spinal cord lesions by about 1.5- to 3-fold and reduced glial scar formation, but hindlimb motor function did not improve relative to controls. | NT-3 fibrin scaffold improved histology without functional improvement | fold-change | YES | 1.5- to 3-fold fiber growth; function not improved | Abstract | medium | Key positive-histology/negative-function boundary. |
| M2B-O013 | M2B-T003 | M2A-P027 | M2A-P027-E001-E002 | Abstract | HA scaffold plus PLGA cargo | Vascularization / axon growth / locomotion | Structured HA hydrogel with anti-NgR and BDNF/VEGF-loaded PLGA microspheres integrated with host tissue, inhibited inflammation/gliosis, increased vessels and regenerated fibers, and improved locomotor recovery after rat dorsal hemisection. | HA+PLGA multi-cargo scaffold improved repair profile | qualitative | YES | exact values not extracted | Abstract | medium | Multiple active components make attribution difficult. |
| M2B-O014 | M2B-T003 | M2A-P036 | M2A-P036-E001-E002 | Abstract | Sequential-release SilMA scaffold | Immunomodulation / neural differentiation | Dual-phase SilMA hydrogel with PLGA microspheres was designed to release Ang-(1-7) early and NT-3 later, reducing inflammation and promoting neural differentiation/axonal regeneration in SCI repair assays. | staged release scaffold targets inflammation then regeneration | qualitative | YES | exact values not extracted | Abstract | medium | Strong design logic; needs full text for timing and effect sizes. |
| M2B-O015 | M2B-T004 | M2A-P014 | M2A-P014-E001-E002 | Abstract | Injectable ECM hydrogel | Integration / angiogenesis / axon ingrowth | Porcine spinal cord and urinary bladder ECM hydrogels integrated into rat hemisection lesions and stimulated neovascularization and axonal ingrowth, while macrophage/mass response created limitations. | injectable ECM supports ingrowth but immune/material response matters | qualitative | YES | qPCR/histology reported; exact values not extracted | Abstract | medium | Important ECM benefit/boundary observation. |
| M2B-O016 | M2B-T004 | M2A-P032 | M2A-P032-E001-E002 | Abstract | HA hydrogel plus astrocyte ECM | Scar / axon penetration | HA hydrogels containing protoplasmic astrocyte-derived ECM reduced glial scar size and increased axon penetration after SCI compared with other ECM conditions. | astrocyte ECM subtype changes HA hydrogel histology | qualitative | YES | exact values not extracted | Abstract | medium | ECM source/subtype is a material boundary condition. |
| M2B-O017 | M2B-T005 | M2A-P006 | M2A-P006-E001-E002 | Abstract | Chronic scar removal plus anisotropic hydrogel | Conduction / locomotion / tract regrowth | Anisotropic alginate hydrogels implanted after scar removal at 4 WPI in chronic complete thoracic transection supported electrophysiological conductivity, locomotor improvement, host-cell migration, reduced scarring, and multiple tract classes growing through/beyond channels. | chronic scar-removal alginate scaffold supports structural and functional repair | months post engraftment | YES | outcomes up to 3 months; exact stats not extracted | Abstract | medium | Strong chronic bridge to Module 1, but abstract-level here. |
| M2B-O018 | M2B-T005 | M2A-P015 | M2A-P015-E001-E002 | Abstract | Chronic canine scar removal plus NeuroRegen/hUC-MSC | Locomotor / scar response | In chronic canine complete T8 transection, delayed scar removal followed by hUC-MSC-loaded NeuroRegen scaffold promoted locomotor recovery, endogenous neurogenesis, and reduced scar response. | large-animal chronic NeuroRegen+hUC-MSC repair signal | months post injury | YES | exact values not extracted | Abstract | medium | Translational large-animal chronic anchor. |
| M2B-O019 | M2B-T007 | M2A-P034 | M2A-P034-E001-E002 | Abstract | Conductive surface scaffold | Cell survival / repair response | HA demilune scaffold with PPY-coated fibers, RAD16 hydrogel, iNPCs, and curcumin preserved iNPC viability, increased neurite outgrowth/migration in vitro/organotypic culture, and was applied as a minimally invasive surface cap after subacute SCI. | surface-capping conductive scaffold supports cells and repair-associated responses | qualitative | YES | exact values not extracted | Abstract | medium | Surface-capping strategy differs from lesion-filling bridges. |
| M2B-O020 | M2B-T007 | M2A-P038 | M2A-P038-E001-E002 | Abstract | Nanofiber/HA hydrogel patch | Inflammation / electrophysiology / function | Schwann-cell exosome and methylprednisolone composite patch improved rat SCI functional and electrophysiological performance, shifted macrophages toward M2-type response, reduced inflammatory response, and increased neuronal survival. | exosome/steroid surface patch modulates inflammation and repair | qualitative | YES | exact values not extracted | Abstract | medium | Patch covers hematoma surface rather than filling cavity. |
| M2B-O021 | M2B-T008 | M2A-P043 | M2A-P043-E001-E002 | Abstract | OEC-seeded scaffold | Boundary condition | OEC-seeded longitudinal collagen scaffold produced functional improvement in acute SCI, but recovery was not correlated with axon regeneration through the scaffold. | functional recovery can dissociate from scaffold-traversing axon regeneration | qualitative | YES | abstract-level; exact correlation metrics not extracted | Abstract | medium | Prevents overinterpreting all recovery as bridge-mediated axon regeneration. |

---

## Pass 5: Author Claim Extraction Tracker

| Topic ID | Paper ID | Claim Types To Extract | Status |
|---|---|---|---|
| M2B-T006 | M2A-P001, P009, P017, P033 | feasibility; safety; efficacy caution | STARTED |
| M2B-T006 | M2A-P015, P029, P030 | translational implication; large-animal repair | STARTED |
| M2B-T001 | M2A-P004, P005, P010, P011, P039, P043 | architecture; guidance; mechanism; boundary | STARTED |
| M2B-T002 | M2A-P012, P016, P018, P020, P041 | cell retention; differentiation; attribution | STARTED |
| M2B-T003 | M2A-P025, P027, P036, P038 | cargo delivery; histology-function boundary; immunomodulation | STARTED |
| M2B-T004 | M2A-P014, P032 | ECM microenvironment; immune/material boundary | STARTED |
| M2B-T005 | M2A-P006, P015 | chronic repair; scar/cavity preparation | STARTED |
| M2B-T008 | M2A-R001-R008, P043 | review-map cautions; model heterogeneity | STARTED |

---

## Pass 5A: Author Claims Extracted

| Claim ID | Topic ID | Paper ID | Claim Text | Claim Type | Confidence Level | Source Section | Extraction Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| M2B-C001 | M2B-T006 | M2A-P001 | Electrophysiology-guided chronic scar resection followed by NeuroRegen scaffold plus autologous BMMC implantation is feasible in a very small complete chronic human SCI cohort. | conclusion | medium | Abstract / source page | medium | Feasibility only; efficacy remains unproven. |
| M2B-C002 | M2B-T006 | M2A-P009 | NeuroRegen scaffold plus hUCB-MSC implantation after scar resection is safe and potentially beneficial in chronic complete human SCI. | conclusion | medium | Abstract | medium | "Potentially beneficial" should be kept cautious until full clinical endpoints are extracted. |
| M2B-C003 | M2B-T006 | M2A-P029 | Porous biodegradable scaffolds can promote tissue remodeling and functional improvement in non-human primate acute SCI. | conclusion | medium | Abstract | medium | Strong translational species, abstract-level extraction. |
| M2B-C004 | M2B-T001 | M2A-P005 | Aligned hydrogel tubes provide physical guidance that can integrate with SCI lesions, reduce scarring, guide axons, support some myelination, and improve function. | conclusion | medium | Abstract | medium | Scaffold-only comparator to gelfoam makes this high-value for architecture topic. |
| M2B-C005 | M2B-T001 | M2A-P039 | Conductive aligned GelMA/CNT hydrogel fibers can combine regenerative scaffold guidance with electrical stimulation. | implication | medium | Abstract | medium | Needs full-text extraction for in vivo effect sizes and ES protocol. |
| M2B-C006 | M2B-T002 | M2A-P012 | Cell-seeded PLGA scaffolds can outperform scaffold-only controls after complete transection SCI. | conclusion | medium | Abstract | medium | One of the clearer scaffold-only comparator claims. |
| M2B-C007 | M2B-T002 | M2A-P016 | Decellularized peripheral nerve matrix is a clinically oriented alternative to Matrigel for Schwann-cell transplantation after SCI. | implication | medium | Abstract | medium | Histology benefit stronger than locomotor superiority. |
| M2B-C008 | M2B-T003 | M2A-P025 | Scaffold-delivered NT-3 can improve axonal sprouting and scar histology without necessarily improving motor function. | boundary condition | high | Abstract | medium | Important histology-function dissociation. |
| M2B-C009 | M2B-T003 | M2A-P036 | Sequential release scaffolds are designed to match SCI temporal biology by reducing early inflammation and promoting later neuronal differentiation/regeneration. | mechanistic | medium | Abstract | medium | Plausible design claim; full-text timing needed. |
| M2B-C010 | M2B-T004 | M2A-P014 | Injectable ECM-derived hydrogels can integrate into lesions and support ingrowth, but ECM source and host macrophage/material response are important constraints. | boundary condition | medium | Abstract | medium | Useful for avoiding "ECM is uniformly pro-regenerative" overclaim. |
| M2B-C011 | M2B-T005 | M2A-P006 | Chronic scar removal followed by anisotropic alginate hydrogel implantation can support conduction, tract growth, and locomotor recovery in chronic complete transection SCI. | conclusion | medium | Abstract | medium | Strong chronic repair signal, but abstract-level. |
| M2B-C012 | M2B-T005 | M2A-P015 | Large-animal chronic NeuroRegen scaffold plus hUC-MSC implantation after scar removal supports translational feasibility of chronic cavity/scar scaffold repair. | implication | medium | Abstract | medium | Needs full text for functional magnitude and scar-removal details. |
| M2B-C013 | M2B-T007 | M2A-P038 | Surface-applied scaffold patches can modulate the post-SCI inflammatory environment without requiring deep lesion-filling implantation. | implication | medium | Abstract | medium | Distinct intervention geometry. |
| M2B-C014 | M2B-T008 | M2A-P043 | Functional improvement after scaffold/cell treatment should not be assumed to reflect axons regenerating through the scaffold. | boundary condition | high | Abstract | medium | Directly based on negative correlation claim. |

---

## Pass 6: Evidence Links Drafted

| Link ID | Claim ID | Observation ID | Link Type | Strength | Notes |
|---|---|---|---|---|---|
| M2B-L001 | M2B-C001 | M2B-O001 | supports | medium | Small human chronic cohort; feasibility only |
| M2B-L002 | M2B-C002 | M2B-O002 | supports | medium | Abstract-level clinical support |
| M2B-L003 | M2B-C003 | M2B-O003 | supports | medium | Non-human primate bridge evidence |
| M2B-L004 | M2B-C004 | M2B-O005 | supports | medium | Aligned tube observation supports guidance claim |
| M2B-L005 | M2B-C005 | M2B-O008 | supports | medium | Conductive/electrical scaffold observation |
| M2B-L006 | M2B-C006 | M2B-O009 | supports | medium | Scaffold-only comparator present |
| M2B-L007 | M2B-C007 | M2B-O010 | supports | medium | Histological superiority vs Matrigel; BBB similar |
| M2B-L008 | M2B-C008 | M2B-O012 | supports | high | Direct histology-positive/function-negative observation |
| M2B-L009 | M2B-C009 | M2B-O014 | supports | medium | Sequential release design and outcomes |
| M2B-L010 | M2B-C010 | M2B-O015 | supports | medium | ECM ingrowth plus immune/material boundary |
| M2B-L011 | M2B-C011 | M2B-O017 | supports | medium | Chronic scar-removal alginate observation |
| M2B-L012 | M2B-C012 | M2B-O018 | supports | medium | Canine chronic scaffold/cell evidence |
| M2B-L013 | M2B-C013 | M2B-O020 | supports | medium | Surface-patch inflammatory modulation |
| M2B-L014 | M2B-C014 | M2B-O021 | supports | high | Boundary condition explicitly reported |
| M2B-L015 | M2B-C004 | M2B-O004 | contextual_support | low | 3D-printed NPC scaffold also supports guidance but is cell-confounded |
| M2B-L016 | M2B-C006 | M2B-O010 | contextual_support | low | Supports scaffold-cell carrier idea but with different cells/material |

---

## Boundary Conditions Draft

| Boundary ID | Topic ID | Boundary Statement | Supporting Evidence | Status |
|---|---|---|---|---|
| M2B-B001 | M2B-T006 | Human scaffold studies in Module 2A support safety/feasibility more than definitive efficacy. | M2B-O001, O002; M2B-C001, C002 | DRAFT |
| M2B-B002 | M2B-T002 | Scaffold-plus-cell studies often cannot separate material effects from cell-source effects. | M2B-O004, O009, O011; review anchors M2A-R005-R007 | DRAFT |
| M2B-B003 | M2B-T003 | Histological regeneration signals do not guarantee functional recovery. | M2B-O012; M2B-C008 | DRAFT |
| M2B-B004 | M2B-T004 | ECM-derived materials are not interchangeable; source tissue and immune response can change outcomes. | M2B-O015, O016; M2B-C010 | DRAFT |
| M2B-B005 | M2B-T005 | Chronic scar-resection scaffold strategies assume a lesion geometry where scar/cavity can be targeted without sacrificing spared functional tissue. | M2B-O001, O002, O017, O018; Module 1B human lesion architecture | DRAFT |
| M2B-B006 | M2B-T008 | Functional improvement after scaffold treatment may arise from mechanisms other than axons traversing the scaffold. | M2B-O021; M2B-C014 | DRAFT |

---

## Consensus Draft Queue

| Consensus Draft ID | Topic ID | Draft Statement | Evidence Status | Notes |
|---|---|---|---|---|
| M2B-S001 | M2B-T001 | Scaffold architecture can provide physical guidance for axons, cells, and tissue organization after SCI, especially when alignment, channels, or printed geometry match lesion topology. | NEEDS MORE LINKS | Strong but partly confounded by cells/cargo |
| M2B-S002 | M2B-T002 | Scaffold-supported cell transplantation improves retention and repair signals in many SCI models, but attribution is usually shared between scaffold, cell source, and cargo. | NEEDS MORE LINKS | Central Module 2B causality caution |
| M2B-S003 | M2B-T003 | Controlled release from scaffolds can improve trophic and inflammatory repair profiles, but histological benefit may not translate into motor recovery. | NEEDS MORE LINKS | Supported by NT-3 fibrin boundary |
| M2B-S004 | M2B-T004 | ECM and hydrogel scaffolds create permissive microenvironments, but source tissue, immune response, and lesion model determine whether integration is beneficial. | NEEDS MORE LINKS | Requires full-text upgrade for ECM papers |
| M2B-S005 | M2B-T005 | Chronic scar/cavity scaffold repair is plausible when lesion anatomy permits resection/filling, but it must be interpreted with Module 1 lesion-boundary evidence. | NEEDS MORE LINKS | Cross-module bridge to Module 1B |
| M2B-S006 | M2B-T006 | Large-animal, primate, and early human data support translational feasibility of scaffold strategies, while definitive clinical efficacy remains unestablished. | NEEDS MORE LINKS | Important user-facing synthesis point |

## Module 2B Current Count

**Total observations extracted**: 21

**Total author claims extracted**: 14

**Total evidence links drafted**: 16

**Boundary records drafted**: 6

**Consensus draft statements queued**: 6

**Extraction confidence mix**: mostly abstract-level first-pass observations; full-text upgrades should prioritize PMC-available papers before final SQL materialization.
