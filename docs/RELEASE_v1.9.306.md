# mSCIdblit release v1.9.306

This release adds 2,198 audited full-sequence evidence-route annotations
across 11 ligand labels. The tranche contains 2,196 shared-source full routes
and two pairwise-source-overlap routes. These annotations make independently
source-linked intracellular, transcription-factor, and target-gene layers
addressable to mSCS while preserving unresolved handoffs for confidence
evaluation and later curation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-all-ligand-full-sequence-507`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion507/`

The annotations are evidence-only. They retain
`causal_status=not_asserted` and `traversal_status=evidence_route_not_causal`;
no graph edges or database confidence scores were created. Receptor aliases,
intracellular component labels, named transcriptional programs, and generic
readouts were excluded from the ligand and target-gene tiers where they would
otherwise create semantic false positives. Legitimate gene aliases, including
parenthesized aliases, remain eligible target endpoints.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 591,165
- Route nodes: 2,478,543
- Route edges: 2,283,559
- Full-sequence curation queue: 15,452
- Literature-expansion annotations: 25,051
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors. The route nodes, route edges,
signaling-route evidence, and full-sequence curation queue exports passed gzip
integrity checks. The validator warning concerning legacy evidence sources
without stable locators is unchanged from prior releases.
