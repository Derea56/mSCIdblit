# Module 24A saturation tranche 019

This tranche synchronized ten duplicate/read-only queue rows with already
validated Module 24A edges and evidence.

## Promotions

- Duplicate neurokinin B/Tacr1–3 rows.
- Duplicate neuropeptide gamma/Tacr1–2 rows.
- Duplicate substance P/Tacr2–3 rows.
- Duplicate UDP-N-acetylglucosamine, UDP-galactose, and UDP-glucose/P2Y14
  rows.

All ten rows are now `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`. No duplicate edge or
evidence record was created; existing weak-cross-reactivity, non-SCI, and
comparator limitations remain attached to the rows.

## Validation disposition

- 151 edges, 200 evidence records, 172 associations, 189 matrix rows, and 31
  explicit no-evidence boundaries remain present.
- 0 unsupported edges and 0 duplicate edge keys.
- Matrix status counts are 105 pair-limit, 29 downstream-context, 9 complex-
  context, 2 supported-context, 17 boundary, and 27 first-pass rows.
- TSV widths and isolated PostgreSQL staging assertions passed.
- Frozen Module 20A manifest SHA256 remains
  `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Search boundary

This was a read-only reuse synchronization tranche. Remaining first-pass rows
are concentrated in exact complement/chemokine receptor gaps, resolution-lipid
receptor assignment, and several legacy functional/context rows where direct
pair or directionality evidence is still unresolved.
