# mSCIdblit release v1.9.257

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-split-output-promotion-380`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion380/`

## Split-output route promotion

This release adds 12 full-layer evidence routes for IL9 and IL11. Each route
combines a source-linked intracellular-to-output observation and a separate
source-linked TF-to-output observation for the same ligand–receptor pair with
an existing target-gene route. The relay-to-TF and target-specific handoffs
remain explicitly unasserted, and the original partial routes are retained.

These are composed evidence routes for mSCS plausibility analysis. No graph
edges, causal assertions, or database confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 340,565 |
| Literature-expansion annotations | 6,897 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 887 |
| Normalized route nodes | 1,308,931 |
| Normalized route edges | 1,286,036 |
| New split-output routes | 12 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows. mSCS imported the
release successfully; its derived-table contract passed and the mechanism-route
test suite passed 18 tests.
