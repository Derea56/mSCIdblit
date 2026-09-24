# mSCIdblit release v1.9.287

This release adds four primary-literature evidence routes across TNC/tenascin-C,
norepinephrine, GABA, and acetylcholine. The routes include
TNC→TLR4→MAPK/NF-κB→IL6, norepinephrine→α1A-adrenergic receptor→PKA→CREB→cFos,
GABA→GABA-A receptor→MAPK/CREB→BDNF, and
acetylcholine→M1 muscarinic receptor→ERK/EGR1→AChE output.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-neuro-injury-gap-450`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion450/`

All four rows retain primary locators, explicit limitations,
`causal_status=not_asserted`, and `traversal_status=evidence_route_not_causal`.
No graph edges or database confidence scores were created. The acetylcholine
route remains a functional-output route because the current graph lacks a clean
ACHE target-gene node; the other three routes retain target-gene nodes.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,215
- Route nodes: 2,463,815
- Route edges: 2,271,778
- Full-sequence curation queue: 15,406
- Literature-expansion annotations: 22,101
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors. The remaining warning concerns
legacy evidence sources without stable locators and is unchanged from the
previous release.
