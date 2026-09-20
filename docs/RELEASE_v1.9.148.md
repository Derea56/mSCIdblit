# mSCIdblit release v1.9.148

## Public signaling-database comparison

This release adds a reproducible, bundle-native comparison between the
`literature-expansion242` mechanism graph and the frozen public-resource
snapshot `mscs_phase2_external_snapshot_2026-08-05`.

The comparison covers CellChatDB mouse, NicheNet neutral v1, LIANA mouse
consensus, and the local master ligand–receptor union. Complexes are compared
using component-normalized identifiers before public-only candidates are
reported.

The comparison does not create graph edges, causal claims, or confidence
scores. Public-only ligand–receptor pairs are emitted as review candidates in
`public_only_lr_candidates.tsv`.

Key mSCIdblit inventory values:

- 5,931 ligand–receptor edge rows
- 5,680 component-normalized ligand–receptor pairs
- 20,196 route-evidence records
- 438 distinct intracellular continuation labels
- 61 distinct transcription-factor labels
- 110 distinct target-gene labels
- 1,987 distinct output labels
- 19,427 contextualized route-evidence records

The comparison report and machine-readable summary are in
`data/processed/public_database_comparison_v2/`.

Reproduce with:

```bash
python3 scripts/compare_release_public_databases_v2.py
```
