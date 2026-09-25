# mSCIdblit release v1.9.329

Release ID: `module20_24_mechanism_graph:2026-09-25-all-ligand-route-promotion-queue-549`

This release adds a second source-linked all-ligand promotion tranche with 412
literature-expansion records across 13 ligands: IL-13, IL-22, CXCL12, IL-12B/
IL-23A, IL-3, IL-31, IL-6, IL-20, IL-24, IL-5, IL-21, LPA, and PGE2.

All 412 records retain explicit intracellular-continuation, transcription-
factor, and target-gene layers. The records are primarily composed evidence
routes: 411 retain unresolved direct handoffs between layers and one is a
source-overlap composition. No graph edges, causal assertions, or confidence
scores are created; mSCS should evaluate route plausibility from the retained
source evidence and missing-link fields.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 592,754 -> 593,166
- Literature-expansion rows: 26,640 -> 27,052
- Full-sequence curation candidates: 15,117 -> 15,118
- Unique ligands in the curation queue: 1,862 (unchanged)
- P1 review candidates: 9,306 (unchanged)

Role-aware coverage remains 150 full target-gene ligands, 110 full
functional-output ligands, 1,545 partial downstream ligands, and 808
ligand-receptor-only ligands. These are evidence-layer summaries, not
confidence scores or causal traversal permissions.

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion549/`
