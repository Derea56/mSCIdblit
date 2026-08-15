# Module 21A priority-8 batches 052-053 summary

Date: 2026-08-15

## Scope

Reviewed 50 priority-8 rows covering GAD2/SLC6A13 and GAD2/SLC6A6 GABA
complexes, GAD2/SLC6A8 GABA complexes, glucagon receptor families, and
connexin-43/connexin-40 gap-junction pairs.

## Results

- 50 unique exact Module20A rows reviewed.
- 39 reusable relay/function candidates were retained.
- 2 binding-only cases were retained.
- 2 downstream functional-only cases were retained.
- 9 exact rows remain unresolved.
- No terminal TF was directly measured or assigned.
- 50 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

GAD2 and SLC6A6/SLC6A8/SLC6A13 labels were treated as synthesis or transporter
context, not receptor activation. GABA-A receptor-complex electrophysiology was
kept distinct from GABA-B subunit coupling. Glucagon receptor branches and
connexin gap-junction function were recorded separately from ligand-receptor
relay and no TF was inferred from receptor-family identity alone.

The raw agent TSVs are retained as `module21a_batch052_review.tsv` and
`module21a_batch053_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches052_053.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches052_053.tsv`
- `module21a_pair_relay_batches052_053_summary.md`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
