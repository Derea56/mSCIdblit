# Module 21A priority-8 batches 046-047 summary

Date: 2026-08-14

## Scope

Reviewed 50 priority-8 GABA rows covering SLC6A11/12/13/6A6-associated labels,
GABA-B1/B2, and multiple GABA-A receptor complexes.

## Results

- 50 unique exact Module20A rows reviewed.
- 44 reusable receptor-proximal relay candidates were retained.
- 3 binding-only cases were retained.
- 3 exact rows remain unresolved.
- No terminal TF was directly measured or assigned.
- 50 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

GAD1 and SLC6A11/12/13/6A6 labels were treated as synthesis or transporter
context rather than receptor activation. GABA-A ligand-gated receptor-complex
electrophysiology was kept distinct from GABA-B1/GABA-B2 heterodimer coupling;
subtype identity alone did not produce a downstream TF handoff.

The raw agent TSVs are retained as `module21a_batch046_review.tsv` and
`module21a_batch047_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches046_047.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches046_047.tsv`
- `module21a_pair_relay_batches046_047_summary.md`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
