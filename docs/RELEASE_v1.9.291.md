# mSCIdblit release v1.9.291

This release adds one primary-literature evidence route for noncanonical
WNT5A→ROR2→JNK/AP-1 signaling with MMP13 expression as the functional output.
The route combines primary evidence for ROR2/FZD7-dependent Dishevelled/Rac and
AP-1 activation with primary evidence for c-Jun/ATF2 recruitment to the MMP13
promoter and JNK-dependent MMP13 expression.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-wnt5a-noncanonical-gap-462`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion462/`

The route retains PMID:20457807 and PMID:22128168,
`causal_status=not_asserted`, and `traversal_status=evidence_route_not_causal`.
The MMP13 target-gene node is unresolved in the current graph, so the route is
reported as `ligand>receptor>intracellular>TF>output`; no graph edges or
database confidence scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,224
- Route nodes: 2,463,857
- Route edges: 2,271,811
- Full-sequence curation queue: 15,415
- Literature-expansion annotations: 22,110
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors. The remaining warning concerns
legacy evidence sources without stable locators and is unchanged from prior
releases.
