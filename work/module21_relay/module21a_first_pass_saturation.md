# Module 21A first-pass saturation packet

## Decision

Module 21A is saturated for a bounded first-pass relay corpus across the nine priority families in the tracker. The original seed packet contained 57 directed relay edges, 14 source-group evidence records, and 17 perturbation records. The Q001–Q009 bounded extraction batch added 37 edges, 26 grouped evidence records, and 28 perturbation records. A targeted Q001/Q003/Q004 second pass added one receptor-context edge, one evidence record, and one perturbation record. A subsequent Q007–Q009 second pass added 7 pathway/function edges, 5 evidence records, and 5 perturbation records, bringing the main saturation registers to 102 edges, 46 evidence records, and 51 perturbation records. It is ready for cross-module reconciliation and candidate simulator export, but not for unrestricted SCI receiver simulation.

The saturation criterion is family-level coverage of the canonical receptor-to-adaptor/kinase-to-TF or transcriptional-output path plus at least one experimentally distinguished branch or explicit boundary. It is not an assertion that every receptor paralog, ligand bias, noncanonical branch, or SCI cell-state weight has been resolved.

## Files

- module21a_saturation_edge_register.tsv: 102 pre-materialization relay edges after the Q001–Q009 bounded batch and targeted second passes.
- module21a_saturation_evidence_register.tsv: primary evidence grouped by family and edge set.
- module21a_saturation_perturbation_register.tsv: branch-specific knockout, deficiency, inhibitor, mutant, and comparison evidence.
- module21a_saturation_matrix.tsv: family-level coverage and explicit gaps.
- module21a_il6_family_batch1_*: retained IL-6/gp130 seed packet.

## Export posture

- high confidence is reserved for primary receptor, adaptor, kinase, processing, or transcriptional-complex evidence.
- medium confidence is used where a paper supports a pathway-complex or contextual branch but not a single molecularly isolated edge.
- export_priority=medium means the edge is a reasonable candidate relay for downstream mapping after species and cell-state checks.
- export_priority=low marks ancillary, receptor-specific, or comparator branches that should not drive receiver-state predictions without matched context.
- No SQL SignalingEdge rows are created in this pass. The TSV packet remains the audit layer until node identity, source registration, and branch semantics are reconciled.

## Explicit boundaries

1. CNTFR-specific receptor-complex evidence is bounded, but SCI astrocyte-specific receptor-complex branch weighting is still open; the gp130 family is not treated as fully receptor-saturated.
2. IFN-lambda is not merged into IFNAR or IFNGR; its astrocyte and injured-SCI receiver weighting remains open.
3. TNFR2, IL-1R2, broad CCL/CCR families, noncanonical SMAD branches, noncanonical WNT branches, and noncanonical Notch outputs were extracted at bounded comparator/pathway resolution; SCI receiver-specific branch weights remain open where noted in the unresolved register.
4. Comparator evidence does not establish SCI astrocyte branch weights. Module 15B IL-6/JAK/STAT3 observations are retained as SCI carry-forward context, not used to upweight every gp130 edge.
5. Complex-level nodes such as ISGF3, destruction complexes, and NICD-RBPJ are intentional modeling abstractions; they should be preserved or decomposed consistently during schema materialization.

## Handoff

The next pass should reconcile these edges against Module 20A receptor/ligand entities, Module 15B receiver-state evidence, and Module 17B/18B innate-inflammatory intersections. Candidate export should begin with canonical edges marked medium priority and should carry the evidence context and non-equivalence boundaries into downstream pathway scoring.
