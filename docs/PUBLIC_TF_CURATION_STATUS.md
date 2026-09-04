# Public TF/regulon curation status

This document consolidates the public-TF triage and evidence-handoff notes
from 2026-08-26 and 2026-08-28. It is a provenance-aware catalog and review
handoff, not a canonical TF, regulon, Module 22B, or database materialization.

## Current checkpoint

At the retained 2026-08-28 checkpoint:

- 3,684 unique provenance-aware regulator–target–species pair groups had been
  reviewed across batches 001–039.
- The comprehensive overlay contained 3,065 exportable catalog rows.
- Evidence tiers were A: 31, B: 30, C: 3,004, D: 508, and E: 111; no rows
  remained unreviewed.
- The queue contained 460 adjudicated database-only outcomes, 18 adjudicated
  nonpromotable outcomes, and 141 resolved-unverifiable outcomes.
- No canonical TF, canonical regulon, Module 22B, or other materialization
  write was performed by the overlay.

The direction/species lane was closed for that pass. The 137 exact
direction/species holds and four identity holds were retained as
`resolved_unverifiable`; the unresolved symbol `ZA` was not mapped by
inference.

## Historical first-pass scope

The initial triage covered 2,051 normalized TF keys absent from the then-current
TF sets. It was an evidence-topology screen rather than a final biological
classification. Identity agreement, profile membership, or aggregated TFLink
membership did not by itself establish an exact regulator–target relationship.

## Authoritative working files

- Overlay: `data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/promoted_interactions.tsv`
- Priority queue: `data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/evidence_priority_queue.tsv`
- Search outcomes: `data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/evidence_search_outcomes.tsv`
- Context adjudications: `data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/context_evidence_adjudications.tsv`
- C-tier review queue: `data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/c_tier_context_review_queue.tsv`
- TFLink source records: `data/raw/public_database_snapshots/tf_union_expansion_v1/tflink_protein_targets_v1/`

## Resume and promotion rules

Continue from the C-tier queue and context adjudications. New work must
preserve literal symbols, species, source records, direction, assay/model
context, and limitations. Distinguish exact-pair evidence from regulator-level
or database membership evidence, and keep component context separate from
exact-pair context.

Unless a separate canonical review explicitly authorizes it, uncertain rows
must retain:

```text
exportable=false
canonical_write_performed=false
```

No ligand-to-TF path may be inferred from a public-TF catalog relationship.
Absence of SCI target-cell evidence remains a context qualifier, not a reason
to fabricate or silently transfer a mechanism.
