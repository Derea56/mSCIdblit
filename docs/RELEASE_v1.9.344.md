# mSCIdblit release v1.9.344

Release ID: `module20_24_mechanism_graph:2026-09-25-receptor-shared-route-promotions-582`

This release adds 876 evidence-route records across 128 ligands by reusing
downstream relay/transcription-factor signatures observed at the same receptor
in other primary-evidence routes. The additions comprise 753 functional-output
routes and 123 target-gene routes, representing 358 new deduplicated
ligand-receptor-intermediate-TF signatures. These records are explicitly marked
as receptor-shared compositions: ligand-specific receptor-to-relay,
relay-to-TF, and endpoint handoffs remain unasserted for mSCS evaluation.

This is an evidence-layer composition. No graph edge, causal assertion,
confidence score, or missing-link assertion was created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 594,614 -> 595,490
- Literature-expansion rows: 28,500 -> 29,376
- Full-sequence curation candidates: 15,139 -> 15,446
- Unique ligands in the curation queue: 1,863 -> 1,867
- P1 review candidates: 9,306 -> 9,617
- Full target-gene ligands: 163 (unchanged)
- Full functional-output ligands: 110 -> 166
- Partial downstream ligands: 1,533 -> 1,477

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion582/`
- `scripts/build_receptor_shared_route_promotions.py`
- `docs/RELEASE_v1.9.344.md`
