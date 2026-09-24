# mSCIdblit release v1.9.293

This release adds four primary-literature evidence routes for IL-2 signaling:
IL-2→IL-2 receptor→JAK1/JAK3→STAT5→CISH, FRA2/FOSL2, IFNG, and MYC target-gene
expression. The routes preserve the intracellular continuation and
transcription-factor layers while keeping unresolved handoffs explicit for
mSCS route-plausibility evaluation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-il2-stat5-gap-468`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion468/`

The routes retain PMID:9129017, PMID:24587342, PMID:15271977, and PMID:10679091,
with `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Receptor-to-relay,
relay-to-STAT5, and STAT5-to-target handoffs remain explicitly unasserted; no
graph edges or database confidence scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,230
- Route nodes: 2,463,887
- Route edges: 2,271,835
- Full-sequence curation queue: 15,417
- Literature-expansion annotations: 22,116
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors. The remaining warning concerns
legacy evidence sources without stable locators and is unchanged from prior
releases.
