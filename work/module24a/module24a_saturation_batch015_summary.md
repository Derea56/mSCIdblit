# Module 24A saturation tranche 015

This tranche promoted ten legacy Module 18 reuse rows after Batch014 repaired
their evidence associations. Promotions were limited to rows with validated
receptor/relay or downstream functional support; each retains its specific
pair, specificity, model-transfer, or overlap limitation.

## Promotions

- Myelin debris/TREM2.
- Extracellular ATP/P2X7R.
- P2Y12R to CD39/CD73-adenosine-A1R and downstream mitophagy.
- Extracellular traps/LL37 to the P2X7R-NF-kB relay.
- LTB4/BLT1.
- HMGB1/TLR2-4 relay context.
- S100A8/TLR4 relay context.
- ATP/P2X4R pharmacologic SCI context.
- CCL2/CCR2 downstream recruitment and myelin-clearance context.
- CCL28/CCR10 downstream Treg-recruitment and recovery context.

All ten are now `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`. The disposition does not
claim purified ligand binding where the evidence is pharmacologic, pathway-
level, or receptor-complex ambiguous, and it does not duplicate frozen Module
20A LR records.

## Validation disposition

- No new edges or evidence records were created.
- 171 queue rows, 151 edges, 200 evidence records, 172 associations, 189
  matrix rows, and 31 explicit no-evidence boundaries remain present.
- 0 unsupported edges and 0 duplicate IDs.
- Matrix status counts are 65 pair-limit, 29 downstream-context, 9 complex-
  context, 2 supported-context, 17 boundary, and 67 first-pass rows.
- TSV widths remain exact and the isolated PostgreSQL staging reload passed all
  embedded assertions.
- Frozen Module 20A manifest SHA256 remains
  `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Remaining boundary

Unresolved C1q receptor assignment, resolution-lipid receptor assignment,
engineered CR2-Crry targeting, exact chemokine receptor gaps, noncognate
complement assignments, and reverse-direction ECM claims remain first-pass or
boundary rows for the next tranche.
