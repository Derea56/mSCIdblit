# mSCIdblit v1.9.90

## Gap-driven primary-literature expansion

This release adds two composite Notch signaling routes:

- DLL4 > NOTCH4 > NICD > RBPJ/CSL > HES1 gene expression
- JAG1 > NOTCH3 > NICD > RBPJ/CSL > HES1 gene expression

The DLL4 route is supported by primary human endothelial-cell evidence
(PMID:12814948). The JAG1 route is supported by primary ovarian-cancer
juxtacrine signaling evidence (PMID:18632624; PMID:23530123). The ligand,
receptor, and measured output evidence is retained with its original model
context. NICD processing, the RBPJ/CSL relay, and HES1 linkage are completed
using shared canonical Notch graph evidence; these are therefore composite
evidence routes rather than single-study causal chains.

Causal status, graph traversal, SCI transfer, and database confidence scores
remain unasserted.

No graph edges or confidence scores are added.

## Release counts

- Route evidence records: 19,493 -> 19,495
- Strict full-route annotations: 75 -> 77
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 2

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion185`.
