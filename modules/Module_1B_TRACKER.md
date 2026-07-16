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
| M1B-T001 | Chronic SCI lesions organize into fibrotic core, astrocytic border, spared/reactive neural tissue, and cavities | M1A-P001, P002, P003, P004, P007, P008, P009, P026, P027, P029, P030, P031, P032, P033 | Extract anatomy observations and boundary/cell-marker claims | QUEUED |
| M1B-T002 | Fibrotic scar cellular origins vary by model and include perivascular fibroblast/pericyte-associated lineages | M1A-P007, P008, P009, P021, P026, P029 | Extract lineage, marker, and compartment observations | QUEUED |
| M1B-T003 | Astrocytic borders are active wound-repair structures, not only inhibitory barriers | M1A-P003, P004, P030, P032, P033 | Extract border formation, signaling, and containment observations | QUEUED |
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
| M1B-T002 | M1A-P008 | M1A-P008-E001–E005 | Col1alpha1, PDGFRbeta, NG2 lineage, fibrotic scar geometry | QUEUED | Anchor for perivascular fibroblast source |
| M1B-T002 | M1A-P009 | M1A-P009-E001–E004 | Type A pericyte scar attenuation, ECM, axon regeneration | QUEUED | Anchor for pericyte-derived scar |
| M1B-T003 | M1A-P003 | M1A-P003-E001–E006 | Chronic astrocyte persistence, N-cadherin/beta1-integrin, recruitment | QUEUED | Anchor for chronic astrocytic scar persistence |
| M1B-T003 | M1A-P030 | M1A-P030-E001–E002 | Corralling, compaction, inflammatory containment | QUEUED | Bridges immune and astrocytic border concepts |

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

---

## Pass 5: Author Claim Extraction Tracker

| Topic ID | Paper ID | Claim Types To Extract | Status |
|---|---|---|---|
| M1B-T004 | M1A-P026 | conclusion; interpretation; mechanism | COMPLETE FIRST PASS |
| M1B-T004 | M1A-P027 | conclusion; interpretation; mechanism | COMPLETE FIRST PASS |
| M1B-T002 | M1A-P008 | conclusion; mechanism | QUEUED |
| M1B-T002 | M1A-P009 | conclusion; mechanism; implication | QUEUED |
| M1B-T003 | M1A-P003 | conclusion; mechanism | QUEUED |
| M1B-T003 | M1A-P030 | conclusion; mechanism | QUEUED |

---

## Pass 5A: Author Claims Extracted

| Claim ID | Topic ID | Paper ID | Claim Text | Claim Type | Confidence Level | Source Section | Extraction Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| M1B-C001 | M1B-T004 | M1A-P026 | Chronic rat hemisection SCI scar has decreased Young's modulus, and scar softening is associated with cavitation, CNS cell loss/dysregulation, dense nuclei packing, and GAG/HA dysregulation. | conclusion | high | Abstract / Conclusion | high | Claim is directly aligned with Fig 1-Fig 4 observations. |
| M1B-C002 | M1B-T004 | M1A-P026 | Differences between chronic scar mechanics studies likely depend on injury model, time point, sample preparation, and AFM methodology. | interpretation | medium | Introduction / Discussion | high | Boundary-condition claim explicitly discusses Cooper 2020 versus Baumann 2020. |
| M1B-C003 | M1B-T004 | M1A-P027 | Chronic severe mouse contusion SCI produces mechanical stiffening of spinal lesion tissue compared with uninjured tissue. | conclusion | high | Abstract / Discussion | high | Directly supported by AFM lesion measurements. |
| M1B-C004 | M1B-T004 | M1A-P027 | Fibrotic scarring is a key driver of chronic mechanical stiffening after SCI, because immune-modifying nanoparticle treatment reduces fibrotic scarring and rescues lesion stiffness. | mechanistic | medium | Abstract / Discussion | high | Supported by IMP intervention but still mechanistic because IMP has immune and scar effects. |
| M1B-C005 | M1B-T004 | M1A-P027 | Chronic lesion stiffness is biologically relevant because mouse and human astrocytes respond to substrate stiffness values in the injured/uninjured spinal cord range. | implication | medium | Results / Discussion | high | Supported by in vitro substrate observations; extrapolation to in vivo phenotype remains interpretive. |

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

---

## Contradiction Map

| Contradiction ID | Topic ID | Claim 1 | Claim 2 | Contradiction Type | Boundary Conditions | Resolution Status |
|---|---|---|---|---|---|---|
| M1B-X001 | M1B-T004 | M1B-C001: chronic rat hemisection scar softening | M1B-C003: chronic mouse contusion lesion stiffening | Directional divergence | Rat hemisection, fresh 500 um sections, 80 um bead, 15-18 WPI versus mouse severe contusion, 10 um freeze/thaw cryosections, 2.5 um radius bead, 12 WPI | PARTIALLY RESOLVED AS MODEL/METHOD-DEPENDENT; not suitable for single-direction consensus |

---

## Consensus Readiness Gates

| Gate | Requirement | Status |
|---|---|---|
| GATE-1 | At least 3 independent papers with linked observations for a topic | NOT MET FOR T004; 2 linked papers |
| GATE-2 | At least 1 contradicting or boundary-condition check for each major consensus topic | MET FOR T004 |
| GATE-3 | Source strength recorded: full-text/source-page/abstract-level | MET FOR PAPER LEVEL |
| GATE-4 | Claims linked to observations through EvidenceLink | STARTED; MET FOR T004 FIRST PASS |
| GATE-5 | No consensus statement depends on a single paper | MET FOR T004 PROFILE; NOT MET GLOBALLY |

---

## Working Notes

- 2026-07-15: Module 1B opened after Module 1A reached practical saturation for lesion-architecture corpus building: 30 papers and 90 experiments through Pass 3.
- 2026-07-15: First recommended extraction target is the scar-mechanics contradiction pair, M1A-P026 versus M1A-P027, because it already contains a clear model-dependent conflict and will exercise the observation/claim/evidence-link workflow.
- 2026-07-16: Began full Module 1 curation. Completed first-pass Observation, AuthorClaim, EvidenceLink, contradiction-map, and consensus-ready profile rows for M1B-T004 using Baumann 2020 and Cooper 2020.
