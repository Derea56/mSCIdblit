# mSCIdblit v1.9.75

## Gap-driven primary-literature expansion

This release upgrades three existing partial route annotations with named
intracellular continuations and target-gene outputs:

- BAFF > TACI > MYD88 > NF-kB > AICDA
- TWEAK > Fn14 > TRAF2:cIAP1/2 > NF-kappaB p50/p65 > CXCL8/IL8
- LEP > LEPR > LEPRb pY1138 > STAT3 > SOCS3

The routes are supported by primary studies reporting receptor engagement,
intracellular signaling and target-gene or transcriptional outputs
(PMID:20676093; PMID:22081603; PMID:10514492; PMID:11018044; PMID:15208705).
They remain evidence-layer routes rather than causal graph traversals. The
route annotations preserve mixed-ligand, receptor-isoform, oligomerization,
cell-type and model-specific limitations. No database confidence score is
added.

## Release counts

- Route evidence records: 19,451 -> 19,454
- Strict full-route annotations: 51 -> 54
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 3

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion170`.
