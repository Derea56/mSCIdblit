# Module 21A priority-8 batches 050-051 summary

Date: 2026-08-14

## Scope

Reviewed 50 priority-8 GABA rows covering GAD2/SLC6A1, GAD2/SLC6A11,
GAD2/SLC6A12, and GAD2/SLC6A13 source labels with GABA-A and GABA-B receptor
complexes.

## Results

- 50 unique exact Module20A rows reviewed.
- 42 reusable GABA-A receptor-proximal relay candidates were retained.
- 2 GABA-B1 binding-only cases were retained.
- 6 exact rows remain unresolved, including standalone GABA-B2 or poorly
  resolved GABA-A complexes.
- No terminal TF was directly measured or assigned.
- 50 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

GAD2 and SLC6A1/SLC6A11/SLC6A12/SLC6A13 labels were retained as synthesis or
transporter context rather than receptor activation. GABA-A ligand-gated
electrophysiology was kept distinct from GABA-B1/GABA-B2 heterodimer binding.
Receptor subtype identity alone did not produce a downstream TF handoff.

The raw agent TSVs are retained as `module21a_batch050_review.tsv` and
`module21a_batch051_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches050_051.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches050_051.tsv`
- `module21a_pair_relay_batches050_051_summary.md`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
