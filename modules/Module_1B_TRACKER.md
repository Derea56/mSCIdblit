# Module 1B: Chronic SCI Lesion Architecture — Evidence Consolidation and Consensus Readiness

## Overview

This tracker begins the post-saturation phase for Module 1A. Module 1B converts the Module 1A experiment-level corpus into atomic observations, author claims, evidence links, contradiction groups, and consensus-ready profiles.

**Boundary condition**: Module 1B may prepare consensus profiles, but project-level `Consensus` records should only be created after observations and author claims are linked to source evidence.

**Input corpus**: Module 1A saturation corpus, 30 papers / 90 experiments through Pass 3.

---

## Module 1B Goals

| Goal ID | Goal | Output Table / Artifact | Status |
|---|---|---|---|
| M1B-G001 | Extract atomic empirical observations from Module 1A experiments | Observation | STARTED |
| M1B-G002 | Extract author interpretations separately from observations | AuthorClaim | STARTED |
| M1B-G003 | Link each claim to supporting or contradicting observations | EvidenceLink | STARTED |
| M1B-G004 | Cluster evidence by lesion-architecture topic | Consensus-ready evidence profiles | STARTED |
| M1B-G005 | Mark contradictions and model-dependent divergences | Contradiction map | STARTED |
| M1B-G006 | Draft consensus statements only after linked evidence exists | Consensus | BLOCKED UNTIL G001-G003 |

---

## Evidence Topic Map

| Topic ID | Consensus-Ready Topic | Primary Papers | Evidence Need | Status |
|---|---|---|---|---|
| M1B-T001 | Chronic SCI lesions organize into fibrotic core, astrocytic border, spared/reactive neural tissue, and cavities | M1A-P001, P002, P003, P004, P007, P008, P009, P026, P027, P029, P030, P031, P032, P033 | Extract anatomy observations and boundary/cell-marker claims | STARTED |
| M1B-T002 | Fibrotic scar cellular origins vary by model and include perivascular fibroblast/pericyte-associated lineages | M1A-P007, P008, P009, P021, P026, P029 | Extract lineage, marker, and compartment observations | STARTED |
| M1B-T003 | Astrocytic borders are active wound-repair structures, not only inhibitory barriers | M1A-P003, P004, P030, P032, P033 | Extract border formation, signaling, and containment observations | STARTED |
| M1B-T004 | Chronic lesion biomechanics are model-dependent and currently directionally conflicting | M1A-P026, P027 | Extract stiffness values, tissue-preparation conditions, and model details | STARTED |
| M1B-T005 | Cavitary lesion and scar-resection studies support scaffold/cell filling as a recurring repair strategy | M1A-P005, P012, P022, P034 | Extract cavity, resection, scaffold, and integration observations | QUEUED |
| M1B-T006 | Spared white matter and remote white matter pathology are major recovery-linked compartments | M1A-P013, P014, P024, P036 | Extract spared WM, Wallerian degeneration, MRI/histology, and recovery observations | QUEUED |
| M1B-T007 | Human chronic SCI pathology shows persistent structural mass, motoneuron loss, remyelination abnormalities, and imaging-visible lesion geometry | M1A-P016, P018, P019, P020, P022, P028 | Extract human-specific tissue/imaging observations | QUEUED |
| M1B-T008 | Immune-glial lesion containment and chronic inflammation shape lesion architecture | M1A-P006, P030, P031, P035 | Extract microglia/macrophage, corralling, and neuroinflammation observations | QUEUED |

---

## Extraction Priority

| Priority | Paper Set | Rationale | Status |
|---|---|---|---|
| 1 | Full-text/source-page papers with dense architecture evidence: P007, P008, P009, P014, P021, P026, P027, P030, P031, P032, P033 | Strongest grounding for first consensus profiles | QUEUED |
| 2 | Human and imaging anchors: P016, P019, P022, P024, P028, P036 | Needed for translational architecture claims | QUEUED |
| 3 | Abstract-level gap fillers: P001, P002, P012, P013, P025, P037 | Use conservatively and label lower confidence | QUEUED |
| 4 | Blocked legacy papers if access improves: P010, P011, P015, P017, P018, P020, P023 | Do not block saturation unless they add a new compartment | DEFERRED |

---

## Pass 4: Observation Extraction Tracker

| Topic ID | Paper ID | Experiment IDs | Target Observation Types | Status | Notes |
|---|---|---|---|---|---|
| M1B-T004 | M1A-P026 | M1A-P026-E001–E004 | Young's modulus, cavity morphometry, ECM/GAG, CNS markers | COMPLETE FIRST PASS | Observation rows M1B-O001–O005 |
| M1B-T004 | M1A-P027 | M1A-P027-E001–E004 | AFM stiffness, fibronectin/GFAP, IMP effect, glial alignment | COMPLETE FIRST PASS | Observation rows M1B-O006–O011 |
| M1B-T002 | M1A-P008 | M1A-P008-E001–E005 | Col1alpha1, PDGFRbeta, NG2 lineage, fibrotic scar geometry | COMPLETE FIRST PASS | Observation rows M1B-O012–O016 |
| M1B-T002 | M1A-P009 | M1A-P009-E001–E004 | Type A pericyte scar attenuation, ECM, axon regeneration | COMPLETE FIRST PASS | Observation rows M1B-O017–O021 |
| M1B-T002 | M1A-P021 | M1A-P021-E001–E005 | PDGFRbeta lineage, fibroblast/pericyte scRNA-seq, CE-F/LA-F, monkey comparison | COMPLETE FIRST PASS | Observation rows M1B-O022–O026 |
| M1B-T003 | M1A-P003 | M1A-P003-E001–E006 | Chronic astrocyte persistence, N-cadherin/beta1-integrin, recruitment | COMPLETE FIRST PASS | Observation rows M1B-O027–O031 |
| M1B-T003 | M1A-P030 | M1A-P030-E001–E002 | Corralling, compaction, inflammatory containment | COMPLETE SOURCE-PAGE PASS | Observation rows M1B-O032–O033 |
| M1B-T003 | M1A-P032 | M1A-P032-E001–E002 | Ryk induction, astrocytic border morphology, wound containment | COMPLETE SOURCE-PAGE PASS | Observation row M1B-O034 |
| M1B-T003 | M1A-P033 | M1A-P033-E001–E002 | Border-forming astrocyte origin and transcriptional program | COMPLETE SOURCE-PAGE PASS | Observation rows M1B-O035–O036 |
| M1B-T001 | M1A-P004 | M1A-P004-E001–E004 | Spatial transcriptomic compartments, scar boundary, marker maps, phase model | COMPLETE FIRST PASS | Observation rows M1B-O037–O040 |
| M1B-T001 | M1A-P007 | M1A-P007-E001–E005 | FnEDA chronic fibrotic scar, GFAP border, fibronectin matrix stability, recovery | COMPLETE FIRST PASS | Observation rows M1B-O041–O044 |
| M1B-T001 | M1A-P001 | M1A-P001-E001–E002 | Chronic repaired tissue zones and scar-ablation/transplantation response | COMPLETE ABSTRACT PASS | Observation row M1B-O045 |
| M1B-T001 | M1A-P031 | M1A-P031-E001–E002 | Single-cell lesion ecology and scar cell-cell interactions | COMPLETE SOURCE-PAGE PASS | Observation row M1B-O046 |

---

## Pass 4A: Atomic Observations Extracted

These rows are tracker-level Observation candidates. They preserve the intended database fields while remaining reviewable before materialization into SQL.

| Observation ID | Topic ID | Paper ID | Experiment ID | Figure Ref | Evidence Type | Outcome Type | Observation Value | Normalized Value | Unit | Quantitative | Statistics Reported | Source Section | Extraction Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M1B-O001 | M1B-T004 | M1A-P026 | M1A-P026-E001 | Fig 1 | AFM microindentation | Young's modulus | Chronic rat hemisection scar/injury region had lower Young's modulus than naive tissue; uninjured region averaged about 2.6-fold higher than around injury. | scar softening vs naive tissue | Pa / fold-change | YES | p < 0.0001; Mann-Whitney-Wilcoxon; N = 3 independent tissues for Fig 1 summary | Results / Figure 1 | high | Fresh 500 um sections, 80 um bead, right lateral hemisection, 15-18 WPI; source quote: "2.6-fold higher". |
| M1B-O002 | M1B-T004 | M1A-P026 | M1A-P026-E002 | Fig 2 | Histology / morphometry | Tissue architecture | Chronic hemisection scar contained cavitation/syrinx areas interspersed with dense, disorganized nuclei packing. | cavitary scar architecture with dense nuclei regions | qualitative + distance | YES | DNA content decreased; nuclei spacing quantified in source | Results / Figure 2 | high | Supports structural explanation for altered mechanics; source quote: "areas of cavitation". |
| M1B-O003 | M1B-T004 | M1A-P026 | M1A-P026-E003 | Fig 3 | Immunohistochemistry | Cell marker distribution | Scar tissue showed loss/dysregulation of dominant CNS cell markers with vimentin upregulation. | reduced CNS cell marker profile; increased vimentin | normalized intensity | YES | IHC quantified by normalized intensity | Results / Figure 3 | high | Markers included beta-III tubulin, GFAP, myelin/antigalactocerebroside, tenascin R, vimentin, and Hoechst. |
| M1B-O004 | M1B-T004 | M1A-P026 | M1A-P026-E004 | Fig 4B-C | Biochemical ECM assay | Sulfated GAG / CSPG content | Total sGAGs decreased in scar-containing tissue, while targeted CSPG analysis showed roughly two-fold increase versus naive tissue. | total sGAG down; CSPG subset up | relative quantity / fold-change | YES | Kruskal-Wallis with Dunn's multiple comparison | Results / Figure 4 | high | Shows ECM components diverge by GAG subclass; source quote: "nearly a two-fold increase". |
| M1B-O005 | M1B-T004 | M1A-P026 | Fig 4D | Biochemical ECM assay | Hyaluronic acid content | Hyaluronic acid was upregulated in chronic scar tissue. | HA upregulated in chronic scar | concentration / relative quantity | YES | Kruskal-Wallis with Dunn's multiple comparison | Results / Figure 4 | high | Authors interpret GAG/HA dysregulation as likely relevant to elastic behavior. |
| M1B-O006 | M1B-T004 | M1A-P027 | M1A-P027-E001 | Fig 1 | AFM microindentation | Method validation | Frozen/thawed and fresh uninjured mouse spinal cord preparations did not differ significantly in measured elastic modulus. | sample preparation comparison showed no significant difference | Pa | YES | p = 0.3823; Mann-Whitney test | Results / Figure 1 | high | Important method-control observation because Cooper used 10 um cryosections on slides. |
| M1B-O007 | M1B-T004 | M1A-P027 | M1A-P027-E002 | Fig 2 | AFM microindentation | Young's modulus | Chronic severe mouse contusion lesion regions were stiffer than uninjured spinal cord. | chronic contusion stiffening vs uninjured | Pa | YES | significance reported in Fig 2 / source tables | Results / Figure 2 | high | Severe T11 contusion, 12 WPI, female C57BL/6 mice. |
| M1B-O008 | M1B-T004 | M1A-P027 | M1A-P027-E003 | Fig 3-Fig 4 | Cell culture morphology | Astrocyte mechanosensitivity | Mouse and human astrocytes cultured on 2000 Pa substrate showed stiffness-associated morphology changes relative to 200 Pa substrate. | astrocytes respond to scar-range stiffness | Pa substrate stiffness | YES | human circularity p < 0.01; complexity p < 0.0001 | Results / Figures 3-4 | high | Supports plausibility that tissue mechanics can influence glial phenotype; source quote: "2000 Pa substrate". |
| M1B-O009 | M1B-T004 | M1A-P027 | M1A-P027-E004 | Fig 5B | AFM microindentation | Young's modulus after treatment | Overall lesion-site stiffness after IMP treatment was 517 Pa versus 1217 Pa in saline-treated injured mice and 405 Pa in uninjured spinal cord. | IMP reduced chronic lesion stiffness toward uninjured values | Pa | YES | p = 0.0180; Kruskal-Wallis test | Results / Figure 5 | high | Directly links reduced fibrotic scarring intervention to reduced stiffness. |
| M1B-O010 | M1B-T004 | M1A-P027 | M1A-P027-E004 | Fig 5C-D | AFM microindentation | Lesion subregion stiffness | In IMP-treated mice, lesion rim was stiffer than lesion core: 601 Pa versus 434 Pa. | IMP-treated rim > core stiffness | Pa | YES | p = 0.0432; Mann-Whitney test | Results / Figure 5 | high | Indicates subregion mechanics remain spatially heterogeneous after treatment. |
| M1B-O011 | M1B-T004 | M1A-P027 | M1A-P027-E004 | Fig 6 | Image analysis / GFAP alignment | Glial fiber alignment | Saline-treated chronic contusion scars showed highly aligned GFAP-positive fibers; IMP-treated tissue had reduced alignment approaching uninjured controls. | IMP reduced pathological glial fiber alignment | alignment coefficient | YES | p < 0.01; one-way ANOVA with Tukey post hoc; n = 5 mice/group | Results / Figure 6 | high | CurveAlign measured glial/fibrotic interface alignment; source quote: "p < 0.01". |
| M1B-O012 | M1B-T002 | M1A-P008 | M1A-P008-E001 | Fig 1A-M | LSFM / immunophenotyping | Baseline scar-lineage identity | In uninjured mouse spinal cord, Col1alpha1-positive cells localized mainly along larger blood vessels, expressed CD13 and PDGFRbeta, and lacked NG2, nestin, alphaSMA, immune, endothelial, astrocyte, oligodendrocyte, and fibrocyte markers. | Col1alpha1-positive perivascular fibroblast-like baseline population | percent marker overlap / qualitative location | YES | 60.9 +/- 5.1% around smooth muscle cells; 78.7% CD13-positive; 95.7% PDGFRbeta-positive | Results / Figure 1 | high | Supports distinction from NG2/nestin pericyte marker profile; source quote: "preferentially around larger-diameter blood vessels". |
| M1B-O013 | M1B-T002 | M1A-P008 | M1A-P008-E002 | Fig 2A-H, K-M | Time-course IHC / LSFM | Fibrotic scar organization | After T8 contusion, Col1alpha1-positive cells accumulated from 4-5 DPI, peaked at 7 DPI, and by 14 DPI formed a fibrous scar apposed to the GFAP-positive astrocytic border; 5-HT axons did not penetrate the Col1alpha1-positive region. | delayed Col1alpha1-positive fibrotic scar formation with axon-excluding border | days post injury / qualitative boundary | YES | one-way ANOVA, p < 0.0001 for cell-density time course | Results / Figure 2 | high | Female Col1alpha1-GFP mice, 75 kdyn T8 contusion, dura largely intact. |
| M1B-O014 | M1B-T002 | M1A-P008 | M1A-P008-E003 | Fig 3A-O | Immunophenotyping | Injury-induced marker shift | Col1alpha1-positive scar cells remained broadly PDGFRbeta-positive after contusion, CD13 expression decreased by 14 DPI, alphaSMA was transient and low by 14 DPI, and nonfibroblast lineage markers remained absent. | PDGFRbeta-positive Col1alpha1 scar cells with dynamic CD13/alphaSMA phenotype | percent marker overlap | YES | 100% PDGFRbeta-positive; 26.9% CD13-positive at 14 DPI; about 3.09% alphaSMA-positive at 14 DPI | Results / Figure 3 | high | Important because PDGFRbeta labels multiple perivascular populations and cannot alone define origin. |
| M1B-O015 | M1B-T002 | M1A-P008 | M1A-P008-E004 | Fig 2I-J, O-V | Comparative histology | Injury-model scar geometry | Dorsal hemisection and contusion had similar timing of Col1alpha1-positive cell accumulation, but hemisection produced a Col1alpha1-positive scar continuous with dura and a laminin distribution throughout the injury site rather than mainly peripheral rim. | dural disruption shifts fibrotic scar geometry toward meningeal continuity | qualitative model comparison | YES | n = 3 per dorsal hemisection time point | Results / Figure 2 | high | Boundary condition for contusion versus penetrating injury origin. |
| M1B-O016 | M1B-T002 | M1A-P008 | M1A-P008-E005 | Fig 4A-L | NG2-CreER lineage tracing | Pericyte contribution | NG2-lineage cells localized mostly outside the Col1alpha1-positive injury epicenter after contusion, and red NG2-lineage cells rarely overlapped with green Col1alpha1-positive scar cells. | NG2-positive pericytes/OPCs not major Col1alpha1-positive scar source | qualitative lineage overlap | YES | n = 3 at 14 DPI; rare overlap noted | Results / Figure 4 | high | Authors caution NG2-CreER labels only a fraction of NG2-positive pericytes. |
| M1B-O017 | M1B-T002 | M1A-P009 | M1A-P009-E001 | Fig 1A-G | Genetic attenuation / histology | Fibrotic scar occupancy | Tamoxifen-induced Glast-Rasless recombination reduced PDGFRbeta-positive stromal scar occupancy after dorsal hemisection; complete blockade in 3 of 12 tamoxifen-treated mice caused failure to close the injury site, whereas 9 of 12 showed partial attenuation with tissue integrity. | partial type A pericyte-derived scar reduction; complete block produces tissue defect | proportion / qualitative phenotype | YES | 3/12 Tam-def; 9/12 Tam intermediate; PDGFRbeta scar occupancy quantified | Results / Figure 1 | high | Separates beneficial attenuation from harmful ablation. |
| M1B-O018 | M1B-T002 | M1A-P009 | M1A-P009-E001 | Fig 1E-G, Fig S2 | RNA-seq / ECM validation | Fibrosis program | At 2 WPI, vehicle versus tamoxifen lesion RNA-seq identified 1,099 differentially expressed genes enriched for ECM organization, collagen fibril organization, adhesion, angiogenesis, and wound healing; fibrosis-associated genes were reduced in Tam animals and clustered with uninjured profiles. | broad ECM/fibrosis transcriptional program depends on type A pericyte progeny | differential expression | YES | FDR-adjusted p < 0.05; fold change > +/-1.5 | Results / Figure 1 | high | Supports mechanism beyond PDGFRbeta area alone. |
| M1B-O019 | M1B-T002 | M1A-P009 | M1A-P009-E002 | Fig 2-Fig 4 | Axon tracing / IHC | Axonal regeneration | Moderate reduction of pericyte-derived scarring reduced CST dieback/retraction features and allowed CST axons to enter or extend beyond lesion tissue at chronic time points, whereas vehicle and tissue-defect animals showed little or no regeneration. | moderate scar attenuation permits CST regeneration | percent traced CST axons / distance | YES | 10.5 +/- 2.1% traced CST axons reached lesion site in Tam animals at 18 WPI | Results / Figures 2-4 | high | Tam-def tissue defects did not improve CST regeneration, reinforcing the partial-attenuation boundary. |
| M1B-O020 | M1B-T002 | M1A-P009 | M1A-P009-E003 | Fig 5-Fig 6 | Optogenetics / electrophysiology | Circuit integration | In scar-attenuated mice with ChR2-labeled CST axons, photostimulation evoked postsynaptic activity caudal to the lesion, supporting functional integration of regenerated CST projections. | regenerated CST axons functionally integrate below lesion | electrophysiological response | YES | electrophysiology and optogenetic stimulation reported | Results / Figures 5-6 | high | Source conclusion links regenerated axons to local spinal circuitry below lesion. |
| M1B-O021 | M1B-T002 | M1A-P009 | M1A-P009-E004 | Fig 7A-H | Behavioral assays / correlation | Functional recovery | Animals with attenuated pericyte-derived scarring showed improved sensorimotor recovery, and regenerated axon number correlated with behavioral improvement. | scar attenuation-associated axon growth tracks recovery | behavioral score / correlation | YES | correlation analyses reported; horizontal ladder, CatWalk, and ChR2-assisted behavior used | Results / Figure 7 | high | Behavioral analysis excluded animals with spared CST fibers and tissue defects. |
| M1B-O022 | M1B-T002 | M1A-P021 | M1A-P021-E001 | Fig 1A-I | PDGFRbeta lineage tracing / IHC | Injury-model recruitment | PDGFRbeta-lineage cells were recruited into lesion cores after both transection and crush SCI, with higher density after transection; many proliferated at 5 DPI and about half were BrdU-positive by 14 DPI. | PDGFRbeta-positive stromal recruitment is injury-model dependent | cell density / percent proliferation | YES | 49.18 +/- 2.86% Ki67-positive after transection and 43.26 +/- 2.24% after crush at 5 DPI | Results / Figure 1 | high | Transection is penetrating; crush is non-penetrating with intact dura. |
| M1B-O023 | M1B-T002 | M1A-P021 | M1A-P021-E002 | Fig 2-Fig 3 | scRNA-seq / lineage tracing | Scar-cell source | PDGFRbeta-positive lesion cells included fibroblasts, dividing fibroblasts, and pericytes/vSMCs, but Col1a2-lineage fibroblasts overlapped strongly with Col1-positive scar regions whereas Myh11- and NG2-lineage pericyte/vSMC cells contributed little to the lesion core. | fibroblasts, not Myh11/NG2 pericytes/vSMCs, primary scar source in this lineage system | cell cluster / lineage overlap | YES | 44,386 PDGFRbeta-lineage scRNA-seq cells; lineage-density comparisons reported | Results / Figures 2-3 | high | Directly boundary-checks pericyte/vSMC interpretation. |
| M1B-O024 | M1B-T002 | M1A-P021 | M1A-P021-E003 | Fig 4A-E | Spatial marker mapping | Fibroblast subtype organization | Meningeal Crabp2/Emb fibroblasts localized mainly to central fibrotic scar regions, while perivascular/pial Lama1/Lama2 fibroblasts localized mainly to peripheral/perivascular scar regions after transection and crush SCI. | CE-F central; LA-F peripheral/perivascular | spatial compartment | YES | Emb/Lama1 and Crabp2/Lama2 areas quantified at 14 DPI | Results / Figure 4 | high | Adds subcompartment structure within the fibrotic scar. |
| M1B-O025 | M1B-T002 | M1A-P021 | M1A-P021-E004 | Fig 6A-H | Monkey scRNA/snRNA-seq / IHC | Cross-species conservation | Rhesus macaque transection lesions showed fibroblast subtype organization comparable to mouse SCI, including CE-F-like and LA-F-like populations in lesion core/edge samples. | mouse fibroblast scar subtypes have monkey analogs | cross-species cell-state comparison | YES | female rhesus macaques sampled at 0, 7, 14, 30 DPI, and 6 MPI | Results / Figure 6 | high | Supports translational relevance but in complete transection monkey model. |
| M1B-O026 | M1B-T002 | M1A-P021 | M1A-P021-E005 | Fig 7-Fig 8 | Pathway analysis / in vitro assays | Fibroblast subtype function | CE-F showed stronger cholesterol synthesis and type I collagen/fibronectin programs, while LA-F showed laminin/type IV collagen, lipid transport/storage, and angiogenesis-associated function including stronger endothelial tube formation support. | CE-F and LA-F have distinct ECM/metabolic/vascular functions | gene program / functional assay | YES | GO enrichment, Bodipy/myelin uptake, RT-qPCR, tube formation, and ligand-receptor analyses reported | Results / Figures 7-8 | high | Functionalizes scar compartments instead of treating fibrosis as one cell state. |
| M1B-O027 | M1B-T003 | M1A-P003 | M1A-P003-E001 | Fig 1A-E | Histology / LMD-qPCR | Chronic astrocytic scar persistence | After T9 contusion, GFAP-positive astrocytic scar area and astrocyte process overlap increased over time and persisted to 12 WPI; chronic astrocytes differed transcriptionally from subacute scar-forming astrocytes. | chronic glial scar persists but changes phenotype over time | area / process overlap / qPCR | YES | p < 0.05 threshold; group comparisons reported | Results / Figure 1 | high | Chronic astrocytes had higher Sox9 but lower Cdh2, Csgalanact1, and Pcan than 2 WPI scar-forming astrocytes. |
| M1B-O028 | M1B-T003 | M1A-P003 | M1A-P003-E002 | Fig 2A-F | In vitro astrocyte culture | Scar-forming astrocyte stability | IL-6 reactive astrocytes converted to collagen-I-grown scar-forming astrocytes on type I collagen; after reseeding onto Poly-D-lysine, Col-I-SAs retained flattened morphology, N-cadherin expression, and SA-marker gene expression. | once induced, Col-I-SA phenotype resists collagen-signal withdrawal | qPCR / morphology | YES | n = 6 wells per group; ANOVA/Tukey-Kramer and Wilcoxon tests | Results / Figure 2 | high | Indicates scar-forming astrocyte state is not simply reversed by removing the initiating collagen surface. |
| M1B-O029 | M1B-T003 | M1A-P003 | M1A-P003-E003 | Fig 3A-D | In vitro antibody blockade | Pathway robustness | Anti-beta1-integrin or N-cadherin-neutralizing antibody treatment did not revert Col-I-SA morphology or SA-marker gene expression to reactive or naive astrocyte states in vitro. | established Col-I-SAs resist beta1-integrin/N-cadherin blockade in vitro | qPCR / morphology | YES | n = 6 wells per group; Wilcoxon rank-sum tests | Results / Figure 3 | high | Distinguishes prevention of transformation from reversal of established scar astrocytes. |
| M1B-O030 | M1B-T003 | M1A-P003 | M1A-P003-E004 | Fig 4A-F | Astrocyte transplantation / LMD-qPCR | Scar-forming astrocyte recruitment | EGFP-positive Col-I-SAs transplanted into naive spinal cord formed N-cadherin-rich astroglial scar-like clusters and induced nearby host GFAP-positive astrocytes to express SA-associated genes. | scar-forming astrocytes self-maintain and recruit adjacent astrocytes | qPCR / IHC | YES | n = 6 mice per group; Wilcoxon rank-sum tests | Results / Figure 4 | high | Host astrocytes increased Cdh2, Sox9, Acan, and Pcan after transplantation. |
| M1B-O031 | M1B-T003 | M1A-P003 | M1A-P003-E005–E006 | Fig 5A-H | In vivo antibody treatment | Chronic scar modulation / axon growth | Anti-beta1-integrin antibody blocked recruitment of host scar-forming astrocytes after SA transplantation and, when injected from 14-28 DPI after SCI, reduced GFAP/N-cadherin-positive chronic astrocytes and increased GAP43-positive area. | beta1-integrin blockade reduces chronic SA recruitment and increases GAP43 signal | cell count / area | YES | n = 6 mice per group; Wilcoxon rank-sum tests; p < 0.05 | Results / Figure 5 | high | Supports intervention on recruitment rather than direct in vitro reversion. |
| M1B-O032 | M1B-T003 | M1A-P030 | M1A-P030-E001 | Fig 1 / source page | Myeloid nuclear RNA-seq | Injury-activated myeloid state | Cx3cr1-CreER INTACT profiling identified temporal injury-activated microglia/macrophage signatures at 3, 7, and 14 DPI after T8 dorsal column transection. | temporal IAM program after SCI | RNA-seq time course | YES | Source-page level in Module 1A | Source page / Module 1A row | medium | Included because astrocytic border formation is coupled to immune corralling and wound compaction. |
| M1B-O033 | M1B-T003 | M1A-P030 | M1A-P030-E002 | Fig 2-Fig 7 / source page | Conditional deletion / histology / function | Corralling and containment | Myeloid Plexin-B2 deletion disrupted lesion-core corralling, astrocytic border containment, matrix compaction, inflammatory restriction, axon regeneration, and motor-sensory recovery after dorsal column transection. | myeloid Plexin-B2 promotes wound compaction and astrocytic containment | qualitative + functional assays | YES | Source-page level in Module 1A | Source page / Module 1A row | medium | Bridges M1B-T003 with immune-glial containment topic M1B-T008. |
| M1B-O034 | M1B-T003 | M1A-P032 | M1A-P032-E001–E002 | Abstract/source page | Astrocyte signaling perturbation | Border morphology / wound architecture | Source-page extraction reports that astrocytic Ryk is induced after SCI and that astrocyte-focused Ryk perturbation alters morphological transformation, scarring, wound architecture, and lesion-core containment. | astrocytic Ryk coordinates border formation and wound healing | source-page qualitative | YES | Source-page level in Module 1A | Abstract / source page | medium | Needs full-text parsing before high-confidence observation materialization. |
| M1B-O035 | M1B-T003 | M1A-P033 | M1A-P033-E001 | Abstract/source page | Lineage analysis | Border astrocyte origin | Source-page extraction reports that border-forming astrocytes after SCI or stroke arise mainly from local astrocytes, with a minority contribution from OPC-derived astrocytes. | local astrocytes are major border-forming source; OPCs minor source | source-page lineage proportion | YES | Source-page level in Module 1A | Abstract / source page | medium | Complements Tamaru's recruitment model with origin tracing. |
| M1B-O036 | M1B-T003 | M1A-P033 | M1A-P033-E002 | Abstract/source page | snRNA-seq / temporal transcriptomics | Wound-repair astrocyte state | Source-page extraction reports temporal transcriptomic and single-nucleus RNA-seq definition of border-forming wound repair astrocyte programs after SCI/stroke. | border astrocytes are a wound-repair transcriptional state | source-page transcriptomic program | YES | Source-page level in Module 1A | Abstract / source page | medium | Supports classification of astrocytic scar as an active wound-repair compartment. |
| M1B-O037 | M1B-T001 | M1A-P004 | M1A-P004-E001 | Fig 1A-L | Spatial transcriptomics / H&E | Scar spatial atlas | Gong generated a T10 lateral hemisection spatial transcriptomic atlas across 3, 7, 14, and 28 DPI using 32 sections and 15,449 spots, mapping clusters back to tissue morphology to define scar regions. | spatially mapped scar maturation atlas | spatial spots / time course | YES | 32 sections; 15,449 spots; 3, 7, 14, 28 DPI | Results / Figure 1 | high | Provides architecture scaffold for Module 1B compartment definitions. |
| M1B-O038 | M1B-T001 | M1A-P004 | M1A-P004-E002 | Fig 2-Fig 8 | ST reclustering / marker mapping | Scar-resident cell composition | Reclustered scar spots resolved six major scar-resident cell groups: microglia, macrophages, astrocytes, oligodendrocytes, fibroblasts, and endothelial cells; fibroblasts occupied the scar center from 7 DPI, with microglia, astrocytes, and oligodendrocytes arranged outward toward the boundary. | multicellular scar with fibroblast core and glial/immune boundary layers | cell-state spatial distribution | YES | Scar-cell fractions quantified across maturation stages | Results / Figures 2-8 | high | Source also notes very few neurons in the scar area. |
| M1B-O039 | M1B-T001 | M1A-P004 | M1A-P004-E004 | Fig 10A-F | Tissue transparency / ST marker maps | Scar boundary markers | Laminin, Fn1, collagen IV staining and ST maps showed changing scar marker distributions; fibroblasts remained central during shrinkage/maturation, while microglial and astrocytic scar regions expanded along white matter at 28 DPI. | ECM marker maps define dynamic scar boundary and subcompartments | spatial marker map / cell fraction | YES | Cell-type spot counts and fractions quantified | Results / Figure 10 | high | Confirms fibrotic scar surrounded by microglial scar wrapped by astrocytic scar in this model. |
| M1B-O040 | M1B-T001 | M1A-P004 | M1A-P004-E003–E004 | Fig 9-Fig 10G | WGCNA / phase synthesis | Scar maturation phase model | Gong proposed four scar-formation phases after lateral hemisection: macrophage infiltration, proliferation/differentiation of scar-resident cells, scar emergence, and stationary scar. | four-phase scar maturation model | phase classification | NO | WGCNA modules and cell-fraction trajectories support synthesis | Results / Discussion | medium | Interpretive synthesis from spatial transcriptomics, not a direct single assay. |
| M1B-O041 | M1B-T001 | M1A-P007 | M1A-P007-E001 | Fig 1A-G | qPCR / western blot | Fibrotic ECM isoform time course | FnEDA and FnEDB were low/detectable in uninjured spinal cord, rose sharply after T11 contusion, and remained elevated even 13 weeks after injury. | persistent cellular fibronectin isoform expression after SCI | fold-change / protein level | YES | FnEDA mRNA about 70-fold and FnEDB about 40-fold at 7 DPI; n = 8-10 for qPCR | Results / Figure 1 | high | FnEDA protein increased around 10-fold by 7 DPI and declined but remained elevated. |
| M1B-O042 | M1B-T001 | M1A-P007 | M1A-P007-E002 | Fig 2A-I | IHC / western blot | Chronic fibrotic scar anatomy | FnEDA-null mice had smaller GFAP-bounded lesion cores and lower fibronectin intensity inside the GFAP-negative lesion core at 90 DPI, while GFAP glial scarring was not reduced. | FnEDA deletion reduces chronic fibrotic core without reducing glial rim | lesion area / intensity | YES | lesion area p < 0.01; fibronectin intensity p < 0.01 | Results / Figure 2 | high | Supports separability of fibrotic core and astrocytic border compartments. |
| M1B-O043 | M1B-T001 | M1A-P007 | M1A-P007-E003 | Fig 3A-F | DOC/SDS fractionation | Matrix stability | At 21 and 90 DPI, FnEDA-null mice had reduced insoluble matrix-assembled fibronectin while soluble fibronectin did not differ from wildtype. | FnEDA stabilizes chronic assembled fibronectin matrix | soluble/insoluble protein fraction | YES | n = 7-8 mice/group; p < 0.01 | Results / Figure 3 | high | No difference in soluble/insoluble fibronectin at 7 DPI. |
| M1B-O044 | M1B-T001 | M1A-P007 | M1A-P007-E004–E005 | Fig 4-Fig 5 | Axon staining / behavior | Axon density and recovery | FnEDA-null mice had higher SMI-312 axonal density in lesion areas at 90 DPI and improved locomotor recovery by BMS and modified BBB compared with wildtype controls. | reduced chronic fibrotic matrix associates with axon density and recovery | staining intensity / behavior score | YES | SMI-312 p < 0.05 or p < 0.01 by distance; behavior p < 0.05 to p < 0.001 | Results / Figures 4-5 | high | Functional link supports chronic fibrotic compartment as recovery-relevant. |
| M1B-O045 | M1B-T001 | M1A-P001 | M1A-P001-E001–E002 | Abstract | Light microscopy histology | Chronic repaired-tissue zones | Abstract-level extraction reports chronic rat contusion repaired tissue organized into fibrotic, cellular, and axonal zones, and scar ablation plus lamina propria/acellular lamina propria transplantation expanded cellular/axonal zones, reduced cavity, and improved integration with spared tissue. | chronic repaired tissue has zone architecture modifiable by ablation/transplantation | abstract-level qualitative | YES | Abstract-level only | PubMed abstract / Module 1A row | low | Full text needed before high-confidence materialization. |
| M1B-O046 | M1B-T001 | M1A-P031 | M1A-P031-E001–E002 | Abstract/source page | scRNA-seq / interaction inference | Single-cell lesion ecology | Source-page extraction reports that single-cell RNA-seq resolved heterogeneous injured-spinal-cord scar-like cell states and inferred cell-cell interactions shaping the wound-healing/scar environment. | scar is multicellular interaction ecosystem | source-page transcriptomic atlas | YES | Source-page level in Module 1A | Abstract / source page | medium | Supports T001/T008 but needs full-text extraction for exact cell-state names. |

---

## Pass 5: Author Claim Extraction Tracker

| Topic ID | Paper ID | Claim Types To Extract | Status |
|---|---|---|---|
| M1B-T004 | M1A-P026 | conclusion; interpretation; mechanism | COMPLETE FIRST PASS |
| M1B-T004 | M1A-P027 | conclusion; interpretation; mechanism | COMPLETE FIRST PASS |
| M1B-T002 | M1A-P008 | conclusion; mechanism | COMPLETE FIRST PASS |
| M1B-T002 | M1A-P009 | conclusion; mechanism; implication | COMPLETE FIRST PASS |
| M1B-T002 | M1A-P021 | conclusion; mechanism; implication | COMPLETE FIRST PASS |
| M1B-T003 | M1A-P003 | conclusion; mechanism | COMPLETE FIRST PASS |
| M1B-T003 | M1A-P030 | conclusion; mechanism | COMPLETE SOURCE-PAGE PASS |
| M1B-T003 | M1A-P032 | conclusion; mechanism | COMPLETE SOURCE-PAGE PASS |
| M1B-T003 | M1A-P033 | conclusion; mechanism | COMPLETE SOURCE-PAGE PASS |
| M1B-T001 | M1A-P004 | conclusion; interpretation | COMPLETE FIRST PASS |
| M1B-T001 | M1A-P007 | conclusion; mechanism; implication | COMPLETE FIRST PASS |
| M1B-T001 | M1A-P001 | conclusion | COMPLETE ABSTRACT PASS |
| M1B-T001 | M1A-P031 | conclusion; mechanism | COMPLETE SOURCE-PAGE PASS |

---

## Pass 5A: Author Claims Extracted

| Claim ID | Topic ID | Paper ID | Claim Text | Claim Type | Confidence Level | Source Section | Extraction Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| M1B-C001 | M1B-T004 | M1A-P026 | Chronic rat hemisection SCI scar has decreased Young's modulus, and scar softening is associated with cavitation, CNS cell loss/dysregulation, dense nuclei packing, and GAG/HA dysregulation. | conclusion | high | Abstract / Conclusion | high | Claim is directly aligned with Fig 1-Fig 4 observations. |
| M1B-C002 | M1B-T004 | M1A-P026 | Differences between chronic scar mechanics studies likely depend on injury model, time point, sample preparation, and AFM methodology. | interpretation | medium | Introduction / Discussion | high | Boundary-condition claim explicitly discusses Cooper 2020 versus Baumann 2020. |
| M1B-C003 | M1B-T004 | M1A-P027 | Chronic severe mouse contusion SCI produces mechanical stiffening of spinal lesion tissue compared with uninjured tissue. | conclusion | high | Abstract / Discussion | high | Directly supported by AFM lesion measurements. |
| M1B-C004 | M1B-T004 | M1A-P027 | Fibrotic scarring is a key driver of chronic mechanical stiffening after SCI, because immune-modifying nanoparticle treatment reduces fibrotic scarring and rescues lesion stiffness. | mechanistic | medium | Abstract / Discussion | high | Supported by IMP intervention but still mechanistic because IMP has immune and scar effects. |
| M1B-C005 | M1B-T004 | M1A-P027 | Chronic lesion stiffness is biologically relevant because mouse and human astrocytes respond to substrate stiffness values in the injured/uninjured spinal cord range. | implication | medium | Results / Discussion | high | Supported by in vitro substrate observations; extrapolation to in vivo phenotype remains interpretive. |
| M1B-C006 | M1B-T002 | M1A-P008 | In contusive SCI with largely intact dura, Col1alpha1-positive perivascular fibroblasts are a major source of the fibrotic scar and are distinct from NG2-positive pericytes. | conclusion | high | Abstract / Discussion / Conclusion | high | Strongly supported by Col1alpha1-GFP mapping, immunophenotyping, LSFM, and NG2 lineage tracing. |
| M1B-C007 | M1B-T002 | M1A-P008 | Fibrotic scar origin and geometry differ with injury type because penetrating injuries that disrupt dura can add meningeal continuity not seen in closed-dura contusion. | interpretation | medium | Results / Discussion | high | Supported by dorsal hemisection versus contusion comparison. |
| M1B-C008 | M1B-T002 | M1A-P009 | Type A pericyte-derived stromal cells are required for fibrotic scar tissue generation and broad injury-induced ECM/fibrosis gene expression after SCI. | mechanistic | high | Results / Discussion | high | Supported by Glast-Rasless attenuation, histology, RNA-seq, qPCR/protein validation. |
| M1B-C009 | M1B-T002 | M1A-P009 | Moderate attenuation of pericyte-derived fibrotic scarring promotes CST and raphespinal axon regeneration, circuit integration, and sensorimotor recovery after SCI. | conclusion | high | Abstract / Results / Conclusion | high | Supported across tracing, optogenetics, electrophysiology, behavior, and correlation analyses. |
| M1B-C010 | M1B-T002 | M1A-P009 | Complete blockade of fibrotic scar formation is harmful because the fibrotic response is needed for tissue closure; the therapeutic window is partial attenuation rather than ablation. | interpretation | medium | Results / Discussion | high | Based on Tam-def animals with tissue defects and poor regeneration/recovery. |
| M1B-C011 | M1B-T002 | M1A-P021 | Fibrotic scars after transection and crush SCI primarily derive from perivascular and meningeal fibroblasts rather than pericytes/vSMCs in the authors' lineage-tracing system. | conclusion | high | Abstract / Results / Discussion | high | Directly boundary-checks the pericyte-origin model using Myh11, NG2, Col1a2, and Crabp2 lineage tools. |
| M1B-C012 | M1B-T002 | M1A-P021 | Fibrotic scar tissue is heterogeneous: central CE-F and peripheral/perivascular LA-F occupy distinct scar regions and have different ECM, lipid, and angiogenesis-associated programs. | conclusion | high | Abstract / Results / Discussion | high | Supported in mouse and monkey datasets plus functional assays. |
| M1B-C013 | M1B-T003 | M1A-P003 | The glial scar persists into the chronic phase through scar-forming astrocytes that maintain a robust N-cadherin-associated phenotype while changing some gene-expression features over time. | conclusion | high | Abstract / Results / Discussion | high | Supported by contusion time course, LMD-qPCR, and chronic 12 WPI analysis. |
| M1B-C014 | M1B-T003 | M1A-P003 | Established scar-forming astrocytes are not readily reverted by removing collagen signaling or blocking beta1-integrin/N-cadherin in vitro, but beta1-integrin blockade can reduce recruitment of new scar-forming astrocytes in vivo. | mechanistic | high | Results / Discussion | high | Important distinction between state maintenance and recruitment. |
| M1B-C015 | M1B-T003 | M1A-P003 | Reducing beta1-integrin-dependent recruitment of chronic scar-forming astrocytes can shrink the glial scar and promote axonal regeneration markers after SCI. | implication | medium | Results / Discussion | high | GAP43-positive area is a regeneration-associated marker, not a full functional recovery endpoint. |
| M1B-C016 | M1B-T003 | M1A-P030 | Injury-activated microglia/macrophages promote corralling, wound compaction, astrocytic border containment, and recovery through Plexin-B2. | mechanistic | medium | Abstract / source page | medium | Source-page level; full-text extraction still needed. |
| M1B-C017 | M1B-T003 | M1A-P032 | Astrocytic Ryk signaling coordinates astrocyte morphological transformation, scarring, wound healing, and lesion-core containment after SCI. | mechanistic | medium | Abstract / source page | medium | Source-page level; full-text extraction still needed. |
| M1B-C018 | M1B-T003 | M1A-P033 | Border-forming wound repair astrocytes are an active, transcriptionally reprogrammed repair state derived mainly from local astrocytes with a minority OPC-derived contribution. | conclusion | medium | Abstract / source page | medium | Source-page level; full-text extraction still needed. |
| M1B-C019 | M1B-T001 | M1A-P004 | SCI scar architecture is spatially heterogeneous and multicellular, with fibroblast-rich central regions, microglial/astrocytic boundary layers, endothelial/oligodendrocyte-associated compartments, and time-dependent maturation. | conclusion | high | Abstract / Results / Discussion | high | Supported by spatial transcriptomic atlas, marker maps, and cell-fraction analyses. |
| M1B-C020 | M1B-T001 | M1A-P004 | Scar formation follows a staged process in the lateral hemisection model: macrophage infiltration, proliferation/differentiation of scar-resident cells, scar emergence, and stationary scar. | interpretation | medium | Results / Discussion | high | Author synthesis from ST time course; should be model-specific. |
| M1B-C021 | M1B-T001 | M1A-P007 | FnEDA is required for long-term stability of the assembled fibronectin matrix and for the chronic fibrotic scar after contusive SCI, without being required for acute fibrotic response or GFAP glial scarring. | mechanistic | high | Abstract / Results / Discussion | high | Strongly supported by FnEDA-null matrix fractionation and chronic lesion histology. |
| M1B-C022 | M1B-T001 | M1A-P007 | Reducing chronic FnEDA-dependent fibrotic scarring improves axonal density and locomotor recovery after contusive SCI. | implication | medium | Abstract / Results / Discussion | high | Supported by genotype comparison; causal inference should stay tied to FnEDA-null model. |
| M1B-C023 | M1B-T001 | M1A-P001 | Chronic contusion repair tissue can be described as fibrotic, cellular, and axonal zones, and combined scar ablation/transplantation can alter zone integration and cavity morphology. | conclusion | low | Abstract | medium | Abstract-level only; useful as historical/zone-architecture support. |
| M1B-C024 | M1B-T001 | M1A-P031 | The injured spinal cord scar environment is a heterogeneous multicellular ecosystem whose cell-cell interactions shape wound healing and inhibitory scar features. | conclusion | medium | Abstract / source page | medium | Source-page level; full text still needed. |

---

## Pass 6A: Evidence Links

| Link ID | Claim ID | Observation ID | Link Type | Notes |
|---|---|---|---|---|
| M1B-L001 | M1B-C001 | M1B-O001 | directly_supports | AFM evidence for chronic hemisection scar softening. |
| M1B-L002 | M1B-C001 | M1B-O002 | directly_supports | Cavitation and dense nuclei organization are proposed contributors to softening. |
| M1B-L003 | M1B-C001 | M1B-O003 | directly_supports | CNS marker loss/dysregulation and vimentin upregulation support altered cell composition. |
| M1B-L004 | M1B-C001 | M1B-O004 | directly_supports | sGAG/CSPG changes support ECM dysregulation. |
| M1B-L005 | M1B-C001 | M1B-O005 | directly_supports | HA upregulation supports GAG/HA dysregulation. |
| M1B-L006 | M1B-C002 | M1B-O001 | directly_supports | Baumann uses fresh 500 um rat hemisection tissue and reports softening. |
| M1B-L007 | M1B-C002 | M1B-O006 | directly_supports | Cooper validates freeze/thaw method in mouse spinal cord. |
| M1B-L008 | M1B-C002 | M1B-O007 | directly_supports | Cooper uses chronic mouse contusion and reports stiffening. |
| M1B-L009 | M1B-C003 | M1B-O007 | directly_supports | AFM observation supports chronic contusion stiffening. |
| M1B-L010 | M1B-C003 | M1B-O001 | contradicts | Baumann's chronic rat hemisection AFM direction differs from Cooper's chronic mouse contusion direction. |
| M1B-L011 | M1B-C004 | M1B-O009 | directly_supports | IMP reduces lesion stiffness from saline-treated injury levels. |
| M1B-L012 | M1B-C004 | M1B-O011 | partially_supports | IMP changes glial/fibrotic interface alignment; supports scar-architecture effect but not fibrosis alone. |
| M1B-L013 | M1B-C005 | M1B-O008 | directly_supports | Human and mouse astrocyte substrate response supports mechanosensitivity claim. |
| M1B-L014 | M1B-C006 | M1B-O012 | directly_supports | Baseline Col1alpha1-positive cells match a perivascular fibroblast-like profile rather than NG2/nestin pericyte profile. |
| M1B-L015 | M1B-C006 | M1B-O013 | directly_supports | Col1alpha1-positive cells accumulate into the contusion fibrotic scar and form the GFAP-apposed scar region. |
| M1B-L016 | M1B-C006 | M1B-O014 | directly_supports | Injured Col1alpha1-positive scar cells remain PDGFRbeta-positive while excluding nonfibroblast markers. |
| M1B-L017 | M1B-C006 | M1B-O016 | directly_supports | NG2 lineage tracing shows little overlap with Col1alpha1-positive scar cells. |
| M1B-L018 | M1B-C007 | M1B-O015 | directly_supports | Dorsal hemisection produces dura-continuous Col1alpha1 scar geometry distinct from contusion. |
| M1B-L019 | M1B-C007 | M1B-O013 | partially_supports | Contusion scar timing and GFAP border organization provide the comparison point for injury-model geometry. |
| M1B-L020 | M1B-C008 | M1B-O017 | directly_supports | Glast-Rasless attenuation reduces PDGFRbeta-positive stromal scar occupancy. |
| M1B-L021 | M1B-C008 | M1B-O018 | directly_supports | RNA-seq and fibrosis-associated gene changes support dependence of ECM/fibrosis program on type A pericyte progeny. |
| M1B-L022 | M1B-C009 | M1B-O019 | directly_supports | Scar attenuation permits CST axon growth into or beyond lesion regions at chronic time points. |
| M1B-L023 | M1B-C009 | M1B-O020 | directly_supports | Optogenetic/electrophysiology evidence supports caudal circuit integration. |
| M1B-L024 | M1B-C009 | M1B-O021 | directly_supports | Behavioral recovery and axon-count correlations support functional relevance. |
| M1B-L025 | M1B-C010 | M1B-O017 | directly_supports | Tam-def animals show tissue defects when scar formation is completely blocked. |
| M1B-L026 | M1B-C010 | M1B-O019 | directly_supports | Tissue-defect animals do not show the same regeneration benefit as partial-attenuation animals. |
| M1B-L027 | M1B-C011 | M1B-O022 | partially_supports | PDGFRbeta-lineage recruitment establishes scar-forming perivascular/meningeal pool but not fibroblast specificity alone. |
| M1B-L028 | M1B-C011 | M1B-O023 | directly_supports | scRNA-seq and lineage tracing support fibroblast origin and little Myh11/NG2 pericyte/vSMC contribution. |
| M1B-L029 | M1B-C011 | M1B-O016 | concordant_boundary | Soderblom's NG2 tracing is directionally consistent with Xue's limited NG2 contribution, though marker systems differ. |
| M1B-L030 | M1B-C011 | M1B-O017 | contradicts | Dias's type A pericyte-derived scar attenuation claim conflicts with Xue's interpretation that GLAST-positive scar-forming cells are fibroblasts/PFs rather than pericytes/vSMCs. |
| M1B-L031 | M1B-C012 | M1B-O024 | directly_supports | CE-F and LA-F spatial compartment mapping supports heterogeneous scar organization. |
| M1B-L032 | M1B-C012 | M1B-O025 | directly_supports | Monkey lesion profiling supports cross-species relevance of fibroblast subtype organization. |
| M1B-L033 | M1B-C012 | M1B-O026 | directly_supports | Functional assays support distinct CE-F and LA-F roles in ECM, lipid, and angiogenesis programs. |
| M1B-L034 | M1B-C013 | M1B-O027 | directly_supports | Chronic 12 WPI contusion time course supports persistence plus phenotype change. |
| M1B-L035 | M1B-C013 | M1B-O030 | partially_supports | Transplanted SAs self-maintain N-cadherin-rich scar-like clusters, supporting robustness of scar-forming state. |
| M1B-L036 | M1B-C014 | M1B-O028 | directly_supports | Reseeding off collagen does not revert Col-I-SAs. |
| M1B-L037 | M1B-C014 | M1B-O029 | directly_supports | In vitro beta1-integrin/N-cadherin blockade does not revert established Col-I-SAs. |
| M1B-L038 | M1B-C014 | M1B-O031 | directly_supports | In vivo beta1-integrin antibody blocks recruitment and reduces chronic GFAP/N-cadherin-positive astrocytes. |
| M1B-L039 | M1B-C015 | M1B-O031 | directly_supports | Anti-beta1-integrin treatment reduces chronic scar-forming astrocytes and increases GAP43-positive area. |
| M1B-L040 | M1B-C016 | M1B-O032 | partially_supports | IAM transcriptional time course establishes injury-activated myeloid program. |
| M1B-L041 | M1B-C016 | M1B-O033 | directly_supports | Plexin-B2 perturbation observation supports corralling, compaction, and border-containment claim. |
| M1B-L042 | M1B-C017 | M1B-O034 | directly_supports | Ryk source-page observation supports astrocyte border and wound-healing coordination claim. |
| M1B-L043 | M1B-C018 | M1B-O035 | directly_supports | Lineage source-page observation supports local astrocyte-majority and OPC-minority origin claim. |
| M1B-L044 | M1B-C018 | M1B-O036 | directly_supports | snRNA-seq/temporal transcriptomic observation supports wound-repair astrocyte state claim. |
| M1B-L045 | M1B-C018 | M1B-O027 | concordant_boundary | Tamaru's chronic phenotype-shift data is consistent with border astrocytes being dynamic rather than static scar cells. |
| M1B-L046 | M1B-C019 | M1B-O037 | directly_supports | ST atlas provides tissue-wide scar region mapping over time. |
| M1B-L047 | M1B-C019 | M1B-O038 | directly_supports | Reclustered ST spots identify multicellular scar-resident composition and spatial ordering. |
| M1B-L048 | M1B-C019 | M1B-O039 | directly_supports | ECM/ST marker maps support fibrotic core and glial boundary structure. |
| M1B-L049 | M1B-C020 | M1B-O040 | directly_supports | Four-phase model observation directly supports staged scar-formation claim. |
| M1B-L050 | M1B-C021 | M1B-O041 | partially_supports | Persistent FnEDA/FnEDB expression establishes fibronectin isoform response after SCI. |
| M1B-L051 | M1B-C021 | M1B-O042 | directly_supports | FnEDA-null chronic histology supports reduced fibrotic core with preserved GFAP glial scarring. |
| M1B-L052 | M1B-C021 | M1B-O043 | directly_supports | Matrix fractionation supports FnEDA role in insoluble assembled fibronectin stability. |
| M1B-L053 | M1B-C022 | M1B-O044 | directly_supports | FnEDA-null axon-density and behavioral results support recovery implication. |
| M1B-L054 | M1B-C022 | M1B-O042 | partially_supports | Smaller chronic fibrotic lesion core provides anatomical context for recovery effect. |
| M1B-L055 | M1B-C023 | M1B-O045 | directly_supports | Abstract-level chronic rat zone architecture and repair modification support historical claim. |
| M1B-L056 | M1B-C024 | M1B-O046 | directly_supports | Source-page scRNA-seq and interaction inference support multicellular ecosystem claim. |
| M1B-L057 | M1B-C024 | M1B-O038 | concordant_boundary | Gong spatial atlas is consistent with Milich source-page single-cell heterogeneity. |

---

## Consensus-Ready Evidence Profiles

### M1B-T004: Chronic Lesion Biomechanics

**Status**: consensus-ready profile started; consensus statement not yet finalized.

| Profile Element | Curated Summary |
|---|---|
| Evidence base | Two full-text studies, M1A-P026 and M1A-P027, with 11 extracted observations and 5 author claims. |
| Agreement | Both papers support the idea that chronic SCI scar/lesion tissue has altered mechanical properties relative to uninjured spinal cord and that mechanics may influence regeneration-relevant cell behavior. |
| Directional conflict | M1A-P026 reports reduced Young's modulus in chronic rat hemisection scar; M1A-P027 reports increased Young's modulus in chronic mouse contusion lesion tissue. |
| Likely boundary conditions | Species, injury type, chronic time point, tissue section thickness, fresh versus freeze/thaw preparation, AFM indenter size, lesion subregion definition, and whether the sampled tissue is dominated by cavitation/fibrotic core/glial rim. |
| Current interpretation | The database should not store a single direction for "chronic scar stiffness." The better curated statement is that chronic lesion mechanics are model- and method-dependent, with both softening and stiffening reported under different experimental conditions. |
| Next evidence needed | Add Saxena/Moeendarbary-type earlier mechanics papers if in corpus or retrieve them as boundary-condition papers; extract exact subregion values from supplementary tables where available. |

### M1B-T002: Fibrotic Scar Cellular Origins

**Status**: consensus-ready profile started; consensus statement not yet finalized.

| Profile Element | Curated Summary |
|---|---|
| Evidence base | Three full-text studies, M1A-P008, M1A-P009, and M1A-P021, with 15 extracted observations and 7 author claims. |
| Agreement | All three papers support the fibrotic/stromal scar as an active lesion compartment produced by perivascular/meningeal-associated cells rather than by astrocytes or infiltrating immune cells alone. |
| Strong points | Soderblom identifies Col1alpha1-positive perivascular fibroblast-like cells as a major closed-dura contusion source; Dias shows that reducing GLAST/type A pericyte-derived scar progeny reduces fibrosis and improves regeneration/recovery when attenuation is partial; Xue resolves fibrotic scar heterogeneity into fibroblast subtypes with distinct spatial and functional programs. |
| Main conflict | Dias frames the therapeutically relevant lineage as type A pericyte-derived, while Soderblom and Xue argue that NG2/Myh11 pericytes or vSMCs are not the primary Col1/PDGFRbeta-positive fibrotic scar source in their systems. |
| Likely boundary conditions | Injury model and dural disruption, marker/Cre-driver choice, pericyte definition, whether GLAST-positive cells are classified as pericytes or perivascular fibroblasts, sampled time point, and whether the endpoint is cell origin, ECM production, tissue closure, or regeneration. |
| Current interpretation | The database should not collapse fibrotic scar origin into a single universal cell name. A safer curated statement is that SCI fibrotic scar is produced by perivascular/meningeal stromal lineages, with lineage labels differing across marker systems; partial modulation can be beneficial, but complete scar ablation can impair lesion closure. |
| Next evidence needed | Add source-page level M1A-P029 and Cooper 2018/M1A-P007 as boundary-condition papers; extract exact GLAST/PDGFRbeta/Col1a2 lineage definitions into controlled vocabulary before final consensus. |

### M1B-T003: Astrocytic Border and Wound-Repair State

**Status**: consensus-ready profile started; consensus statement not yet finalized.

| Profile Element | Curated Summary |
|---|---|
| Evidence base | One full-text study, M1A-P003, plus three source-page studies, M1A-P030, M1A-P032, and M1A-P033, with 10 extracted observations and 6 author claims. |
| Agreement | The astrocytic scar/border is an active wound-repair structure that persists, changes over time, is influenced by matrix and cell-cell signaling, and interacts with immune/stromal lesion containment rather than functioning only as a passive inhibitory wall. |
| Strong points | Tamaru gives high-confidence evidence that scar-forming astrocytes persist to chronic time points, recruit neighboring astrocytes, and can be modulated through beta1-integrin-dependent recruitment. Zhou, Shen, and O'Shea extend the concept toward immune corralling, Ryk-mediated astrocyte morphology, and transcriptionally defined wound-repair astrocytes. |
| Main uncertainty | The newer border-mechanism papers are currently source-page level in this tracker; they should not yet carry the same weight as Tamaru's full-text extraction. |
| Likely boundary conditions | Acute/subacute versus chronic phase, contusion versus transection, whether the endpoint is astrocyte state maintenance or recruitment of new border astrocytes, and whether border failure is driven primarily by astrocytes or by myeloid corralling defects. |
| Current interpretation | A safe curated statement is that astrocytic borders are dynamic repair compartments with separable processes of formation, maintenance, recruitment, and containment. Established scar astrocytes may be hard to revert directly, while recruitment and border organization remain intervention-sensitive. |
| Next evidence needed | Pull full text for M1A-P030, M1A-P032, and M1A-P033 into local evidence files; add M1A-P004 spatial transcriptomics as a full-text bridge between astrocyte, fibroblast, myeloid, and endothelial scar states. |

### M1B-T001: Core Lesion Architecture

**Status**: consensus-ready profile started; consensus statement not yet finalized.

| Profile Element | Curated Summary |
|---|---|
| Evidence base | Two full-text studies, M1A-P004 and M1A-P007, plus abstract/source-page support from M1A-P001 and M1A-P031, with 10 extracted observations and 6 author claims. |
| Agreement | Chronic and maturing SCI lesions are compartmentalized rather than homogeneous: fibrotic/ECM-rich central regions, immune/microglial and astrocytic boundary layers, altered white-matter-adjacent zones, and sometimes cavities or repaired-tissue zones. |
| Strong points | Gong provides spatial transcriptomic evidence for multicellular scar compartments and maturation phases; Cooper provides intervention/genetic evidence that the fibrotic matrix compartment can be reduced independently of GFAP glial scarring. |
| Main uncertainty | Older chronic rat/dog zone and cavity observations are abstract-level here, and Milich single-cell interaction support remains source-page level. |
| Likely boundary conditions | Hemisection versus contusion, acute/subacute/intermediate/chronic timing, whether cavity formation occurs, spatial resolution of the assay, and whether compartments are defined anatomically, histologically, mechanically, or transcriptionally. |
| Current interpretation | The database should represent lesion architecture as multiple linked compartments rather than a single "scar" field. Fibrotic matrix, astrocytic border, microglial/myeloid containment, spared/reactive neural tissue, and cavity/repaired-tissue zones should remain separately queryable. |
| Next evidence needed | Pull full text for M1A-P001, M1A-P002, and M1A-P031; integrate M1A-P004 with T002/T003/T008 controlled vocabularies so spatial compartments can link to lineage and signaling evidence. |

---

## Contradiction Map

| Contradiction ID | Topic ID | Claim 1 | Claim 2 | Contradiction Type | Boundary Conditions | Resolution Status |
|---|---|---|---|---|---|---|
| M1B-X001 | M1B-T004 | M1B-C001: chronic rat hemisection scar softening | M1B-C003: chronic mouse contusion lesion stiffening | Directional divergence | Rat hemisection, fresh 500 um sections, 80 um bead, 15-18 WPI versus mouse severe contusion, 10 um freeze/thaw cryosections, 2.5 um radius bead, 12 WPI | PARTIALLY RESOLVED AS MODEL/METHOD-DEPENDENT; not suitable for single-direction consensus |
| M1B-X002 | M1B-T002 | M1B-C008/M1B-C009: type A pericyte-derived scarring drives fibrosis and recovery limits | M1B-C006/M1B-C011: Col1alpha1/Col1a2 fibroblasts, not NG2/Myh11 pericytes, are primary fibrotic scar source | Lineage-definition divergence | GLAST/type A pericyte lineage and functional attenuation versus Col1alpha1/Col1a2 fibroblast lineage, NG2/Myh11 pericyte/vSMC exclusion, contusion/hemisection/transection/crush models, dura intact/disrupted | PARTIALLY RESOLVED AS MARKER-AND-DEFINITION-DEPENDENT; store cell-origin evidence with driver/marker context |
| M1B-X003 | M1B-T003 | M1B-C014: established scar-forming astrocytes resist direct in vitro reversion | M1B-C015/M1B-C016/M1B-C017: astrocytic border recruitment, corralling, and morphology remain intervention-sensitive in vivo | Process-boundary distinction | Established astrocyte state maintenance versus recruitment of neighboring astrocytes; in vitro Col-I-SA assays versus in vivo chronic contusion/transplantation and source-page wound-healing perturbations | RESOLVED AS PROCESS-SPECIFIC; distinguish astrocyte-state reversal from border recruitment/organization |

---

## Consensus Readiness Gates

| Gate | Requirement | Status |
|---|---|---|
| GATE-1 | At least 3 independent papers with linked observations for a topic | MET FOR T001, T002, AND T003; NOT MET FOR T004; 2 linked papers |
| GATE-2 | At least 1 contradicting or boundary-condition check for each major consensus topic | MET FOR T002, T003, AND T004 |
| GATE-3 | Source strength recorded: full-text/source-page/abstract-level | MET FOR PAPER LEVEL |
| GATE-4 | Claims linked to observations through EvidenceLink | STARTED; MET FOR T001, T002, T003, AND T004 FIRST PASS |
| GATE-5 | No consensus statement depends on a single paper | MET FOR T001, T002, T003, AND T004 PROFILES; NOT MET GLOBALLY |

---

## Working Notes

- 2026-07-15: Module 1B opened after Module 1A reached practical saturation for lesion-architecture corpus building: 30 papers and 90 experiments through Pass 3.
- 2026-07-15: First recommended extraction target is the scar-mechanics contradiction pair, M1A-P026 versus M1A-P027, because it already contains a clear model-dependent conflict and will exercise the observation/claim/evidence-link workflow.
- 2026-07-16: Began full Module 1 curation. Completed first-pass Observation, AuthorClaim, EvidenceLink, contradiction-map, and consensus-ready profile rows for M1B-T004 using Baumann 2020 and Cooper 2020.
- 2026-07-16: Completed first-pass Observation, AuthorClaim, EvidenceLink, contradiction-map, and consensus-ready profile rows for M1B-T002 using Soderblom 2013, Dias 2018, and Xue 2024.
- 2026-07-16: Completed first-pass Observation, AuthorClaim, EvidenceLink, and consensus-ready profile rows for M1B-T003 using Tamaru 2023 full text plus source-page rows for Zhou 2020, Shen 2025, and O'Shea 2024.
- 2026-07-16: Completed first-pass Observation, AuthorClaim, EvidenceLink, and consensus-ready profile rows for M1B-T001 using Gong 2023 and Cooper 2018 full text plus abstract/source-page rows for Zhang 2011 and Milich 2021.
