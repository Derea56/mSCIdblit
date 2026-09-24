# mSCIdblit release v1.9.307

This release adds an all-ligand route-coverage index for mSCS route selection.
The index is derived from the existing graph route-evidence and literature-
expansion tables; no biological edge or literature annotation was added in
this release.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-all-ligand-route-coverage-508`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion508/`

New files:

- `mechanism_ligand_route_coverage.tsv.gz`
- `ligand_route_coverage_summary.json`
- `ligand_route_coverage_release_summary.json`

The coverage index contains one row per semantically valid ligand node and
reports LR-pair, intracellular, TF, functional-output, target-gene, and full-
route counts. It is an evidence-layer index only: it does not assign
confidence, authorize causal traversal, or create graph edges.

Coverage counts:

- Ligand nodes indexed: 2,613
- Full target-gene route: 59
- Full intracellular–TF functional-output route: 167
- Partial downstream route: 1,583
- Ligand–receptor-only: 804

Inherited bundle counts remain unchanged from v1.9.306:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 591,165
- Route nodes: 2,478,543
- Route edges: 2,283,559
- Full-sequence curation queue: 15,452
- Literature-expansion annotations: 25,051

The graph validator and gzip integrity checks passed. The unchanged validator
warning concerning legacy evidence sources without stable locators remains.
