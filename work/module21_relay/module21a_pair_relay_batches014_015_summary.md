# Module 21A priority-6 batches 014-015 summary

Date: 2026-08-14

## Scope

Reviewed the first 50 priority-6 low/uncertain ECM rows, covering COL1A1,
COL1A2, COL2A1, COL4A1-COL4A5, GPVI, CD44, SDC1, alpha1/2/3/9/10/11beta1,
and alphaVbeta8 assignments. One queue-ID mismatch was explicitly corrected:
the COL2A1-SDC1 row is `M20A-EXT-0181`, while `M20A-EXT-0201` is COL4A2-SDC1.
The overlapping 0181 result was deduplicated before integration.

## Results

- 50 unique exact Module20A rows reviewed.
- 1 reusable Module21A functional candidate added:
  COL4A3-alpha2beta1 renal matrix maturation/fibrosis genetic interaction.
- 9 rows retained as native collagen/multichain or fragment binding-only
  evidence, without a downstream relay.
- 40 rows retained as unresolved exact chain-receptor cases.
- 50 stable batch evidence IDs added to the detailed evidence register.
- No terminal TF activation candidate was added.

## Evidence-layer handling

The batch is intentionally conservative. Native collagen-IV network, collagen
fragment, collagen-family, GPVI comparator, and alphaVbeta8-latent-TGFbeta
observations were not reassigned to isolated COL4A1-COL4A5 chain pairs. The
one functional candidate remains functional genetic evidence rather than a
direct binding claim. Search boundaries covered exact-symbol PubMed and PMC
queries, publisher pages, Reactome family records, and collagen-family
comparators; family-level pathway records were retained as context only.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches014_015.tsv`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
