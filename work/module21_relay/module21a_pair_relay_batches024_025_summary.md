# Module 21A priority-7 batches 024-025 summary

Date: 2026-08-14

## Scope

Reviewed 50 exact Module20A priority-7 low/uncertain rows covering collagen
chains with syndecan-4, collagen-VI receptors, COMP/DSPP, laminin chains with
SV2A/B/C, and selected laminin/integrin pairs.

## Results

- 50 unique exact Module20A rows reviewed.
- Batch024: 25 unresolved exact chain/receptor cases.
- Batch025: 8 binding-only material/family-scope cases and 17 unresolved cases.
- No receptor-proximal relay, downstream functional-output, or terminal TF
  activation candidate was established.
- 50 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

Exact chain/receptor evidence was kept separate from collagen-family,
syndecan-family, integrin-family, and SV2 isoform evidence. Reactome and
pathway context was retained only as context or search boundary. DSP–β6 and
SV2–laminin observations were not promoted to the queued exact pairs without
matching receptor/isoform resolution.

The raw agent TSVs are retained as `module21a_batch024_review.tsv` and
`module21a_batch025_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches024_025.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches024_025.tsv`
- `module21a_pair_relay_batches024_025_summary.md`
- `module21a_all_pair_relay_handoff.md`
- `scripts/integrate_module21a_pair_review_batches024_025.py`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
