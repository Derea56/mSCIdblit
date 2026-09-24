# mSCIdblit release v1.9.289

This release adds four primary-literature evidence routes for canonical WNT3A
signaling across FZD2, FZD4, FZD7, and the reconstituted FZD8:LRP6 receptor
context. The routes retain WNT3A→Frizzled/LRP6→β-catenin/TCF signaling with
MYC or CCND1 gene-expression outputs.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-wnt-canonical-gap-456`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion456/`

The routes use primary locators including PMID:20093360, PMID:21975427,
PMID:25605717, PMID:26798342, PMID:28733458, and PMID:31235524. They retain
`causal_status=not_asserted` and `traversal_status=evidence_route_not_causal`.
Receptor-to-relay, relay-to-TCF, and TCF-to-target handoffs remain explicitly
unasserted; no graph edges or database confidence scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,222
- Route nodes: 2,463,848
- Route edges: 2,271,804
- Full-sequence curation queue: 15,413
- Literature-expansion annotations: 22,108
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors. The remaining warning concerns
legacy evidence sources without stable locators and is unchanged from the
previous release.
