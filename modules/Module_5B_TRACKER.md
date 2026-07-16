# Module 5B: Axon Regeneration, Remyelination, and White Matter Repair After SCI - Evidence Consolidation and Consensus Readiness

## Overview

This tracker records the B-phase evidence-consolidation layer for Module 5A. It converts the current seed corpus into atomic observations, author claims, evidence links, boundary conditions, and consensus draft statements.

**Boundary condition**: This is a provisional seed-consensus layer, not a saturation-level consensus. It is useful for hypothesis framing and cross-module synthesis, but it should be upgraded after Module 5A reaches practical saturation and experiment-level extraction is completed.

**Input corpus**: Module 5A seed corpus, 9 registered primary papers; Module 5A remains active and not saturated.

**Module 5 seed-consensus note**: 2026-07-16. Status: Module 5A remains ACTIVE / NOT SATURATED; Module 5B is PROVISIONAL SEED-CONSENSUS FIRST PASS.

---

## Module 5B Goals

| Goal ID | Goal | Output Table / Artifact | Status |
|---|---|---|---|
| 5B-G001 | Extract seed atomic observations from current A-phase papers | Observation | COMPLETE SEED PASS |
| 5B-G002 | Extract seed author interpretations separately from observations | AuthorClaim | COMPLETE SEED PASS |
| 5B-G003 | Link each seed claim to supporting or boundary observations | EvidenceLink | COMPLETE SEED PASS |
| 5B-G004 | Cluster seed evidence by topic | Provisional consensus profiles | COMPLETE SEED PASS |
| 5B-G005 | Mark boundaries caused by incomplete saturation and mechanism heterogeneity | Boundary map | COMPLETE SEED PASS |
| 5B-G006 | Draft provisional consensus statements only after linked seed evidence exists | Consensus | COMPLETE SEED PASS |

## Evidence Topic Map

| Topic ID | Provisional Consensus Topic | Primary Papers | Evidence Need | Status |
|---|---|---|---|---|
| M5B-T001 | Chronic scar and graft-enabled axon regeneration | M5A-P001, M5A-P007 | Separate regeneration through permissive bridges from spontaneous tract repair. | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M5B-T002 | Scar attenuation and inhibitory-receptor release of CST/RST growth | M5A-P002, M5A-P006 | Track pericyte scar, CSPG, and PTP-sigma boundaries. | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M5B-T003 | White matter repair and remote glial-immune control | M5A-P003 | Connect lesion-remote astrocyte and microglia programs to white matter repair. | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M5B-T004 | Human ventral-root axon loss and remyelination pathology | M5A-P004 | Anchor animal repair mechanisms against human pathology. | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M5B-T005 | Intrinsic neuronal growth state, energetics, and transcriptional regression | M5A-P005, M5A-P008 | Separate intrinsic growth competence from environmental permissiveness. | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M5B-T006 | Activity, stimulation, and signaling-enabled sprouting/regeneration | M5A-P009 | Preserve distinction between sprouting, regeneration, and functional regeneration. | PROVISIONAL SEED-CONSENSUS FIRST PASS |

## Extraction Priority

| Priority | Paper Set | Rationale | Status |
|---|---|---|---|
| 1 | All current Module 5A carried anchors and Phase 1A candidates | Seed consensus requires every registered paper to contribute at least one observation | COMPLETE SEED PASS |
| 2 | Queued Module 5A search phases | Needed before this tracker can be upgraded from seed consensus to saturation-level consensus | QUEUED |
| 3 | Full-text experiment extraction | Needed for effect sizes, comparator logic, and figure-level evidence | QUEUED |

## Pass 4: Observation Extraction Tracker

| Topic ID | Paper ID | Experiment IDs | Target Observation Types | Status | Notes |
|---|---|---|---|---|---|
| M5B-T001 | M5A-P001, M5A-P007 | Seed abstract/source-level rows | Chronic scar and graft-enabled axon regeneration | COMPLETE SEED PASS | Separate regeneration through permissive bridges from spontaneous tract repair. |
| M5B-T002 | M5A-P002, M5A-P006 | Seed abstract/source-level rows | Scar attenuation and inhibitory-receptor release of CST/RST growth | COMPLETE SEED PASS | Track pericyte scar, CSPG, and PTP-sigma boundaries. |
| M5B-T003 | M5A-P003 | Seed abstract/source-level rows | White matter repair and remote glial-immune control | COMPLETE SEED PASS | Connect lesion-remote astrocyte and microglia programs to white matter repair. |
| M5B-T004 | M5A-P004 | Seed abstract/source-level rows | Human ventral-root axon loss and remyelination pathology | COMPLETE SEED PASS | Anchor animal repair mechanisms against human pathology. |
| M5B-T005 | M5A-P005, M5A-P008 | Seed abstract/source-level rows | Intrinsic neuronal growth state, energetics, and transcriptional regression | COMPLETE SEED PASS | Separate intrinsic growth competence from environmental permissiveness. |
| M5B-T006 | M5A-P009 | Seed abstract/source-level rows | Activity, stimulation, and signaling-enabled sprouting/regeneration | COMPLETE SEED PASS | Preserve distinction between sprouting, regeneration, and functional regeneration. |

## Pass 4A: Atomic Observations Extracted

These rows are tracker-level Observation candidates. They preserve intended database fields while remaining reviewable before materialization into SQL.

| Observation ID | Topic ID | Paper ID | Experiment ID | Figure Ref | Evidence Type | Outcome Type | Observation Value | Normalized Value | Unit | Quantitative | Statistics Reported | Source Section | Extraction Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M5B-O001 | M5B-T001 | M5A-P001 | M5A-P001-E001 | Abstract / tracker seed | Regeneration through chronic scar/graft | Axon regeneration / chronic lesion permissiveness | Lu P 2007 anchors axon regeneration through scars and into chronic SCI sites, linking chronic lesion architecture to permissive graft contexts. | lu p 2007 anchors axon regeneration through scars and into chronic sci sites, linking chronic lesion architecture to permissive graft contexts. | qualitative | NO | Seed pass; exact statistics not extracted | Module 5A tracker / paper title metadata | medium | Carried Module 1A anchor. |
| M5B-O002 | M5B-T002 | M5A-P002 | M5A-P002-E001 | Abstract / tracker seed | Scar attenuation intervention | CST/RST regeneration / recovery | Dias DO 2018 indicates reducing pericyte-derived scarring can promote recovery after SCI and is relevant to CST/RST regeneration boundaries. | dias do 2018 indicates reducing pericyte-derived scarring can promote recovery after sci and is relevant to cst/rst regeneration boundaries. | qualitative | NO | Seed pass; exact statistics not extracted | Module 5A tracker / paper title metadata | medium | Scar modulation bridge to Module 1. |
| M5B-O003 | M5B-T003 | M5A-P003 | M5A-P003-E001 | Abstract / tracker seed | Remote glial repair mechanism | White matter repair | McCallum S 2026 indicates lesion-remote astrocytes govern microglia-mediated white matter repair. | mccallum s 2026 indicates lesion-remote astrocytes govern microglia-mediated white matter repair. | qualitative | NO | Seed pass; exact statistics not extracted | Module 5A tracker / paper title metadata | medium | Connects Module 5 to Module 3 immune-glial repair. |
| M5B-O004 | M5B-T004 | M5A-P004 | M5A-P004-E001 | Abstract / tracker seed | Human pathology anchor | Ventral-root axon loss / remyelination pathology | Grumbles RM 2017 anchors motoneuron death after human SCI and creates a human pathology bridge for ventral-root axon loss and remyelination interpretation. | grumbles rm 2017 anchors motoneuron death after human sci and creates a human pathology bridge for ventral-root axon loss and remyelination interpretation. | qualitative | NO | Seed pass; exact statistics not extracted | Module 5A tracker / paper title metadata | medium | Human pathology boundary. |
| M5B-O005 | M5B-T005 | M5A-P005 | M5A-P005-E001 | Abstract / tracker seed | Metabolic intervention | Axonal regeneration / functional recovery | Han Q 2020 indicates restoring cellular energetics can promote axonal regeneration and functional recovery after SCI. | han q 2020 indicates restoring cellular energetics can promote axonal regeneration and functional recovery after sci. | qualitative | NO | Seed pass; exact statistics not extracted | Module 5A tracker / paper title metadata | low | Candidate intrinsic/metabolic growth anchor. |
| M5B-O006 | M5B-T002 | M5A-P006 | M5A-P006-E001 | Abstract / tracker seed | Inhibitory receptor mechanism | CST regeneration / CSPG receptor pathway | Fry EJ 2010 links receptor protein tyrosine phosphatase sigma deficiency to CST regeneration after SCI. | fry ej 2010 links receptor protein tyrosine phosphatase sigma deficiency to cst regeneration after sci. | qualitative | NO | Seed pass; exact statistics not extracted | Module 5A tracker / paper title metadata | low | Extrinsic inhibitory-matrix receptor anchor. |
| M5B-O007 | M5B-T001 | M5A-P007 | M5A-P007-E001 | Abstract / tracker seed | Graft-enabled regeneration | CST regeneration through neural graft | Kadoya K 2016 indicates homologous neural graft reconstitution enables robust corticospinal regeneration. | kadoya k 2016 indicates homologous neural graft reconstitution enables robust corticospinal regeneration. | qualitative | NO | Seed pass; exact statistics not extracted | Module 5A tracker / paper title metadata | low | Bridge to Module 4 transplantation. |
| M5B-O008 | M5B-T005 | M5A-P008 | M5A-P008-E001 | Abstract / tracker seed | Intrinsic neuronal state | Embryonic transcriptional growth state | Poplawski GHD 2020 indicates injured adult neurons can regress to an embryonic transcriptional growth state. | poplawski ghd 2020 indicates injured adult neurons can regress to an embryonic transcriptional growth state. | qualitative | NO | Seed pass; exact statistics not extracted | Module 5A tracker / paper title metadata | low | Intrinsic growth-state anchor. |
| M5B-O009 | M5B-T006 | M5A-P009 | M5A-P009-E001 | Abstract / tracker seed | Signaling / stimulation intervention | CST sprouting and functional regeneration | Boato F 2023 links MAP2K activation by genetic engineering or HF-rTMS to CST axon sprouting and functional regeneration. | boato f 2023 links map2k activation by genetic engineering or hf-rtms to cst axon sprouting and functional regeneration. | qualitative | NO | Seed pass; exact statistics not extracted | Module 5A tracker / paper title metadata | low | Activity/signaling intervention anchor. |

## Pass 5: Author Claim Extraction Tracker

| Topic ID | Paper ID | Claim Types To Extract | Status |
|---|---|---|---|
| M5B-T001 | M5A-P001, M5A-P007 | Chronic scar and graft-enabled axon regeneration; 3 seed claim rows | COMPLETE SEED PASS |
| M5B-T002 | M5A-P002, M5A-P006 | Scar attenuation and inhibitory-receptor release of CST/RST growth; 3 seed claim rows | COMPLETE SEED PASS |
| M5B-T003 | M5A-P003 | White matter repair and remote glial-immune control; 1 seed claim rows | COMPLETE SEED PASS |
| M5B-T004 | M5A-P004 | Human ventral-root axon loss and remyelination pathology; 1 seed claim rows | COMPLETE SEED PASS |
| M5B-T005 | M5A-P005, M5A-P008 | Intrinsic neuronal growth state, energetics, and transcriptional regression; 3 seed claim rows | COMPLETE SEED PASS |
| M5B-T006 | M5A-P009 | Activity, stimulation, and signaling-enabled sprouting/regeneration; 3 seed claim rows | COMPLETE SEED PASS |

## Pass 5A: Author Claims Extracted

| Claim ID | Topic ID | Paper ID | Claim Text | Claim Type | Confidence Level | Source Section | Extraction Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| M5B-C001 | M5B-T001 | M5A-P001 | Chronic lesion environments can become permissive to axon growth when scar/graft architecture supports regeneration. | implication | medium | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C002 | M5B-T001 | M5A-P007 | Homologous neural grafts can enable robust corticospinal regeneration in selected experimental contexts. | conclusion | low | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C003 | M5B-T001 | M5A-P001,M5A-P007 | Graft-enabled regeneration should be cross-tagged with Module 4 rather than treated as scaffold-free intrinsic regeneration. | curation rule | high | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C004 | M5B-T002 | M5A-P002 | Pericyte-derived scar attenuation is a candidate route to CST/RST regeneration and recovery. | conclusion | medium | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C005 | M5B-T002 | M5A-P006 | CSPG-receptor pathway manipulation can release corticospinal growth constraints after SCI. | mechanistic | low | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C006 | M5B-T002 | M5A-P002,M5A-P006 | Extrinsic inhibition should be separated into scar-cell, matrix, and receptor mechanisms. | evidence standard | high | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C007 | M5B-T003 | M5A-P003 | Lesion-remote astrocyte control of microglia-mediated white matter repair links tract repair to immune-glial regulation. | mechanistic | medium | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C008 | M5B-T004 | M5A-P004 | Human motoneuron and ventral-root pathology should constrain animal remyelination and axon-repair translation. | boundary condition | medium | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C009 | M5B-T005 | M5A-P005 | Cellular energetics is a plausible intrinsic-growth intervention axis for axonal regeneration. | mechanistic | low | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C010 | M5B-T005 | M5A-P008 | Adult injured neurons may re-enter embryonic-like transcriptional growth states. | mechanistic | low | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C011 | M5B-T005 | M5A-P005,M5A-P008 | Intrinsic growth competence should be curated separately from environmental permissiveness. | evidence standard | high | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C012 | M5B-T006 | M5A-P009 | MAP2K activation or HF-rTMS can be framed as an activity/signaling-enabled sprouting-regeneration strategy. | implication | low | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C013 | M5B-T006 | M5A-P009 | Sprouting, regeneration, and functional regeneration require distinct labels in Module 5. | evidence standard | high | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |
| M5B-C014 | M5B-T006 | M5A-P001-M5A-P009 | Module 5B currently supports a seed mechanism map, not saturation-level consensus. | curation boundary | high | Module 5A tracker / abstract metadata | low | Seed claim; full-text extraction required before saturation-level consensus. |

## Pass 6: Evidence Links Drafted

| Link ID | Claim ID | Observation ID | Relationship | Evidence Weight | Notes |
|---|---|---|---|---|---|
| M5B-L001 | M5B-C001 | M5B-O001 | supports | medium | Primary seed evidence link. |
| M5B-L002 | M5B-C002 | M5B-O007 | supports | low | Primary seed evidence link. |
| M5B-L003 | M5B-C003 | M5B-O001 | supports | low | Primary seed evidence link. |
| M5B-L004 | M5B-C004 | M5B-O002 | supports | medium | Primary seed evidence link. |
| M5B-L005 | M5B-C005 | M5B-O006 | supports | low | Primary seed evidence link. |
| M5B-L006 | M5B-C006 | M5B-O002 | supports | low | Primary seed evidence link. |
| M5B-L007 | M5B-C007 | M5B-O003 | supports | medium | Primary seed evidence link. |
| M5B-L008 | M5B-C008 | M5B-O004 | supports | medium | Primary seed evidence link. |
| M5B-L009 | M5B-C009 | M5B-O005 | supports | low | Primary seed evidence link. |
| M5B-L010 | M5B-C010 | M5B-O008 | supports | low | Primary seed evidence link. |
| M5B-L011 | M5B-C011 | M5B-O005 | supports | low | Primary seed evidence link. |
| M5B-L012 | M5B-C012 | M5B-O009 | supports | low | Primary seed evidence link. |
| M5B-L013 | M5B-C013 | M5B-O009 | supports | low | Primary seed evidence link. |
| M5B-L014 | M5B-C014 | M5B-O001 | supports | low | Primary seed evidence link. |
| M5B-L015 | M5B-C002 | M5B-O001 | boundary support | low | Additional seed boundary link. |
| M5B-L016 | M5B-C003 | M5B-O007 | boundary support | low | Additional seed boundary link. |
| M5B-L017 | M5B-C005 | M5B-O002 | boundary support | low | Additional seed boundary link. |
| M5B-L018 | M5B-C006 | M5B-O006 | boundary support | low | Additional seed boundary link. |
| M5B-L019 | M5B-C007 | M5B-O004 | boundary support | low | Additional seed boundary link. |
| M5B-L020 | M5B-C009 | M5B-O008 | boundary support | low | Additional seed boundary link. |
| M5B-L021 | M5B-C010 | M5B-O005 | boundary support | low | Additional seed boundary link. |

## Boundary Conditions Draft

| Boundary ID | Boundary | Interpretation Rule | Supporting Evidence | Confidence |
|---|---|---|---|---|
| M5B-B001 | Regeneration versus sprouting boundary | CST/RST sprouting, tract regeneration, and functional regeneration need separate labels. | O002, O006, O009 | high |
| M5B-B002 | Graft attribution boundary | Graft-enabled axon growth overlaps with Module 4 transplantation and should not be read as cell-free regeneration. | O001, O007 | high |
| M5B-B003 | Extrinsic versus intrinsic mechanism boundary | Scar, CSPG receptor, metabolic, transcriptional, and stimulation strategies test different repair axes. | O002, O005-O009 | high |
| M5B-B004 | White matter immune-glial boundary | White matter repair may depend on remote astrocyte-microglia programs, linking Module 5 to Module 3. | O003 | medium |
| M5B-B005 | Human translation boundary | Human motoneuron and ventral-root pathology should constrain animal white-matter repair claims. | O004 | medium |
| M5B-B006 | Seed corpus boundary | Module 5A has not reached saturation and has not completed experiment-level extraction. | O001-O009 | high |

## Consensus Draft Queue

| Consensus Draft ID | Topic ID | Draft Statement | Supporting Claims | Supporting Observations | Boundary Notes | Status |
|---|---|---|---|---|---|---|
| M5B-S001 | M5B-T001 | Seed evidence supports graft- or permissive-context-enabled axon regeneration, especially in chronic scar/graft and homologous neural graft settings. | C001-C003 | O001, O007 | B002, B006 | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M5B-S002 | M5B-T002 | Scar attenuation and CSPG-receptor pathway manipulation are distinct extrinsic routes for releasing CST/RST growth constraints. | C004-C006 | O002, O006 | B001, B003, B006 | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M5B-S003 | M5B-T003 | White matter repair may be governed by lesion-remote astrocyte and microglia interactions, making immune-glial state part of axon repair synthesis. | C007 | O003 | B004, B006 | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M5B-S004 | M5B-T004 | Human motoneuron and ventral-root pathology should remain a translation checkpoint for remyelination and axon-repair claims. | C008 | O004 | B005, B006 | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M5B-S005 | M5B-T005 | Intrinsic neuronal growth competence includes metabolic and transcriptional state changes that should be curated separately from environmental permissiveness. | C009-C011 | O005, O008 | B003, B006 | PROVISIONAL SEED-CONSENSUS FIRST PASS |
| M5B-S006 | M5B-T006 | Module 5B should keep sprouting, regeneration, and functional regeneration separated until saturation and experiment-level extraction are complete. | C012-C014 | O001-O009 | all boundary records | PROVISIONAL SEED-CONSENSUS FIRST PASS |

## Module 5B Current Count

| Artifact | Count | Status |
|---|---:|---|
| Atomic observations | 9 | COMPLETE SEED PASS |
| Author claims | 14 | COMPLETE SEED PASS |
| Evidence links | 21 | COMPLETE SEED PASS |
| Boundary records | 6 | COMPLETE SEED PASS |
| Consensus drafts | 6 | PROVISIONAL SEED-CONSENSUS FIRST PASS |

