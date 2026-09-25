# mSCIdblit release v1.9.331

Release ID: `module20_24_mechanism_graph:2026-09-25-histamine-angii-primary-routes-queue-553`

This release adds three primary-literature evidence routes for canonical
ligands whose receptor-proximal signaling was already represented in the
graph: two histamine–HRH1 routes and one angiotensin-II–AGTR1 route. The
routes retain intracellular, transcription-factor, and target-gene layers,
while unresolved handoffs remain explicitly marked. No graph edges, causal
assertions, or confidence scores were created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,196 -> 593,199
- Literature-expansion rows: 27,082 -> 27,085
- Full-sequence curation candidates: 15,118 -> 15,121
- Unique ligands in the curation queue: 1,862 (unchanged)
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 150 -> 152
- Partial downstream ligands: 1,545 -> 1,543

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion553/`
- `scripts/build_primary_histamine_angii_routes.py`
