# mSCIdblit release v1.9.234

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-il31-stat3-352`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion352/`

## IL-31 JAK1/STAT3 output expansion

This release adds two evidence-layer route annotations:

- IL-31 → IL31RA:OSMRβ → JAK1 → STAT3 → POMC expression
- IL-31 → IL31RA:OSMRβ → JAK1 → STAT3 → CCL2 expression

Primary receptor studies support IL31RA:OSMRβ receptor assembly, JAK1
association, and STAT3 activation. Separate primary output studies support
IL-31-induced POMC or CCL2 expression in human epithelial systems. The direct
JAK1-to-STAT3 handoff remains unasserted, and the component studies retain
their distinct epithelial/neuroendocrine contexts. No causal graph edge or
database confidence score is created.

Primary locators retained in the new rows include PMID:15184896,
PMID:17379091, PMID:15194700, PMID:17148439, PMID:11104795,
PMCID:PMC381469, PMID:22578170, PMCID:PMC3482403, PMID:27216177,
PMID:23874436, and DOI:10.1371/journal.pone.0067666.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,105 |
| Literature-expansion annotations | 437 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,577 |
| Normalized route edges | 1,275,505 |

The release validator passed with zero errors; the existing stable-locator
warning remains. The mSCS import and focused route-test verification are
recorded with the release handoff.
