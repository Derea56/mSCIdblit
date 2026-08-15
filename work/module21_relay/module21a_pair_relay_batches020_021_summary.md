# Module 21A priority-6 batches 020-021 summary

Date: 2026-08-14

## Scope

Reviewed 50 exact Module20A priority-6 low/uncertain rows covering laminin
chains, NCAM1/NCAM2, and thrombospondin-2 receptor candidates.

## Results

- 50 unique exact Module20A rows reviewed.
- 2 receptor-proximal relay candidates were retained:
  LAMA2–α3β1 through ERK1/2-AKT and proliferation, and
  LAMC3-containing laminin–DAG1 through DLL4/Notch vascular phenotypes.
- The LAMC3 result is explicitly a receptor-complex/pathway edge for assembled
  gamma-3-containing laminin; it is not an isolated LAMC3 direct-binding edge.
- 1 laminin-1/β8-family case was retained as binding-only at family scope.
- 47 exact chain/receptor cases remain unresolved or negative-boundary cases.
- No terminal TF was directly measured in either batch.
- 50 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

Direct binding, receptor-complex/pathway relay, and functional observations were
kept distinct. Laminin-family transfer, intact-complex ambiguity, pathway
co-membership, expression associations, and noncognate receptor comparisons
were retained only as limitations or negative search boundaries. No TF was
assigned from ERK/AKT or DLL4/Notch pathway context alone.

The raw agent TSVs are retained as `module21a_batch020_review.tsv` and
`module21a_batch021_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches020_021.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches020_021.tsv`
- `module21a_pair_relay_batches020_021_summary.md`
- `module21a_all_pair_relay_handoff.md`
- `scripts/integrate_module21a_pair_review_batches020_021.py`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
