# mSCIdblit release v1.9.230

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-il6-parallel-jak-348`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion348/`

## IL-6 parallel JAK2/TYK2 route expansion

This release adds four evidence-layer route annotations for the parallel
receptor-proximal JAK2 and TYK2 alternatives of the IL-6R:gp130 route:

- IL-6 → IL-6R:gp130 → JAK2 → STAT3 → SOCS3 expression
- IL-6 → IL-6R:gp130 → JAK2 → STAT3 → MYC expression
- IL-6 → IL-6R:gp130 → TYK2 → STAT3 → SOCS3 expression
- IL-6 → IL-6R:gp130 → TYK2 → STAT3 → MYC expression

Primary receptor-proximal studies support IL-6-induced JAK2 and TYK2
activation, while separate primary target studies support STAT3-associated
SOCS3 and MYC expression. The direct JAK-to-STAT3 handoff remains an
evidence-layer gap. No causal graph edge or database confidence score is
created.

Primary locators retained in the new rows include PMID:7537214,
PMID:16718380, PMCID:PMC2441693, PMID:9874564, PMCID:PMC1887683,
PMID:11412113, PMID:8511589, and PMID:7744001.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,068 |
| Literature-expansion annotations | 400 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,392 |
| Normalized route edges | 1,275,357 |

The release validator passed with zero errors; the existing stable-locator
warning remains. The mSCS import and focused route-test verification are
recorded with the release handoff.
