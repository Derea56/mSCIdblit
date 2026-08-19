# Module 24A saturation tranche 021

This final first-pass tranche completed the disposition of all remaining Module
24A matrix rows. Exact unsupported receptor assignments were converted to
explicit reviewed boundaries; comparator-only and transcriptomic rows were
classified without promoting them to direct molecular edges.

## Boundary dispositions

Converted to `REVIEWED_BOUNDARY`:

- CXCL10/CCR3.
- CXCL11/CCR3 and CXCL11/CXCR3.
- CXCL9/CCR3 and CXCL9/CXCR3.
- Intact C3/C3aR1.
- C3a/C5aR1.
- C4a/C3aR1.
- C5a/C3aR1.
- Hc/C5aR1.
- C3a/C5aR1 and C5a/C3aR1 noncognate duplicate candidates.
- C4b/CR2.

Each boundary points to an existing explicit no-evidence search record or
retains the exact-pair limitation already documented in the evidence register.

## Context dispositions

- CXCL2/CXCR2 was classified as `REVIEWED_SUPPORTED_CONTEXT` because the local
  support is transcriptomic/pathway context without ligand-specific
  perturbation.
- CXCL5/CXCR2 and XCL1/XCR1 were classified as
  `REVIEWED_SUPPORTED_DOWNSTREAM_CONTEXT` and remain peripheral-nerve-injury
  comparators, not traumatic-SCI evidence.
- The duplicate foam-cell/C1q context row was classified as
  `REVIEWED_SUPPORTED_DOWNSTREAM_CONTEXT` with receptor assignment unresolved.

## Validation disposition

- No new edges or evidence records were created.
- All 189 matrix rows are now dispositioned; 0 `REVIEWED_FIRST_PASS` rows
  remain.
- 151 edges, 200 evidence records, 172 associations, and 31 explicit
  no-evidence boundaries remain present.
- 0 unsupported edges and 0 duplicate edge keys.
- Final matrix status counts are 106 pair-limit, 41 downstream-context, 30
  boundary, 9 complex-context, and 3 supported-context rows.
- TSV widths and isolated PostgreSQL staging assertions passed.
- Frozen Module 20A manifest SHA256 remains
  `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Completion boundary

Module 24A first-pass saturation is complete at the audit-layer disposition
level. The remaining 30 boundary rows are explicit search-bounded unresolved
cases, not inferred negative biology. Further work should be a targeted
second-pass primary-literature search or downstream materialization review,
not automatic promotion of these boundaries.
