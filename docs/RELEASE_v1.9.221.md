# mSCIdblit release v1.9.221

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-primary-full-sequence-routes-339`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion339/`

## All-ligand full-route continuation

This release adds five previously unmaterialized full-intermediate evidence
routes across three ligand labels present in the curation queue: IL-6, LIF,
and YAP1. These routes are graph-linked compositions with stable primary
locators. They preserve the ligand → receptor → intracellular continuation →
TF → output ordering, while retaining the explicit limitation that the
relay-to-TF handoff is not asserted by a single source and no causal graph
edge or confidence score is created.

The bundle now contains 344 literature route annotations across 102 ligand
labels and 334,026 normalized signaling-route evidence records.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,026 |
| Full-sequence literature annotations | 344 |
| Ligand labels represented in literature annotations | 102 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,188 |
| Normalized route edges | 1,275,189 |

The release validator passed with zero errors; the existing stable-locator
warning remains.
