# mSCIdblit release v1.9.296

This release adds four primary-literature evidence routes for IL-6 signaling:
IL-6→IL-6R/gp130→JAK1→STAT3→CRP, HAMP/hepcidin, CEBPD, and SOCS3 target-gene
expression. The routes preserve the intracellular continuation and
transcription-factor layers while keeping unresolved handoffs explicit for
mSCS route-plausibility evaluation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-il6-stat3-gap-477`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion477/`

The routes retain PMID:35430542, PMID:17595889, PMID:16835372, PMID:9528783,
PMID:16718380, and PMID:12560330, with `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Receptor-to-relay,
relay-to-STAT3, and STAT3-to-target handoffs remain explicitly unasserted; no
graph edges or database confidence scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,242
- Route nodes: 2,463,947
- Route edges: 2,271,883
- Full-sequence curation queue: 15,418
- Literature-expansion annotations: 22,128
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors, and all compressed route artifacts
passed gzip integrity checks. The remaining warning concerns legacy evidence
sources without stable locators and is unchanged from prior releases.
