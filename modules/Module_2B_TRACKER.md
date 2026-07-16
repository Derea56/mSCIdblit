# Module 2B: Biomaterials and Scaffold Repair in SCI — Evidence Consolidation and Consensus Readiness

## Overview

This tracker records the post-saturation phase for Module 2A. Module 2B converts the Module 2A scaffold-repair corpus into atomic observations, author claims, evidence links, boundary conditions, and consensus-ready profiles.

**Boundary condition**: Module 2B may prepare consensus profiles, but project-level `Consensus` records should only be created after observations and author claims are linked to source evidence. Full SQL materialization should wait until the first-pass evidence links are complete.

**Input corpus**: Module 2A saturation corpus, 43 experiment-level papers / 84 extracted experiments plus 8 review/map anchors.

**Module 2 first-pass curation freeze**: 2026-07-16. Status: Module 2A corpus is saturated/frozen first pass; Module 2B evidence consolidation is consensus-ready first pass.

---

## Module 2B Goals

| Goal ID | Goal | Output Table / Artifact | Status |
|---|---|---|---|
| M2B-G001 | Extract atomic empirical observations from Module 2A experiments | Observation | COMPLETE FIRST PASS |
| M2B-G002 | Extract author interpretations separately from observations | AuthorClaim | COMPLETE FIRST PASS |
| M2B-G003 | Link each claim to supporting or contradicting observations | EvidenceLink | COMPLETE FIRST PASS |
| M2B-G004 | Cluster evidence by scaffold-repair topic | Consensus-ready evidence profiles | COMPLETE FIRST PASS |
| M2B-G005 | Mark contradictions, material-specific boundaries, and translational limitations | Boundary / contradiction map | COMPLETE FIRST PASS |
| M2B-G006 | Draft consensus statements only after linked evidence exists | Consensus | CONSENSUS-READY FIRST PASS |

---

## Evidence Topic Map

| Topic ID | Consensus-Ready Topic | Primary Papers | Evidence Need | Status |
|---|---|---|---|---|
| M2B-T001 | Scaffold architecture and physical guidance can organize axon/cell growth across SCI lesions | M2A-P004, P005, P008, P010, P011, P018, P021, P035, P037, P039, P040, P042, P043 | Extract channel/alignment/3D-printing observations and distinguish in vitro guidance from in vivo repair | CONSENSUS-READY FIRST PASS |
| M2B-T002 | Scaffold-plus-cell combinations improve cell retention and lesion bridging but confound material versus cell effects | M2A-P001, P002, P003, P009, P012, P013, P015, P016, P018, P020, P022, P023, P024, P033, P035, P041, P042 | Extract cell-source, scaffold-carrier, graft survival, differentiation, and functional outcomes | CONSENSUS-READY FIRST PASS |
| M2B-T003 | Controlled cargo delivery from scaffolds can modulate inflammation, trophic support, and regeneration | M2A-P007, P013, P025, P026, P027, P028, P030, P031, P036, P037, P038, P040 | Extract cargo identity, release logic, inflammatory/trophic outcome, and functional endpoints | CONSENSUS-READY FIRST PASS |
| M2B-T004 | Natural and decellularized ECM scaffolds provide tissue-like microenvironments but produce context-dependent immune and repair effects | M2A-P003, P014, P016, P020, P022, P032 | Extract ECM source, integration, angiogenesis, axon ingrowth, immune reaction, and cell-support outcomes | CONSENSUS-READY FIRST PASS |
| M2B-T005 | Chronic scar-resection scaffold strategies are translationally important but depend on lesion completeness and scar/neural-tissue separation | M2A-P001, P002, P003, P006, P009, P015 | Extract chronic lesion preparation, scar/cavity removal, scaffold filling, safety, electrophysiology, and functional outcomes | CONSENSUS-READY FIRST PASS |
| M2B-T006 | Large-animal, primate, and human scaffold studies support feasibility more strongly than efficacy | M2A-P001, P009, P015, P017, P029, P030, P033 | Extract safety, species/model, follow-up, adverse events, locomotor/electrophysiology, and endpoint limitations | CONSENSUS-READY FIRST PASS |
| M2B-T007 | Conductive/electrical and surface-patch scaffold strategies expand the intervention space beyond passive bridging | M2A-P019, P024, P034, P038, P039 | Extract conductivity, electrical stimulation, patch/surface application, macrophage/neuron response, and functional outcomes | CONSENSUS-READY FIRST PASS |
| M2B-T008 | Scaffold repair evidence is mostly positive but limited by abstract-level extraction, combination therapies, and model heterogeneity | M2A-P004-P043; M2A-R001-R008 | Extract boundary conditions, negative/neutral findings, review-map cautions, and places where mechanism exceeds data | CONSENSUS-READY FIRST PASS |

---

## Extraction Priority

| Priority | Paper Set | Rationale | Status |
|---|---|---|---|
| 1 | Translational anchors: P001, P009, P015, P017, P029, P030, P033 | Human, canine, and non-human primate studies determine translational boundary conditions | COMPLETE FIRST PASS |
| 2 | Architecture/guidance anchors: P004, P005, P008, P010, P011, P018, P035, P039, P040, P042, P043 | Needed to separate scaffold structure from cargo/cell effects | COMPLETE FIRST PASS |
| 3 | Cargo and release anchors: P007, P025, P026, P027, P028, P030, P031, P036, P037, P038 | Needed for trophic, anti-inflammatory, and timed-release claims | COMPLETE FIRST PASS |
| 4 | ECM/hydrogel anchors: P003, P014, P016, P020, P022, P032 | Needed for material microenvironment and immune-response claims | COMPLETE FIRST PASS |
| 5 | Remaining abstract-level combinatorial papers | Fill topic coverage conservatively; queue full-text upgrades where PMC is available | COMPLETE FIRST PASS |

---

## Pass 4: Observation Extraction Tracker

| Topic ID | Paper ID | Experiment IDs | Target Observation Types | Status | Notes |
|---|---|---|---|---|---|
| M2B-T006 | M2A-P001, P009, P017, P033 | clinical scaffold/cell experiments | safety, feasibility, electrophysiology, sensory/motor outcomes | COMPLETE FIRST PASS | Human clinical evidence should remain feasibility-oriented |
| M2B-T006 | M2A-P015, P029, P030 | large-animal/primate experiments | locomotor recovery, tissue remodeling, conduction, histology | COMPLETE FIRST PASS | Cross-species bridge between rodent and human claims |
| M2B-T001 | M2A-P004, P005, P008, P010, P011 | scaffold architecture experiments | channels, alignment, 3D printing, hydrogel tubes, axon guidance | COMPLETE FIRST PASS | Core physical-guidance evidence profile |
| M2B-T001 | M2A-P018, P021, P035, P039, P040, P042, P043 | advanced guidance experiments | aligned collagen, magnetic alignment, GelMA channels, conductive fibers, agarose channels, OEC scaffold boundary | COMPLETE FIRST PASS | Includes boundary condition where functional recovery may not track axon regeneration |
| M2B-T002 | M2A-P002, P003, P012, P013, P016, P020, P022, P023, P024, P041, P042 | scaffold-plus-cell experiments | graft survival, differentiation, retention, myelination, repair | COMPLETE FIRST PASS | Combination therapy makes causal attribution difficult |
| M2B-T003 | M2A-P007, P025, P026, P027, P028, P030, P031, P036, P037, P038 | cargo/release experiments | NT-3, bFGF, BDNF/VEGF, steroid, exosomes, timed release | COMPLETE FIRST PASS | Separate scaffold carrier effect from bioactive cargo effect |
| M2B-T004 | M2A-P014, P016, P020, P022, P032 | ECM scaffold experiments | integration, neovascularization, axon ingrowth, immune response, cell support | COMPLETE FIRST PASS | Material source matters: spinal cord, urinary bladder, peripheral nerve, brain, astrocyte ECM |
| M2B-T005 | M2A-P001, P002, P003, P006, P009, P015 | chronic scar/cavity experiments | scar resection, cavity filling, chronicity, safety, function | COMPLETE FIRST PASS | Direct bridge to Module 1 lesion-architecture findings |
| M2B-T007 | M2A-P019, P024, P034, P038, P039 | conductive/electrical/patch experiments | conductivity, electrical stimulation, surface patch, macrophage polarization, axonal response | COMPLETE FIRST PASS | Emerging intervention family |
| M2B-T008 | M2A-R001-R008; P043 | review/boundary records | translational cautions, model heterogeneity, combination-therapy confounding | COMPLETE FIRST PASS | Prevent overclaiming from positive abstract-level studies |

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
| M2B-O022 | M2B-T006 | M2A-P017 | M2A-P017-E001 | Abstract | Acute human clinical intervention | Safety / neurological monitoring | Two strictly diagnosed acute complete SCI patients received NeuroRegen scaffold plus MSC transplantation and one-year monitoring. | acute complete human scaffold/MSC feasibility signal | patients / year | YES | n = 2; exact endpoints not extracted | Abstract | medium | Supports feasibility only because cohort is extremely small. |
| M2B-O023 | M2B-T006 | M2A-P033 | M2A-P033-E001-E002 | Abstract | Animal-to-clinical translation | Safety / repair | Collagen scaffold plus hUC-MSC strategy was tested in rat/canine complete transection models and a phase I acute complete human SCI trial. | collagen+hUC-MSC tested across animal and human phase I settings | multi-species | YES | exact human outcome values not extracted | Abstract | medium | Important translational bridge but cell/scaffold effects are bundled. |
| M2B-O024 | M2B-T001 | M2A-P008 | M2A-P008-E001-E002 | Abstract | Aligned nanofiber-hydrogel scaffold | Axon guidance / scar response | Aligned nanofiber-hydrogel scaffold after rat C5 hemi-incision provided nonviral delivery, contact guidance, early aligned axon regeneration, and no excessive inflammatory or scar response. | aligned nanofiber scaffold supports delivery/guidance without excessive scar | 1 WPI early axon assessment | YES | exact values not extracted | Abstract | medium | Combines scaffold guidance with molecular delivery. |
| M2B-O025 | M2B-T001 | M2A-P018 | M2A-P018-E001-E002 | Abstract | Aligned collagen scaffold plus NSPCs | Cell retention / axon guidance | Aligned collagen sponge scaffold supported human spinal cord-derived NSPC transplantation after complete transection SCI and was used to compare hSC-NSPCs with brain-derived NSPCs. | aligned collagen scaffold supports human NSPC repair platform | qualitative | YES | exact values not extracted | Abstract | medium | Cell-source comparison is central, but scaffold provides retention/guidance platform. |
| M2B-O026 | M2B-T001 | M2A-P021 | M2A-P021-E001-E002 | Abstract | Magnetically aligned injectable peptide hydrogel | Axon infiltration | Magnetically responsive self-assembling peptide hydrogels aligned under a 100-Gauss field and were validated for promoting/aliging axon infiltration at SCI sites. | injectable hydrogel topology can be externally aligned | Gauss / qualitative | YES | 100-Gauss alignment condition reported | Abstract | medium | Distinct injectable alignment strategy. |
| M2B-O027 | M2B-T001 | M2A-P035 | M2A-P035-E001-E002 | Abstract | 3D-printed GelMA microchannel scaffold | Circuit repair / function | GelMA microchannel scaffold loaded with hAEC-derived neural-like cells improved neural circuit and hindlimb recovery after rat full transection SCI. | microchannel GelMA scaffold plus hAEC neural-like cells supports circuit repair | qualitative | YES | exact values not extracted | Abstract | medium | Architecture and cell effects are bundled. |
| M2B-O028 | M2B-T001 | M2A-P037 | M2A-P037-E001-E002 | Abstract | Coaxial 3D-printed hierarchical hydrogel | Endogenous NSC recruitment / repair | Coaxial 3D-printed HA/alginate/gelatin-cellulose scaffold delivered timed cues for oxidative-stress control, endogenous NSC migration, neuronal differentiation, and SCI repair. | printed hydrogel can program time-sequenced repair cues | qualitative | YES | exact values not extracted | Abstract | medium | Also belongs to cargo/release topic. |
| M2B-O029 | M2B-T001 | M2A-P042 | M2A-P042-E001-E002 | Abstract | 3D-bioprinted collagen/silk scaffold | Nerve regeneration | 3D-bioprinted collagen/silk fibroin scaffold with spinal-cord-like cavities plus NSCs promoted nerve regeneration after SCI. | bioprinted silk/collagen scaffold plus NSCs supports regeneration | qualitative | YES | exact values not extracted | Abstract | medium | Printed architecture and cell effect bundled. |
| M2B-O030 | M2B-T002 | M2A-P002 | M2A-P002-E001-E002 | Abstract | Chronic scar resection plus collagen/hUC-MSC scaffold | Locomotor / electrophysiology / histology | NeuroRegen collagen scaffold plus hUC-MSCs after 12-week chronic rat scar resection was assessed by locomotion, motor/somatosensory evoked potentials, and histological repair. | chronic rat scaffold/cell repair after scar resection | 12 WPI scar resection | YES | exact values not extracted | Abstract | medium | Chronic repair bridge; full text unavailable in tracker. |
| M2B-O031 | M2B-T002 | M2A-P003 | M2A-P003-E001-E002 | Abstract/source page | dECM scaffold plus hNS/PC | Histological repair / function boundary | Chronic complete SCI scar resection plus dECM hydrogel and hNS/PC transplantation improved histological repair signals but did not show functional recovery in the Module 2A extraction. | histological repair without functional recovery after dECM+hNS/PC chronic repair | qualitative | YES | exact values not extracted | Abstract / source page | medium | Important chronic histology-function boundary. |
| M2B-O032 | M2B-T002 | M2A-P013 | M2A-P013-E001-E002 | Abstract | Chitosan bridge plus NSPC and immobilized cues | Lineage organization | Methacrylamide chitosan hydrogel and conduit bridge delivered adult NSPCs with immobilized IFN-gamma or PDGF-AA to bias neuronal or oligodendrocytic lineages after rat hemisection SCI. | chitosan bridge couples cell delivery with lineage cues | qualitative | YES | exact values not extracted | Abstract | medium | A clear example of scaffold/cell/cue confounding by design. |
| M2B-O033 | M2B-T002 | M2A-P020 | M2A-P020-E001-E002 | Abstract | dSCM/GelMA plus MenSC | Cell support / functional reconstruction | dSCM/GelMA composite scaffold provided a bioactive microenvironment for human menstrual blood-derived stem cells and improved SCI functional reconstruction in rat in vivo testing. | spinal cord dECM/GelMA supports stem-cell repair | qualitative | YES | exact values not extracted | Abstract | medium | ECM and cell effects bundled. |
| M2B-O034 | M2B-T002 | M2A-P022 | M2A-P022-E001-E002 | Abstract | DBM/PDRN/TI-EV/NPC hydrogel | Multimodal regeneration | HA hydrogel with decellularized brain matrix, PDRN, primed MSC EVs, and NPCs induced angiogenesis, anti-inflammatory/anti-apoptotic effects, neural differentiation, regeneration, and functional recovery in rat SCI. | multimodal hydrogel scaffold supports multi-process repair | qualitative | YES | exact values not extracted | Abstract | medium | Highly combinatorial; cannot attribute effect to one component. |
| M2B-O035 | M2B-T002 | M2A-P023 | M2A-P023-E001-E002 | Abstract | Gelatin/alginate + hEnSC + curcumin PLGA | Regeneration / inflammation | Gelatin/alginate hydrogel seeded with hEnSCs and curcumin-loaded PLGA nanoparticles improved regeneration and anti-inflammatory repair effects in rat SCI. | hydrogel+cell+drug nanoparticle strategy improves repair profile | qualitative | YES | exact values not extracted | Abstract | medium | Triple combination limits causal attribution. |
| M2B-O036 | M2B-T002 | M2A-P024 | M2A-P024-E001-E002 | Abstract | Conductive chitosan/alginate + hAEC + Noggin | Neural differentiation / repair | Noggin-loaded nanochitosan/polypyrrole-alginate conductive scaffold supported hAEC attachment/neural differentiation and SCI repair-marker testing in an animal model. | conductive chitosan scaffold supports hAEC differentiation and repair testing | qualitative | YES | exact values not extracted | Abstract | medium | Conductive/cell/growth-factor combination. |
| M2B-O037 | M2B-T003 | M2A-P007 | M2A-P007-E001-E002 | Abstract | Collagen-I scaffold plus miR21 exosomes | Retention / sustained release | CBD-modified miR21-loaded exosomes tethered to collagen-I scaffold improved local exosome retention, sustained release, and SCI repair logic. | collagen scaffold tethers engineered exosomes for sustained delivery | qualitative | YES | exact values not extracted | Abstract | medium | Cargo-delivery exemplar. |
| M2B-O038 | M2B-T003 | M2A-P026 | M2A-P026-E001-E002 | Abstract | bFGF hydrogel | Tissue ingrowth / function | bFGF-incorporated HEMA-MOETACL hydrogel implanted 5 days after T9 complete transection supported regenerating tissue ingrowth and functional recovery by 8 weeks. | delayed bFGF hydrogel supports tissue and functional repair | weeks post injury | YES | exact values not extracted | Abstract | medium | Growth-factor hydrogel anchor. |
| M2B-O039 | M2B-T003 | M2A-P028 | M2A-P028-E001-E002 | Abstract | NT-3 collagen hydrogel | Function / local healing | Injectable collagen hydrogel and NT-3-loaded hydrogel increased functional recovery and altered neuronal growth, scar formation, inflammation, and collagen deposition after hemisection SCI. | injectable NT-3 collagen scaffold supports local healing and function | 1 and 6 WPI | YES | exact values not extracted | Abstract | medium | Complements fibrin/NT-3 boundary. |
| M2B-O040 | M2B-T003 | M2A-P030 | M2A-P030-E001-E002 | Abstract | NT-3/fibroin gelatin scaffold | Conduction / inflammation / regeneration | NT-3/fibroin-modified gelatin sponge scaffold improved canine hindlimb movement, neural conduction, inflammation, vessel formation, synaptic structures, and nerve fiber regeneration. | large-animal NT-3/fibroin scaffold improves conduction and repair profile | qualitative | YES | exact values not extracted | Abstract | medium | Large-animal cargo-release anchor. |
| M2B-O041 | M2B-T003 | M2A-P031 | M2A-P031-E001-E002 | Abstract | PCL/PSA/MP nanofiber scaffold | Inflammation / apoptosis / recovery | PCL/polysialic-acid nanofiber scaffold with methylprednisolone reduced inflammatory cytokines, microglia/macrophage activation, and caspase-3 while supporting axonal regeneration and functional recovery after rat transection. | drug-loaded nanofiber scaffold reduces inflammation and supports regeneration | qualitative | YES | exact values not extracted | Abstract | medium | Anti-inflammatory scaffold/cargo anchor. |
| M2B-O042 | M2B-T003 | M2A-P040 | M2A-P040-E001-E002 | Abstract | Functionalized agarose hydrogel | Timed protein release | PEG/PAA/protein layer-by-layer films over agarose hydrogels provided a strategy for sustained BDNF release from templated SCI channel bridges. | agarose channel scaffold can support controlled protein release | qualitative | NO | release details not extracted | Abstract | medium | Methods anchor for release rather than in vivo efficacy. |
| M2B-O043 | M2B-T004 | M2A-P003 | M2A-P003-E001-E002 | Abstract/source page | dECM scaffold after chronic scar resection | Angiogenesis / histology | dECM hydrogel scaffold after chronic complete SCI scar resection supported cavitary lesion filling, vascular endothelial migration, microenvironment changes, and tissue repair signals. | chronic dECM scaffold supports histological repair after scar resection | qualitative | YES | exact values not extracted | Abstract/source page | medium | Chronic ECM scaffold anchor. |
| M2B-O044 | M2B-T004 | M2A-P020 | M2A-P020-E001-E002 | Abstract | spinal cord dECM/GelMA scaffold | Bioactive microenvironment | dSCM/GelMA composite scaffold retained bioactive spinal cord matrix components and favorable microstructure/mechanics for stem-cell support. | spinal-cord-derived ECM/GelMA recreates local matrix niche | qualitative | YES | exact values not extracted | Abstract | medium | Material microenvironment observation. |
| M2B-O045 | M2B-T004 | M2A-P022 | M2A-P022-E001-E002 | Abstract | decellularized brain matrix hydrogel | Multimodal repair | Decellularized brain matrix within HA hydrogel contributed to a composite scaffold designed to support angiogenesis, anti-inflammation, anti-apoptosis, and neural differentiation. | brain-derived ECM is used as bioactive component in multimodal scaffold | qualitative | YES | exact values not extracted | Abstract | medium | ECM component cannot be isolated from other cargos. |
| M2B-O046 | M2B-T005 | M2A-P001 | M2A-P001-E002 | Clinical source page / M1A carried | Human resected scar histology | Scar identity | Resected chronic human scar tissue was immunostained for CSPGs, vimentin, NF, nestin, Tuj-1, and S100 to verify scar identity before interpreting scaffold implantation. | chronic human resection target can be scar-marker rich and neural-marker poor | qualitative | YES | exact marker values not extracted | Source page / M1A carried | medium | Cross-links Module 1 lesion anatomy with scaffold targeting. |
| M2B-O047 | M2B-T005 | M2A-P009 | M2A-P009-E001 | Abstract | Chronic human scar resection plus scaffold/cell | Safety / sensory recovery | Chronic complete SCI patients underwent scar resection and NeuroRegen/hUCB-MSC implantation with safety and neurological/electrophysiological follow-up. | chronic human scar-resection scaffold strategy feasible | patients / year | YES | exact values not extracted | Abstract | medium | Human chronic strategy but efficacy remains cautious. |
| M2B-O048 | M2B-T007 | M2A-P019 | M2A-P019-E001-E002 | Abstract | AFG/fSAP composite hydrogel | Biophysical and biochemical cues | Aligned fibrin hydrogel plus functionalized self-assembling peptide formed an interpenetrating composite presenting structural and biochemical cues to enhance SCI regeneration. | composite hydrogel combines guidance and regulatory cues | qualitative | YES | exact values not extracted | Abstract | medium | Connects passive guidance to active cue delivery. |
| M2B-O049 | M2B-T008 | M2A-R002-M2A-R004 | Review anchors | Review synthesis | Material taxonomy / translation | Hydrogel and biomaterial reviews frame SCI scaffolds as bridges, delivery reservoirs, and cell carriers, but emphasize that material class, lesion geometry, and combination therapy determine interpretability. | review-map supports material- and model-specific interpretation | N/A | qualitative | NO | review-level | Review map | medium | Prevents one-size-fits-all scaffold conclusions. |
| M2B-O050 | M2B-T008 | M2A-R005-M2A-R008 | Review anchors | Review synthesis | Cell therapy / chronic translation | Scaffold-supported cell transplantation reviews emphasize that cells, scaffolds, growth factors, timing, and chronic lesion state interact, limiting simple causal claims. | review-map supports combination-therapy caution | N/A | qualitative | NO | review-level | Review map | medium | Supports boundary records B002 and B005. |

---

## Pass 5: Author Claim Extraction Tracker

| Topic ID | Paper ID | Claim Types To Extract | Status |
|---|---|---|---|
| M2B-T006 | M2A-P001, P009, P017, P033 | feasibility; safety; efficacy caution | COMPLETE FIRST PASS |
| M2B-T006 | M2A-P015, P029, P030 | translational implication; large-animal repair | COMPLETE FIRST PASS |
| M2B-T001 | M2A-P004, P005, P010, P011, P039, P043 | architecture; guidance; mechanism; boundary | COMPLETE FIRST PASS |
| M2B-T002 | M2A-P012, P016, P018, P020, P041 | cell retention; differentiation; attribution | COMPLETE FIRST PASS |
| M2B-T003 | M2A-P025, P027, P036, P038 | cargo delivery; histology-function boundary; immunomodulation | COMPLETE FIRST PASS |
| M2B-T004 | M2A-P014, P032 | ECM microenvironment; immune/material boundary | COMPLETE FIRST PASS |
| M2B-T005 | M2A-P006, P015 | chronic repair; scar/cavity preparation | COMPLETE FIRST PASS |
| M2B-T008 | M2A-R001-R008, P043 | review-map cautions; model heterogeneity | COMPLETE FIRST PASS |

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
| M2B-C015 | M2B-T006 | M2A-P017 | Acute complete human NeuroRegen scaffold plus MSC implantation is feasible to test in carefully diagnosed complete SCI, but n = 2 is not efficacy-grade evidence. | boundary condition | high | Abstract | medium | Keeps acute clinical signal appropriately constrained. |
| M2B-C016 | M2B-T006 | M2A-P033 | Collagen scaffold plus hUC-MSC repair has translational continuity across rodent, canine, and phase I human contexts. | implication | medium | Abstract | medium | Strong as translational path, weaker as efficacy proof. |
| M2B-C017 | M2B-T001 | M2A-P004 | Biomimetic 3D-printed spinal cord scaffolds can impose lesion-scale architecture that supports host-graft axonal relay formation. | conclusion | medium | Abstract | medium | Confounded by NPC graft but central to architecture topic. |
| M2B-C018 | M2B-T001 | M2A-P010 | Multi-channel scaffold architecture is a reusable experimental platform for separating geometry, cell, and molecule effects. | implication | medium | Abstract | medium | Platform claim rather than outcome claim. |
| M2B-C019 | M2B-T001 | M2A-P021 | Injectable scaffolds can be given tunable alignment after delivery, expanding guidance strategies beyond prefabricated implants. | implication | medium | Abstract | medium | Based on magnetic peptide hydrogel design. |
| M2B-C020 | M2B-T001 | M2A-P035 | Microchannel GelMA scaffolds can pair geometry with neural-like cell placement to improve repair after complete transection. | conclusion | medium | Abstract | medium | Cell and architecture effects not separable. |
| M2B-C021 | M2B-T002 | M2A-P002 | Chronic rat scar resection plus collagen/hUC-MSC scaffold repair improves enough outcome domains to justify chronic scaffold/cell testing. | conclusion | low | Abstract | medium | Full-text unavailable, so claim is cautious. |
| M2B-C022 | M2B-T002 | M2A-P003 | dECM scaffold plus hNS/PC transplantation can improve chronic lesion histology even when functional recovery remains absent. | boundary condition | high | Abstract/source page | medium | Useful histology-function boundary in chronic complete SCI. |
| M2B-C023 | M2B-T002 | M2A-P013 | Chitosan bridges with immobilized factors are best interpreted as combined scaffold-cell-cue systems rather than scaffold-only interventions. | boundary condition | high | Abstract | medium | Directly designed as combination therapy. |
| M2B-C024 | M2B-T002 | M2A-P020 | Spinal cord-derived dECM/GelMA scaffolds are used to recreate a lesion-local matrix niche for stem-cell survival and repair. | mechanistic | medium | Abstract | medium | Matrix-niche claim; effect attribution remains bundled. |
| M2B-C025 | M2B-T003 | M2A-P007 | Collagen scaffold tethering can convert exosome delivery from diffuse bolus logic into a local sustained-release strategy. | mechanistic | medium | Abstract | medium | Based on collagen-binding exosome design. |
| M2B-C026 | M2B-T003 | M2A-P026 | Growth-factor-loaded hydrogels can support tissue ingrowth and functional recovery after complete transection, but material and trophic effects are inseparable. | conclusion | medium | Abstract | medium | Applies to bFGF/HEMA-MOETACL system. |
| M2B-C027 | M2B-T003 | M2A-P031 | Drug-loaded nanofiber scaffolds can combine physical support with anti-inflammatory treatment after SCI. | conclusion | medium | Abstract | medium | Methylprednisolone/PCL/PSA anchor. |
| M2B-C028 | M2B-T003 | M2A-P040 | Protein-release scaffold methods matter because they can replace cell-based trophic delivery in channel-bridge strategies. | implication | medium | Abstract | medium | Methods anchor, not efficacy anchor. |
| M2B-C029 | M2B-T004 | M2A-P032 | HA hydrogels can be made more or less permissive by the biological identity of incorporated ECM. | conclusion | medium | Abstract | medium | Protoplasmic versus fibrous astrocyte ECM distinction. |
| M2B-C030 | M2B-T004 | M2A-P022 | Decellularized matrix components in multimodal hydrogels are usually one part of a larger regenerative cocktail. | boundary condition | medium | Abstract | medium | Avoids assigning all benefit to DBM alone. |
| M2B-C031 | M2B-T005 | M2A-P001 | Chronic human scar-resection scaffold strategies depend on correctly distinguishing scar-rich target tissue from functionally important spared cord. | boundary condition | high | Source page / M1A carried | medium | Cross-module alignment with Module 1B. |
| M2B-C032 | M2B-T005 | M2A-P006 | Chronic scar removal plus anisotropic scaffold channels can turn a chronic transection cavity into a guided repair substrate in rodents. | conclusion | medium | Abstract | medium | Strong chronic animal model claim. |
| M2B-C033 | M2B-T007 | M2A-P019 | Composite hydrogels can intentionally combine structural guidance with biochemical regulation, blurring scaffold and cargo categories. | implication | medium | Abstract | medium | AFG/fSAP anchor. |
| M2B-C034 | M2B-T007 | M2A-P034 | Surface-capping scaffolds are a distinct repair geometry from implanted lesion bridges and may be useful for modulating exposed injury environments. | implication | medium | Abstract | medium | HA demilune scaffold anchor. |
| M2B-C035 | M2B-T008 | M2A-R001-R008 | The scaffold literature should be synthesized by material, cargo, cell source, injury model, chronicity, and outcome class rather than by a single global pro-repair claim. | synthesis | high | Review map | medium | Central synthesis caution. |
| M2B-C036 | M2B-T008 | M2A-R005-R008 | Chronic translation requires anatomical compatibility between scaffold strategy and lesion architecture, not just a positive acute rodent repair signal. | synthesis | high | Review map / Module 1B bridge | medium | Cross-module synthesis statement. |

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
| M2B-L017 | M2B-C015 | M2B-O022 | supports | high | n = 2 clinical boundary |
| M2B-L018 | M2B-C016 | M2B-O023 | supports | medium | Multi-species translational continuity |
| M2B-L019 | M2B-C017 | M2B-O004 | supports | medium | 3D printed NPC scaffold relay observation |
| M2B-L020 | M2B-C018 | M2B-O006 | supports | medium | Multi-channel PLGA platform observation |
| M2B-L021 | M2B-C019 | M2B-O026 | supports | medium | Magnetic alignment observation |
| M2B-L022 | M2B-C020 | M2B-O027 | supports | medium | GelMA microchannel + hAEC neural-like cells |
| M2B-L023 | M2B-C021 | M2B-O030 | supports | low | Abstract-only chronic rat scaffold/cell support |
| M2B-L024 | M2B-C022 | M2B-O031 | supports | high | Chronic histology-positive/function-negative boundary |
| M2B-L025 | M2B-C023 | M2B-O032 | supports | high | Designed scaffold-cell-cue combination |
| M2B-L026 | M2B-C024 | M2B-O033 | supports | medium | dSCM/GelMA stem-cell support observation |
| M2B-L027 | M2B-C024 | M2B-O044 | contextual_support | medium | Material niche observation |
| M2B-L028 | M2B-C025 | M2B-O037 | supports | medium | Collagen-tethered exosome delivery |
| M2B-L029 | M2B-C026 | M2B-O038 | supports | medium | bFGF hydrogel complete transection observation |
| M2B-L030 | M2B-C027 | M2B-O041 | supports | medium | PCL/PSA/MP anti-inflammatory nanofiber observation |
| M2B-L031 | M2B-C028 | M2B-O042 | supports | medium | Agarose protein-release methods anchor |
| M2B-L032 | M2B-C029 | M2B-O016 | supports | medium | Astrocyte ECM subtype observation |
| M2B-L033 | M2B-C030 | M2B-O034 | supports | medium | DBM/PDRN/TI-EV/NPC multimodal hydrogel observation |
| M2B-L034 | M2B-C030 | M2B-O045 | supports | medium | DBM component boundary |
| M2B-L035 | M2B-C031 | M2B-O046 | supports | high | Resected human scar marker observation |
| M2B-L036 | M2B-C031 | M2B-O001 | contextual_support | medium | Human scar resection feasibility context |
| M2B-L037 | M2B-C032 | M2B-O017 | supports | medium | Chronic anisotropic alginate observation |
| M2B-L038 | M2B-C033 | M2B-O048 | supports | medium | AFG/fSAP combined cue observation |
| M2B-L039 | M2B-C034 | M2B-O019 | supports | medium | HA demilune surface capping observation |
| M2B-L040 | M2B-C035 | M2B-O049 | supports | high | Review-map material taxonomy caution |
| M2B-L041 | M2B-C035 | M2B-O050 | supports | high | Review-map combination therapy caution |
| M2B-L042 | M2B-C036 | M2B-O050 | supports | high | Review-map chronic translation caution |
| M2B-L043 | M2B-C036 | M2B-O046 | contextual_support | medium | Human scar/neural boundary context |
| M2B-L044 | M2B-C004 | M2B-O024 | contextual_support | medium | Aligned nanofiber guidance/delivery support |
| M2B-L045 | M2B-C004 | M2B-O025 | contextual_support | medium | Aligned collagen scaffold guidance/cell-retention support |
| M2B-L046 | M2B-C004 | M2B-O026 | contextual_support | medium | Injectable alignment support |
| M2B-L047 | M2B-C005 | M2B-O048 | contextual_support | medium | Composite structural/biochemical guidance support |
| M2B-L048 | M2B-C006 | M2B-O023 | contextual_support | low | Another scaffold/cell translation context |
| M2B-L049 | M2B-C007 | M2B-O034 | contextual_support | low | ECM/cell-carrier contextual support |
| M2B-L050 | M2B-C008 | M2B-O031 | contextual_support | high | Another histology-positive/function-negative example |
| M2B-L051 | M2B-C009 | M2B-O028 | contextual_support | medium | Timed cue scaffold supports temporal-design concept |
| M2B-L052 | M2B-C010 | M2B-O043 | contextual_support | medium | dECM chronic scaffold context |
| M2B-L053 | M2B-C011 | M2B-O030 | contextual_support | low | Chronic scar-resection scaffold/cell context |
| M2B-L054 | M2B-C012 | M2B-O047 | contextual_support | medium | Human chronic NeuroRegen/hUC-MSC context |
| M2B-L055 | M2B-C013 | M2B-O019 | contextual_support | medium | Surface-capping scaffold context |
| M2B-L056 | M2B-C014 | M2B-O012 | contextual_support | medium | Functional dissociation also seen with NT-3 fibrin |

---

## Boundary Conditions Draft

| Boundary ID | Topic ID | Boundary Statement | Supporting Evidence | Status |
|---|---|---|---|---|
| M2B-B001 | M2B-T006 | Human scaffold studies in Module 2A support safety/feasibility more than definitive efficacy. | M2B-O001, O002, O022, O023; M2B-C001, C002, C015, C016 | COMPLETE FIRST PASS |
| M2B-B002 | M2B-T002 | Scaffold-plus-cell studies often cannot separate material effects from cell-source effects. | M2B-O004, O009, O011, O032-O036; review anchors M2A-R005-R007 | COMPLETE FIRST PASS |
| M2B-B003 | M2B-T003 | Histological regeneration signals do not guarantee functional recovery. | M2B-O012, O031; M2B-C008, C022 | COMPLETE FIRST PASS |
| M2B-B004 | M2B-T004 | ECM-derived materials are not interchangeable; source tissue and immune response can change outcomes. | M2B-O015, O016, O043-O045; M2B-C010, C029, C030 | COMPLETE FIRST PASS |
| M2B-B005 | M2B-T005 | Chronic scar-resection scaffold strategies assume a lesion geometry where scar/cavity can be targeted without sacrificing spared functional tissue. | M2B-O001, O002, O017, O018, O046, O047; Module 1B human lesion architecture | COMPLETE FIRST PASS |
| M2B-B006 | M2B-T008 | Functional improvement after scaffold treatment may arise from mechanisms other than axons traversing the scaffold. | M2B-O021; M2B-C014 | COMPLETE FIRST PASS |
| M2B-B007 | M2B-T001 | Architecture/guidance observations are strongest when scaffold-only or simple controls exist; printed/cell-loaded systems often bundle geometry with graft biology. | M2B-O004-O008, O024-O029; M2B-C017-C020 | COMPLETE FIRST PASS |
| M2B-B008 | M2B-T007 | Conductive and surface-patch scaffolds are emerging categories and should not be collapsed into passive cavity-filling scaffold claims. | M2B-O008, O019, O020, O048; M2B-C005, C013, C033, C034 | COMPLETE FIRST PASS |

---

## Consensus Draft Queue

| Consensus Draft ID | Topic ID | Draft Statement | Evidence Status | Notes |
|---|---|---|---|---|
| M2B-S001 | M2B-T001 | Scaffold architecture can provide physical guidance for axons, cells, and tissue organization after SCI, especially when alignment, channels, or printed geometry match lesion topology. | CONSENSUS-READY FIRST PASS | Supported by O004-O008 and O024-O029; partly confounded by cells/cargo |
| M2B-S002 | M2B-T002 | Scaffold-supported cell transplantation improves retention and repair signals in many SCI models, but attribution is usually shared between scaffold, cell source, and cargo. | CONSENSUS-READY FIRST PASS | Supported by O009-O011 and O030-O036; central Module 2B causality caution |
| M2B-S003 | M2B-T003 | Controlled release from scaffolds can improve trophic and inflammatory repair profiles, but histological benefit may not translate into motor recovery. | CONSENSUS-READY FIRST PASS | Supported by O012-O014 and O037-O042; NT-3 fibrin gives boundary condition |
| M2B-S004 | M2B-T004 | ECM and hydrogel scaffolds create permissive microenvironments, but source tissue, immune response, and lesion model determine whether integration is beneficial. | CONSENSUS-READY FIRST PASS | Supported by O015-O016 and O043-O045 |
| M2B-S005 | M2B-T005 | Chronic scar/cavity scaffold repair is plausible when lesion anatomy permits resection/filling, but it must be interpreted with Module 1 lesion-boundary evidence. | CONSENSUS-READY FIRST PASS | Supported by O001-O002, O017-O018, and O046-O047 |
| M2B-S006 | M2B-T006 | Large-animal, primate, and early human data support translational feasibility of scaffold strategies, while definitive clinical efficacy remains unestablished. | CONSENSUS-READY FIRST PASS | Supported by O001-O003, O018, O022-O023, and O040 |
| M2B-S007 | M2B-T007 | Conductive, electrical, multimodal, and surface-patch scaffolds broaden scaffold repair beyond passive lesion filling by adding electrical interfaces, inflammatory modulation, or surface capping. | CONSENSUS-READY FIRST PASS | Supported by O008, O019-O020, and O048 |
| M2B-S008 | M2B-T008 | Module 2 scaffold evidence is best synthesized by material, cell/cargo combination, lesion chronicity, species, and outcome class rather than as a single uniformly pro-regenerative intervention family. | CONSENSUS-READY FIRST PASS | Supported by O049-O050 and all boundary records |

## Module 2B Current Count

**Total observations extracted**: 50

**Total author claims extracted**: 36

**Total evidence links drafted**: 56

**Boundary records drafted**: 8

**Consensus-ready statements drafted**: 8

**Extraction confidence mix**: mostly abstract-level first-pass observations; full-text upgrades should prioritize PMC-available papers before final SQL materialization.

**Module 2B status**: CONSENSUS-READY FIRST PASS as of 2026-07-16. The evidence base is linked enough for synthesis, but SQL materialization should wait until the same style of exporter/validator used for Module 1 is generalized beyond Module 1-specific scripts.
