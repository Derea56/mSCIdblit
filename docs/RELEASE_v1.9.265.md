# mSCIdblit release v1.9.265

> Superseded by corrected release [v1.9.266](RELEASE_v1.9.266.md) before mSCS import because the v388 batch re-emitted carried-forward route IDs.

Release date: 2026-09-24

Graph identifier: `module20_24_mechanism_graph:2026-09-24-il1a-il33-il18-routes-388`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion388/`

## IL-1A, IL-33, and IL-18 route curation

This release carries forward the prior ligand-specific route annotations and
adds four bounded evidence routes:

- IL-1A → IL1R1-IL1RAP → MYD88 → RELA → IL6
- IL-33 → IL1RL1/ST2:IL1RAP → MYD88 → STAT3 → IL10
- IL-33 → IL1RL1/ST2:IL1RAP → MYD88 → STAT3 → MMP9
- IL-18 → IL18R1:IL18RAP → MYD88 → STAT4 → IFNG

The IL-33 receptor-to-MYD88 layer is retained as an adjacent receptor-complex
component because the current ligand–receptor edge resolves to a closely
related receptor node; that handoff remains explicitly unasserted. The
MYD88-to-TF handoff is unasserted for all four routes. Existing TF-to-target
edges and direct ligand-associated outputs are retained as separate evidence
layers. No graph edges, causal assertions, or database confidence scores were
created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 341,048 |
| Literature-expansion annotations | 7,380 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 1,370 |
| Normalized route nodes | 1,311,345 |
| Normalized route edges | 1,287,967 |
| New routes in this release | 4 |

The mSCIdblit validator passed with zero errors.
