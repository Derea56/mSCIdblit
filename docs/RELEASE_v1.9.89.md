# mSCIdblit v1.9.89

## Gap-driven primary-literature expansion

This release adds three IL17A receptor-proximal output routes:

- IL17A > IL17RA:IL17RC > ACT1/CIKS > DEFB4 gene expression
- IL17A > IL17RA:IL17RC > ACT1/CIKS > CXCL8/IL-8 release
- IL17A > IL17RA:IL17RC > ACT1/CIKS > CSF3/G-CSF secretion

The routes preserve measured outputs from primary studies (PMID:15322213,
PMID:11692108, and PMID:15972674) while retaining the missing TF and terminal
target-gene layers. They are composite evidence routes: causal status, graph
traversal, SCI transfer, and database confidence scores remain unasserted.

No graph edges or confidence scores are added.

## Release counts

- Route evidence records: 19,490 -> 19,493
- Strict full-route annotations: 75 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 3

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion184`.
