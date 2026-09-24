# mSCIdblit release v1.9.301

This release adds three primary-literature evidence routes for IL-1beta
signaling through IL1R1/IL1RAP, MyD88 and NF-kB-associated inflammatory
transcription to IL6, CCL20 and CXCL1 gene-expression outputs. The routes
preserve the intracellular continuation and transcription-factor layers while
keeping unresolved handoffs explicit for mSCS route-plausibility evaluation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-il1b-myd88-nfkb-492`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion492/`

The routes retain PMID:1644898, PMID:12528183, PMID:35384588, and the associated
primary full-text records, with `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. The IL-1beta→IL1R1/IL1RAP and
IL1R1/IL1RAP→MyD88 layers are linked to existing graph evidence; the
MyD88-to-NF-kB and NF-kB-to-target handoffs remain unasserted. No graph edges
or database confidence scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,256
- Route nodes: 2,464,017
- Route edges: 2,271,939
- Full-sequence curation queue: 15,420
- Literature-expansion annotations: 22,142
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors, and all compressed route artifacts
passed gzip integrity checks. The remaining warning concerns legacy evidence
sources without stable locators and is unchanged from prior releases.
