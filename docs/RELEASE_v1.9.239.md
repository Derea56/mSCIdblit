# mSCIdblit release v1.9.239

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-all-ligand-output-linked-362`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion362/`

## IL1B target-link curation

This release adds three primary-supported IL1B evidence routes that connect the
existing IL1R1/IL1RAP → MYD88 route to graph-supported transcriptional targets:

- IL1B → IL1R1/IL1RAP → MYD88 → NF-κB-family target → ICAM1/CD54 expression
- IL1B → IL1R1/IL1RAP → MYD88 → NF-κB-family target → IL6 expression
- IL1B → IL1R1/IL1RAP → MYD88 → NF-κB-family target → CXCL1 expression

The ligand-output and TF-target components are linked to existing primary-backed
graph edges. The intracellular-to-TF handoff remains explicitly unasserted, so
these are evidence routes for mSCS plausibility analysis rather than causal graph
edges or database confidence scores. The cumulative clean overlay now contains
108 route annotations added over the v1.9.233 baseline and 549 total
literature-expansion rows.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,217 |
| Literature-expansion annotations | 549 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,293,137 |
| Normalized route edges | 1,275,991 |

The release validator passed with zero errors. No graph edges, causal assertions,
or database confidence scores were created.
