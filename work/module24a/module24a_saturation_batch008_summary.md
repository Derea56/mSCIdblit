# Module 24A saturation tranche 008

This tranche targeted unresolved SCI-specific lipid, complement, and
extracellular-protease gaps while preserving direct molecular,
receptor-proximal, and downstream/function layers separately.

## Additions

- `M24A-E146` / `M24A-B008-EVID-001`: LTB4 release and post-traumatic
  polymorphonuclear infiltration functional context in rat SCI.
- `M24A-E147` / `M24A-B008-EVID-002`: direct human iC3b-CR3 alpha-I structural
  binding comparator for the processed C3b fragment.
- `M24A-E148` / `M24A-B008-EVID-003`: rat SCI C3/CR3 pathway association with
  SCI-evoked neuropathic pain and dorsal-horn NR2B context.
- `M24A-E149` / `M24A-B008-EVID-004`: mouse SCI MMP2/MMP9 apoptotic and
  blood-spinal-cord-barrier/vascular-inflammatory pathway function.

## Promotions and limits

- `M24A-Q0062` is now `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`: BLT1 and LTB4
  release/PMN functional context are supported; BLT2-specific SCI receptor
  causality remains unresolved.
- `M24A-Q0063` is now `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`: MMP2/MMP9 SCI
  pathway/function is supported; exact MMP-to-receptor activation remains
  unresolved.
- `M24A-Q0069` is now `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`: iC3b-CR3 direct
  structural comparator and rat SCI C3/CR3 functional association are
  supported; intact C3-to-CR3 activation and endogenous SCI fragment identity
  remain unresolved.
- `M24A-Q0070` and the intact C3-to-CR4 boundary were not promoted.
- No direct molecular receptor interaction was inferred from the LTB4 release,
  C3/CR3 expression association, or MMP pathway/function studies.

## Validation disposition

- Four new edges and four new evidence records were added.
- The integrated registers now contain 149 edges, 198 evidence records, 31
  explicit no-evidence boundaries, 167 edge/evidence associations, and 189
  saturation-matrix rows.
- Independent PostgreSQL checks passed in a fresh temporary database on port
  `55433`: zero unsupported edges, preserved layer labels for all four new
  edges, and 31 explicit boundaries.

## Search boundary

Primary sources validated rat SCI LTB4 release/PMN association, human iC3b-CR3
fragment binding, rat SCI C3/CR3 functional association, and mouse SCI MMP2/MMP9
pathway effects. The search did not establish BLT2-specific SCI causality,
C5aR2-specific SCI causality, intact C3-to-CR3 or C3-to-CR4 SCI activation, or
an exact MMP2/MMP9-to-receptor molecular edge.
