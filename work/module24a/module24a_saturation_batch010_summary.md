# Module 24A saturation tranche 010

This tranche targeted the specialized pro-resolving receptor branch while
keeping SCI, spinal pain comparator, and human GPR32 evidence separate.

## Addition

- `M24A-E151` / `M24A-B010-EVID-001`: rat spinal FPR2/ALX functional
  comparator for RvD1-family suppression of inflammatory pain and TNF release,
  with human astrocyte ERK and GPR32-expression context.

## Promotion and limits

- `M24A-Q0065` remains `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`, now incorporating
  rat FPR2/ALX spinal comparator function alongside the existing human GPR32
  pharmacology and SCI RvD1 functional record.
- The new record is not a traumatic-SCI edge and does not establish GPR32
  causality, rodent GPR32 orthology, or receptor-selective FPR2 dependence.
- C4b–CR2 and Hc–C5aR1 searches remained negative and were not promoted.

## Validation disposition

- One downstream/function edge and one evidence record were added.
- The integrated registers now contain 151 edges, 200 evidence records, 31
  explicit no-evidence boundaries, 169 edge/evidence associations, and 189
  saturation-matrix rows.
- PostgreSQL staging passed with zero unsupported edges and preserved the
  downstream-function layer for `M24A-E151`.

## Search boundary

The primary comparator was [Abdelmoaty et al., PLOS One, PMID
24086560](https://pubmed.ncbi.nlm.nih.gov/24086560/). It used peripheral
carrageenan inflammation rather than SCI, so its FPR2/ALX and human astrocyte
findings do not establish SCI receptor causality.
