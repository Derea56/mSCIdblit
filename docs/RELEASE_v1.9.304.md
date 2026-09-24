# mSCIdblit release v1.9.304

This release adds five source-linked full-sequence evidence compositions for
HGF (cleaved two-chain form)→MET→GAB1→STAT3→TWIST1. The component observations
share a primary source queue and PMID:15218027; they remain evidence-only
compositions for mSCS route-plausibility evaluation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-source-linked-501`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion501/`

The routes retain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Intracellular-to-TF and
TF-to-target handoffs remain unasserted. No graph edges or database confidence
scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,266
- Route nodes: 2,464,067
- Route edges: 2,271,981
- Full-sequence curation queue: 15,427
- Literature-expansion annotations: 22,152
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors, and all compressed route artifacts
passed gzip integrity checks. The remaining warning concerns legacy evidence
sources without stable locators and is unchanged from prior releases.
