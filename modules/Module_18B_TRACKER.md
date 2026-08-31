# Module 18B: Non-TLR DAMP Sensing and Downstream Danger Signaling - Evidence Consolidation and Query Readiness

## Overview

This tracker converts Module 18A experiments into a queryable danger-signaling graph using the shared pathway schema introduced for Module 17. It separates DAMP release evidence, sensor/receptor edges, inflammasome and death-program assembly, pathway intersections, perturbation evidence, phenotypes, and author claims.

**Input corpus**: Module 18A non-TLR DAMP literature, initially seeded from Modules 3, 5, 12, and 13.

**Status**: CONSOLIDATED / LOCAL FULL-TEXT EXTRACTION COMPLETE; PUBMED-ONLY ACCESS GAPS BOUNDED.

## Evidence Topic Map

| Topic ID | Consensus-Ready Topic | Required Evidence |
|---|---|---|
| M18B-T001 | DAMP source and release | Injury/death source, release route, extracellular exposure, and timing |
| M18B-T002 | HMGB1/RAGE and extracellular protein danger signaling | HMGB1, RAGE, S100, IL-33, histones, and receptor-specific perturbations |
| M18B-T003 | Purinergic and extracellular ATP sensing | ATP, P2X7, P2Y12, adenosine conversion, and neuron-glia effects |
| M18B-T004 | Inflammasome and pyroptosis/PANoptosis | NLRP3, AIM2, ZBP1, ASC, CASP1, GSDMD, and rescue/epistasis |
| M18B-T005 | Cytosolic nucleic-acid danger sensing | cGAS-STING, AIM2, RIG-I/MDA5-MAVS, mtDNA, and IRF outputs |
| M18B-T006 | Debris, lipid, complement, and extracellular-trap danger | Myelin debris, TREM2, C1q, foam cells, NETs/METs, and synaptic/tissue outcomes |
| M18B-T007 | Metabolic danger signals | Lactate, TMAO, ROS, mitochondrial dysfunction, and TXNIP/NLRP3 intersections |
| M18B-T008 | SCI translation boundaries | Microglia, macrophage, endothelial, oligodendrocyte, neuron, axon, lesion, locomotor, pain, and safety outcomes |

## Pass 4A: Atomic Danger-Signaling Observations

| Observation ID | Topic ID | Paper ID | Experiment ID | DAMP or Edge | Evidence Type | Observation Value | Context | Extraction Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| M18B-O001 | M18B-T002 | M18A-P001 | M18A-P001-E001 | Injury -> HMGB1 availability | Primary release/localization | Cytoplasmic HMGB1 accumulated in GFAP-positive astrocytes and serum HMGB1 peaked at 3 dpi; this establishes injury-associated DAMP availability, while necroptotic source attribution is supported by prior work cited in the paper rather than directly perturbed here | Rat T8 crush SCI | high | EXTRACTED / FULL-TEXT |
| M18B-O002 | M18B-T003 | M18A-P017 | M18A-P017-E001 | ATP -> P2X7R | Primary SCI mechanism | Sustained ATP release activates neuronal P2X7R, producing calcium overload and cell death; antagonists improve acute recovery | Rat impact SCI | high | EXTRACTED |
| M18B-O003 | M18B-T003 | M18A-P018 | M18A-P018-E001 | P2X7R -> microglial/gliotic inflammation | Primary SCI intervention | Systemic BBG reduced CD68-positive microglia, GFAP, neutrophils, atrophy, and functional deficits | Mouse traumatic SCI | high | EXTRACTED |
| M18B-O004 | M18B-T004 | M18A-P019 | M18A-P019-E001 | Injury -> AIM2 induction | Primary localization | AIM2 increased in injured spinal cells; DNA ligand and direct necessity require separate causal records | Mouse SCI | medium | EXTRACTED |
| M18B-O005 | M18B-T004 | M18A-P020 | M18A-P020-E001 | Cytosolic dsDNA -> AIM2/ASC/caspase-1 -> pyroptosis | Primary causal experiment | AIM2 knockdown reduced cleaved caspase-1, IL-1beta, and spinal neuronal pyroptosis after ischemia-reperfusion | Mouse spinal IR | high | EXTRACTED |
| M18B-O006 | M18B-T005 | M18A-P021 | M18A-P021-E001 | mtDNA -> cGAS-STING -> IRF3/NF-kappaB | Primary SCI mechanism | Mfn2 loss and mitochondrial damage released mtDNA; microglia-specific STING loss or C-176 reduced inflammatory signaling and improved recovery | Mouse SCI microglia | high | EXTRACTED |
| M18B-O007 | M18B-T005 | M18A-P022 | M18A-P022-E001 | cGAS-STING -> NF-kappaB/M1 state | Primary pharmacology | Tryptanthrin inhibited the axis, reduced microglial inflammatory polarization and neuronal loss, and improved recovery | Mouse SCI | high | EXTRACTED |
| M18B-O008 | M18B-T004 | M18A-P023 | M18A-P023-E001 | cGAS-STING -> NLRP3/GSDMD | Primary SCI mechanism | MS4A7 knockdown reduced cGAS-STING-linked NLRP3 pyroptosis and improved locomotor and pain outcomes | Mouse SCI microglia | medium | EXTRACTED |
| M18B-O009 | M18B-T002 | M18A-P024 | M18A-P024-E001 | Extracellular histone H3 -> TLR2/YB-1 -> axon inhibition | Primary DAMP mechanism | Histone H3 was elevated in human SCI CSF and injured CNS; histone-mediated growth-cone collapse was reversed by activated protein C | Human SCI plus CNS comparator | high | EXTRACTED / TLR INTERSECTION |
| M18B-O010 | M18B-T002 | M18A-P025 | M18A-P025-E001 | IL-33 -> anti-inflammatory myeloid state | Primary SCI intervention | Recombinant IL-33 reduced tissue loss, demyelination, astrogliosis, and inflammatory cytokines while increasing Arg1-positive myeloid cells | Mouse contusion SCI | medium | EXTRACTED |
| M18B-O011 | M18B-T002 | M18A-P026 | M18A-P026-E001 | S100A9 -> neutrophil infiltration | Primary SCI intervention | S100A9 blockade reduced neutrophil infiltration and improved functional recovery; RAGE/TLR4 receptor necessity was not isolated | Mouse traumatic SCI | high | EXTRACTED |
| M18B-O012 | M18B-T006 | M18A-P004 | M18A-P004-E001 | Foam-cell state -> remodeling | Primary debris/lipid atlas | Foam-cell states emerged by 5 dpi and persisted into chronic SCI; clodronate macrophage depletion improved motor outcomes | Mouse SCI | high | EXTRACTED / FULL-TEXT |
| M18B-O013 | M18B-T006 | M18A-P005 | M18A-P005-E001 | Myelin debris -> TREM2/PI3K-AKT | Primary debris-sensor mechanism | TREM2 loss impaired myelin-debris engulfment/degradation, increased foamy macrophages, and reduced DAM activation | Mouse SCI | high | EXTRACTED / FULL-TEXT |
| M18B-O014 | M18B-T007 | M18A-P006 | M18A-P006-E001 | Lactate -> H3K9la/TXNIP | Primary metabolic chromatin mapping | SCI-associated lactate and macrophage H3K9la were linked to TXNIP inflammatory regulation by metabolomics, CUT&Tag, and RNA-seq | Mouse SCI and human serum | high | EXTRACTED / FULL-TEXT |
| M18B-O015 | M18B-T004 | M18A-P007 | M18A-P007-E001 | ATP/NLRP3 -> PANoptosis | Primary comparator | LPS/ATP challenge activated AMPK/NF-kappaB-linked PANoptosis; metformin reduced the death program | Macrophage/inflammatory comparator | medium | EXTRACTED / COMPARATOR |

## Cross-Module Observation Ledger

| Observation ID | Cross-Index Experiment | Atomic Observation | Evidence Type | Context | Confidence | Status |
|---|---|---|---|---|---|---|
| M18B-O016 | M18A-X001 | Necroptotic astrocyte HMGB1 activated RAGE-linked NF-kappaB and pro-inflammatory microglial/macrophage polarization. | Primary SCI mechanism | Rat SCI and microglia | high | EXTRACTED / CROSS-MODULE |
| M18B-O017 | M18A-X002 | HMGB1 or RAGE inhibition reduced neuronal loss/demyelination and improved functional recovery. | Primary SCI perturbation | Rat SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O018 | M18A-X003 | Macrophage extracellular traps accumulated after SCI and DNase I reduced trap-associated injury. | Primary SCI mechanism | Rat SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O019 | M18A-X004 | LL37-P2X7R-NF-kappaB linked extracellular traps to inflammatory polarization; serum markers tracked human severity. | Primary mechanism plus human association | Rat SCI and human serum | high | EXTRACTED / CROSS-MODULE |
| M18B-O020 | M18A-X005 | iPSC-NSC exosomes reduced microglial GSDMD/caspase-1 pyroptosis and improved tissue and motor outcomes. | Primary SCI intervention | Mouse SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O021 | M18A-X006 | Exosomal let-7b-5p directly targeted LRIG3 and reduced microglial pyroptosis; LRIG3 rescue reversed the effect. | Primary epistasis | BV2 and mouse SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O022 | M18A-X007 | Foam cells emerged early and persisted as a lipid-laden macrophage state associated with chronic SCI remodeling. | Primary atlas/perturbation | Mouse SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O023 | M18A-X008 | Foam-cell lipid accumulation increased C1q and synaptic engulfment; lipid lowering and C1q blockade preserved synapses. | Primary causal mechanism | Mouse SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O024 | M18A-X009 | TREM2 loss impaired myelin-debris engulfment/degradation and PI3K-AKT-linked DAM activation. | Primary knockout mechanism | Mouse SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O025 | M18A-X010 | Sustained TREM2 activation created an early-clearance versus late-fibrosis/inflammation tradeoff. | Primary timing comparison | Mouse SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O026 | M18A-X011 | SCI-associated lactate and macrophage H3K9la were linked to TXNIP inflammatory chromatin regulation. | Primary metabolic/chromatin mechanism | Mouse SCI and human serum | high | EXTRACTED / CROSS-MODULE |
| M18B-O027 | M18A-X012 | 2-DG, TXNIP knockdown, or H3K9la-peptide inhibition reduced TXNIP/NLRP3 and improved recovery-associated outcomes. | Primary causal mechanism | Mouse SCI macrophages | high | EXTRACTED / CROSS-MODULE |
| M18B-O028 | M18A-X013 | Metformin reduced LPS/ATP-induced pyroptosis, apoptosis, necroptosis, cytokines, and M1 polarization through AMPK/NF-kappaB. | Primary comparator mechanism | BV2/macrophage comparator | high | EXTRACTED / CROSS-MODULE |
| M18B-O029 | M18A-X014 | AMPK-dependent metformin treatment improved axon regrowth, remyelination, motor, and electrophysiologic recovery. | Primary SCI pharmacology | Rat SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O030 | M18A-X015 | Microglial pyroptosis/apoptosis/necroptosis signatures were concentrated in SCI multi-omics data, with IRF1 and ZBP1 nominated. | Primary multi-omics observation | Rat SCI | medium | EXTRACTED / CROSS-MODULE |
| M18B-O031 | M18A-X016 | IRF1 occupied the Zbp1 promoter and its inhibition reduced ZBP1/PANoptosis and inflammatory cytokines. | Primary mechanism | Rat SCI and microglia | high | EXTRACTED / CROSS-MODULE |
| M18B-O032 | M18A-X017 | TMAO aggravated SCI neuroinflammation through microglial NLRP3 activation. | Primary SCI mechanism | Mouse SCI | medium | EXTRACTED / CROSS-MODULE |
| M18B-O033 | M18A-X018 | TMAO-associated NLRP3 activation was linked to inflammatory and functional outcomes. | Primary source-level validation | Mouse SCI | low | EXTRACTED / CROSS-MODULE |
| M18B-O034 | M18A-X019 | Thiolutin suppressed NLRP3-linked microglial pyroptosis, neuroinflammation, and neuronal apoptosis. | Primary SCI pharmacology | Mouse SCI | medium | EXTRACTED / CROSS-MODULE |
| M18B-O035 | M18A-X020 | Source-level validation supports NLRP3 inhibition as the proximate thiolutin mechanism. | Primary source-level validation | Mouse SCI | low | EXTRACTED / CROSS-MODULE |
| M18B-O036 | M18A-X021 | Diabetes worsened SCI lesion, demyelination, and recovery while increasing microglial NLRP3/pyroptosis programs. | Primary disease-state mechanism | Mouse T2D plus SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O037 | M18A-X022 | Conditional microglial caspase-1 deletion improved BMS, damage, and remyelination in diabetic SCI. | Primary conditional knockout | Mouse T2D plus SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O038 | M18A-X023 | RAGE/ROS/TXNIP intervention reduced NLRP3 signaling and improved inflammatory, phagocytic, and remyelination readouts. | Primary pathway convergence | BV2 and diabetic SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O039 | M18A-X024 | P2Y12R-driven ATP-to-adenosine conversion promoted A1R/PINK1/Parkin neuronal mitophagy; pathway blockade attenuated benefit. | Primary receptor/epistasis mechanism | Microglia-neuron co-culture | high | EXTRACTED / CROSS-MODULE |
| M18B-O040 | M18A-X025 | Targeted P2Y12R restoration reduced lesion cavity and neuronal apoptosis and increased mitophagy. | Primary SCI intervention | Mouse SCI and ex vivo slices | high | EXTRACTED / CROSS-MODULE |
| M18B-O041 | M18A-X026 | P2Y12R/mitophagy treatment improved long-term myelin, axon, evoked-potential, motor, and neuronal outcomes. | Primary SCI follow-up | Mouse SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O042 | M18A-X027 | Lesion-remote astrocyte CCN1 supported microglial lipid storage, debris handling, and repair-associated buffering. | Primary SCI mechanism | Mouse SCI and human CNS comparator | high | EXTRACTED / CROSS-MODULE |
| M18B-O043 | M18A-X028 | CCN1 loss blunted debris clearance and neurologic recovery through loss of the CCN1-SDC4 relay. | Primary causal mechanism | Mouse SCI | high | EXTRACTED / CROSS-MODULE |
| M18B-O044 | M18A-P001-E002 | HMGB1 increased pro-inflammatory microglial markers and RAGE-linked phospho-NF-kappaB p65; FPS-ZM1 partially reversed the response. | Primary in vitro mechanism | Primary rat microglia | high | EXTRACTED / FULL-TEXT |
| M18B-O045 | M18A-P001-E003 | Glycyrrhizin or FPS-ZM1 reduced inflammatory polarization, lesion size, neuronal loss, and demyelination and improved BBB/RHI after rat T8 crush SCI. | Primary in vivo pharmacology | Rat SCI | high | EXTRACTED / FULL-TEXT |
| M18B-O046 | M18A-P002-E001 | DNase I reduced CitH3/CD68-positive macrophage extracellular traps, apoptosis, M1 markers, cavity formation, and functional deficits after rat T10 contusion SCI. | Primary in vivo extracellular-trap intervention | Rat SCI | high | EXTRACTED / FULL-TEXT |
| M18B-O047 | M18A-P002-E002 | LL37 co-immunoprecipitated with P2X7R and trap-associated NF-kappaB activation tracked with rat SCI; human serum trap markers inversely correlated with ASIA scores. | Primary mechanism plus human association | Rat SCI and human serum | high | EXTRACTED / FULL-TEXT |
| M18B-O048 | M18A-P003-E001 | iPSC-NSC conditioned medium/exosomes reduced LPS/ATP-induced BV2 pyroptosis, while GW4869 reversed the protection. | Primary in vitro vesicle mechanism | BV2 comparator | high | EXTRACTED / FULL-TEXT |
| M18B-O049 | M18A-P003-E002 | Intrathecal iPSC-NSC exosomes reduced spinal microglial/macrophage pyroptosis and improved myelin, axon, neuronal, electrophysiologic, and motor outcomes in mice. | Primary in vivo vesicle intervention | Mouse SCI | high | EXTRACTED / FULL-TEXT |
| M18B-O050 | M18A-P003-E003 | Exosomal let-7b-5p directly targeted LRIG3; cargo gain/loss and LRIG3 rescue shifted BV2 and mouse SCI pyroptosis and recovery phenotypes. | Primary epistasis | BV2 and mouse SCI | high | EXTRACTED / FULL-TEXT |
| M18B-O051 | M18A-P004-E002 | Foam-cell lipid accumulation increased C1q and synaptic engulfment; bazedoxifene and anti-C1q preserved synapses and improved recovery. | Primary causal complement mechanism | Mouse SCI and BMDMs | high | EXTRACTED / FULL-TEXT |
| M18B-O052 | M18A-P005-E002 | COG1410 produced an early-clearance benefit but long-term TREM2 activation increased fibrosis/inflammation and impaired late axon, neuronal, and locomotor outcomes. | Primary timing comparison | Mouse SCI | high | EXTRACTED / FULL-TEXT |
| M18B-O053 | M18A-P006-E002 | 2-DG, TXNIP knockdown, and H3K9la-peptide inhibition reduced TXNIP/NLRP3 and mitochondrial injury and improved structural, functional, and bladder outcomes. | Primary causal metabolic intervention | Mouse SCI macrophages | high | EXTRACTED / FULL-TEXT |
| M18B-O054 | M18A-P012-E001 | Microglial P2Y12R promoted CD39/CD73 ATP-to-adenosine conversion, neuronal A1R signaling, and PINK1/Parkin/LC3 mitophagy; pathway blockade attenuated protection. | Primary receptor/epistasis mechanism | Microglia-neuron co-culture | high | EXTRACTED / FULL-TEXT |
| M18B-O055 | M18A-P012-E002 | P2Y-TK-Nano restored P2Y12R after mouse SCI, reduced lesion/apoptosis, and increased neuronal mitophagy in vivo and ex vivo. | Primary SCI nanoparticle intervention | Mouse SCI and ex vivo slices | high | EXTRACTED / FULL-TEXT |
| M18B-O056 | M18A-P012-E003 | P2Y12R/mitophagy treatment improved long-term myelin, axons, evoked potentials, locomotion, neurons, and GFAP organization. | Primary long-term follow-up | Mouse SCI | high | EXTRACTED / FULL-TEXT |
| M18B-O057 | M18A-P011-E001 | Diabetes worsened SCI lesion, demyelination, survival, conduction, remyelination, and recovery while increasing microglial NLRP3/caspase-1/GSDMD programs. | Primary disease-state mechanism | Mouse T2D plus SCI | high | EXTRACTED / FULL-TEXT |
| M18B-O058 | M18A-P011-E002 | Conditional microglial caspase-1 deletion improved BMS and remyelination and reduced damaged area and cleaved-caspase-1 signal in diabetic SCI. | Primary conditional knockout | Mouse T2D plus SCI | high | EXTRACTED / FULL-TEXT |
| M18B-O059 | M18A-P011-E003 | Verapamil, NAC, and FPS-ZM1 converged on reduced ROS/TXNIP/NLRP3 signaling and improved inflammatory, phagocytic, axonal, and remyelination readouts, with systemic specificity unresolved. | Primary pathway-convergence pharmacology | BV-2 and mouse T2D plus SCI | high | EXTRACTED / FULL-TEXT |

## Pass 4B: Directed Danger-Edge Register

| Edge ID | Source Entity | Relation | Target Entity | Pathway | Context | Evidence IDs | Status |
|---|---|---|---|---|---|---|---|
| M18B-E001 | HMGB1 | activates | RAGE | HMGB1-RAGE signaling | Primary rat microglia; recombinant HMGB1 and FPS-ZM1 | M18B-O044 | EXTRACTED / FULL-TEXT |
| M18B-E002 | Extracellular ATP | activates | P2X7R | Purinergic excitotoxicity | Acute SCI neurons | M18B-O002 | EXTRACTED |
| M18B-E003 | P2X7R | promotes | Microglial/gliotic inflammation | Purinergic secondary injury | Traumatic SCI | M18B-O003 | EXTRACTED |
| M18B-E004 | Cytosolic dsDNA | activates | AIM2/ASC/caspase-1 | DNA inflammasome | Spinal ischemia-reperfusion | M18B-O004, M18B-O005 | EXTRACTED |
| M18B-E005 | mtDNA | activates | cGAS-STING | Cytosolic DNA sensing | SCI microglia | M18B-O006 | EXTRACTED |
| M18B-E006 | cGAS-STING | activates | NF-kappaB/M1 polarization | DNA-sensing inflammatory relay | SCI microglia | M18B-O006, M18B-O007 | EXTRACTED |
| M18B-E007 | cGAS-STING | activates / primes | NLRP3/GSDMD pyroptosis | DNA-inflammasome convergence | SCI microglia | M18B-O008 | EXTRACTED |
| M18B-E008 | Extracellular histone H3 | signals through | TLR2/YB-1 | Axon-growth inhibition | Human SCI CSF and CNS injury | M18B-O009 | EXTRACTED / TLR INTERSECTION |
| M18B-E009 | IL-33 | promotes | Anti-inflammatory myeloid state | Alarmin repair signaling | Mouse contusion SCI | M18B-O010 | EXTRACTED |
| M18B-E010 | S100A9 | promotes | Neutrophil infiltration | Alarmin inflammatory recruitment | Mouse traumatic SCI | M18B-O011 | EXTRACTED |
| M18B-E011 | C1q | promotes | Synaptic engulfment | Lipid/debris-complement signaling | Mouse SCI | M18B-O012, M18B-O051 | EXTRACTED / FULL-TEXT |
| M18B-E012 | Myelin debris | engages | TREM2/PI3K-AKT | Debris clearance and repair | Mouse SCI | M18B-O013 | EXTRACTED |
| M18B-E013 | H3K9la/lactate | activates | TXNIP/NLRP3 | Metabolic chromatin-danger intersection | SCI macrophages | M18B-O014, M18B-O053 | EXTRACTED / FULL-TEXT |
| M18B-E014 | ATP plus LPS | activates | PANoptosis program | Metabolic/inflammasome comparator | Macrophage challenge | M18B-O015 | EXTRACTED / COMPARATOR |
| M18B-E015 | Extracellular traps | release / present | LL37/P2X7R/NF-kappaB signal | Trap-mediated inflammation | Rat SCI and human serum | M18B-O018, M18B-O019 | EXTRACTED / CROSS-MODULE |
| M18B-E016 | Exosomal let-7b-5p | represses | LRIG3/pyroptosis program | Vesicle-associated immune death | BV2 and mouse SCI | M18B-O020, M18B-O021 | EXTRACTED / CROSS-MODULE |
| M18B-E017 | Foam-cell lipid accumulation | increases | C1q | Lipid/debris-complement signaling | Mouse SCI | M18B-O022, M18B-O023 | EXTRACTED / CROSS-MODULE |
| M18B-E018 | C1q | promotes | Synaptic engulfment | Complement-linked synaptic loss | Mouse SCI | M18B-O023 | EXTRACTED / CROSS-MODULE |
| M18B-E019 | Myelin debris | engages | TREM2 | Debris clearance | Mouse SCI | M18B-O024, M18B-O025 | EXTRACTED / CROSS-MODULE |
| M18B-E020 | TREM2 | activates | PI3K-AKT/DAM debris program | Timing-dependent repair | Mouse SCI | M18B-O024, M18B-O025, M18B-O052 | EXTRACTED / FULL-TEXT |
| M18B-E021 | Lactate/H3K9la | activates | TXNIP | Metabolic chromatin-danger signaling | Mouse SCI macrophages | M18B-O026, M18B-O027 | EXTRACTED / CROSS-MODULE |
| M18B-E022 | TXNIP | activates | NLRP3 | Metabolic inflammasome signaling | Mouse SCI macrophages | M18B-O027 | EXTRACTED / CROSS-MODULE |
| M18B-E023 | AMPK | suppresses / coordinates | PANoptosis program | Metformin comparator | Rat SCI and BV2 | M18B-O028, M18B-O029 | EXTRACTED / CROSS-MODULE |
| M18B-E024 | IRF1 | activates | ZBP1/PANoptosis | Transcriptional death-program convergence | Rat SCI | M18B-O030, M18B-O031 | EXTRACTED / CROSS-MODULE |
| M18B-E025 | TMAO | activates | NLRP3 | Metabolic danger | Mouse SCI | M18B-O032, M18B-O033 | EXTRACTED / CROSS-MODULE |
| M18B-E026 | Thiolutin | inhibits | NLRP3-linked pyroptosis | Pharmacologic inflammasome modulation | Mouse SCI | M18B-O034, M18B-O035 | EXTRACTED / CROSS-MODULE |
| M18B-E027 | Diabetes | increases | Microglial NLRP3/caspase-1/GSDMD | Disease-state danger signaling | Mouse T2D plus SCI | M18B-O036, M18B-O037 | EXTRACTED / CROSS-MODULE |
| M18B-E028 | Caspase-1 | promotes | Pyroptotic injury | Inflammasome effector | Mouse T2D plus SCI | M18B-O037 | EXTRACTED / CROSS-MODULE |
| M18B-E029 | RAGE/ROS | activates | TXNIP/NLRP3 | Protein-danger and oxidative convergence | BV2 and diabetic SCI | M18B-O038 | EXTRACTED / CROSS-MODULE |
| M18B-E030 | P2Y12R | promotes | CD39/CD73 -> adenosine/A1R | Purinergic repair relay | Microglia-neuron co-culture | M18B-O039, M18B-O054 | EXTRACTED / FULL-TEXT |
| M18B-E031 | P2Y12R/adenosine | promotes | PINK1/Parkin neuronal mitophagy | Purinergic mitochondrial repair | Mouse SCI | M18B-O040, M18B-O041, M18B-O055, M18B-O056 | EXTRACTED / FULL-TEXT |
| M18B-E032 | Astrocyte CCN1 | engages | Microglial SDC4/lipid buffering | Lesion-remote debris handling | Mouse SCI | M18B-O042, M18B-O043 | EXTRACTED / CROSS-MODULE |
| M18B-E033 | RAGE | activates | NF-kappaB p65 | HMGB1-RAGE inflammatory relay | Primary rat microglia | M18B-O044 | EXTRACTED / FULL-TEXT |
| M18B-E034 | HMGB1/RAGE inhibition | reduces | Inflammatory polarization and secondary tissue injury | HMGB1-RAGE neuroprotection | Rat T8 crush SCI | M18B-O045 | EXTRACTED / FULL-TEXT |
| M18B-E035 | Extracellular traps | promote | M1-like macrophage/microglia polarization | Trap-mediated secondary inflammation | Rat T10 contusion SCI | M18B-O046, M18B-O047 | EXTRACTED / FULL-TEXT |
| M18B-E036 | LL37 | activates | P2X7R -> NF-kappaB | Trap-mediated inflammatory relay | Rat SCI tissue | M18B-O047 | EXTRACTED / FULL-TEXT |
| M18B-E037 | Exosomal let-7b-5p | represses | LRIG3-linked pyroptosis program | Vesicle-associated immune-death regulation | BV2 and mouse SCI | M18B-O048, M18B-O050 | EXTRACTED / FULL-TEXT |
| M18B-E038 | Diabetes | increases | Microglial NLRP3/caspase-1/GSDMD | Metabolic disease danger signaling | Mouse T2D plus SCI | M18B-O057 | EXTRACTED / FULL-TEXT |
| M18B-E039 | Microglial caspase-1 | promotes | Pyroptotic demyelination and impaired recovery | Inflammasome effector | Mouse T2D plus SCI | M18B-O058 | EXTRACTED / FULL-TEXT |
| M18B-E040 | RAGE/ROS | activates | TXNIP/NLRP3 | Diabetic SCI oxidative-inflammasome convergence | BV-2 and mouse T2D plus SCI | M18B-O059 | EXTRACTED / FULL-TEXT |

## Pass 4C: Perturbation and Phenotype Matrix

| Perturbation ID | Experiment ID | Entity | Perturbation Type | Scope | Phenotype ID | Effect Direction | Rescue / Epistasis | Evidence ID | Status |
|---|---|---|---|---|---|---|---|---|---|
| M18B-PERT001 | M18A-P001-E003 | HMGB1/RAGE | glycyrrhizin or FPS-ZM1 | Rat T8 crush SCI | Inflammatory polarization, lesion, myelin, neuronal survival, and locomotor recovery | Reduced inflammatory and tissue injury phenotypes; BBB/RHI improved | Systemic pharmacology; direct microglia-specific mediation unresolved | M18B-O045 | EXTRACTED / FULL-TEXT |
| M18B-PERT002 | M18A-P017-E001 | P2X7R | antagonist | Rat acute SCI | Neuronal death and motor recovery | Reduced neuronal death and improved recovery | OxATP/PPADS pharmacology | M18B-O002 | EXTRACTED |
| M18B-PERT003 | M18A-P018-E001 | P2X7R | systemic antagonist | Mouse traumatic SCI | Microglia, gliosis, neutrophils, recovery | Reduced inflammation and improved recovery | Systemic BBG translational boundary | M18B-O003 | EXTRACTED |
| M18B-PERT004 | M18A-P020-E001 | AIM2 | knockdown | Spinal ischemia-reperfusion | Neuronal pyroptosis | Reduced AIM2 inflammasome output and pyroptosis | Knockdown specificity as reported | M18B-O005 | EXTRACTED |
| M18B-PERT005 | M18A-P021-E001 | STING | microglia-specific knockout or C-176 inhibition | Mouse SCI | Microglial polarization, neuronal death, neurologic recovery | Reduced inflammation and improved recovery | Mfn2/MASM7 modulation of mtDNA release | M18B-O006 | EXTRACTED |
| M18B-PERT006 | M18A-P022-E001 | cGAS-STING | tryptanthrin inhibition | Mouse SCI | M1/M2 polarization, neuronal apoptosis, function | Reduced inflammatory signaling and improved recovery | Pathway-targeting pharmacology | M18B-O007 | EXTRACTED |
| M18B-PERT007 | M18A-P023-E001 | MS4A7 | shRNA knockdown or overexpression | Mouse SCI microglia | NLRP3/GSDMD pyroptosis, pain, locomotion | Knockdown improved outcomes; overexpression worsened them | diABZI/C-176 and MCC950 epistasis | M18B-O008 | EXTRACTED |
| M18B-PERT008 | M18A-P024-E001 | Extracellular histone H3 | activated protein C; TLR2/YB-1 pathway tests | Human SCI and CNS injury comparator | Axon outgrowth and growth-cone collapse | Activated protein C reversed inhibition and promoted regeneration | TLR2/YB-1 boundary retained | M18B-O009 | EXTRACTED |
| M18B-PERT009 | M18A-P025-E001 | IL-33 | recombinant protein administration | Mouse contusion SCI | Tissue loss, demyelination, gliosis, locomotion | Improved repair-associated phenotype | ST2 necessity not directly tested | M18B-O010 | EXTRACTED |
| M18B-PERT010 | M18A-P026-E001 | S100A9 | blockade | Mouse traumatic SCI | Neutrophil infiltration and recovery | Reduced infiltration and improved recovery | Receptor identity unresolved | M18B-O011 | EXTRACTED |
| M18B-PERT011 | M18A-P004-E001 | Macrophages/foam cells | clodronate depletion | Mouse SCI | Foam-cell state and motor recovery | Depletion improved recovery and defined persistent lipid-laden states | Cell depletion is not complement-specific | M18B-O012 | EXTRACTED / FULL-TEXT |
| M18B-PERT012 | M18A-P005-E001 | TREM2 | knockout | Mouse SCI | Myelin debris, foamy cells, DAM activation | Impaired debris handling and PI3K-AKT-linked activation | Necessity limited to tested context | M18B-O013 | EXTRACTED / FULL-TEXT |
| M18B-PERT013 | M18A-P006-E002 | H3K9la/TXNIP | 2-DG, TXNIP knockdown, H3K9la-peptide inhibition | Mouse SCI macrophages | NLRP3, mitochondria, axons, function | Reduced inflammation and improved outcomes | Lactate non-histone effects remain possible | M18B-O053 | EXTRACTED / FULL-TEXT |
| M18B-PERT014 | M18A-P007-E001 | AMPK/PANoptosis | metformin | LPS/ATP macrophage comparator | Inflammatory cell death | Reduced PANoptosis-associated output | Comparator, not direct sterile SCI | M18B-O015 | EXTRACTED / COMPARATOR |
| M18B-PERT015 | M18A-X001 | HMGB1/RAGE | glycyrrhizin or FPS-ZM1 | Rat SCI | Inflammatory polarization and recovery | Reduced RAGE-linked injury | Source pharmacology | M18B-O016, M18B-O017 | EXTRACTED / CROSS-MODULE |
| M18B-PERT016 | M18A-X003 | Extracellular traps | DNase I | Rat SCI | Trap-associated inflammation and motor deficits | Reduced trap-associated injury | Does not identify every trap constituent | M18B-O018 | EXTRACTED / CROSS-MODULE |
| M18B-PERT017 | M18A-X005 | iPSC-NSC exosomes | Intrathecal exosome delivery | Mouse SCI | Microglial pyroptosis and functional recovery | Reduced pyroptosis and improved recovery | Vesicle cargo specificity requires separation | M18B-O020 | EXTRACTED / CROSS-MODULE |
| M18B-PERT018 | M18A-X006 | let-7b-5p/LRIG3 | gain/loss and LRIG3 rescue | BV2 and mouse SCI | Pyroptosis | let-7b-5p reduced pyroptosis; LRIG3 rescue reversed it | Direct target validation | M18B-O021 | EXTRACTED / CROSS-MODULE |
| M18B-PERT019 | M18A-X007 | Macrophages | clodronate depletion | Mouse SCI | Foam-cell state and motor recovery | Depletion improved recovery | Cell depletion is not sensor-specific | M18B-O022 | EXTRACTED / CROSS-MODULE |
| M18B-PERT020 | M18A-X008 | C1q/foam-cell lipid | bazedoxifene and anti-C1q | Mouse SCI | Synaptic engulfment and recovery | Preserved synapses and improved function | Lipid-lowering mechanism unresolved | M18B-O023 | EXTRACTED / CROSS-MODULE |
| M18B-PERT021 | M18A-X009 | TREM2 | knockout | Mouse SCI | Debris clearance and DAM activation | Impaired clearance and PI3K-AKT program | Necessity limited to tested context | M18B-O024 | EXTRACTED / CROSS-MODULE |
| M18B-PERT022 | M18A-X010 | TREM2 | COG1410 short versus long activation | Mouse SCI | Early recovery versus late fibrosis | Long-term activation worsened late outcomes | Timing contradiction retained | M18B-O025 | EXTRACTED / CROSS-MODULE |
| M18B-PERT023 | M18A-X012 | H3K9la/TXNIP | 2-DG, TXNIP knockdown, peptide inhibition | Mouse SCI macrophages | NLRP3 and recovery | Reduced inflammation and improved outcomes | Lactate has non-histone effects | M18B-O027 | EXTRACTED / CROSS-MODULE |
| M18B-PERT024 | M18A-X013 | AMPK | metformin/compound C | Rat SCI and BV2 | PANoptosis and recovery | Metformin benefit was blocked by compound C | Pharmacologic specificity boundary | M18B-O028, M18B-O029 | EXTRACTED / CROSS-MODULE |
| M18B-PERT025 | M18A-X016 | IRF1 | DNA-binding-domain inhibition | Rat SCI/microglia | ZBP1/PANoptosis and cytokines | Reduced ZBP1/PANoptosis and inflammatory output | No direct genetic rescue | M18B-O031 | EXTRACTED / CROSS-MODULE |
| M18B-PERT026 | M18A-X017 | TMAO | exposure | Mouse SCI | NLRP3 inflammation | Worsened inflammatory phenotype | PubMed-only source in local archive; dose and quantitative endpoints unavailable | M18B-O032 | EXTRACTED / CROSS-MODULE / ACCESS GAP |
| M18B-PERT027 | M18A-X019 | NLRP3 | thiolutin inhibition | Mouse SCI | Pyroptosis and neuronal apoptosis | Reduced inflammatory death | PubMed-only source in local archive; target specificity and quantitative endpoints unavailable | M18B-O034 | EXTRACTED / CROSS-MODULE / ACCESS GAP |
| M18B-PERT028 | M18A-X022 | Caspase-1 | conditional microglial knockout | Mouse T2D plus SCI | Remyelination and function | Improved recovery and reduced pyroptosis | Conditional model boundary retained | M18B-O037 | EXTRACTED / CROSS-MODULE |
| M18B-PERT029 | M18A-X023 | RAGE/ROS/TXNIP | FPS-ZM1, NAC, verapamil | BV2 and diabetic SCI | NLRP3, phagocytosis, remyelination | Reduced inflammatory signaling and improved outcomes | Systemic target specificity unresolved | M18B-O038 | EXTRACTED / CROSS-MODULE |
| M18B-PERT030 | M18A-X024 | P2Y12R/adenosine/mitophagy | receptor, enzyme, A1R, PINK1/Parkin blockade | Microglia-neuron culture | Neuronal mitochondrial recovery | Blockade attenuated P2Y12R-associated protection | Multi-node epistasis | M18B-O039 | EXTRACTED / CROSS-MODULE |
| M18B-PERT031 | M18A-X025 | P2Y12R | P2Y-TK-Nano | Mouse SCI | Lesion, apoptosis, mitophagy | Improved tissue and mitochondrial outcomes | Nanoparticle delivery boundary | M18B-O040 | EXTRACTED / CROSS-MODULE |
| M18B-PERT032 | M18A-X027 | CCN1 | astrocyte Ccn1 depletion | Mouse SCI | Lipid handling and debris clearance | Impaired microglial buffering | Astrocyte-to-microglia relay | M18B-O042, M18B-O043 | EXTRACTED / CROSS-MODULE |
| M18B-PERT033 | M18A-P001-E002 | RAGE | FPS-ZM1 1 micromolar | Primary rat microglia exposed to HMGB1 | Pro-inflammatory markers and NF-kappaB p65 | Reduced HMGB1-induced iNOS/CD86/TNF-alpha, RAGE, and phospho-NF-kappaB p65 | TLR4 expression was measured but not causally resolved | M18B-O044 | EXTRACTED / FULL-TEXT |
| M18B-PERT034 | M18A-P002-E001 | Extracellular traps | DNase I 5 mg/kg tail vein immediately post-injury | Rat T10 contusion SCI | Trap burden, inflammatory polarization, tissue injury, nerve conduction, and motor recovery | Reduced trap-associated inflammation and injury and improved function | DNA degradation is not sensor-specific | M18B-O046 | EXTRACTED / FULL-TEXT |
| M18B-PERT035 | M18A-P003-E001 | Exosome secretion | GW4869 10 micromolar | BV2 LPS/ATP pyroptosis comparator | GSDMD/caspase-1 and IL-1beta/IL-18 | GW4869 reversed conditioned-medium/exosome protection | Exosome inhibitor is not cargo-specific | M18B-O048 | EXTRACTED / FULL-TEXT |
| M18B-PERT036 | M18A-P003-E002 | iPSC-NSC exosomes | Immediate intrathecal delivery after SCI | Mouse T8 impact SCI | Microglial pyroptosis, myelin, axons, neurons, electrophysiology, and motor recovery | Reduced pyroptosis and improved repair/behavior | Vesicle cargo specificity requires the let-7b arm | M18B-O049 | EXTRACTED / FULL-TEXT |
| M18B-PERT037 | M18A-P003-E003 | let-7b-5p/LRIG3 | let-7b-5p OE/KD exosomes plus LRIG3 gain/loss | BV2 and mouse SCI | Pyroptosis and functional recovery | let-7b-5p OE was protective; KD worsened; LRIG3 gain/loss rescued the phenotype | Direct 3-prime-UTR and rescue evidence | M18B-O050 | EXTRACTED / FULL-TEXT |
| M18B-PERT038 | M18A-P004-E002 | C1q/foam-cell lipid | Bazedoxifene and anti-C1q | Mouse SCI and BMDMs | Synaptic engulfment and recovery | Preserved synapses and improved function | Lipid-lowering mechanism unresolved; complement blockade is more specific | M18B-O051 | EXTRACTED / FULL-TEXT |
| M18B-PERT039 | M18A-P005-E002 | TREM2 | COG1410 short versus long activation | Mouse SCI | Early recovery versus late fibrosis/inflammation | Long-term activation worsened late outcomes | Timing contradiction retained | M18B-O052 | EXTRACTED / FULL-TEXT |
| M18B-PERT040 | M18A-P012-E001 | P2Y12R/adenosine/mitophagy | Receptor, enzyme, A1R, or PINK1/Parkin blockade | Microglia-neuron culture | Neuronal mitochondrial recovery | Blockade attenuated P2Y12R-associated protection | Multi-node epistasis | M18B-O054 | EXTRACTED / FULL-TEXT |
| M18B-PERT041 | M18A-P012-E002 | P2Y12R | P2Y-TK-Nano | Mouse SCI and ex vivo slices | Lesion, apoptosis, and mitophagy | Improved tissue and mitochondrial outcomes | Nanoparticle delivery boundary | M18B-O055 | EXTRACTED / FULL-TEXT |
| M18B-PERT042 | M18A-P011-E002 | Caspase-1 | conditional microglial knockout | Mouse T2D plus SCI | Remyelination, lesion damage, and motor recovery | Improved recovery and reduced pyroptosis | Conditional model boundary retained | M18B-O058 | EXTRACTED / FULL-TEXT |
| M18B-PERT043 | M18A-P011-E003 | RAGE/ROS/TXNIP | FPS-ZM1, NAC, verapamil, and VRP | BV-2 and mouse T2D plus SCI | NLRP3, phagocytosis, axons, conduction, and remyelination | Reduced inflammatory signaling and improved outcomes | Systemic drugs and convergent pharmacology are not microglia-specific | M18B-O059 | EXTRACTED / FULL-TEXT |

## Query Readiness Requirements

- Queries must distinguish a DAMP from its sensor, downstream effector, and phenotype.
- A molecule can have multiple sensors; each route needs its own context and evidence provenance.
- NLRP3 and PANoptosis should be represented as downstream convergence programs, not automatically as DAMP receptors.
- TLR and non-TLR intersections must be directed, context-specific, and independently evidenced.
- Knockout or inhibitor phenotypes must retain species, cell type, timing, ligand, and injury boundaries.

## Consolidation and Saturation Record

- 27 indexed paper/anchor records and 59 experiment-level rows now span protein alarmins, purinergic sensing, debris/complement, metabolic danger, inflammasomes, cytosolic DNA, and cell-death convergence.
- 59 atomic observations, 40 directed edges, and 43 perturbation rows are linked to experiments with receptor, sensor, or convergence boundaries retained.
- Direct SCI causal evidence is strongest for P2X7, AIM2, cGAS-STING/mtDNA, IL-33, S100A9, HMGB1-RAGE, TREM2/C1q, and NLRP3-linked programs.
- RIG-I/MDA5-MAVS remains a search gap in sterile traumatic SCI; S100A9, IL-33, and histone receptor assignment remains contextual rather than canonical.
- Two confirmation search phases added no new mechanistic category; the graph is ready for query use with targeted full-text upgrades still distinguishable from saturation.
