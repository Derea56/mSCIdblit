# mSCIdblit release v1.9.233

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-il23-tyk2-351`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion351/`

## IL-23 TYK2/STAT3 route expansion

This release adds three evidence-layer route annotations for the TYK2 branch
of the IL-23 receptor pathway:

- IL-23 → IL12RB1:IL23R → TYK2 → STAT3 → IL17A expression
- IL-23 → IL12RB1:IL23R → TYK2 → STAT3 → IL17F expression
- IL-23 → IL12RB1:IL23R → TYK2 → STAT3 → IL22 expression

These rows complement the existing JAK2 alternatives. Primary IL-23 receptor/
TYK2 evidence and primary STAT3 target-gene evidence support the component
layers; the direct TYK2-to-STAT3 handoff remains unasserted. No causal graph
edge or database confidence score is created.

Primary locators retained in the new rows include PMID:12023369,
PMCID:PMC5773378, PMID:9038232, PMCID:PMC3148263, PMCID:PMC3408191,
and PMCID:PMC3919552.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,103 |
| Literature-expansion annotations | 435 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,567 |
| Normalized route edges | 1,275,497 |

The release validator passed with zero errors; the existing stable-locator
warning remains. The mSCS import and focused route-test verification are
recorded with the release handoff.
