# Module 17B: TLR Signaling Cascade and Innate Receptor Pathway Architecture - Evidence Consolidation and Query Readiness

## Overview

This tracker converts Module 17A experiments into a queryable signaling graph. The consolidation layer separates canonical pathway membership from context-specific directed edges, perturbation evidence, phenotypes, author claims, and cross-module conditioning context.

**Input corpus**: Module 17A receptor-to-cascade literature, initially seeded from Modules 3, 12, and 13.

**Status**: FIRST-PASS CONSOLIDATION COMPLETE; TARGETED FULL-TEXT UPGRADES QUEUED.

## Evidence Topic Map

| Topic ID | Consensus-Ready Topic | Required Evidence |
|---|---|---|
| M17B-T001 | Receptor and ligand specificity | TLR identity, co-receptor, agonist/antagonist, species, and compartment |
| M17B-T002 | Surface versus endosomal adaptor routing | TIRAP/MAL, TRAM, MyD88, TRIF, trafficking and internalization evidence |
| M17B-T003 | MyD88-proximal kinase cascade | IRAK4/IRAK1/TRAF6/TAK1/IKK/MAPK perturbation and transcriptional outputs |
| M17B-T004 | TRIF-TBK1-IRF3/7 cascade | Endosomal TLR3/TLR4 routing, interferon output, and pathway-specific necessity |
| M17B-T005 | Transcription-factor convergence | Which TLRs activate NF-kappaB, AP-1, IRF3/5/7, STAT1/3 under which contexts |
| M17B-T006 | Pathway intersections | IL-1R/IL-18R, NOD, RIG-I, STING, PI3K-AKT, inflammasome, autophagy, and cell death |
| M17B-T007 | Perturbation phenotypes | Knockout, knockdown, inhibitor, agonist, rescue, and epistasis phenotype matrix |
| M17B-T008 | SCI translation boundaries | Microglia, macrophage, endothelial, oligodendrocyte, axon, lesion, locomotor, pain, and safety outcomes |

## Pass 4A: Atomic Signaling Observations

| Observation ID | Topic ID | Paper ID | Experiment ID | Edge or Pathway Member | Evidence Type | Observation Value | Context | Extraction Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| M17B-O001 | M17B-T002 | M17A-P008 | M17A-P008-E001 | TLR4 -> TRAM -> TRIF | Primary mechanism | Pending full-text extraction | Endosomal routing | uncertain | QUEUED |
| M17B-O002 | M17B-T001 | M17A-P013 | M17A-P013-E001 | TLR2/TLR4 injury signaling | Primary SCI phenotype | SCI increased TLR1/2/4/5/7 and MyD88/NF-kappaB-associated signaling; TLR2-null and TLR4-mutant mice had worse recovery and myelin/glial phenotypes | Traumatic SCI | high | EXTRACTED |
| M17B-O003 | M17B-T004 | M17A-P014 | M17A-P014-E001 | TLR4 -> NF-kappaB and TRIF/IRF3 balance | Primary knockout | TLR4 deficiency increased NF-kappaB-linked inflammatory injury but reduced p-IRF3 and IFN-beta | Acute mouse SCI | high | EXTRACTED |
| M17B-O004 | M17B-T005 | M17A-P015 | M17A-P015-E001 | TLR2/4 -> TNF; TLR3 -> TRIF/IFN-regulated spinal output | Primary comparator | TLR2/4 ligand-induced allodynia was TNF-dependent; TLR3 ligand output was distinct; TRIF/type-I-IFN loss prolonged allodynia | Spinal glia and nociceptive circuits | high | EXTRACTED |
| M17B-O005 | M17B-T004 | M17A-P016 | M17A-P016-E001 | TLR3 -> neuroprotective spinal response | Primary SCI experiment | Poly(I:C) improved neuron volume and swimming after zebrafish lesion; TLR3 inhibition reduced both | Zebrafish SCI | medium | EXTRACTED |
| M17B-O006 | M17B-T005 | M17A-P017 | M17A-P017-E001 | TLR9 -> inflammatory pain response | Primary antagonist | TLR9 antagonist reduced SCI pain hypersensitivity and inflammation; locomotor effect was not established | Mouse traumatic SCI | medium | EXTRACTED |
| M17B-O007 | M17B-T004 | M17A-P018 | M17A-P018-E001 | TBK1 -> IRF3/YAP and noncanonical NF-kappaB | Primary kinase inhibition | TBK1 inhibition reduced astrocyte reactivity, inflammatory cytokines, infiltration, and IRF3 phosphorylation | Mouse SCI astrocytes | high | EXTRACTED |
| M17B-O008 | M17B-T001 | M17A-P019 | M17A-P019-E001 | TLR7 spinal immune expression | Primary viral comparator | TLR7 was enriched in spinal microglia and required for antiviral humoral immunity in EV71 infection; sterile-SCI relevance remains untested | Viral spinal infection | medium | EXTRACTED / BOUNDARY |
| M17B-O009 | M17B-T003 | M17A-P005 | M17A-P005-E001 | TLR2 TIR -> MyD88 | Structural/biochemical mechanism | TLR2 TIR-domain binding specificity supports receptor-adaptor assignment but does not establish SCI phenotype | Receptor-adaptor comparator | medium | EXTRACTED / COMPARATOR |
| M17B-O010 | M17B-T003 | M17A-P006 | M17A-P006-E001 | TLR2 -> MyD88 assembly | Structural/biochemical mechanism | TLR2 TIR interactions assemble a MyD88 signaling platform; cell-state and ligand boundaries retained | Receptor-adaptor comparator | medium | EXTRACTED / COMPARATOR |
| M17B-O011 | M17B-T003 | M17A-P009 | M17A-P009-E001 | MyD88 alternative splicing -> NF-kappaB feedback | Primary mechanism | MyD88S lacks the exon required for IRAK4 recruitment and attenuates MyD88-dependent NF-kappaB signaling | Innate signaling comparator | high | EXTRACTED |
| M17B-O012 | M17B-T005 | M17A-P010 | M17A-P010-E001 | TLR2/TLR4 -> IL-10 mRNA stability | Primary comparator | TLR2 and TLR4 differ in IL-10 transcript stabilization and output despite shared proximal signaling components | Macrophage comparator | medium | EXTRACTED |
| M17B-O013 | M17B-T006 | M17A-P011 | M17A-P011-E001 | TLR2 -> PI3K-AKT | Primary neuroprotection comparator | TLR2 agonism engaged PI3K-AKT-associated survival signaling and reduced ischemic neuronal injury | Brain ischemia comparator | medium | EXTRACTED / COMPARATOR |

## Cross-Module Observation Ledger

| Observation ID | Cross-Index Experiment | Atomic Observation | Evidence Type | Context | Confidence | Status |
|---|---|---|---|---|---|---|
| M17B-O014 | M17A-X001 | LPS preconditioning produced an IL-10/IRF3-associated resident-microglial repair state after SCI. | Primary SCI source-module observation | Traumatic SCI | medium | EXTRACTED / CROSS-MODULE |
| M17B-O015 | M17A-X002 | Repeated LPS primed spinal microglia/endothelium and protected against ischemic SCI. | Primary spinal ischemia observation | Spinal ischemia | high | EXTRACTED / CROSS-MODULE |
| M17B-O016 | M17A-X003 | IL-1R1 participated in the microglia-vascular relay associated with repeated LPS protection. | Primary cross-pathway observation | Spinal ischemia | high | EXTRACTED / CROSS-MODULE |
| M17B-O017 | M17A-X004 | TLR4 tolerance can redirect output toward TRIF/IRF3 with altered NF-kappaB rather than abolishing signaling. | Primary comparator mechanism | Brain ischemia | high | EXTRACTED / CROSS-MODULE |
| M17B-O018 | M17A-X005 | Endothelial MyD88/CXCL10 is a measurable peripheral-to-CNS relay in LPS preconditioning. | Primary comparator mechanism | Brain ischemia | medium | EXTRACTED / CROSS-MODULE |
| M17B-O019 | M17A-X006 | TLR4 is required for an injury-associated oligodendrocyte-formation response. | Primary SCI boundary | Traumatic SCI | medium | EXTRACTED / CROSS-MODULE |
| M17B-O020 | M17A-X007 | Post-injury LPS benefit is distinct from pre-injury conditioning and is timing/context dependent. | Primary SCI source-module observation | Traumatic SCI | medium | EXTRACTED / CROSS-MODULE |
| M17B-O021 | M17A-X008 | Chronic SCI microglia remain responsive to LPS and can re-enter inflammatory/plasticity states. | Primary chronic-SCI observation | Chronic SCI | medium | EXTRACTED / CROSS-MODULE |
| M17B-O022 | M17A-X009 | Hemorrhage changes the relationship between TLR4 expression and microglial activation. | Primary lesion-context boundary | Hemorrhagic SCI | medium | EXTRACTED / CROSS-MODULE |
| M17B-O023 | M17A-X010 | Low-dose LPS preconditioning reduced apoptosis-associated SCI readouts. | Primary SCI source-module observation | Traumatic SCI | medium | EXTRACTED / CROSS-MODULE |
| M17B-O024 | M17A-X011 | LPS preconditioning was associated with Nrf2/antioxidant signaling. | Primary SCI source-module observation | Traumatic SCI | medium | EXTRACTED / CROSS-MODULE |
| M17B-O025 | M17A-X012 | Durable MPLA training required MyD88 and did not require TRIF in macrophages. | Primary comparator mechanism | Trained-immunity comparator | high | EXTRACTED / CROSS-MODULE |
| M17B-O026 | M17A-X013 | TLR2/1 agonism protected the ischemic brain across infarct, barrier, and neurologic endpoints. | Primary comparator mechanism | Brain ischemia | high | EXTRACTED / CROSS-MODULE |
| M17B-O027 | M17A-X014 | TLR2/Pam3CSK4 protection required PI3K-AKT-associated survival signaling. | Primary comparator mechanism | Brain ischemia | high | EXTRACTED / CROSS-MODULE |
| M17B-O028 | M17A-X015 | Pam3CSK4 reduced axonal dieback and oligodendroglial loss in ex vivo SCI tissue. | Primary ex vivo SCI observation | Ex vivo SCI | medium | EXTRACTED / CROSS-MODULE |
| M17B-O029 | M17A-X016 | TLR2 TIR-domain binding supports MyD88 as a receptor-proximal adaptor. | Structural mechanism | Receptor-domain comparator | medium | EXTRACTED / CROSS-MODULE |
| M17B-O030 | M17A-X017 | TLR2 TIR domains nucleate higher-order MyD88 assemblies. | Structural mechanism | Receptor-domain comparator | medium | EXTRACTED / CROSS-MODULE |
| M17B-O031 | M17A-X018 | TLR4 endocytosis is coupled by TRAM to IFN-beta induction. | Primary trafficking mechanism | Receptor-trafficking comparator | high | EXTRACTED / CROSS-MODULE |
| M17B-O032 | M17A-X019 | Endocytic routing changes TLR4 pathway output. | Primary trafficking boundary | Receptor-trafficking comparator | medium | EXTRACTED / CROSS-MODULE |
| M17B-O033 | M17A-X020 | LPS-induced MyD88 alternative splicing provides negative feedback on TLR signaling. | Primary regulatory mechanism | Mouse macrophages | high | EXTRACTED / CROSS-MODULE |
| M17B-O034 | M17A-X021 | MyD88S fails to recruit IRAK4 and attenuates MyD88-dependent signaling. | Primary mechanism | Signaling comparator | medium | EXTRACTED / CROSS-MODULE |
| M17B-O035 | M17A-X022 | IL-10 constrains sphingolipid metabolism in TLR2-activated macrophages. | Primary intersection | TLR2 macrophage comparator | medium | EXTRACTED / CROSS-MODULE |
| M17B-O036 | M17A-X023 | TLR4/TRIF/p38 stabilizes Il10 mRNA more strongly than TLR2 activation. | Primary branch-output comparison | Macrophage comparator | high | EXTRACTED / CROSS-MODULE |
| M17B-O037 | M17A-X024 | MPLA-induced endothelial tolerance was reported as MyD88-dependent rather than TRIF-dependent. | Primary intersection | Human HUVECs | high | EXTRACTED / CROSS-MODULE |
| M17B-O038 | M17A-X025 | MPLA reduced LPS-induced endothelial cytokine/chemokine output. | Primary comparator mechanism | Human HUVECs | high | EXTRACTED / CROSS-MODULE |
| M17B-O039 | M17A-X026 | TLR2/MAPK/NF-kappaB signaling regulated endothelial MMP-2/9 and tight-junction outputs. | Primary intersection | Brain endothelial cells | high | EXTRACTED / CROSS-MODULE |
| M17B-O040 | M17A-X027 | Chronic SCI LPS challenge reactivated diverse microglial states. | Primary chronic-SCI observation | Chronic SCI | medium | EXTRACTED / CROSS-MODULE |

## Pass 4B: Directed Edge Register

| Edge ID | Source Entity | Relation | Target Entity | Pathway | Context | Evidence IDs | Status |
|---|---|---|---|---|---|---|---|
| M17B-E001 | TLR4 | recruits / routes | TRAM | TLR4 compartmentalized signaling | Endosomal, ligand- and cell-type-specific | M17B-O001 | QUEUED |
| M17B-E002 | TLR2/TLR4 | coordinates | MyD88/NF-kappaB-associated injury response | Sterile SCI receptor signaling | Traumatic mouse SCI | M17B-O002 | EXTRACTED / CONTEXTUAL |
| M17B-E003 | TLR4 | supports | IRF3/IFN-beta branch | TLR4 branch balance | TLR4-deficient SCI mice | M17B-O003 | EXTRACTED |
| M17B-E004 | TLR2/TLR4 | activates | TNF-dependent spinal output | TIRAP/MyD88-associated nociceptive signaling | Intrathecal HKLM or LPS | M17B-O004 | EXTRACTED |
| M17B-E005 | TLR3 | signals through | TRIF/IFN-regulated output | Endosomal dsRNA response | Intrathecal poly(I:C) and zebrafish SCI | M17B-O004, M17B-O005 | EXTRACTED |
| M17B-E006 | TLR9 | promotes | SCI inflammatory pain response | Endosomal endogenous-DNA response | Mouse traumatic SCI | M17B-O006 | EXTRACTED |
| M17B-E007 | TBK1 | activates / coordinates | IRF3 and YAP-linked astrocyte response | Downstream innate kinase convergence | Mouse SCI | M17B-O007 | EXTRACTED |
| M17B-E008 | TLR7 | marks / supports | Spinal antiviral humoral response | Viral comparator | EV71 spinal infection | M17B-O008 | EXTRACTED / BOUNDARY |
| M17B-E009 | TLR2 | binds / recruits | MyD88 | MyD88 proximal cascade | TIR-domain comparator | M17B-O009, M17B-O010 | EXTRACTED / COMPARATOR |
| M17B-E010 | MyD88S | attenuates | IRAK4/NF-kappaB signaling | Negative feedback | Alternative-splicing comparator | M17B-O011 | EXTRACTED |
| M17B-E011 | TLR2/TLR4 | differentially regulates | IL-10 mRNA stability | Branch-specific output | Macrophage comparator | M17B-O012 | EXTRACTED |
| M17B-E012 | TLR2 | intersects with | PI3K-AKT survival signaling | Neuroprotection comparator | Brain ischemia and SCI ex vivo context | M17B-O013 | EXTRACTED / COMPARATOR |
| M17B-E013 | TLR4 preconditioning | promotes | IL-10/IRF3-associated microglial repair state | SCI conditioning | Low-dose LPS before traumatic SCI | M17B-O014 | EXTRACTED / CROSS-MODULE |
| M17B-E014 | TLR4 | coordinates | spinal microglia/endothelium | Ischemic SCI conditioning | Repeated systemic LPS | M17B-O015 | EXTRACTED / CROSS-MODULE |
| M17B-E015 | TLR4 conditioning | intersects with | IL-1R1 | Spinal vascular-immune relay | Repeated LPS | M17B-O016 | EXTRACTED / CROSS-MODULE |
| M17B-E016 | TLR4 | redirects toward | TRIF/IRF3 tolerance output | Brain ischemia comparator | LPS preconditioning | M17B-O017 | EXTRACTED / CROSS-MODULE |
| M17B-E017 | MyD88 | regulates | Endothelial CXCL10 relay | Brain ischemia comparator | Peripheral LPS preconditioning | M17B-O018 | EXTRACTED / CROSS-MODULE |
| M17B-E018 | TLR4 | supports | Oligodendrocyte formation | Traumatic SCI repair boundary | TLR4 deficiency | M17B-O019 | EXTRACTED / CROSS-MODULE |
| M17B-E019 | TLR4-associated signaling | reactivates | Chronic microglial states | Chronic SCI | LPS challenge | M17B-O021, M17B-O040 | EXTRACTED / CROSS-MODULE |
| M17B-E020 | TLR2/1 | activates | PI3K-AKT survival signaling | CNS ischemia comparator | Pam3CSK4 | M17B-O026, M17B-O027 | EXTRACTED / CROSS-MODULE |
| M17B-E021 | TLR2/1 | protects | Ex vivo spinal tissue | Ex vivo SCI | Pam3CSK4 | M17B-O028 | EXTRACTED / CROSS-MODULE |
| M17B-E022 | TLR4 | couples through | TRAM/TRIF to IFN-beta | Receptor-trafficking comparator | LPS-induced endocytosis | M17B-O031, M17B-O032 | EXTRACTED / CROSS-MODULE |
| M17B-E023 | LPS/TLR signaling | induces | MyD88 alternative splicing | Macrophage negative feedback | LPS stimulation | M17B-O033 | EXTRACTED / CROSS-MODULE |
| M17B-E024 | MyD88S | inhibits | IRAK4 recruitment | Negative regulation | Alternative splice isoform | M17B-O034 | EXTRACTED / CROSS-MODULE |
| M17B-E025 | TLR2/TLR4 | differentially regulates | IL-10 mRNA stability | Macrophage branch output | Receptor-specific activation | M17B-O035, M17B-O036 | EXTRACTED / CROSS-MODULE |
| M17B-E026 | TLR4/MPLA | induces | Endothelial tolerance | Human HUVECs | MPLA priming and LPS challenge | M17B-O037, M17B-O038 | EXTRACTED / CROSS-MODULE |
| M17B-E027 | TLR2 | activates | MAPK/NF-kappaB endothelial output | Brain endothelial barrier context | Pam3CSK4 | M17B-O039 | EXTRACTED / CROSS-MODULE |

## Pass 4C: Perturbation and Phenotype Matrix

| Perturbation ID | Experiment ID | Entity | Perturbation Type | Scope | Phenotype ID | Effect Direction | Rescue / Epistasis | Evidence ID | Status |
|---|---|---|---|---|---|---|---|---|---|
| M17B-PERT001 | M17A-P003-E001 | TLR4 | knockout | SCI model, as reported | Oligodendrocyte formation / recovery | Pending extraction | Pending extraction | Pending | QUEUED |
| M17B-PERT002 | M17A-P013-E001 | TLR2/TLR4 | knockout or signaling-defective mutation | Traumatic mouse SCI | Locomotion, demyelination, gliosis, macrophage activation | Worse recovery and myelin/glial phenotypes in deficient animals | No rescue reported | M17B-O002 | EXTRACTED |
| M17B-PERT003 | M17A-P014-E001 | TLR4 | knockout/deficiency | Acute mouse SCI | NF-kappaB, IRF3/IFN-beta, neuronal death | More inflammatory injury and neuronal death; lower IRF3/IFN-beta | No rescue reported | M17B-O003 | EXTRACTED |
| M17B-PERT004 | M17A-P015-E001 | TNF, TRIF, IFNAR | knockout or rescue | Spinal ligand challenge | Allodynia and cytokine output | TNF loss reduced TLR2/4 effects; TRIF/IFN loss prolonged allodynia; IFN-beta relieved TLR2/4 effects | IFN-beta rescue | M17B-O004 | EXTRACTED |
| M17B-PERT005 | M17A-P016-E001 | TLR3 | agonist or inhibitor | Zebrafish spinal lesion | Neuron volume and locomotion | Poly(I:C) improved outcomes; inhibitor worsened them | Pharmacologic bidirectionality | M17B-O005 | EXTRACTED |
| M17B-PERT006 | M17A-P017-E001 | TLR9 | antagonist | Mouse traumatic SCI | Pain hypersensitivity and inflammation | Reduced pain and inflammation; locomotor benefit unresolved | No rescue reported | M17B-O006 | EXTRACTED |
| M17B-PERT007 | M17A-P018-E001 | TBK1 | inhibitor | Mouse SCI astrocyte response | Reactive astrocytes, cytokines, infiltration, IRF3 | Reduced inflammatory response and altered YAP/IRF3 output | Target is downstream and not TLR-specific | M17B-O007 | EXTRACTED |
| M17B-PERT008 | M17A-P019-E001 | TLR7 | knockout | EV71 spinal infection | Antiviral humoral immunity | Impaired antiviral humoral response | Viral comparator only | M17B-O008 | EXTRACTED / BOUNDARY |
| M17B-PERT009 | M17A-P009-E001 | MyD88S | alternative splice isoform | Innate signaling comparator | NF-kappaB output | Reduced IRAK4 recruitment and attenuated signaling | Isoform comparison | M17B-O011 | EXTRACTED |
| M17B-PERT010 | M17A-P011-E001 | TLR2 | agonist or pathway inhibition | Ischemic brain and ex vivo SCI comparator | Neuronal survival | TLR2/PI3K-AKT-associated protection was context- and timing-dependent | Comparator boundaries retained | M17B-O013 | EXTRACTED / COMPARATOR |
| M17B-PERT011 | M17A-X001 | TLR4 | preconditioning | Traumatic SCI | Microglial IL-10/IRF3 and recovery | Improved repair-associated state | Timing and dose boundary | M17B-O014 | EXTRACTED / CROSS-MODULE |
| M17B-PERT012 | M17A-X002 | TLR4 | repeated LPS conditioning | Spinal ischemia | Microglia/endothelium and recovery | Protective conditioning phenotype | IL-1 cross-talk retained | M17B-O015 | EXTRACTED / CROSS-MODULE |
| M17B-PERT013 | M17A-X003 | IL-1R1 | pathway test | Spinal ischemia | Microglia-vascular relay | IL-1R1 contributed to conditioning response | Cross-pathway, not TLR-specific | M17B-O016 | EXTRACTED / CROSS-MODULE |
| M17B-PERT014 | M17A-X004 | TRIF/IRF3 | pathway comparison | Brain ischemia | Tolerance and NF-kappaB output | TRIF/IRF3-associated redirection | Comparator model | M17B-O017 | EXTRACTED / CROSS-MODULE |
| M17B-PERT015 | M17A-X005 | MyD88 | endothelial relay comparison | Brain ischemia | CXCL10 and CNS protection | MyD88/CXCL10 relay implicated | Peripheral-to-CNS boundary | M17B-O018 | EXTRACTED / CROSS-MODULE |
| M17B-PERT016 | M17A-X006 | TLR4 | deficiency | Traumatic SCI | Oligodendrocyte formation | Impaired repair-associated myelin biology | No rescue reported | M17B-O019 | EXTRACTED / CROSS-MODULE |
| M17B-PERT017 | M17A-X007 | LPS/indomethacin | post-injury treatment | Traumatic SCI | Repair and locomotion | Improved outcomes in source context | Distinct from preconditioning | M17B-O020 | EXTRACTED / CROSS-MODULE |
| M17B-PERT018 | M17A-X008 | LPS | chronic challenge | Chronic SCI | Microglial state/plasticity | Reactivated inflammatory states | Chronic timing boundary | M17B-O021 | EXTRACTED / CROSS-MODULE |
| M17B-PERT019 | M17A-X012 | MyD88/TRIF | trained-immunity perturbation | Macrophage comparator | Durable macrophage state | MPLA training required MyD88, not TRIF | Comparator | M17B-O025 | EXTRACTED / CROSS-MODULE |
| M17B-PERT020 | M17A-X014 | TLR2/PI3K-AKT | agonist and pathway perturbation | Brain ischemia | Neuronal survival | Protection required TLR2 and PI3K-AKT | Comparator | M17B-O027 | EXTRACTED / CROSS-MODULE |
| M17B-PERT021 | M17A-X015 | TLR2/1 | ex vivo agonist | Ex vivo SCI | Axonal and oligodendroglial preservation | Reduced injury | Route/timing boundary | M17B-O028 | EXTRACTED / CROSS-MODULE |
| M17B-PERT022 | M17A-X020 | MyD88 splicing | LPS-induced alternative isoform | Macrophage comparator | Negative feedback | MyD88S-like splicing attenuated signaling | Isoform comparison | M17B-O033 | EXTRACTED / CROSS-MODULE |
| M17B-PERT023 | M17A-X021 | MyD88S | isoform expression | Signaling comparator | IRAK4 recruitment | Reduced recruitment and signaling | Full-length MyD88 control | M17B-O034 | EXTRACTED / CROSS-MODULE |
| M17B-PERT024 | M17A-X024 | MPLA | endothelial priming | Human HUVECs | LPS tolerance | Reduced secondary cytokine response | MyD88/TRIF knockdown boundary | M17B-O037 | EXTRACTED / CROSS-MODULE |
| M17B-PERT025 | M17A-X026 | TLR2 | Pam3CSK4 stimulation/inhibition | Brain endothelial cells | MMP/tight-junction output | Altered MAPK/NF-kappaB barrier program | Barrier-risk boundary | M17B-O039 | EXTRACTED / CROSS-MODULE |

## Query Readiness Requirements

- Protein-to-pathway membership must distinguish canonical, context-dependent, disputed, and inferred membership.
- Receptor-to-transcription-factor queries must support recursive traversal and direct-edge filtering.
- Knockout phenotype queries must join perturbation, experiment, observation, and phenotype records.
- Every graph edge must be traceable to one or more observations or explicitly marked as review/inferred context.
- Contradictory edges and context-specific phenotypes must remain queryable rather than overwritten.

## Consolidation and Saturation Record

- 20 indexed paper/anchor records and 40 experiment-level rows now cover the major receptor, adaptor, kinase, transcription-factor, intersection, and phenotype layers.
- 40 atomic observations, 27 directed edges, and 25 perturbation rows are linked to experiments or explicitly marked comparator/boundary evidence.
- Direct sterile-SCI evidence is strongest for TLR2, TLR3, TLR4, and TLR9; TLR7 is represented by a viral spinal comparator and TLR5/8 plus RIG-I/MDA5 remain gaps.
- Two confirmation search phases added no new mechanistic category; the graph is ready for query use with targeted full-text upgrades still distinguishable from saturation.
