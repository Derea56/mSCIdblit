# Module 3B: Immune and Myeloid Modulation After SCI - Evidence Consolidation and Consensus Readiness

## Overview

This tracker records the B-phase evidence-consolidation layer for Module 3A. It converts the current seed corpus into atomic observations, author claims, evidence links, boundary conditions, and consensus draft statements.

**Boundary condition**: This is a provisional seed-consensus layer, not a saturation-level consensus. It is useful for hypothesis framing and cross-module synthesis, but it should be upgraded after Module 3A reaches practical saturation and experiment-level extraction is completed.

**Input corpus**: Module 3A seed corpus, 7 registered primary papers; Module 3A remains active and not saturated.

**Module 3 seed-consensus note**: 2026-07-16. Status: Module 3A remains ACTIVE / NOT SATURATED; Module 3B is PROVISIONAL SEED-CONSENSUS FIRST PASS.

---

## Module 3B Goals

| Goal ID | Goal | Output Table / Artifact | Status |
|---|---|---|---|
| 3B-G001 | Extract seed atomic observations from current A-phase papers | Observation | COMPLETE SEED PASS |
| 3B-G002 | Extract seed author interpretations separately from observations | AuthorClaim | COMPLETE SEED PASS |
| 3B-G003 | Link each seed claim to supporting or boundary observations | EvidenceLink | COMPLETE SEED PASS |
| 3B-G004 | Cluster seed evidence by topic | Provisional consensus profiles | COMPLETE SEED PASS |
| 3B-G005 | Mark boundaries caused by incomplete saturation and mechanism heterogeneity | Boundary map | COMPLETE SEED PASS |
| 3B-G006 | Draft provisional consensus statements only after linked seed evidence exists | Consensus | COMPLETE SEED PASS |

## Evidence Topic Map

| Topic ID | Provisional Consensus Topic | Primary Papers | Evidence Need | Status |
|---|---|---|---|---|
| M3B-T001 | Microglial depletion and CSF1R modulation | M3A-P001, M3A-P003 | Separate timing-dependent depletion benefit from broad anti-inflammatory claims. | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M3B-T002 | Microglia/macrophage corralling and wound compaction | M3A-P002 | Preserve beneficial containment functions of myeloid cells. | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M3B-T003 | Macrophage/microglia polarization and danger signaling | M3A-P004, M3A-P005 | Track HMGB1-RAGE, extracellular traps, P2X7R, NF-kappaB, and polarization language cautiously. | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M3B-T004 | Pyroptosis and exosome-mediated immune modulation | M3A-P006 | Connect cell/exosome interventions to immune-state rather than direct neural replacement. | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M3B-T005 | Metabolic immune reprogramming and lymphocyte recruitment | M3A-P007 | Capture histone lactylation and microglia/macrophage-T cell crosstalk. | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M3B-T006 | Seed-level immune consensus boundaries | M3A-P001-M3A-P007 | Prevent overgeneralization while Module 3A remains unsaturated. | PROVISIONAL SEED-CONSENSUS FIRST PASS |

## Extraction Priority

| Priority | Paper Set | Rationale | Status |
|---|---|---|---|
| 1 | All current Module 3A carried anchors and Phase 1A candidates | Seed consensus requires every registered paper to contribute at least one observation | COMPLETE SEED PASS |
| 2 | Queued Module 3A search phases | Needed before this tracker can be upgraded from seed consensus to saturation-level consensus | QUEUED |
| 3 | Full-text experiment extraction | Needed for effect sizes, comparator logic, and figure-level evidence | QUEUED |

## Pass 4: Observation Extraction Tracker

| Topic ID | Paper ID | Experiment IDs | Target Observation Types | Status | Notes |
|---|---|---|---|---|---|
| M3B-T001 | M3A-P001, M3A-P003 | Seed abstract/source-level rows | Microglial depletion and CSF1R modulation | COMPLETE SEED PASS | Separate timing-dependent depletion benefit from broad anti-inflammatory claims. |
| M3B-T002 | M3A-P002 | Seed abstract/source-level rows | Microglia/macrophage corralling and wound compaction | COMPLETE SEED PASS | Preserve beneficial containment functions of myeloid cells. |
| M3B-T003 | M3A-P004, M3A-P005 | Seed abstract/source-level rows | Macrophage/microglia polarization and danger signaling | COMPLETE SEED PASS | Track HMGB1-RAGE, extracellular traps, P2X7R, NF-kappaB, and polarization language cautiously. |
| M3B-T004 | M3A-P006 | Seed abstract/source-level rows | Pyroptosis and exosome-mediated immune modulation | COMPLETE SEED PASS | Connect cell/exosome interventions to immune-state rather than direct neural replacement. |
| M3B-T005 | M3A-P007 | Seed abstract/source-level rows | Metabolic immune reprogramming and lymphocyte recruitment | COMPLETE SEED PASS | Capture histone lactylation and microglia/macrophage-T cell crosstalk. |
| M3B-T006 | M3A-P001-M3A-P007 | Seed abstract/source-level rows | Seed-level immune consensus boundaries | COMPLETE SEED PASS | Prevent overgeneralization while Module 3A remains unsaturated. |

## Pass 4A: Atomic Observations Extracted

These rows are tracker-level Observation candidates. They preserve intended database fields while remaining reviewable before materialization into SQL.

| Observation ID | Topic ID | Paper ID | Experiment ID | Figure Ref | Evidence Type | Outcome Type | Observation Value | Normalized Value | Unit | Quantitative | Statistics Reported | Source Section | Extraction Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M3B-O001 | M3B-T001 | M3A-P001 | M3A-P001-E001 | Abstract / tracker seed | Immune intervention | Chronic inflammation / remote degeneration / recovery | Li Y 2020 indicates delayed microglial depletion can reduce chronic inflammation and remote neurodegeneration while improving neurological recovery in male mice. | li y 2020 indicates delayed microglial depletion can reduce chronic inflammation and remote neurodegeneration while improving neurological recovery in male mice. | qualitative | NO | Seed pass; exact statistics not extracted | Module 3A tracker / paper title metadata | medium | Carried Module 1A anchor; timing and sex boundary retained. |
| M3B-O002 | M3B-T002 | M3A-P002 | M3A-P002-E001 | Abstract / tracker seed | Immune-glial mechanism | Wound corralling / compaction / recovery | Zhou X 2020 indicates microglia and macrophages can promote corralling, wound compaction, and recovery via Plexin-B2 after SCI. | zhou x 2020 indicates microglia and macrophages can promote corralling, wound compaction, and recovery via plexin-b2 after sci. | qualitative | NO | Seed pass; exact statistics not extracted | Module 3A tracker / paper title metadata | medium | Important counterweight to simple depletion logic. |
| M3B-O003 | M3B-T001 | M3A-P003 | M3A-P003-E001 | Abstract / tracker seed | Immune intervention | Microglia proliferation / tissue preservation / motor recovery | Gerber YN 2018 indicates CSF1R inhibition reduces microglia proliferation, promotes tissue preservation, and improves motor recovery after SCI. | gerber yn 2018 indicates csf1r inhibition reduces microglia proliferation, promotes tissue preservation, and improves motor recovery after sci. | qualitative | NO | Seed pass; exact statistics not extracted | Module 3A tracker / paper title metadata | medium | CSF1R intervention anchor; cell-specificity needs full text. |
| M3B-O004 | M3B-T003 | M3A-P004 | M3A-P004-E001 | Abstract / tracker seed | Danger-signaling intervention | Pro-inflammatory polarization / neuroprotection | Fan H 2020 links HMGB1-RAGE inhibition to reduced pro-inflammatory macrophage/microglia polarization and neuroprotection after SCI. | fan h 2020 links hmgb1-rage inhibition to reduced pro-inflammatory macrophage/microglia polarization and neuroprotection after sci. | qualitative | NO | Seed pass; exact statistics not extracted | Module 3A tracker / paper title metadata | low | Polarization terminology should be upgraded with markers during full-text pass. |
| M3B-O005 | M3B-T003 | M3A-P005 | M3A-P005-E001 | Abstract / tracker seed | Innate injury-amplification mechanism | Extracellular traps / polarization / secondary injury | Zhang C 2022 links macrophage extracellular traps to worsened secondary SCI through LL37, P2X7R, NF-kappaB, and macrophage/microglia polarization. | zhang c 2022 links macrophage extracellular traps to worsened secondary sci through ll37, p2x7r, nf-kappab, and macrophage/microglia polarization. | qualitative | NO | Seed pass; exact statistics not extracted | Module 3A tracker / paper title metadata | low | Recent candidate; mechanism needs detailed extraction. |
| M3B-O006 | M3B-T004 | M3A-P006 | M3A-P006-E001 | Abstract / tracker seed | Exosome immune modulation | Pyroptosis / motor function | Liu J 2024 indicates iPSC-NSC-derived exosomal let-7b-5p improves motor function by modulating microglial/macrophage pyroptosis. | liu j 2024 indicates ipsc-nsc-derived exosomal let-7b-5p improves motor function by modulating microglial/macrophage pyroptosis. | qualitative | NO | Seed pass; exact statistics not extracted | Module 3A tracker / paper title metadata | low | Bridge to Module 4 cell-derived products; immune mechanism is primary here. |
| M3B-O007 | M3B-T005 | M3A-P007 | M3A-P007-E001 | Abstract / tracker seed | Metabolic immune-state mechanism | Histone lactylation / CD8 T-cell recruitment / injury aggravation | Ge X 2025 links metabolic reprogramming through histone lactylation in microglia and macrophages to CD8 T lymphocyte recruitment and aggravated SCI. | ge x 2025 links metabolic reprogramming through histone lactylation in microglia and macrophages to cd8 t lymphocyte recruitment and aggravated sci. | qualitative | NO | Seed pass; exact statistics not extracted | Module 3A tracker / paper title metadata | low | Seed row for immune-metabolic crosstalk. |

## Pass 5: Author Claim Extraction Tracker

| Topic ID | Paper ID | Claim Types To Extract | Status |
|---|---|---|---|
| M3B-T001 | M3A-P001, M3A-P003 | Microglial depletion and CSF1R modulation; 2 seed claim rows | COMPLETE SEED PASS |
| M3B-T002 | M3A-P002 | Microglia/macrophage corralling and wound compaction; 2 seed claim rows | COMPLETE SEED PASS |
| M3B-T003 | M3A-P004, M3A-P005 | Macrophage/microglia polarization and danger signaling; 3 seed claim rows | COMPLETE SEED PASS |
| M3B-T004 | M3A-P006 | Pyroptosis and exosome-mediated immune modulation; 2 seed claim rows | COMPLETE SEED PASS |
| M3B-T005 | M3A-P007 | Metabolic immune reprogramming and lymphocyte recruitment; 1 seed claim rows | COMPLETE SEED PASS |
| M3B-T006 | M3A-P001-M3A-P007 | Seed-level immune consensus boundaries; 2 seed claim rows | COMPLETE SEED PASS |

## Pass 5A: Author Claims Extracted

| Claim ID | Topic ID | Paper ID | Claim Text | Claim Type | Confidence Level | Source Section | Extraction Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| M3B-C001 | M3B-T001 | M3A-P001 | Delayed microglial depletion may reduce chronic inflammatory damage when timed after the acute phase. | boundary condition | medium | Module 3A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M3B-C002 | M3B-T001 | M3A-P003 | CSF1R-pathway inhibition is a candidate strategy for reducing microglial proliferation and preserving tissue after SCI. | conclusion | medium | Module 3A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M3B-C003 | M3B-T002 | M3A-P002 | Microglia and macrophages can be beneficial wound-organizing cells, not only damaging inflammatory cells. | boundary condition | medium | Module 3A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M3B-C004 | M3B-T002 | M3A-P002 | Plexin-B2-linked corralling supports recovery by compacting and containing the SCI wound. | mechanistic | medium | Module 3A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M3B-C005 | M3B-T003 | M3A-P004 | HMGB1-RAGE signaling contributes to pro-inflammatory macrophage/microglia polarization after SCI. | mechanistic | low | Module 3A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M3B-C006 | M3B-T003 | M3A-P005 | Macrophage extracellular traps can amplify secondary injury through LL37/P2X7R/NF-kappaB signaling. | mechanistic | low | Module 3A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M3B-C007 | M3B-T003 | M3A-P004-M3A-P005 | Polarization claims require marker-level extraction before they can support high-confidence consensus. | evidence standard | high | Module 3A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M3B-C008 | M3B-T004 | M3A-P006 | Cell-derived exosomes can act as immune-state modulators when their effect is tied to microglial/macrophage pyroptosis. | implication | low | Module 3A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M3B-C009 | M3B-T004 | M3A-P006 | Cell therapy products should be cross-tagged with immune mechanisms when the reported mechanism is exosomal immune modulation. | curation rule | medium | Module 3A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M3B-C010 | M3B-T005 | M3A-P007 | Metabolic and epigenetic state changes in myeloid cells may recruit lymphocytes and worsen SCI. | mechanistic | low | Module 3A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M3B-C011 | M3B-T006 | M3A-P001-M3A-P007 | Module 3B currently supports immune-state hypotheses but not saturation-level immune consensus. | curation boundary | high | Module 3A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M3B-C012 | M3B-T006 | M3A-P001-M3A-P007 | Future Module 3 synthesis must stratify by timing, myeloid subtype, depletion versus modulation, and injury phase. | synthesis rule | high | Module 3A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |

## Pass 6: Evidence Links Drafted

| Link ID | Claim ID | Observation ID | Relationship | Evidence Weight | Notes |
|---|---|---|---|---|---|
| M3B-L001 | M3B-C001 | M3B-O001 | supports | medium | Primary seed evidence link. |
| M3B-L002 | M3B-C002 | M3B-O003 | supports | medium | Primary seed evidence link. |
| M3B-L003 | M3B-C003 | M3B-O002 | supports | medium | Primary seed evidence link. |
| M3B-L004 | M3B-C004 | M3B-O002 | supports | medium | Primary seed evidence link. |
| M3B-L005 | M3B-C005 | M3B-O004 | supports | low | Primary seed evidence link. |
| M3B-L006 | M3B-C006 | M3B-O005 | supports | low | Primary seed evidence link. |
| M3B-L007 | M3B-C007 | M3B-O004 | supports | low | Primary seed evidence link. |
| M3B-L008 | M3B-C008 | M3B-O006 | supports | low | Primary seed evidence link. |
| M3B-L009 | M3B-C009 | M3B-O006 | supports | low | Primary seed evidence link. |
| M3B-L010 | M3B-C010 | M3B-O007 | supports | low | Primary seed evidence link. |
| M3B-L011 | M3B-C011 | M3B-O001 | supports | low | Primary seed evidence link. |
| M3B-L012 | M3B-C012 | M3B-O001 | supports | low | Primary seed evidence link. |
| M3B-L013 | M3B-C001 | M3B-O003 | boundary support | low | Additional seed boundary link. |
| M3B-L014 | M3B-C002 | M3B-O001 | boundary support | low | Additional seed boundary link. |
| M3B-L015 | M3B-C003 | M3B-O001 | boundary support | low | Additional seed boundary link. |
| M3B-L016 | M3B-C005 | M3B-O005 | boundary support | low | Additional seed boundary link. |
| M3B-L017 | M3B-C006 | M3B-O004 | boundary support | low | Additional seed boundary link. |
| M3B-L018 | M3B-C007 | M3B-O005 | boundary support | low | Additional seed boundary link. |
| M3B-L019 | M3B-C010 | M3B-O006 | boundary support | low | Additional seed boundary link. |
| M3B-L020 | M3B-C011 | M3B-O007 | boundary support | low | Additional seed boundary link. |
| M3B-L021 | M3B-C012 | M3B-O002 | boundary support | low | Additional seed boundary link. |

## Boundary Conditions Draft

| Boundary ID | Boundary | Interpretation Rule | Supporting Evidence | Confidence |
|---|---|---|---|---|
| M3B-B001 | Timing boundary | Microglial depletion can be interpreted differently in acute versus delayed or chronic windows. | O001, O003 | high |
| M3B-B002 | Beneficial myeloid function boundary | Myeloid cells can promote corralling and wound compaction, so broad suppression claims are unsafe. | O002 | high |
| M3B-B003 | Polarization vocabulary boundary | M1/M2 or pro-inflammatory labels require marker-level and cell-identity extraction. | O004-O005 | high |
| M3B-B004 | Cell product boundary | Exosome or stem-cell products belong in Module 3 when immune-state modulation is the reported mechanism. | O006 | medium |
| M3B-B005 | Immune crosstalk boundary | Myeloid mechanisms may involve lymphocyte recruitment and cannot be reduced to macrophage-only effects. | O007 | medium |
| M3B-B006 | Seed corpus boundary | Module 3A has not reached saturation and has not completed experiment-level extraction. | O001-O007 | high |

## Consensus Draft Queue

| Consensus Draft ID | Topic ID | Draft Statement | Supporting Claims | Supporting Observations | Boundary Notes | Status |
|---|---|---|---|---|---|---|
| M3B-S001 | M3B-T001 | Seed evidence supports timing-sensitive microglial/CSF1R modulation as a tissue-preservation strategy, but not broad immune depletion as a universal rule. | C001-C002, C012 | O001, O003 | B001, B006 | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M3B-S002 | M3B-T002 | Microglia and macrophages can organize SCI wound containment through corralling and compaction, creating a beneficial myeloid-function boundary. | C003-C004 | O002 | B002, B006 | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M3B-S003 | M3B-T003 | Danger-signaling and extracellular-trap pathways are plausible pro-inflammatory injury amplifiers but need marker-level full-text extraction. | C005-C007 | O004-O005 | B003, B006 | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M3B-S004 | M3B-T004 | Cell-derived exosome interventions should be treated as immune-modulating therapies when the claimed mechanism is pyroptosis regulation. | C008-C009 | O006 | B004, B006 | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M3B-S005 | M3B-T005 | Immune-metabolic reprogramming may couple microglia/macrophages to adaptive immune recruitment after SCI. | C010 | O007 | B005, B006 | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M3B-S006 | M3B-T006 | Module 3B should remain a provisional seed consensus until more myeloid, neutrophil, monocyte, and single-cell papers are extracted. | C011-C012 | O001-O007 | all boundary records | PROVISIONAL SEED-CONSENSUS FIRST PASS |

## Module 3B Current Count

| Artifact | Count | Status |
|---|---:|---|
| Atomic observations | 7 | COMPLETE SEED PASS |
| Author claims | 12 | COMPLETE SEED PASS |
| Evidence links | 21 | COMPLETE SEED PASS |
| Boundary records | 6 | COMPLETE SEED PASS |
| Consensus drafts | 6 | PROVISIONAL SEED-CONSENSUS FIRST PASS |

