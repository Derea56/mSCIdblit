# mSCIdblit release v1.9.345

Release ID: `module20_24_mechanism_graph:2026-09-25-receptor-component-promotions-584`

This release adds 42 evidence-route records covering 11 new
ligand-receptor-intermediate-TF signatures across 11 ligands. The records
combine separately curated relay and transcription-factor components observed
at the same receptor, while retaining the ligand-specific endpoint evidence.
They are explicitly marked as two-source receptor component compositions; the
receptor-to-relay, relay-to-TF, and endpoint handoffs remain unasserted for
mSCS evaluation.

This is an evidence-layer composition. No graph edge, causal assertion,
confidence score, or missing-link assertion was created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 595,490 -> 595,532
- Literature-expansion rows: 29,376 -> 29,418
- Full-sequence curation candidates: 15,446 -> 15,457
- Unique ligands in the curation queue: 1,867 (unchanged)
- P1 review candidates: 9,617 -> 9,628
- Full target-gene ligands: 163 (unchanged)
- Full functional-output ligands: 166 -> 168
- Partial downstream ligands: 1,477 -> 1,475

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion584/`
- `scripts/build_receptor_component_route_promotions.py`
- `docs/RELEASE_v1.9.345.md`
