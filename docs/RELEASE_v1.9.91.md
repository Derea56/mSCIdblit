# mSCIdblit v1.9.91

## Gap-driven primary-literature expansion

This release adds five output-bearing composite routes from unresolved
receptor/downstream gaps:

- IL11 > IL11R-alpha:gp130 > STAT3-associated response > IL33 expression
- IL11 > IL11R-alpha:gp130 > STAT3-associated response > CCL20 expression/secretion
- IL11 > IL11R-alpha:gp130 > STAT3-associated response > CXCL8/IL-8 expression/secretion
- IL11 > IL11R-alpha:gp130 > STAT3-associated response > IL-6 expression/secretion
- BMP9/GDF2 > ACVRL1/ALK1 > SMAD1/5/8 > ID1 expression

The IL-11 routes use primary human fibroblast evidence showing early STAT3
phosphorylation and inflammatory transcriptional/secreted outputs
(PMID:36012165). The BMP9 route uses primary human pulmonary endothelial-cell
evidence showing ALK1-dependent SMAD1/5 phosphorylation and ID1 expression
(PMID:19366699). Missing kinase ordering, direct target-specific TF linkage,
and SCI transfer remain explicitly unresolved where the studies do not measure
them.

No graph edges or confidence scores are added.

## Release counts

- Route evidence records: 19,495 -> 19,500
- Strict full-route annotations: 77 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 5

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion186`.
