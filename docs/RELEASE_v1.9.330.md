# mSCIdblit release v1.9.330

Release ID: `module20_24_mechanism_graph:2026-09-25-all-ligand-route-promotion-queue-551`

This release adds a third source-linked all-ligand promotion tranche with 30
literature-expansion records across IL-21, PGE2, and CXCL12. Every record
retains explicit intracellular-continuation, transcription-factor, and
target-gene layers. Direct handoffs remain marked as unresolved where the
current graph does not assert them; no graph edges, causal assertions, or
confidence scores are created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,166 -> 593,196
- Literature-expansion rows: 27,052 -> 27,082
- Full-sequence curation candidates: 15,118 (unchanged)
- Unique ligands in the curation queue: 1,862 (unchanged)
- P1 review candidates: 9,306 (unchanged)

Role-aware coverage remains 150 full target-gene ligands, 110 full
functional-output ligands, 1,545 partial downstream ligands, and 808
ligand-receptor-only ligands. These are evidence-layer summaries, not
confidence scores or causal traversal permissions.

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion551/`
