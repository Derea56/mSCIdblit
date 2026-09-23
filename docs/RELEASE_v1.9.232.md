# mSCIdblit release v1.9.232

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-il12-stat4-targets-350`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion350/`

## IL-12 STAT4 target-gene expansion

This release adds 30 evidence-layer routes: 15 direct STAT4 target-gene
alternatives, each represented with both the JAK2 and TYK2 receptor-proximal
evidence branches. Targets include IL18R1, FURIN, IL12RB2, MYD88, HLX1,
GADD45G, LCP2, RUNX1, RUNX3, BHLHE40, LTA, IL24, IL10, ZBTB32, and IRF8.

The new rows extend the IL-12 TBX21 and IFNG routes with primary-supported
STAT4 transcriptional outputs. The receptor-to-JAK and JAK-to-STAT4 handoffs
remain explicitly unasserted because the current graph does not contain
IL-12-specific traversable edges for those links. No causal graph edge or
database confidence score is created.

Primary locators retained in the new rows include PMID:17380127,
PMCID:PMC1852779, PMCID:PMC1895858, PMCID:PMC1817634,
PMCID:PMC4323636, PMCID:PMC2768040, PMCID:PMC6265048,
PMCID:PMC10842983, PMCID:PMC2748807, PMCID:PMC2689787,
PMCID:PMC4025587, and PMCID:PMC6233715, alongside the primary IL-12
receptor/JAK locators PMID:8943050, PMID:9498755, and PMID:7638186.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,100 |
| Literature-expansion annotations | 432 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,552 |
| Normalized route edges | 1,275,485 |

The release validator passed with zero errors; the existing stable-locator
warning remains. The mSCS import and focused route-test verification are
recorded with the release handoff.
