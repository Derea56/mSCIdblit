# mSCIdblit release v1.9.292

This release adds two primary-literature evidence routes for CNTF signaling:
CNTF→CNTFR-alpha/gp130/LIFR→JAK/STAT3→SOCS3 and
CNTF→CNTFR-alpha/gp130/LIFR→JAK/STAT3→CXCL10. The routes preserve the
receptor-associated JAK/STAT relay, STAT3-family transcriptional layer, and
target-gene expression outputs.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-cntf-stat3-gap-465`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion465/`

The routes retain PMID:19272793 and PMID:32780864,
`causal_status=not_asserted`, and `traversal_status=evidence_route_not_causal`.
Receptor-to-relay, relay-to-STAT3, and STAT3-to-target handoffs remain
explicitly unasserted; no graph edges or database confidence scores were
created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,226
- Route nodes: 2,463,867
- Route edges: 2,271,819
- Full-sequence curation queue: 15,416
- Literature-expansion annotations: 22,112
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors. The remaining warning concerns
legacy evidence sources without stable locators and is unchanged from prior
releases.
