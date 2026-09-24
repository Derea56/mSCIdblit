# mSCIdblit release v1.9.241

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-all-ligand-output-linked-364`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion364/`

## EGF route curation

This release adds one bounded primary-supported evidence route:

- EGF → EGFR → SHC1/GRB2-SOS1/HRAS/RAF-MEK-ERK → ELK1 → EGR1 expression

The route links the existing EGF–EGFR receptor-assembly record, the EGFR
Shc/Grb2/Sos-Ras-ERK pathway backbone, and the EGF-responsive ELK1-to-EGR1
promoter record. The receptor-complex identity is retained as an explicit alias,
and the intracellular-to-ELK1 handoff remains unasserted because no exact graph
edge currently represents that intermediate transition. The route therefore
remains evidence-only and does not create a direct EGF-to-EGR1 graph edge,
causal assertion, or database confidence score.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,224 |
| Literature-expansion annotations | 556 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,293,172 |
| Normalized route edges | 1,276,026 |

The release validator passed with zero errors. The stable primary locators
retained for the added route are PMID:12297050, PMID:7798267, PMID:8649846,
PMID:11278445, PMID:22593802, and PMID:26551735.
