# mSCIdblit release v1.9.268

Release date: 2026-09-24

Graph identifier: `module20_24_mechanism_graph:2026-09-24-il20-stat3-routes-391`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion391/`

## IL-20/STAT3 target-gene route curation

This release adds four receptor-specific IL-20 evidence routes:

- IL-20 → IL20RA:IL20RB → ???? → STAT3 → CCL2
- IL-20 → IL20RA:IL20RB → ???? → STAT3 → HGF
- IL-20 → IL22RA1:IL20RB → ???? → STAT3 → CCL2
- IL-20 → IL22RA1:IL20RB → ???? → STAT3 → HGF

The receptor-complex and terminal target evidence are retained, while the
intracellular continuation and receptor-to-STAT3 handoffs remain explicitly
unresolved. No graph edges, causal assertions, or database confidence scores
were created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 341,053 |
| Literature-expansion annotations | 7,385 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 1,368 |
| Normalized route nodes | 1,311,363 |
| Normalized route edges | 1,287,980 |
| New routes in this release | 4 |

The mSCIdblit validator passed with zero errors.
