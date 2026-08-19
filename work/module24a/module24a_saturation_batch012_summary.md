# Module 24A saturation tranche 012

This tranche audited existing primary evidence and promoted 16 non-duplicate
matrix rows without adding edges or evidence records.

## Promotions

- APC/EPCR/PAR1, thrombin/PAR1, C3a/C3aR1, C5a/C5aR1, substance P/Tacr1,
  and Tac1-derived substance P SCI rows.
- CX3CL1/CX3CR1, CXCL1/CXCR2, CXCL10/CXCR3, and CXCL3/CXCR2 SCI or
  ischemia-reperfusion rows.
- CCN1/SDC4 binding/function rows, LL37/P2X7R, extracellular ATP/P2X7R,
  P2Y12R-to-adenosine relay, and myelin-debris/TREM2.

All 16 are now `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`. Their `next_gap` fields
retain purified-binding, receptor-specificity, model-transfer, timing, and
cell-source limitations where applicable.

## Validation disposition

- No new edges or evidence records were created.
- Counts remain 151 edges, 200 evidence records, 169 associations, 189 matrix
  rows, and 31 explicit boundaries.
- Matrix status counts now include 45 `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT` rows
  and 87 `REVIEWED_FIRST_PASS` rows.
- Register widths and existing evidence coverage remain valid.

## Search boundary

This was a disposition audit of already validated primary records. It does not
convert pathway/function records into direct ligand-receptor binding claims and
does not modify the frozen Module 20A LR ledger.
