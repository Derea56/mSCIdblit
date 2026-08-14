# Module 21A targeted second-pass summary: Q001, Q003, Q004

Date: 2026-08-14

## Additions and promotions

- Added `M21A-E103`, `lesioned CNS astrocytes expresses CNTFR-alpha`, as receptor-context evidence from primary rat lesion and cultured astrocyte work (PMID:8075814).
- Added `M21A-SAT-EVID-041` and `M21A-SAT-P046` for the new edge.
- Q001 case `M21A-UNRES-002` moved from `unresolved_after_bounded_search` to `partially_resolved`.
- Q003 gained a stable contusive-SCI source documenting TNFR2/GFAP astrocyte co-localization (PMCID:PMC9220050), but no new signaling edge was promoted because the study does not perturb the astrocyte TNFR2 death/survival branch.
- Q004 gained no new edge. The second-pass SCI source continues to support IL1R1 astrocyte signaling and increased IL1R2 in microglia, not direct IL1R2 astrocyte signaling.

## Boundaries retained

- The CNTFRα/gp130/LIFR versus CNTFRα/gp130/OSMR distinction remains unresolved in injured contusive-SCI astrocytes.
- TNFR2 astrocyte localization after SCI is not equivalent to evidence for a TNFR2-to-NF-κB/PI3K branch in astrocytes.
- IL1R2 decoy function remains separate from the IL1R1–MyD88 SCI astrocyte injury branch.
- No Module 20A LR ledger, classification, or frozen manifest was modified.

## Validation

Post-update checks passed: unique IDs, unique cross-register edge keys, evidence support for every edge, layer assignment for the added edge, and unchanged Module 20A manifest SHA-256 `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

Main registers now contain 95 edges, 41 grouped evidence records, 46 perturbations, and 38 evidence-layer rows. SQL materialization remains deferred.

