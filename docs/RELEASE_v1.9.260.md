# mSCIdblit release v1.9.260

Release date: 2026-09-24

Graph identifier: `module20_24_mechanism_graph:2026-09-24-vip-vpac2-routes-383`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion383/`

## WNT3A and VIP route curation

This release carries forward the 15 WNT3A canonical routes from v1.9.259 and
adds two VIP/VPAC2 routes:

- VIP → VPAC2 → GNAS → CREB → Per1
- VIP → VPAC2 → GNAS → CREB → IL6

The WNT3A routes cover FZD2, FZD4, FZD5, FZD7, and FZD10 branches with MYC,
CCND1, and CDKN1A outputs. The VIP routes retain primary receptor/cAMP and
transcriptional-output evidence while leaving the GNAS-to-CREB and
CREB-to-target handoffs explicitly unasserted. These are evidence-layer
annotations only; no graph edges, causal assertions, or database confidence
scores were created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 341,035 |
| Literature-expansion annotations | 7,367 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 1,357 |
| Normalized route nodes | 1,311,280 |
| Normalized route edges | 1,287,915 |
| New routes in this release | 2 |

The mSCIdblit validator passed with zero errors. mSCS imported the bundle; its
derived-table contract passed and the mechanism-route test suite passed 18
tests.
