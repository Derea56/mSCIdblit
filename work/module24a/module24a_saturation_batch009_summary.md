# Module 24A saturation tranche 009

This tranche targeted the unresolved C3-to-CR4 complement candidate while
keeping processed-fragment binding distinct from intact precursor and SCI
activation claims.

## Addition

- `M24A-E150` / `M24A-B009-EVID-001`: direct human iC3b–CR4/alphaX-beta2
  structural and biochemical binding comparator using purified ectodomain
  complexes and negative-stain EM.

## Promotion and limits

- `M24A-Q0070` is now `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`.
- The evidence supports processed iC3b recognition by CR4/alphaX-beta2, not
  intact C3 binding, endogenous SCI fragment identity, or an SCI receptor
  relay.
- `M24A-Q0071` (C4b–CR2) remains unresolved; no qualifying exact endogenous
  C4b–CR2 SCI edge was validated.
- Hc–C5aR1 remains unresolved and was not promoted from adjacent C5a/C5aR1
  evidence.

## Validation disposition

- One new direct molecular edge and one evidence record were added.
- The integrated registers now contain 150 edges, 199 evidence records, 31
  explicit no-evidence boundaries, 168 edge/evidence associations, and 189
  saturation-matrix rows.
- PostgreSQL staging passed with zero unsupported edges and preserved the
  ligand-receptor-binding layer for `M24A-E150`.

## Search boundary

The primary CR4 paper is a human non-SCI comparator: [Chen et al., PNAS,
PMID 22393018](https://pubmed.ncbi.nlm.nih.gov/22393018/). It does not establish
intact C3–CR4 activation or endogenous SCI causality. C4b–CR2 and Hc–C5aR1
remain explicit no-evidence boundaries.
