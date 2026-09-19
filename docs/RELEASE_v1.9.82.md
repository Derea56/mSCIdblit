# mSCIdblit v1.9.82

## Gap-driven primary-literature expansion

This release adds an intracellular/output evidence route for tenascin-C:

- Tenascin-C FBG > TLR4 > p38/JNK/NF-kappaB relay > cytokine output

Primary studies support tenascin-C FBG interaction with TLR4, MAPK/NF-kappaB
activation, and TNF, IL-6, and IL-8 secretion in human macrophage systems
(PMID:29150600; PMCID:PMC5338747). Because the evidence does not establish a
single terminal target-gene link, the route remains an output annotation.

Surfactant protein D was not promoted as a productive route: its primary
study reports TLR4/MD-2 binding with attenuation of LPS-induced NF-kappaB and
TNF responses (PMID:18990700), which is inhibitory/modulatory evidence.

All routes remain evidence-layer annotations: non-causal, non-traversable and
without database confidence scores. No new graph edges are asserted.

## Release counts

- Route evidence records: 19,473 -> 19,474
- Strict full-route annotations: 71 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 1

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion177`.
