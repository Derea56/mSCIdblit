# mSCIdblit v1.9.66

## Gap-driven primary-literature expansion

This release adds two cytokine-to-STAT5 target-gene annotations:

- IL-15 > IL2RB:IL2RG > JAK1/JAK3 > STAT5 > BCL2
- TPO > MPL > JAK2 > STAT5 > CISH

The IL-15 route is supported by a primary effector-CD8 study showing that
IL-15 and STAT5 are required for Bcl-2 expression and maintenance of effector
cells (PMID:20644163; PMCID:PMC2991082). The TPO route is supported by primary
megakaryocytic progenitor work showing TPO-dependent STAT5 redistribution to
canonical target loci, including Cish (PMID:26702099; PMCID:PMC4801948).
The routes retain lineage, chromatin, and functional-dependency boundaries;
they do not imply universal outputs or direct promoter mechanisms in every
cell type.

The broader downstream curation queue still contains 3,331 records. Candidate
list exhaustion remains a workflow boundary, not evidence that signaling
literature is saturated. Continued work should search unresolved output tiers,
receptor-subtype-specific studies, and target-gene evidence that can be joined
without overstating the underlying experiments.

All additions remain evidence-layer routes: causal status is not asserted,
graph traversal is not asserted, and no database confidence score is created.

## Release counts

- Route evidence records: 19,429 -> 19,431
- Strict full-route annotations: 34 -> 36
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 2

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion161`.
