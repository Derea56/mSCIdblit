# mSCIdblit release v1.9.231

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-il12-tbx21-349`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion349/`

## IL-12 JAK2/TYK2–STAT4–TBX21 route expansion

This release adds two evidence-layer route annotations:

- IL-12 → IL12RB1:IL12RB2 → JAK2 → STAT4 → TBX21 expression
- IL-12 → IL12RB1:IL12RB2 → TYK2 → STAT4 → TBX21 expression

The existing graph already retained primary-supported IL-12 receptor/JAK2/TYK2/
STAT4 evidence and STAT4→IFNG routes. These additions expose the parallel
STAT4-responsive TBX21 target-gene branch. The receptor-to-JAK and
JAK-to-STAT4 handoffs remain explicitly unasserted because the current graph
does not contain IL-12-specific traversable edges for those links. No IL-23
receptor edge is reused, and no causal graph edge or database confidence score
is created.

Primary locators retained in the new rows include PMID:8943050,
PMID:9498755, PMID:7638186, PMID:17575072, PMCID:PMC1988915,
PMID:12023369, PMID:28630278, and PMID:9038232.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,070 |
| Literature-expansion annotations | 402 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,402 |
| Normalized route edges | 1,275,365 |

The release validator passed with zero errors; the existing stable-locator
warning remains. The mSCS import and focused route-test verification are
recorded with the release handoff.
