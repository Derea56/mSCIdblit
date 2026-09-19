# mSCIdblit v1.9.88

## Gap-driven primary-literature expansion

This release adds three IL2 receptor-to-target-gene evidence routes using
STAT5 as the transcription-factor layer:

- IL2 > IL2RA:IL2RB:IL2RG > JAK1/JAK3 > STAT5 > CISH transcription
- IL2 > IL2RA:IL2RB:IL2RG > JAK1/JAK3 > STAT5 > MYC transcription
- IL2 > IL2RA:IL2RB:IL2RG > JAK1/JAK3 > STAT5 > IL9 transcription

The routes combine primary receptor-proximal IL2/JAK/STAT5 studies with
primary target-locus studies: CISH (PMID:9129017; PMCID:PMC109171), MYC
(PMID:36427325; PMCID:PMC9844264), and IL9 (PMID:34348976;
PMCID:PMC8387395). They are retained as composite evidence routes, with
model-specific limitations recorded in the route evidence rather than
asserted as uninterrupted causal chains.

These remain evidence-layer annotations: causal status, graph traversal, SCI
transfer, and database confidence scores are unasserted. No graph edges or
confidence scores are added.

## Release counts

- Route evidence records: 19,487 -> 19,490
- Strict full-route annotations: 72 -> 75
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 3

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion183`.
