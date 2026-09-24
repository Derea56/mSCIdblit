# mSCIdblit release v1.9.297

This release adds two primary-literature evidence routes for norepinephrine
signaling through the existing ADRB2/Gs/GNAS and CREB layers to measured BDNF
exon IV and exon VI transcript outputs in rat cortical astrocytes. The routes
retain the intracellular continuation and transcription-factor layers while
keeping unresolved handoffs explicit for mSCS route-plausibility evaluation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-norepi-adrb2-creb-480`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion480/`

The routes retain PMID:28983964, PMID:22593004, and PMID:17681645, with
`causal_status=not_asserted` and `traversal_status=evidence_route_not_causal`.
The norepinephrine→ADRB2 and ADRB2→GNAS layers are linked to existing graph
evidence; the intracellular-to-CREB and CREB-to-output handoffs remain
unasserted. The beta2 contribution is not treated as exclusive, and alternative
CREB-associated mechanisms are retained in the evidence description. No graph
edges or database confidence scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,244
- Route nodes: 2,463,957
- Route edges: 2,271,891
- Full-sequence curation queue: 15,419
- Literature-expansion annotations: 22,130
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors, and all compressed route artifacts
passed gzip integrity checks. The remaining warning concerns legacy evidence
sources without stable locators and is unchanged from prior releases.
