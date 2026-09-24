# mSCIdblit release v1.9.295

This release adds four primary-literature evidence routes for IL-21 signaling:
IL-21→IL-21 receptor→JAK1/JAK3→STAT3→PRDM1/Blimp-1, XBP1, IL2RA/CD25, and BCL6
target-gene expression. The routes preserve the intracellular continuation and
transcription-factor layers while keeping unresolved handoffs explicit for
mSCS route-plausibility evaluation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-il21-stat3-gap-474`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion474/`

The routes retain PMID:23325890, PMID:22491065, PMID:20048285,
PMID:24159173, PMID:20142429, and PMID:20142430, with
`causal_status=not_asserted` and `traversal_status=evidence_route_not_causal`.
Receptor-to-relay, relay-to-STAT3, and STAT3-to-target handoffs remain
explicitly unasserted; no graph edges or database confidence scores were
created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,238
- Route nodes: 2,463,927
- Route edges: 2,271,867
- Full-sequence curation queue: 15,418
- Literature-expansion annotations: 22,124
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors, and all compressed route artifacts
passed gzip integrity checks. The remaining warning concerns legacy evidence
sources without stable locators and is unchanged from prior releases.
