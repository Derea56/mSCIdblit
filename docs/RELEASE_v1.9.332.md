# mSCIdblit release v1.9.332

Release ID: `module20_24_mechanism_graph:2026-09-25-bounded-pacap-alias-routes-queue-555`

This release adds four bounded primary-evidence alias routes for PACAP
ligand labels. ADCYAP1/PACAP and PACAP-27/PACAP-38 are now linked to the
existing PAC1→GNAS or PAC1→GNAQ/GNA11→CREB→Bdnf promoter-IV evidence routes.
The alias promotions preserve unresolved handoffs and do not create graph
edges, causal assertions, or confidence scores.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,199 -> 593,203
- Literature-expansion rows: 27,085 -> 27,089
- Full-sequence curation candidates: 15,121 -> 15,125
- Unique ligands in the curation queue: 1,862 (unchanged)
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 152 -> 154
- Partial downstream ligands: 1,543 -> 1,541

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion555/`
- `scripts/build_primary_pacap_alias_routes.py`
