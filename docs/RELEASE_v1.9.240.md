# mSCIdblit release v1.9.240

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-all-ligand-output-linked-363`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion363/`

## CSF3/G-CSF and TNF route curation

This release adds six primary-supported evidence routes:

- CSF3/G-CSF → CSF3R → SHC1 → STAT3 → SOCS3 expression
- CSF3/G-CSF → CSF3R → GRB2 → STAT3 → SOCS3 expression
- TNF → TNFR1 → TRADD → NF-κB-family target → ICAM1/CD54 expression
- TNF → TNFR1 → TRADD → NF-κB-family target → IL6 expression
- TNF → TNFR2 → NF-κB relay → NF-κB-family target → ICAM1/CD54 expression
- TNF → TNFR2 → NF-κB relay → NF-κB-family target → IL6 expression

Each route links existing primary-backed ligand–receptor, intracellular,
transcription-factor target, and output observations. The intracellular-to-TF
handoff remains explicitly unasserted; these annotations are evidence routes for
mSCS plausibility analysis and do not create causal graph edges or confidence
scores. The cumulative clean overlay now contains 114 route annotations added
over the v1.9.233 baseline and 555 total literature-expansion rows.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,223 |
| Literature-expansion annotations | 555 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,293,167 |
| Normalized route edges | 1,276,021 |

The release validator passed with zero errors. No graph edges, causal assertions,
or database confidence scores were created.
