# Public TF union second-wave expansion

The original 16-TF panel is complete. The remaining imported union is much
larger and is being handled as a ranked evidence queue rather than being
treated as literature-promoted by default.

## Inventory

- 45,795 imported TRRUST/DoRothEA source records remain intact.
- 1,676 species-specific non-priority TF candidates remain after excluding the
  original panel and obvious protein-accession identifiers.
- Those candidates represent 1,090 normalized TF keys.
- 1,172 candidate rows have both human and mouse coverage.
- 18 candidate rows overlap existing 20B/21B/23B/24B paper queues.

## Module routing

Every public TF→target assertion defaults to Module 22B. Existing overlap with
20B, 21B, 23B, or 24B is recorded as a routing flag only. A cross-module
promotion requires exact module-specific evidence and an independent
corroborating paper; citation reuse alone does not move a TF-target row into
another module.

## Current tranche

The first 20 normalized TF keys are being reviewed in five disjoint lanes:

`RELA`, `NFKB1`, `STAT3`, `RELB`, `ESR1`, `VDR`, `AR`, `CEBPA`, `E2F1`,
`HNF4A`, `CTCF`, `SMAD3`, `SMAD4`, `STAT5A`, `ELK1`, `TFAP2A`, `MITF`,
`SPI1`, `SP3`, and `CREB1`.

The source-level inventory is
[new_tf_inventory.tsv](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_v1/module_curation/new_tf_inventory.tsv).
It is a queue, not a promotion ledger: rows remain `new_candidate` until
exact-pair primary and corroborating evidence is adjudicated.

## First evidence tranche result

The first bounded tranche produced 22 exact human TF-target rows:

- 20 promoted to Module 22B staging, each with a primary and independent
  corroborating PMID.
- 2 held as direction conflicts: RELB→IL6 and SP3→CDKN1A.
- 0 cross-module promotions.

The staged files are
[new_tf_merged.tsv](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_v1/module_curation/new_tf_merged/new_tf_merged.tsv),
[new TF promotions](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_v1/module_curation/new_tf_materialized/priority_tf_agent_promoted.tsv),
and the [new TF materialization manifest](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_v1/module_curation/new_tf_materialized/priority_tf_agent_materialization_manifest.json).

## Remaining 54-batch completion

The remaining ranked queue is now lane-complete. All 54 batches cover 1,070
normalized TF keys and were validated against the batch manifest. The bounded
agent lanes produced six exact-pair promotions; the other 1,064 rows remain
explicitly `database_only_unverified` holds because the existing TRRUST/DoRothEA
source lead did not by itself establish exact-pair primary evidence plus an
independent corroborating paper. No citation-overlap-only promotion was made.

The full batch [merge manifest](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_v1/module_curation/new_tf_batch_merged/all_remaining/new_tf_batch_merge_manifest.json),
[merged decision ledger](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_v1/module_curation/new_tf_batch_merged/all_remaining/new_tf_batch_merged.tsv),
[materialization manifest](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_v1/module_curation/new_tf_batch_materialized/all_remaining/priority_tf_agent_materialization_manifest.json),
and [release validation report](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_v1/public_tf_union_validation_all_remaining.json)
are the audit artifacts. All promoted rows are staged in Module 22B; module
20B/21B/23B/24B overlap remains a routing/review flag and was not promoted by
shared citation.

## Literature re-review

The 54-batch queue was subsequently re-opened as a literature search. For each
batch, the strongest TRRUST/DoRothEA-linked records were converted into bounded
PubMed packets; 3,621 unique linked PMIDs returned abstracts and publication metadata.
Abstract-level exact-pair adjudication produced 108 new Module 22B promotions,
516 exact-pair single-source holds, and 446 unverified source leads. Every new
promotion has two distinct exact-pair primary PMIDs in the staged ledger; the
remaining rows were not promoted merely because TRRUST contained a citation.

The [evidence-search merge manifest](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_v1/module_curation/new_tf_evidence_merged/all_remaining/new_tf_batch_merge_manifest.json),
[evidence-search ledger](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_v1/module_curation/new_tf_evidence_merged/all_remaining/new_tf_batch_merged.tsv),
[evidence-search materialization](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_v1/module_curation/new_tf_evidence_materialized/all_remaining/priority_tf_agent_materialization_manifest.json),
and [evidence-search validation report](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_v1/public_tf_union_validation_evidence_search.json)
contain the provenance and release checks.
