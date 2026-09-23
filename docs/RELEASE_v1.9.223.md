# mSCIdblit release v1.9.223

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-il22-primary-route-341`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion341/`

## IL-22 primary route expansion

This release adds two evidence-layer route annotations for IL-22 signaling:

- IL22 → IL22RA1:IL10RB → JAK1 → STAT3 → SOCS3 expression
- IL22 → IL22RA1:IL10RB → TYK2 → STAT3 → SOCS3 expression

JAK1 and TYK2 are represented as parallel continuation alternatives, not as
serial steps. The primary studies support IL-22 receptor/JAK/STAT activation
and SOCS3 induction across receptor-reconstituted and human colon epithelial
systems, while the route table explicitly leaves receptor-to-kinase,
kinase-to-STAT3, and direct IL-22-specific TF-to-target handoffs unresolved.
These rows are evidence-only and do not create causal graph edges or database
confidence scores.

Primary locators: PMID:12087100, PMID:15120652, PMID:32611765, and
PMCID:PMC7458808.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,028 |
| Literature-expansion annotations | 360 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,198 |
| Normalized route edges | 1,275,197 |

The release validator passed with zero errors; the existing stable-locator
warning remains.
