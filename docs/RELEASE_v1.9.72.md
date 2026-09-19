# mSCIdblit v1.9.72

## Gap-driven primary-literature expansion

This release adds an IL-7 route to a named transcriptional output:

- IL-7 > IL7RA:IL2RG > JAK1 > STAT5 > BCL2

The route joins the existing IL-7 receptor/JAK1/STAT5 scaffold and STAT5→BCL2
target edge with primary evidence showing IL-7-associated BCL2 expression and
STAT5 DNA-binding at BCL2 promoter-enhancer elements (PMID:11675351), while
retaining the shared IL-7/IL-15 comparator context. No causal edge or database
confidence score is added.

## Release counts

- Route evidence records: 19,446 -> 19,447
- Strict full-route annotations: 47 -> 48
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 1

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion167`.
