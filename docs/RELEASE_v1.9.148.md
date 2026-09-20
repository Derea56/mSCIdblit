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

The public-only candidate inventory is split by evidence gate. Candidates with
a PMID/PMCID/DOI-like locator are copied to
`primary_evidence_review_queue.tsv`, but remain explicitly unverified until a
primary paper is checked for the exact interaction and context. No candidate
from this comparison is automatically promoted to an edge or route.

The first ranked batch is `primary_evidence_top25.tsv`. Its ranking is a
review-priority heuristic based on independent public-source support and
locator density; it is not a biological confidence score.

Reproduce with:

```bash
python3 scripts/compare_release_public_databases_v2.py
```
