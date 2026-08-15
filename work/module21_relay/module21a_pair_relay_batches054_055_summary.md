# Module 21A priority-8 batches 054-055 summary

Date: 2026-08-15

## Scope

Reviewed 50 priority-8 connexin/gap-junction and glutamate receptor-complex
rows, including AMPA, kainate, NMDA, and metabotropic glutamate receptors.

## Results

- 50 unique exact Module20A rows reviewed.
- 41 reusable relay/function candidates were retained.
- 6 downstream functional-only connexin cases were retained.
- 2 exact kainate rows remain unresolved: GluK3/GluK4 and GluK3/GluK5.
- No terminal TF was directly measured or assigned.
- 50 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

Connexin gap-junction function was kept separate from ligand-receptor relay.
SLC17A6 and GLS/GLS2 labels were treated as glutamate storage or synthesis
context. Ionotropic receptor electrophysiology and metabotropic G-protein
coupling were kept as distinct receptor-proximal branches; receptor subtype
identity alone did not produce a TF handoff.

The raw agent TSVs are retained as `module21a_batch054_review.tsv` and
`module21a_batch055_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches054_055.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches054_055.tsv`
- `module21a_pair_relay_batches054_055_summary.md`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
