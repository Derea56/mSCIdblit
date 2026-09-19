# mSCIdblit v1.9.61

## Gap-driven primary-literature expansion

This release adds four source-linked route annotations to the Module 20B-24B
mechanism evidence snapshot. The additions target cytokine routes that already
had receptor, STAT, or target-gene evidence but lacked a documented endpoint
or receptor-proximal relay.

Added evidence-layer routes:

- IL-6 > IL-6R-gp130 > JAK1 > STAT3 > SOCS3
- IL-7 > IL7RA:IL2RG > JAK1/JAK3 > STAT5 > BCL2
- IL-22 > IL22RA1:IL10RB > STAT3 > SOCS3 (intracellular relay remains
  explicitly unresolved)
- IL-31 > IL31RA:OSMRbeta > JAK1 > STAT3 > SOCS3

Primary locators include PMID:16718380, PMID:20644163, PMID:15120652, and
PMID:26306032. These annotations preserve the source study's species,
cell-type, receptor-complex, stimulation, feedback, and assay qualifiers. The
IL-22 route is intentionally retained as a partial evidence route because the
current graph does not materialize a receptor-specific JAK/TYK2 edge for that
branch. All additions remain evidence-layer routes: causal status is not
asserted, graph traversal is not asserted, and no database confidence score is
created.

## Release counts

- Route evidence records: 19,417 -> 19,421
- Strict full-route annotations: 23 -> 26
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 4

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion156`.

This targeted expansion does not establish literature saturation. An exhausted
candidate queue means that the current discovery pass has no unreviewed queue
records; it does not mean that every signaling paper has been found or that
all receptor-to-output routes are resolved.
