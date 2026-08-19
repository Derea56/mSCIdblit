# Module 24A saturation tranche 018

This tranche dispositioned ten validated comparator and duplicate-seed rows.
The records support P2Y14 or FPR receptor pharmacology, or reuse already
validated tachykinin edges, but they do not establish traumatic-SCI release or
SCI-specific downstream function.

## Promotions

- UDP-glucuronic acid/P2Y14.
- FAM3D/FPR1 and FAM3D/FPR2.
- TAFA5/FAM19A5/FPR2, retaining the alternate-receptor limitation.
- Duplicate hemokinin-1/Tacr1–3 rows.
- Duplicate neurokinin A/Tacr1–3 rows.

All ten rows are now `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`. Duplicate rows point
to existing validated edges and evidence rather than creating new records.

## Validation disposition

- No new edges or evidence records were created.
- 151 edges, 200 evidence records, 172 associations, 189 matrix rows, and 31
  explicit no-evidence boundaries remain present.
- 0 unsupported edges and 0 duplicate edge keys.
- Matrix status counts are 95 pair-limit, 29 downstream-context, 9 complex-
  context, 2 supported-context, 17 boundary, and 37 first-pass rows.
- TSV widths and isolated PostgreSQL staging assertions passed.
- Frozen Module 20A manifest SHA256 remains
  `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Search boundary

The promotions preserve non-SCI comparator status, weak or alternate-receptor
limitations, and the distinction between direct pharmacology and downstream
function. Remaining first-pass rows are concentrated in unresolved complement,
exact chemokine, resolution-lipid, and legacy receptor-assignment gaps.
