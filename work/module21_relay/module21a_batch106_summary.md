# Module 21A batch 106 review

Batch 106 covers the exact filtered priority-8 queue ordinal slice 1951–1975. The slice contains 25 rows: review IDs `M20A-EXT-1069` through `M20A-EXT-1086`, then `M20A-EXT-1088` through `M20A-EXT-1094`; `M20A-EXT-1087` is absent from the filtered queue. All 25 output rows match the queue IDs and pair labels exactly.

## Disposition

- 1 `reviewed_binding_only`: CCL22–DPP4/CD26. Primary evidence shows N-terminal processing of CCL22 into truncated products that lose CCR4 activity and are not recognized by ACKR2/D6 (PMID 15067078). This is a direct extracellular chemokine-processing edge, not DPP4 receptor signaling.
- 24 `reviewed_unresolved`.
- 0 `reviewed_relay_candidate`.
- 0 `reviewed_function_only`.
- 0 terminal-TF assignments.

## Evidence boundaries

- CCL21B was not promoted to CCR10, GRM7, or MTNR1A. CCL21-family evidence remains centered on CCR7, while primary CCR10 evidence supports CCL27/CCL28 rather than CCL21B.
- CCL25 was not promoted to ACKR2, ADRA2A, CCR10, GRM7, or MTNR1A. CCR9 and homeostatic atypical-receptor annotations were not transferred to ACKR2 or CCR10 without exact pair assays.
- CCL27B–ACKR2 and CCL28–ACKR2 remain unresolved. Broad ACKR2 promiscuity is not sufficient for an exact paralog/species assignment. A primary ACKR comparison found CCL28 binding/uptake through GPR182 rather than ACKR2/ACKR4 (PMCID PMC10405735), so CCL28–ACKR2 was not promoted.
- CCL4–CCR3, CNR2, GPR152, and GPRC5D remain unresolved. CCL4–CCR5 is the supported subtype boundary; a primary CCR8 study specifically found that MIP-1β/CCL4 did not bind or activate CCR8 at physiologically relevant concentrations (PMID 10540332).
- CCL5–ACKR4 and CCL5–ADRA2A remain unresolved. Canonical CCL5 receptor and ACKR2 evidence was not transferred to ACKR4 or ADRA2A.
- No generic chemokine-family, GPCR-family, expression, or pathway annotation was used to infer a direct molecular edge or terminal TF.

## Search boundary

Searches covered exact pair strings and aliases across PubMed, PMC, publisher pages, and pathway/database annotations, including CCL21B/CCL21, CCL27B/CCL27, MIP-1β/CCL4, D6/ACKR2, CCX-CKR/ACKR4, CD26/DPP4, CCR10, CCR2, CCR3, CCR8, CNR2/CB2, GPR152, GPRC5D, GRM7/mGlu7, and MTNR1A/MT1. Database or pathway entries were retained only as search-boundary context when no exact primary assay was found.

The frozen Module 20A manifest and all shared Module 21A registers, ledgers, and integration outputs were left unchanged.
