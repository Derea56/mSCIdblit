# Public TF/regulon evidence curation handoff

**Date:** 2026-08-28  
**Repository:** `/Users/derea/Documents/SCI/mSCIdblit`  
**Starting branch:** `main` after merge of the completed evidence pass

## Mission

Continue the public TF/regulon union evidence project as a comprehensive,
provenance-aware catalog of possible regulator–target–species relationships.
The catalog is not restricted to SCI target cells: peer-reviewed evidence from
other biological systems may support a catalog-level interaction when the
relationship is reasonably supported. Preserve the exact limitation and
mechanism instead of relabeling noncanonical biology as a sequence-specific TF
edge.

Never invent evidence, aliases, citations, species transfers, or directionality.
Use literal symbols from the queue and retain provenance back to the source
database and source snapshot.

## Current checkpoint

- Batches 001–039 are reviewed: 3,684 unique provenance-aware pair groups.
- The deterministic TFLink source-set queue is exhausted for this pass; there
  is no active literal-pair search packet.
- The comprehensive overlay contains 3,065 exportable catalog rows.
- Evidence-confidence tiers across all 3,684 reviewed pair groups:
  - A independent literature corroborated: 31
  - B independent literature single source: 30
  - C TFLink source-table evidence only: 3,004
  - D database-only, no pair-specific evidence: 508
  - E reviewed but nonpromotable: 111
  - U unreviewed: 0
- Queue disposition:
  - already promoted: 3,065
  - searched and pending adjudication: 0
  - adjudicated database-only outcomes: 460
  - adjudicated nonpromotable outcomes: 18
  - resolved unverifiable outcomes: 141 (137 direction/species; 4 identity)
  - identity hold: 0
- No canonical TF, canonical regulon, Module 22B, or other materialization write
  was performed by the public-TF overlay.

The direction/species lane is now closed for this pass. All 137 exact queue
keys were adjudicated against their bounded batch-review evidence; none was
verified sufficiently for promotion. They are recorded as
`resolved_unverifiable` and routed to the archive while retaining their
original limitations and provenance. The four final identity keys used raw
symbol `ZA`; no authoritative approved human-gene mapping was identified, so
they were also finalized as `resolved_unverifiable` without transferring any
target evidence.

## Authoritative files

- Triage history: `docs/PUBLIC_TF_EXPANSION_TRIAGE_SUMMARY_2026-08-26.md`
- Overlay: `data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/promoted_interactions.tsv`
- Priority queue: `data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/evidence_priority_queue.tsv`
- Completed search outcomes: `data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/evidence_search_outcomes.tsv`
- Overlay validation: `data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/promotion_validation.json`
- Priority summary: `data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/evidence_priority_summary.json`
- Batch reviews: `data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_001/` through `batch_039/`
- TFLink source records: `data/raw/public_database_snapshots/tf_union_expansion_v1/tflink_protein_targets_v1/`

## Module integration staging

All reviewed public-TF evidence is now staged for module-level screening in
`data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/`.
This is an additive evidence layer, not canonical materialization. It contains
3,555 module-assignment rows from the 3,684 reviewed queue rows, plus 619 rows
retained as catalog-only because they have no explicit module route. Multi-module
assignments remain separate. The original A/B/C/D/E evidence tier is preserved
exactly, with a separate reversible rank (A=3, B=2, C=1, D=0, E=0) for later
weighting. D/E rows are included for screening only, are non-exportable, and
remain blocked from materialization. U rows are excluded.

Module-assignment counts are 2,720 for 20B, 16 for 21B, 127 for 22B, 584 for
23B, and 108 for 24B. The staging manifest explicitly records
`module_materialization_allowed=false`, `canonical_tf_writes=false`, and
`module22b_writes=false`. The next step is module-owner review of these staged
rows before any module tracker or database materialization.

## Best next work

1. Read the triage summary and inspect the queue before editing anything.
2. The 18 remaining E-tier rows from completed search outcomes have now been
   adjudicated as non-promotable and routed to the archive/hold lane. Retain
   their actual mechanisms and source limitations; do not repeat those
   searches unless new traceable evidence is found.
3. No identity or direction/species holds remain open in this pass. The 141
   resolved-unverifiable rows should only be reopened if new literal,
   source-backed identity or pair evidence is found; do not infer an alias,
   paralog, fusion, fragment, cross-species pair, or reverse-direction match.
4. Leave the 508 D-tier rows as reviewed database-only rows unless a new,
   traceable source is found. Do not bulk-promote them because a database
   membership or regulon label exists.
5. If new candidates are added, mark them `U_unreviewed` until a complete pair
   review exists. Preserve unique provenance-aware keys and all raw source
   fields.

## Promotion rules

Distinguish database membership, regulator-level evidence, exact pair evidence,
binding/association, perturbation/downstream expression, functional
noncanonical evidence, cross-species or reverse-direction near matches, and
unresolved identity. Primary papers, authoritative database records, and direct
source links are preferred; record PMID/DOI/URL, species, model/cell context,
assay, direction, and evidence limitations. When a source supports a module-
specific role, route it to the correct Module 20B–24B category rather than
calling it canonical TF evidence.

For uncertain findings, keep:

```text
exportable=false
canonical_write_performed=false
```

Do not materialize canonical TF or Module 22B records from this overlay. The
overlay is a catalog-level evidence layer; absence of SCI target-cell evidence
is a context qualifier, not permission to overstate the mechanism.

Known identity cautions: RBP2 means CRBP2/P50120 in this queue, mouse H1-6 means
H1f6/H1t, CSHL1 is a secreted chorionic somatomammotropin-like protein, and ZA
is unresolved. Keep species-specific symbols separate unless the evidence
explicitly supports transfer.

## Validation and safe operating procedure

After each batch or promotion pass, validate row counts, unique provenance
keys, flags, duplicate pair records, and absence of canonical writes:

```bash
python3 scripts/validate_public_tf_union_expansion_v1.py
python3 scripts/validate_public_tf_union_v1.py \
  --output-dir data/processed/public_tf_union_v1 \
  --repo-root .
```

Update the triage summary after completed work. Preserve unrelated uncommitted
work in the repository. Do not run destructive cleanup, reset, force-push, or
unscoped staging. Do not access Biowulf or Helix directly from a worker task;
follow `AGENTS.md` and route any HPC work through an explicitly designated,
approved routing task. Local literature retrieval may be used when network
access is available, but every claim must remain traceable.

## Expected report

At handoff, report exact TF promotions, noncanonical functional candidates,
unresolved identities, database-only candidates, module-specific routing,
remaining evidence gaps, materialization status, validation results, and the
exact files changed.
