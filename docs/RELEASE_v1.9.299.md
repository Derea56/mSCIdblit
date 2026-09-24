# mSCIdblit release v1.9.299

This release adds five primary-literature evidence routes for type-I
interferon signaling through IFNAR and JAK1 to ISGF3- or STAT1-associated
target-gene outputs: IFIT1, OAS1, ISG15, MX2, and IRF7. The routes preserve the
intracellular continuation and transcription-factor layers while keeping
unresolved handoffs explicit for mSCS route-plausibility evaluation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-type1-ifn-isgf3-486`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion486/`

The routes retain PMID:17507495, PMID:31231385, PMID:12509459, and PMID:19551150,
with `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. IFIT1, OAS1, and ISG15 use the
existing ISGF3 target evidence; MX2 and IRF7 use the existing STAT1 target
evidence. The JAK1-to-TF handoffs remain unasserted. No graph edges or database
confidence scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,250
- Route nodes: 2,463,987
- Route edges: 2,271,915
- Full-sequence curation queue: 15,420
- Literature-expansion annotations: 22,136
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors, and all compressed route artifacts
passed gzip integrity checks. The remaining warning concerns legacy evidence
sources without stable locators and is unchanged from prior releases.
