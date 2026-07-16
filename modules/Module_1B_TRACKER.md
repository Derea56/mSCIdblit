# Module 1B: Chronic SCI Lesion Architecture — Evidence Consolidation and Consensus Readiness

## Overview

This tracker begins the post-saturation phase for Module 1A. Module 1B converts the Module 1A experiment-level corpus into atomic observations, author claims, evidence links, contradiction groups, and consensus-ready profiles.

**Boundary condition**: Module 1B may prepare consensus profiles, but project-level `Consensus` records should only be created after observations and author claims are linked to source evidence.

**Input corpus**: Module 1A saturation corpus, 30 papers / 90 experiments through Pass 3.

---

## Module 1B Goals

| Goal ID | Goal | Output Table / Artifact | Status |
|---|---|---|---|
| M1B-G001 | Extract atomic empirical observations from Module 1A experiments | Observation | NOT STARTED |
| M1B-G002 | Extract author interpretations separately from observations | AuthorClaim | NOT STARTED |
| M1B-G003 | Link each claim to supporting or contradicting observations | EvidenceLink | NOT STARTED |
| M1B-G004 | Cluster evidence by lesion-architecture topic | Consensus-ready evidence profiles | NOT STARTED |
| M1B-G005 | Mark contradictions and model-dependent divergences | Contradiction map | NOT STARTED |
| M1B-G006 | Draft consensus statements only after linked evidence exists | Consensus | BLOCKED UNTIL G001-G003 |

---

## Evidence Topic Map

| Topic ID | Consensus-Ready Topic | Primary Papers | Evidence Need | Status |
|---|---|---|---|---|
| M1B-T001 | Chronic SCI lesions organize into fibrotic core, astrocytic border, spared/reactive neural tissue, and cavities | M1A-P001, P002, P003, P004, P007, P008, P009, P026, P027, P029, P030, P031, P032, P033 | Extract anatomy observations and boundary/cell-marker claims | QUEUED |
| M1B-T002 | Fibrotic scar cellular origins vary by model and include perivascular fibroblast/pericyte-associated lineages | M1A-P007, P008, P009, P021, P026, P029 | Extract lineage, marker, and compartment observations | QUEUED |
| M1B-T003 | Astrocytic borders are active wound-repair structures, not only inhibitory barriers | M1A-P003, P004, P030, P032, P033 | Extract border formation, signaling, and containment observations | QUEUED |
| M1B-T004 | Chronic lesion biomechanics are model-dependent and currently directionally conflicting | M1A-P026, P027 | Extract stiffness values, tissue-preparation conditions, and model details | QUEUED |
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
| M1B-T004 | M1A-P026 | M1A-P026-E001–E004 | Young's modulus, cavity morphometry, ECM/GAG, CNS markers | QUEUED | Start here because contradiction with P027 is already logged |
| M1B-T004 | M1A-P027 | M1A-P027-E001–E004 | AFM stiffness, fibronectin/GFAP, IMP effect, glial alignment | QUEUED | Pair with P026 |
| M1B-T002 | M1A-P008 | M1A-P008-E001–E005 | Col1alpha1, PDGFRbeta, NG2 lineage, fibrotic scar geometry | QUEUED | Anchor for perivascular fibroblast source |
| M1B-T002 | M1A-P009 | M1A-P009-E001–E004 | Type A pericyte scar attenuation, ECM, axon regeneration | QUEUED | Anchor for pericyte-derived scar |
| M1B-T003 | M1A-P003 | M1A-P003-E001–E006 | Chronic astrocyte persistence, N-cadherin/beta1-integrin, recruitment | QUEUED | Anchor for chronic astrocytic scar persistence |
| M1B-T003 | M1A-P030 | M1A-P030-E001–E002 | Corralling, compaction, inflammatory containment | QUEUED | Bridges immune and astrocytic border concepts |

---

## Pass 5: Author Claim Extraction Tracker

| Topic ID | Paper ID | Claim Types To Extract | Status |
|---|---|---|---|
| M1B-T004 | M1A-P026 | conclusion; interpretation; mechanism | QUEUED |
| M1B-T004 | M1A-P027 | conclusion; interpretation; mechanism | QUEUED |
| M1B-T002 | M1A-P008 | conclusion; mechanism | QUEUED |
| M1B-T002 | M1A-P009 | conclusion; mechanism; implication | QUEUED |
| M1B-T003 | M1A-P003 | conclusion; mechanism | QUEUED |
| M1B-T003 | M1A-P030 | conclusion; mechanism | QUEUED |

---

## Consensus Readiness Gates

| Gate | Requirement | Status |
|---|---|---|
| GATE-1 | At least 3 independent papers with linked observations for a topic | NOT MET |
| GATE-2 | At least 1 contradicting or boundary-condition check for each major consensus topic | NOT MET |
| GATE-3 | Source strength recorded: full-text/source-page/abstract-level | MET FOR PAPER LEVEL |
| GATE-4 | Claims linked to observations through EvidenceLink | NOT MET |
| GATE-5 | No consensus statement depends on a single paper | NOT MET |

---

## Working Notes

- 2026-07-15: Module 1B opened after Module 1A reached practical saturation for lesion-architecture corpus building: 30 papers and 90 experiments through Pass 3.
- 2026-07-15: First recommended extraction target is the scar-mechanics contradiction pair, M1A-P026 versus M1A-P027, because it already contains a clear model-dependent conflict and will exercise the observation/claim/evidence-link workflow.

