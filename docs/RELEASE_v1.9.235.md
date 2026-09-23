# mSCIdblit release v1.9.235

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-il22-stat3-targets-353`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion353/`

## IL-22 STAT3 epithelial-output expansion

This release adds four evidence-layer routes for the IL-22 STAT3 output
branches:

- IL-22 → IL22RA1:IL10RB → JAK1 → STAT3 → MUC1 expression
- IL-22 → IL22RA1:IL10RB → JAK1 → STAT3 → LCN2 expression
- IL-22 → IL22RA1:IL10RB → TYK2 → STAT3 → MUC1 expression
- IL-22 → IL22RA1:IL10RB → TYK2 → STAT3 → LCN2 expression

Primary IL-22 receptor/STAT3 evidence and IL-22-induced epithelial MUC1/LCN2
output studies support the component layers. The receptor-to-JAK and
JAK-to-STAT3 handoffs remain explicitly unasserted because the current graph
does not contain IL-22-specific traversable edges for those links. No causal
graph edge or database confidence score is created.

Primary locators retained in the new rows include PMID:12513909,
PMID:12087100, PMID:20462497, PMID:18172556, PMCID:PMC2157567,
PMID:19564350, PMCID:PMC2715097, PMID:30782844, PMCID:PMC6463718,
PMID:22851691, PMCID:PMC3457542, and DOI:10.1074/jbc.RA118.007290.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,109 |
| Literature-expansion annotations | 441 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,597 |
| Normalized route edges | 1,275,521 |

The release validator passed with zero errors; the existing stable-locator
warning remains. The mSCS import and focused route-test verification are
recorded with the release handoff.
