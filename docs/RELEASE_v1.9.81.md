# mSCIdblit v1.9.81

## Gap-driven primary-literature expansion

This release adds four evidence-layer routes for soluble biglycan signaling:

- Biglycan > TLR2 > MyD88/p38/ERK/NF-kappaB > TNF gene
- Biglycan > TLR2 > MyD88/p38/ERK/NF-kappaB > CXCL2 gene
- Biglycan > TLR4 > MyD88/p38/ERK/NF-kappaB > TNF gene
- Biglycan > TLR4 > MyD88/p38/ERK/NF-kappaB > CXCL2 gene

The routes are supported by primary macrophage and receptor-perturbation
evidence reporting biglycan interaction with TLR2/TLR4, MyD88-dependent
p38/ERK/NF-kappaB signaling, and TNF/MIP-2 induction (PMID:16025156).
MIP-2 is represented by the CXCL2 gene node.

The routes remain evidence-layer annotations: they are non-causal,
non-traversable and carry no database confidence score. The primary study
supports convergent TLR2/TLR4 signaling rather than receptor exclusivity; the
receptor-proximal relay and NF-kappaB target links are composite evidence
annotations. No new graph edges are asserted by this release.

## Release counts

- Route evidence records: 19,469 -> 19,473
- Strict full-route annotations: 67 -> 71
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 4

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion176`.
