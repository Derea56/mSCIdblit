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

The module screening overlay now separates explicitly noncanonical A/B
module-context rows into
`module_integration_staging_v1/noncanonical_gene_expression_regulators.tsv`.
These rows retain their A/B evidence tiers and module routes. The vocabulary is
now explicitly orthogonal:

| Axis | Meaning |
|---|---|
| `regulator_role_class` / `canonical_role_status` | Biological role: canonical sequence-specific TF, noncanonical gene-expression regulator, non-transcriptional regulator, or unresolved |
| `evidence_weight_tier` | Reviewed evidence strength: A/B/C/D/E; unchanged by this vocabulary update |
| `sci_context_status` | SCI relevance: direct, indirect, non-SCI transferable, unresolved, not assessed, or not applicable |
| `context_level_regulator` / `context_level_target` / `context_level_exact_pair` | Graded context specificity: L0 no context evidence, L1 non-CNS, L2 CNS, L3 spinal-cord tissue, or L4 SCI |
| `context_evidence_scope` | Whether that context applies to the exact pair, regulator, target, only a pathway/component, or no qualifying context was found in the bounded screen |
| `context_promotion_lane` | Context-aware promotion destination, kept separate from A–E evidence strength; current adjudications are recorded in `context_evidence_adjudications.tsv` |
| `module_fit_status` | Whether an explicit module route exists and whether it still needs review |
| `materialization_lane` | Canonical TF/regulon candidate, noncanonical module-context candidate, external context, or low-tier screen-out |
| `mechanism_evidence_type` / `mechanism_evidence_definition` | The molecular bridge actually supported, stated in plain language; omitted intermediates and promoter occupancy are not implied |

Thus, “canonical” describes regulator biology, not SCI evidence. A canonical
TF can have `sci_context_status=not_assessed` or `unresolved_sci_context`,
while a noncanonical cofactor or chromatin regulator can retain A/B evidence
and, if later supported, direct SCI context. The legacy
`canonical_tf_eligible` field remains only for compatibility and must not be
read as an SCI-context result.

Mechanism labels are intentionally explicit. For example,
`indirect_extracellular_signal_to_target_rna` means an external
ligand/protease/receptor relay is associated with a downstream target-RNA
change; it does not claim that every intermediate step or target-promoter
occupancy was demonstrated. This is an input-to-output relationship with a
partial mechanistic bridge, not a canonical TF-to-promoter edge.

The graded-context registry is now populated for the A/B promotion set and all
3,004 C-tier relationships. It
records non-CNS, CNS, spinal-cord-tissue, or SCI context only when the cited
evidence supports that level, keeps exact-pair context separate from component
context, and uses L0 for pairs with no context evidence. The adjudication
registry is
`data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/context_evidence_adjudications.tsv`.
`L1_non_CNS_context` captures evidence from non-CNS models or tissues;
`L2_CNS_context` captures neural/CNS evidence outside spinal cord;
`L3_spinal_cord_tissue_context` captures spinal-cord tissue or spinal-cord-cell
evidence without an SCI model; and `L4_SCI_context` captures an SCI model,
lesion tissue, or SCI patient material. A component can be L4 while the exact
regulator-target pair remains L0, so component context must not be promoted as
exact-pair SCI evidence.

The fillable module-owner review packet is
`module_integration_staging_v1/noncanonical_module_owner_review.tsv`; its
controlled decision vocabulary and rubric are in
`module_integration_staging_v1/noncanonical_module_owner_review_rubric.md`.
All 49 rows begin as `pending_review`. An approved row would be materialized
only in the separate noncanonical module-context layer, never as a canonical
TF/regulon edge.

The current mechanism-scope pre-triage is recorded in
`module_integration_staging_v1/noncanonical_module_context_triage.tsv`:
35 module-context rows (31 unique pair keys) remain candidates for focused
module/SCI review, while 14 rows (9 unique pair keys) remain upstream or
protein-level context only. This pre-triage does not constitute owner approval.

The 35 candidate adjudications are recorded in
`module_integration_staging_v1/noncanonical_module_context_adjudication.tsv`.
All remain `needs_more_context`: the existing reviews support plausible
noncanonical mechanisms, but the SCI target-cell/module-context or requested
corroboration/occupancy gates are not yet satisfied. Their role class is
noncanonical independently of that unresolved context gate, and no
noncanonical or canonical materialization was performed.

The C-tier context queue is
`module_integration_staging_v1/c_tier_context_review_queue.tsv`. It contains
3,004 unique regulator-target-species relationships: 2,459 module-routed and
545 catalog-only. All retain `C_tflink_source_table_only`. The current packet
has adjudications for all 3,004 C relationships. A bounded round-240 recheck
covered the 16 relationships that previously had L0 for both components.
Species-matched HPA, NCBI, MGI, and primary-literature evidence provided
component context for all 16; their exact regulator-target pairs remain L0
because no direct contextual mechanism or occupancy was verified. The
remaining exact-pair L0 values are therefore not assertions that both
components lack context. This is bounded to the reviewed evidence packet, not
a claim of exhaustive literature absence. No materialization was performed.

## Resume point

The C-tier context pass is resumable for the current evidence packet. Start the
next task by reading this handoff, then inspect:

1. `module_integration_staging_v1/c_tier_context_review_queue.tsv` for the
   complete 3,004-relationship C queue;
2. `module_integration_staging_v1/context_evidence_adjudications.tsv` for the
3,004 C adjudications plus the 61 A/B adjudications; and
3. `module_integration_staging_v1/module_screening_summary.json` for the latest
   derived screening counts.

The next productive work is continued bounded search for new authoritative
context evidence, followed by module-owner review of the 2,459 explicitly
routed C relationships. Remaining exact-pair L0 records may be searched in
ranked batches; each batch must log exact queries, species checks, sources, and
no-upgrade outcomes. Component overlays are not exact-pair evidence and must
remain separate from pair-level promotion. Round-240 recheck details are
embedded in the updated ledger rows and identified by the `round_240_` marker.

The targeted search ledgers are
`module_integration_staging_v1/c_tier_context_search_round_001.tsv`,
`module_integration_staging_v1/c_tier_context_search_round_002.tsv`,
`module_integration_staging_v1/c_tier_context_search_round_003.tsv`, and
`module_integration_staging_v1/c_tier_context_search_round_004.tsv`. They record
the queue ranks searched, exact queries, species checks, source citations,
upgrade decisions, and bounded no-upgrade outcomes. Round 240 covered queue
ranks recorded in the updated ledger rows; all 16 are component-only upgrades
and all 16 exact pairs remain L0. The updated rows are identifiable by the
`round_240_` fields and retain their original ledger rows and prior search
history.

Round 241 then audited all 2,994 remaining C-tier exact-pair L0 records against
their species-specific TFLink raw snapshots. All 2,994 had an existing snapshot,
matching SHA-256, matching regulator and target rows, matching organism, and
matching recorded source metadata. The detailed audit is
`module_integration_staging_v1/c_tier_exact_pair_source_chain_audit.tsv`.
This is provenance verification only: it does not upgrade an exact-pair context
level or establish causal regulation. The `round_241_tflink_gtrd_source_chain`
marker is attached to each corresponding ledger row.

Round 242 added two component-only upgrades while preserving exact-pair L0.
Allen Mouse Brain Atlas mouse spinal-cord ISH evidence for target
`2610001J05Rik/Smim30` raised the target component to L3 for
`public_tf_comprehensive_096` (`AHCY -> 2610001J05Rik`). Human Protein Atlas
mouse-brain evidence for `Actr2` raised the target component to L2 for
`public_tf_comprehensive_1246` (`MFSD11 -> Actr2`). Neither source established
direct pair mechanism or occupancy. The decisions are recorded in
`module_integration_staging_v1/c_tier_context_search_round_242.tsv` and the
cumulative ledgers. A resumable PubMed exact-pair screen was started but not
completed after transient NCBI resolver failures; failed requests were removed
from the partial output and were not counted as negative evidence.

Round 243 closed the remaining ledger-coverage gap for 43 C-tier L0 rows that
lacked an explicit literal-symbol exact-pair search record. Each row received a
bounded PubMed web exact-symbol screen with a traceable query locator; no direct
species-matched pair mechanism or occupancy was found, and no exact-pair level
changed. Same-article or component-only candidates were recorded as rejected
candidates where applicable. The complete 43-row ledger is
`module_integration_staging_v1/c_tier_context_search_round_243.tsv`.

If source or adjudication inputs change, rebuild the derived staging outputs in
this order:

```bash
python3 scripts/build_public_tf_context_adjudications.py
python3 scripts/screen_public_tf_module_integration.py
python3 scripts/build_public_tf_c_context_review_queue.py
```

Then run the validation commands below. No canonical TF, regulon, Module 22B,
module-tracker, or mechanism-edge materialization has been performed. This
checkpoint is limited to public-TF evidence curation and provenance artifacts;
unrelated module/release work must remain unstaged.

## Best next work

1. Resume from the C queue and the Round-241 source-chain audit before editing
   anything.
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
