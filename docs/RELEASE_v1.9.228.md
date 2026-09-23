# mSCIdblit release v1.9.228

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-il9-jak-stat-346`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion346/`

## IL-9 JAK/STAT feedback-route expansion

This release adds six evidence-layer route annotations:

- IL-9 → IL9RA:IL2RG → JAK1 or JAK3 → STAT5 → CISH expression
- IL-9 → IL9RA:IL2RG → JAK1 or JAK3 → STAT5 → SOCS2 expression
- IL-9 → IL9RA:IL2RG → JAK1 or JAK3 → STAT3 → SOCS3 expression

Primary IL-9 receptor work supports JAK1/JAK3-associated STAT1/3/5
activation, and primary IL-9 receptor-mutant work supports STAT-dependent
CIS/SOCS2/SOCS3 induction. The direct JAK-to-STAT handoff remains an
evidence-layer gap; no causal graph edge or database confidence score is
created.

Primary locators retained in the new rows include PMID:7718508,
PMID:9535918, PMID:11115404, PMID:9129017, PMID:28009300,
PMID:16718380, PMCID:PMC5217531, and PMCID:PMC2441693.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,059 |
| Literature-expansion annotations | 391 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,347 |
| Normalized route edges | 1,275,321 |

The release validator passed with zero errors; the existing stable-locator
warning remains. mSCS imported the bundle successfully and its focused route
test suite passed 18 tests.
