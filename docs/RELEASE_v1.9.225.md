# mSCIdblit release v1.9.225

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-tslp-primary-relay-343`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion343/`

## TSLP JAK/STAT5 output expansion

This release adds two evidence-layer route annotations:

- TSLP → TSLPR/CRLF2:IL7RA → JAK1 → STAT5 → GATA3 expression output
- TSLP → TSLPR/CRLF2:IL7RA → JAK2 → STAT5 → GATA3 expression output

JAK1 and JAK2 are parallel continuation alternatives. The primary studies
support the TSLP receptor/JAK/STAT5 relay and GATA3 expression in human ILC2s,
but no terminal GATA3 target gene or single-source end-to-end chain is
asserted. These rows are evidence-only and do not create causal graph edges or
database confidence scores.

Primary locators include PMID:10570284, PMID:11418668, PMID:20128689,
PMID:20974963, and PMID:23063330.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,036 |
| Literature-expansion annotations | 368 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,232 |
| Normalized route edges | 1,275,223 |

The release validator passed with zero errors; the existing stable-locator
warning remains.
