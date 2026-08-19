# Module 24A saturation tranche 020

This tranche separated downstream/context-supported legacy rows from unresolved
direct-pair claims and synchronized the final validated P2Y14 duplicate in this
group.

## Promotions

Promoted to `REVIEWED_SUPPORTED_DOWNSTREAM_CONTEXT`:

- Foam-cell lipid accumulation/C1q.
- RvD3 and RvD1 resolution-function rows.
- C3 breakdown-fragment/engineered CR2-Crry context.
- CCL3/CCR1 context.
- Tenascin-C/TLR4 boundary context.
- Decorin/protease-adjacent remodeling.
- TLR4-signaling-to-MMP9 downstream direction.
- C1q/synaptic engulfment read-only reuse.

Promoted to `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`:

- Duplicate UDP-glucuronic acid/P2Y14.

These promotions preserve unresolved receptor assignment, fragment identity,
single-agent attribution, receptor-specific perturbation, and directionality
limitations. No direct molecular interaction was inferred from functional or
pathway evidence.

## Validation disposition

- No new edges or evidence records were created.
- 151 edges, 200 evidence records, 172 associations, 189 matrix rows, and 31
  explicit no-evidence boundaries remain present.
- 0 unsupported edges and 0 duplicate edge keys.
- Matrix status counts are 106 pair-limit, 38 downstream-context, 9 complex-
  context, 2 supported-context, 17 boundary, and 17 first-pass rows.
- TSV widths and isolated PostgreSQL staging assertions passed.
- Frozen Module 20A manifest SHA256 remains
  `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Remaining search boundary

Seventeen first-pass rows remain. They are mostly exact chemokine receptor gaps
and noncognate/uncertain complement assignments; these should be resolved as
explicit boundaries or promoted only after exact primary evidence is validated.
