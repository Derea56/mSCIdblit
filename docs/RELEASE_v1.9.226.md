# mSCIdblit release v1.9.226

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-common-gamma-primary-344`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion344/`

## Shared-gamma cytokine route expansion

This release adds 15 evidence-layer route annotations for three cytokines:

- IL-7 → IL7RA:IL2RG → JAK1 or JAK3 → STAT5 → BCL2, BCL2L1, or CISH expression
- IL-15 → IL15RA:IL2RB:IL2RG → JAK1 or JAK3 → STAT5 → BCL2, BCL2L1, or CISH expression
- IL-5 → IL5RA:CSF2RB → JAK2 → STAT5 → BCL2, BCL2L1, or CISH expression

The JAK alternatives are parallel receptor-proximal continuations. Primary
evidence supports the receptor/JAK layer and reusable STAT5 target-gene layer,
but the direct JAK-to-STAT5 relay is not asserted as a graph edge and no
single-source end-to-end chain is claimed. These rows are evidence-only and
do not create causal graph edges or database confidence scores.

Primary locators retained in the new rows include PMID:7875201,
PMID:7489741, PMID:7568001, PMID:8530383, PMID:9363920, PMID:19050240,
PMID:22528658, PMID:38614096, PMID:9129017, PMCID:PMC2826763,
PMCID:PMC2865298, and PMCID:PMC5521770.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,051 |
| Literature-expansion annotations | 383 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,307 |
| Normalized route edges | 1,275,283 |

The release validator passed with zero errors; the existing stable-locator
warning remains. mSCS imported the bundle successfully and its focused route
test suite passed 18 tests.
