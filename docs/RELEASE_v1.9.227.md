# mSCIdblit release v1.9.227

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-cntf-jak-stat3-345`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion345/`

## CNTF intracellular route expansion

This release adds two evidence-layer route annotations:

- CNTF → CNTFR-alpha:gp130:LIFR → JAK1 → STAT3 → JUNB expression
- CNTF → CNTFR-alpha:gp130:LIFR → JAK2 → STAT3 → JUNB expression

The JAK1 and JAK2 branches are parallel alternatives. Primary CNTF signaling
work supports JAK1/JAK2 and STAT3 activation, while primary promoter work
supports CNTF/IL-6-responsive STAT3-dependent JUNB activation. The exact
receptor-to-JAK and JAK-to-STAT3 handoffs remain evidence-layer compositions,
not asserted graph edges. No causal traversal or database confidence score is
created.

Primary locators retained in the new rows include PMID:8390097,
PMID:8385113, PMID:7500350, PMID:11882386, and PMID:7898939.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,053 |
| Literature-expansion annotations | 385 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,317 |
| Normalized route edges | 1,275,291 |

The release validator passed with zero errors; the existing stable-locator
warning remains. mSCS imported the bundle successfully and its focused route
test suite passed 18 tests.
