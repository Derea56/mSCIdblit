# mSCIdblit Module Roadmap

This roadmap keeps saturation modules separate from evidence-consolidation modules.

## Active and Planned Saturation Modules

| Module | Topic | Role | Status | Notes |
|---|---|---|---|---|
| Module 1A | Chronic SCI lesion architecture | Corpus saturation | SATURATED / FROZEN FIRST PASS | 30-paper consensus corpus; 95 extracted experiments after full-text access-gap upgrades |
| Module 1B | Chronic SCI lesion architecture evidence consolidation | Observation and claim linkage | CONSENSUS-READY FIRST PASS | 84 observations, 50 author claims, 107 evidence links, 7 boundary records, and 8 consensus-ready statements from the saturated Module 1A corpus; full SQL materialization exported |
| Module 2A | Biomaterials and scaffold repair in SCI | Corpus saturation | SATURATED / FROZEN FIRST PASS | 43-paper consensus corpus; 84 extracted experiments plus 8 review/map anchors across scaffold-only, scaffold plus cells, hydrogels, conduits, decellularized matrices, and chronic scar-resection scaffold studies |
| Module 2B | Biomaterials and scaffold repair evidence consolidation | Observation and claim linkage | CONSENSUS-READY FIRST PASS | 50 observations, 36 author claims, 56 evidence links, 8 boundary records, and 8 consensus-ready statements from the saturated Module 2A corpus; tracker bundle and full SQL materialization exported |
| Module 3A | Immune and myeloid modulation after SCI | Corpus saturation | SATURATED / FROZEN FIRST PASS | 47 primary papers, 94 extracted experiments, and 10 review/map anchors across depletion, corralling, monocyte/macrophage scar, neutrophil, single-cell, polarization, inflammasome, immune-metabolic, debris-handling, and immune-delivery categories |
| Module 3B | Immune and myeloid modulation evidence consolidation | Observation and claim linkage | CONSENSUS-READY FIRST PASS | 47 observations, 36 author claims, 60 evidence links, 8 boundary records, and 8 consensus-ready statements from the saturated Module 3A corpus |
| Module 4A | Cell transplantation and graft integration after SCI | Corpus saturation | SATURATED / FROZEN FIRST PASS | 60 primary/clinical papers, 113 extracted experiments, and 12 review/map anchors across NS/PC, iPSC, Schwann, OEC, MSC/BMMC, restricted precursor, OPC/remyelination, fetal/embryonic graft, organoid, clinical safety, autonomic/respiratory, and scaffold-cell categories |
| Module 4B | Cell transplantation and graft integration evidence consolidation | Observation and claim linkage | CONSENSUS-READY FIRST PASS | 60 observations, 40 author claims, 72 evidence links, 8 boundary records, and 8 consensus-ready statements from the saturated Module 4A corpus; abstract-level confidence retained for full-text upgrade queue |
| Module 5A | Axon regeneration, remyelination, and white matter repair after SCI | Corpus saturation | SATURATED / FROZEN FIRST PASS | 47 primary papers, 94 extracted experiments, and 12 review/map anchors across CST/RST regeneration, serotonergic/propriospinal relay, remyelination, white matter repair, CSPG/Nogo/PTEN/SOCS3, intrinsic growth, activity/stimulation, and graft/scaffold-enabled axon repair categories |
| Module 5B | Axon regeneration, remyelination, and white matter repair evidence consolidation | Observation and claim linkage | CONSENSUS-READY FIRST PASS | 47 observations, 36 author claims, 60 evidence links, 8 boundary records, and 8 consensus-ready statements from the saturated Module 5A corpus |
| Module 6A | Human chronic SCI pathology and translational imaging | Corpus saturation | SATURATED / FROZEN FIRST PASS | 36-paper first-pass corpus plus 8 review/map anchors spanning chronic MRI stereology, autopsy pathology, DTI/qMRI/MRS/fMRI, tissue-bridge prognosis, surgical screening anatomy, syrinx/cyst pathology, tract integrity, and remote motor-system degeneration |
| Module 6B | Human chronic SCI pathology and translational imaging evidence consolidation | Observation and claim linkage | CONSENSUS-READY FIRST PASS | 36 observations, 36 author claims, 104 evidence links, 8 boundary records, and 8 consensus-ready statements from the saturated Module 6A corpus; tracker-level evidence bundle exported |
| Module 7A | Host fibroinflammatory conditioning before regenerative reconstruction or transplantation | Corpus saturation | SATURATED / FROZEN FIRST PASS | 40-paper first-pass corpus plus 8 review/map anchors spanning breast implant capsular contracture prophylaxis, flap/ischemic tissue preconditioning, islet engraftment and IBMIR, organ-tolerance bridge evidence, SCI leukotriene/resolution conditioning, and scar/wound anti-fibrotic boundary evidence |
| Module 7B | Host fibroinflammatory conditioning evidence consolidation | Observation and claim linkage | CONSENSUS-READY FIRST PASS | 40 observations, 36 author claims, 88 evidence links, 8 boundary records, and 8 consensus-ready statements from the saturated Module 7A corpus; tracker-level evidence bundle exported |

## Saturation Rule

A topic is considered practically saturated when two consecutive targeted search phases add no new mechanistic or experimental category and the remaining candidates are mostly repeats, reviews, off-topic clinical outcomes, or inaccessible legacy papers.

## Module Naming Rule

`A` modules are corpus-building and experiment-extraction modules. Follow-on `B` modules consolidate observations, author claims, evidence links, contradiction groups, and consensus readiness after the corresponding `A` module reaches practical saturation.

## Module 1 Freeze Note

Module 1 is frozen as a first-pass lesion-architecture evidence base as of 2026-07-16. Remaining queued Module 1A candidate papers are future opportunistic upgrades unless they introduce a new lesion-architecture compartment or materially change a boundary condition. The next Module 1 step is consensus drafting and optional SQL materialization from the curated tracker rows, not more saturation searching.

## Cross-Module Synthesis Note

The first Module 1 + Module 2 synthesis draft is recorded in `docs/MODULE_1_2_SYNTHESIS.md`. It bridges chronic lesion architecture to scaffold-repair strategy, defines first-pass design rules, and proposes grounded hypotheses derived from the SQL-materialized consensus bases.

The Module 3B-5B synthesis draft is recorded in `docs/MODULE_3_5_CONSENSUS.md`. It bridges immune/myeloid state, cell transplantation, and axon/white-matter repair using refreshed consensus-ready first-pass 3B and 5B layers plus the mature 4B layer.
