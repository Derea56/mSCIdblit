# Module 21A priority-8 batches 048-049 summary

Date: 2026-08-14

## Scope

Reviewed 50 priority-8 GABA rows covering SLC6A6, SLC6A8, GAD2/SLC32A1,
GAD2/SLC6A1, GABA-A receptor complexes, and GABA-B subunits.

## Results

- 50 unique exact Module20A rows reviewed.
- 44 reusable GABA-A receptor-proximal relay candidates were retained.
- 3 GABA-B1 binding-only cases were retained.
- 3 standalone GABA-B2 exact rows remain unresolved.
- No terminal TF was directly measured or assigned.
- 50 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

GAD2 and SLC6A6/SLC6A8/SLC32A1/SLC6A1 labels were treated as synthesis,
storage, or transporter context rather than receptor activation. GABA-A
ligand-gated electrophysiology was kept distinct from GABA-B1/GABA-B2
heterodimer binding and signaling. Receptor subtype identity alone did not
produce a downstream TF handoff.

The raw agent TSVs are retained as `module21a_batch048_review.tsv` and
`module21a_batch049_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches048_049.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches048_049.tsv`
- `module21a_pair_relay_batches048_049_summary.md`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
