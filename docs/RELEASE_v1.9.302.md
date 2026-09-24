# mSCIdblit release v1.9.302

This release adds three primary-literature evidence routes for IL-33/ST2
signaling: two routes to IL-5 and IL-13 protein production by mouse lung ILC2s
and one ERK/CREB-associated route to GZMC mRNA in mouse bone-marrow-derived mast
cells. The routes preserve intracellular and output layers while keeping
unresolved handoffs explicit for mSCS route-plausibility evaluation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-il33-st2-495`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion495/`

The routes retain PMID:22198948 and PMID:36342273 with
`causal_status=not_asserted` and `traversal_status=evidence_route_not_causal`.
The IL-33/ST2 receptor layer and measured intracellular/output evidence are
retained; intracellular-to-TF handoffs remain unasserted. Protein outputs are
not promoted to gene-expression outputs. No graph edges or database confidence
scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,259
- Route nodes: 2,464,032
- Route edges: 2,271,953
- Full-sequence curation queue: 15,422
- Literature-expansion annotations: 22,145
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors, and all compressed route artifacts
passed gzip integrity checks. The remaining warning concerns legacy evidence
sources without stable locators and is unchanged from prior releases.
