# mSCIdblit release v1.9.263

Release date: 2026-09-24

Graph identifier: `module20_24_mechanism_graph:2026-09-24-il21-stat3-routes-386`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion386/`

## IL-21 route curation

This release carries forward the prior ligand-specific route annotations and
adds two IL-21/STAT3 evidence routes:

- IL-21 → IL-21R:IL2RG → JAK1/JAK3 → STAT3 → IL21
- IL-21 → IL-21R:IL2RG → JAK1/JAK3 → STAT3 → IL17A

Primary studies support IL-21/STAT3 autoregulation at the IL21 promoter and
STAT3-dependent IL17A output in Th17 contexts. The JAK1/JAK3-to-STAT3 handoff
remains explicitly unasserted as a direct graph edge. No graph edges, causal
assertions, or database confidence scores were created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 341,041 |
| Literature-expansion annotations | 7,373 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 1,363 |
| Normalized route nodes | 1,311,310 |
| Normalized route edges | 1,287,939 |
| New routes in this release | 2 |

The mSCIdblit validator passed with zero errors.
