# mSCIdblit release v1.9.294

This release adds four primary-literature evidence routes for IL-4 signaling:
IL-4→IL-4 receptor→JAK1/JAK3→STAT6→ARG1, CCL17/TARC, GATA3, and CHIL3/Ym1
target-gene expression. The routes preserve the intracellular continuation and
transcription-factor layers while keeping unresolved handoffs explicit for
mSCS route-plausibility evaluation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-il4-stat6-gap-471`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion471/`

The routes retain PMID:11160269, PMID:16810739, PMID:11283251, and PMID:19567879,
with `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Receptor-to-relay,
relay-to-STAT6, and STAT6-to-target handoffs remain explicitly unasserted; no
graph edges or database confidence scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,234
- Route nodes: 2,463,907
- Route edges: 2,271,851
- Full-sequence curation queue: 15,418
- Literature-expansion annotations: 22,120
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors, and all compressed route artifacts
passed gzip integrity checks. The remaining warning concerns legacy evidence
sources without stable locators and is unchanged from prior releases.
