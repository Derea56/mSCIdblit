# mSCIdblit release v1.9.346

Release ID: `module20_24_mechanism_graph:2026-09-25-receptor-endpoint-promotions-586`

This release adds 738 endpoint-specific evidence-route records across 84
ligands. The ligand, receptor, and endpoint are retained from partial primary
evidence, while the intracellular relay/transcription-factor signature is
drawn from a curated route at the same receptor. The source index excludes
the broad prior promotion overlays, and every generated record retains the
receptor-shared limitation for mSCS evaluation.

The additions comprise 382 target-gene routes and 356 functional-output
routes. They complete endpoint-specific route representations even when the
same ligand-receptor-intermediate-TF signature already existed elsewhere in
the graph evidence corpus.

This is an evidence-layer composition. No graph edge, causal assertion,
confidence score, or missing-link assertion was created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 595,532 -> 596,270
- Literature-expansion rows: 29,418 -> 30,156
- Full-sequence curation candidates: 15,457 (unchanged after signature deduplication)
- Unique ligands in the curation queue: 1,867 (unchanged)
- P1 review candidates: 9,628 -> 9,725
- Full target-gene ligands: 163 (unchanged)
- Full functional-output ligands: 168 (unchanged)
- Partial downstream ligands: 1,475 (unchanged)

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion586/`
- `scripts/build_receptor_endpoint_route_promotions.py`
- `docs/RELEASE_v1.9.346.md`
