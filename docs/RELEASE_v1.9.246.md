# mSCIdblit release v1.9.246

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-bdnf-creb-arc-369`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion369/`

## BDNF-TrkB target-gene route expansion

This release adds three parallel, evidence-only routes for BDNF stimulation:

`BDNF > NTRK2/TrkB receptor > PLCG1 > CREB > Arc expression`

`BDNF > NTRK2/TrkB receptor > FRS2A > CREB > Arc expression`

`BDNF > NTRK2/TrkB receptor > SHC1 > CREB > Arc expression`

The relay branches and BDNF-responsive CREB/Arc output are supported by
primary-linked literature, but the intracellular-to-CREB and CREB-to-Arc
handoffs remain explicitly unasserted. The routes therefore preserve the full
layered path expression for mSCS plausibility analysis without creating graph
edges, causal assertions, or database confidence scores.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 340,051 |
| Literature-expansion annotations | 6,383 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 427 |
| Normalized route nodes | 1,306,459 |
| Normalized route edges | 1,284,072 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows.
