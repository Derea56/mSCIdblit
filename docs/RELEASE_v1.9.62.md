# mSCIdblit v1.9.62

## Gap-driven primary-literature expansion

This release adds two source-linked route annotations that connect existing
receptor-proximal and STAT5 evidence to a BCL2L1 target-gene output:

- EPO > EPOR > JAK2 > STAT5 > BCL2L1
- TPO > MPL > JAK2/STAT5 > BCL2L1

The EPO route is supported by EPO-stimulated pSTAT5 occupancy and nascent
Bcl2l1 transcription in murine erythroid cells (PMID:28732065). The TPO route
is supported by TPO-induced Bcl-xL/BCL2L1 expression and STAT5/NF-kB-associated
promoter evidence in megakaryocytic systems (PMID:11756417). Species,
cell-type, cofactor, and assay boundaries remain explicit. These annotations
do not assert a STAT5-only mechanism for TPO or transfer either output to SCI
receiver cells.

The targeted gap-driven expansion candidate list is exhausted for this
discovery pass, but the broader downstream curation queue still contains 3,331
records. Neither queue exhaustion establishes literature saturation: these
queues report the state of the search and curation workflow, not whether all
signaling papers have been found. Further work should continue through
targeted searches of unresolved route tiers and newly identified target-gene
or functional-output studies.

All additions remain evidence-layer routes: causal status is not asserted,
graph traversal is not asserted, and no database confidence score is created.

## Release counts

- Route evidence records: 19,421 -> 19,423
- Strict full-route annotations: 26 -> 28
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 2

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion157`.
