# mSCIdblit v1.9.76

## Gap-driven primary-literature expansion

This release upgrades two existing cytokine route annotations with named
intracellular continuations and target-gene outputs:

- IL-21 > IL21R:IL2RG > JAK1/JAK3 > STAT3 > SOCS3
- IL-10 > IL10RA:IL10RB > JAK1/TYK2 > STAT3 > SOCS3

The routes are supported by primary studies reporting receptor-dependent
JAK/STAT signaling and cytokine-associated SOCS3 induction
(PMID:19608866; PMID:35469842; PMID:8662928; PMID:10433356; PMID:11034314).
They remain evidence-layer routes rather than causal graph traversals. Cell
state, receptor-reconstitution, model and direct-promoter-occupancy limits
are preserved. No database confidence score is added.

## Release counts

- Route evidence records: 19,454 -> 19,456
- Strict full-route annotations: 54 -> 56
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 2

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion171`.
