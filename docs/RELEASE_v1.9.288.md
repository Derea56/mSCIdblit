# mSCIdblit release v1.9.288

This release adds three primary-literature evidence routes across glutamate,
decorin, and ATP. The additions preserve glutamate→NMDA receptor→ERK→CREB→cFos
expression, decorin→TLR2→MyD88/MAPK/NF-κB inflammatory output, and
ATP→P2X7→NF-κB/AP-1→IL-8 output.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-glutamate-matrix-gap-453`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion453/`

All three rows retain primary locators, explicit limitations,
`causal_status=not_asserted`, and `traversal_status=evidence_route_not_causal`.
No graph edges or database confidence scores were created. The decorin and ATP
routes remain functional-output routes because their source-supported outputs do
not map to a single clean terminal target-gene node in the current graph.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,218
- Route nodes: 2,463,828
- Route edges: 2,271,788
- Full-sequence curation queue: 15,409
- Literature-expansion annotations: 22,104
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors. The remaining warning concerns
legacy evidence sources without stable locators and is unchanged from the
previous release.
