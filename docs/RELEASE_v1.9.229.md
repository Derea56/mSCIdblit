# mSCIdblit release v1.9.229

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-il4-jak3-stat6-347`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion347/`

## IL-4 type-I receptor JAK3/STAT6 route expansion

This release adds five evidence-layer route annotations for the parallel JAK3
branch of the existing IL-4 type-I receptor route:

- IL-4 → IL4RA:IL2RG → JAK3 → STAT6 → GATA3 expression
- IL-4 → IL4RA:IL2RG → JAK3 → STAT6 → ARG1 expression
- IL-4 → IL4RA:IL2RG → JAK3 → STAT6 → CCL26 expression
- IL-4 → IL4RA:IL2RG → JAK3 → STAT6 → RETNLA expression
- IL-4 → IL4RA:IL2RG → JAK3 → STAT6 → CHIL3 expression

The new rows complement the previously curated JAK1 branch with the same five
STAT6 target-gene alternatives. Primary receptor/JAK and target-gene studies
support the component layers, while the direct JAK3-to-STAT6 handoff remains
an evidence-layer gap. No causal graph edge or database confidence score is
created.

Primary locators retained in the new rows include PMID:9492265,
PMID:8887542, PMID:20956546, PMCID:PMC2964576, PMID:15922518,
DOI:10.1016/j.gene.2005.04.004, PMID:22226123, PMID:12574343, and
PMID:12215441.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,064 |
| Literature-expansion annotations | 396 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,372 |
| Normalized route edges | 1,275,341 |

The release validator passed with zero errors; the existing stable-locator
warning remains. The mSCS import and focused route-test verification are
recorded with the release handoff.
