# Module 21A priority-6 batches 022-023 summary

Date: 2026-08-14

## Scope

Reviewed the final 23 priority-6 low/uncertain rows in the external review
queue, covering thrombospondin-3/4, tenascin-C/N/R, and tenascin-X-binding
protein candidates.

## Results

- 23 unique exact Module20A rows reviewed.
- 1 receptor-proximal relay candidate was retained for TNN-associated
  α9β1-dependent motility/neurite-repulsion evidence, but the exact queued
  TNN–α9β1 assignment remains unresolved because the primary study used
  tenascin-N/W material rather than an isolated TNN chain.
- 22 exact chain/receptor cases remain unresolved or comparator-boundary cases.
- No terminal TF was directly measured in either batch.
- 23 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

Tenascin family, TNX, and integrin comparator evidence was not transferred
between ligands or receptor complexes. The one retained pathway entry is
explicitly receptor-complex/pathway-level and does not establish a direct
isolated-chain molecular interaction. No TF was assigned from motility,
adhesion, or TGFβ pathway context alone.

The raw agent TSVs are retained as `module21a_batch022_review.tsv` and
`module21a_batch023_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches022_023.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches022_023.tsv`
- `module21a_pair_relay_batches022_023_summary.md`
- `module21a_all_pair_relay_handoff.md`
- `scripts/integrate_module21a_pair_review_batches022_023.py`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
