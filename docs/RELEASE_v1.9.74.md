# mSCIdblit v1.9.74

## Gap-driven primary-literature expansion

This release adds three named downstream routes to existing receptor and
transcription-factor scaffolds:

- IL-5 > IL5RA:CSF2RB > JAK2 > STAT5 > CISH
- IL-4 > IL4RA:IL2RG > JAK1/JAK3 > STAT6 > Chil3/Ym1
- IL-31 > IL31RA:OSMRbeta > JAK1 > STAT3 > SOCS3

The routes are supported by primary studies reporting cytokine-dependent
kinase/STAT activation and target-gene expression or promoter response
(PMID:11245630; PMID:12215441; PMID:26306032). They remain evidence-layer
routes rather than causal graph traversals, and model-specific receptor,
cell-type and comparator limitations are preserved. No database confidence
score is added.

## Release counts

- Route evidence records: 19,448 -> 19,451
- Strict full-route annotations: 48 -> 51
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 3

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion169`.
