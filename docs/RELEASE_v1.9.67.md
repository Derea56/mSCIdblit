# mSCIdblit v1.9.67

## Gap-driven primary-literature expansion

This release adds three cytokine-to-target-gene route annotations:

- IL-4 > IL4RA:IL2RG > JAK1/JAK3 > STAT6 > CCL26
- IL-21 > IL21R:IL2RG > JAK1/JAK3 > STAT3 > BCL6
- TSLP > TSLPR/IL7RA > JAK2 > STAT5 > BCL2

The IL-4 route is supported by primary keratinocyte work showing that IL-4
induces CCL26 through a JAK/STAT6-dependent proximal promoter element
(PMID:22226123). The IL-21 route is supported by primary human B-cell work
showing IL-21-dependent BCL6 expression in a STAT3-competent context under
CD40L co-stimulation (PMID:20048285; PMCID:PMC2812540). The TSLP route is
supported by primary CD8 T-cell work showing TSLP-induced STAT5 activation and
Bcl-2 induction, joined to primary TSLP receptor/JAK1-JAK2-STAT5 work
(PMID:19017958; PMCID:PMC2735224; PMID:20974963; PMCID:PMC2984176).

These annotations preserve the model, co-stimulation, receptor-subtype, and
assay boundaries of the source studies. The IL-21 entry intentionally does not
assert a new direct STAT3-to-BCL6 graph edge; it records a STAT3-dependent
ligand-to-output bridge. None of the routes asserts SCI transfer, causal graph
traversal, or a database confidence score.

The broader downstream curation queue still contains 3,331 records. Candidate
list exhaustion remains a workflow boundary, not evidence that signaling
literature is saturated. Continued work should search unresolved output tiers,
receptor-subtype-specific studies, and target-gene evidence that can be joined
without overstating the underlying experiments.

## Release counts

- Route evidence records: 19,431 -> 19,434
- Strict full-route annotations: 36 -> 39
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 3

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion162`.
