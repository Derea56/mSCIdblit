# mSCIdblit release v1.9.333

Release ID: `module20_24_mechanism_graph:2026-09-25-optimized-alias-full-routes-queue-557`

This release adds three source-linked full-sequence routes for the `Il15`
ligand alias and optimizes the alias-promotion builder by indexing canonical
routes by ligand and receptor identity. The optimization changes execution
time only; its evidence and route-matching rules are unchanged. No graph
edges, causal assertions, or confidence scores were created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,203 -> 593,206
- Literature-expansion rows: 27,089 -> 27,092
- Full-sequence curation candidates: 15,125 (unchanged)
- Unique ligands in the curation queue: 1,862 (unchanged)
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 154 (unchanged)
- Partial downstream ligands: 1,541 (unchanged)

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion557/`
- `scripts/build_primary_alias_target_route_batch.py`
