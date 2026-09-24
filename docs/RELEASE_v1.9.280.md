# mSCIdblit release v1.9.280

This release adds 72 additional source-linked composed full-sequence route
records across 12 ligand labels. These routes extend the all-ligand evidence
overlay when the relay, TF, and target observations do not share one source
queue but at least one component pair shares a public literature locator.

The records are separated into two evidence tiers: 16 routes with two
pairwise locator overlaps and 56 routes with one. They are available to mSCS
as lower-tier plausibility candidates; they do not assert a single-paper
causal chain.

Graph identifier: `module20_24_mechanism_graph:2026-09-24-pairwise-source-overlap-queue-425`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion425/`

All new rows use
`ligand>receptor>intracellular>TF>target_gene_expression`, retain
`causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`, and leave unresolved
intracellular-to-TF and TF-to-target handoffs explicit unless an existing graph
edge is present. No graph edge or database confidence score is created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 587,704
- Route nodes: 2,461,314
- Route edges: 2,269,776
- Full-sequence curation queue: 15,388
- Literature-expansion annotations: 21,590
- Unique ligand candidates in queue: 1,862

Graph validation passed with no errors; the retained warning concerns evidence
sources without stable public locators. The queue remains a curation worklist,
not a confidence layer.
