# mSCIdblit release v1.9.224

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-il17a-primary-relay-342`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion342/`

## IL-17A receptor-proximal relay expansion

This release adds six evidence-layer route annotations for IL-17A epithelial
outputs. Each of DEFB4, CCL20, and CXCL8 is represented with ACT1/CIKS and
TRAF6 continuation alternatives:

- IL17A → IL17RA:IL17RC → ACT1 → target-gene expression
- IL17A → IL17RA:IL17RC → TRAF6 → target-gene expression

The routes preserve primary receptor-proximal and output evidence while
leaving the transcription-factor layer unresolved. ACT1 and TRAF6 are
alternatives in the current one-continuation route schema, not a claim that
the two proteins are serially collapsed into one node. These rows are
evidence-only and do not create causal graph edges or database confidence
scores.

Primary locators include PMID:17035243, PMID:17277779, PMID:21335551,
PMID:19825828, PMID:15322213, PMID:16272323, and PMID:11692108.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,034 |
| Literature-expansion annotations | 366 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,222 |
| Normalized route edges | 1,275,215 |

The release validator passed with zero errors; the existing stable-locator
warning remains.
