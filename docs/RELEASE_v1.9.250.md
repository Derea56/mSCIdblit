# mSCIdblit release v1.9.250

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-prolactin-stat5-csn2-373`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion373/`

## Prolactin STAT5 target-gene route expansion

This release adds one target-gene evidence route:

`Prolactin > PRLR > JAK2 > STAT5 > Csn2 (beta-casein) expression`

The primary prolactin/PRLR literature supports JAK2-dependent STAT5 activation
and beta-casein reporter output. The STAT5-to-Csn2 handoff remains explicitly
unasserted, and the route is evidence-only.

The prior CSF1/IL-34 ERK/c-FOS routes remain in the cumulative bundle. This
release does not create graph edges, causal assertions, or database confidence
scores.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 340,062 |
| Literature-expansion annotations | 6,394 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 438 |
| Normalized route nodes | 1,306,514 |
| Normalized route edges | 1,284,122 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows.
