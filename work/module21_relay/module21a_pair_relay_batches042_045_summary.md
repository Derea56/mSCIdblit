# Module 21A priority-8 batches 042-045 summary

Date: 2026-08-14

## Scope

Reviewed 100 priority-8 low/uncertain rows spanning dopamine receptor
subtypes, desmosomal adhesion, estrogen receptors, FLRT guidance receptors,
and GABA receptor complexes.

## Results

- 100 unique exact Module20A rows reviewed.
- 66 reusable relay/function candidates were retained.
- 21 binding-only cases were retained.
- 5 downstream functional-only cases were retained.
- 8 exact rows remain unresolved.
- Direct TF handoffs were retained for ESR1, ESR2, and CREB only where the
  matched receptor or receptor-relay studies directly supported them.
- 100 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

DOPA-DDC and SLC18/SLC6 labels were treated as dopamine production, storage, or
transport context rather than receptor activation. Desmosomal and FLRT
adhesion/guidance observations were not promoted to intracellular signaling
without receptor-dependent perturbation. GABA-A receptor-complex and GABA-B
branches were kept distinct; receptor-family identity alone did not produce a
TF handoff.

The raw agent TSVs are retained as `module21a_batch042_review.tsv` through
`module21a_batch045_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches042_045.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches042_045.tsv`
- `module21a_pair_relay_batches042_045_summary.md`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
