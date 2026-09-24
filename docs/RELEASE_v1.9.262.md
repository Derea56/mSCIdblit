# mSCIdblit release v1.9.262

Release date: 2026-09-24

Graph identifier: `module20_24_mechanism_graph:2026-09-24-il15-jak-stat5-routes-385`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion385/`

## IL-15 route curation

This release carries forward the prior WNT3A, VIP/VPAC2, and PACAP/PAC1 route
annotations and adds two IL-15/JAK/STAT5 evidence routes ending at the Il17A
locus:

- IL-15 → IL-15Rα/IL-2Rβ/γc → JAK1 → STAT5 → IL17A
- IL-15 → IL-15Rα/IL-2Rβ/γc → JAK3 → STAT5 → IL17A

The routes retain primary evidence for IL-15 receptor signaling, JAK/STAT5
activation, and STAT5 occupancy at the Il17A locus. The kinase-to-STAT5
handoff remains explicitly unasserted, and the target effect is retained as
context-dependent inhibitory evidence rather than a universal causal claim.
No graph edges, causal assertions, or database confidence scores were created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 341,039 |
| Literature-expansion annotations | 7,371 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 1,361 |
| Normalized route nodes | 1,311,300 |
| Normalized route edges | 1,287,931 |
| New routes in this release | 2 |

The mSCIdblit validator passed with zero errors.
