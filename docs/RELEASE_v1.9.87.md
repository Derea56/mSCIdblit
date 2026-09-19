# mSCIdblit v1.9.87

## Gap-driven primary-literature expansion

This release adds six IL33–ST2:IL1RAP evidence routes from a primary human
skin mast-cell study:

- IL33 > ST2:IL1RAP > NF-kappa-B/p38-associated signaling > CCL1 release
- IL33 > ST2:IL1RAP > NF-kappa-B/p38-associated signaling > CCL2 release
- IL33 > ST2:IL1RAP > NF-kappa-B/p38-associated signaling > IL-5 release
- IL33 > ST2:IL1RAP > NF-kappa-B/p38-associated signaling > CXCL8/IL-8 release
- IL33 > ST2:IL1RAP > NF-kappa-B/p38-associated signaling > IL-13 release
- IL33 > ST2:IL1RAP > NF-kappa-B/p38-associated signaling > TNF-alpha release

The primary study measured NF-kappa-B pathway activation, p38/JNK
contributions, and cytokine protein outputs in human skin-derived mast cells
(PMID:33808264; PMCID:PMC8036466). These routes preserve the intracellular
evidence while leaving the terminal TF and target-gene layers unasserted.

These remain evidence-layer annotations: causal status, graph traversal, and
SCI transfer are unasserted. No graph edges or confidence scores are added.

## Release counts

- Route evidence records: 19,481 -> 19,487
- Strict full-route annotations: 72 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 6

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion182`.
