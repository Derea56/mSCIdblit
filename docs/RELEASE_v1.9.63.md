# mSCIdblit v1.9.63

## Gap-driven primary-literature expansion

This release adds three source-linked route annotations that connect existing
receptor-proximal and STAT5 evidence to terminal target-gene outputs:

- GH > GHR > JAK2 > STAT5 > CISH
- Prolactin > PRLR > JAK2 > STAT5 > CISH
- GM-CSF > CSF2RA:CSF2RB > JAK2 > STAT5 > BCL2

The GH route is supported by primary studies reporting GH-dependent STAT5
occupancy near Cish and Cish transcription in mouse liver (PMID:25088465;
PMCID:PMC6283433). The prolactin route is supported by primary studies
reporting prolactin-induced STAT5 recruitment at the CISH promoter and
prolactin-responsive CISH transcription in mammary or breast epithelial
systems (PMID:7925280; PMCID:PMC5313097). The GM-CSF route is supported by a
primary neural-progenitor study linking GM-CSF/JAK/STAT5 signaling to Bcl2
expression and survival-associated output (PMID:21052840). Species, cell-type,
cofactor, chromatin, and assay boundaries remain explicit. These annotations
do not transfer any output to SCI receiver cells or assert that the reused
STAT5-target edge is universal in every source context.

The targeted gap-driven expansion candidate list remains exhausted for this
discovery pass, but the broader downstream curation queue still contains
3,331 records. Neither queue exhaustion establishes literature saturation:
these queues report the state of the search and curation workflow, not whether
all signaling papers have been found. Further work should continue through
targeted searches of unresolved route tiers and newly identified target-gene
or functional-output studies.

All additions remain evidence-layer routes: causal status is not asserted,
graph traversal is not asserted, and no database confidence score is created.

## Release counts

- Route evidence records: 19,423 -> 19,426
- Strict full-route annotations: 28 -> 31
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 3

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion158`.
