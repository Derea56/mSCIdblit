# mSCIdblit release v1.9.300

This release adds three primary-literature evidence routes for IFN-gamma
signaling through IFNGR and JAK1 to STAT1-associated IRF1, GBP2, and CXCL9
target-gene outputs. The routes preserve the intracellular continuation and
transcription-factor layers while keeping unresolved handoffs explicit for
mSCS route-plausibility evaluation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-ifng-stat1-489`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion489/`

The routes retain PMID:19929594, PMID:7645205, PMID:17293456, PMID:20585034,
and the associated primary full-text records, with
`causal_status=not_asserted` and `traversal_status=evidence_route_not_causal`.
The IFN-gamma→IFNGR and IFNGR→JAK1 layers are linked to existing graph
evidence; the JAK1-to-STAT1 handoffs remain unasserted. No graph edges or
database confidence scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,253
- Route nodes: 2,464,002
- Route edges: 2,271,927
- Full-sequence curation queue: 15,420
- Literature-expansion annotations: 22,139
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors, and all compressed route artifacts
passed gzip integrity checks. The remaining warning concerns legacy evidence
sources without stable locators and is unchanged from prior releases.
