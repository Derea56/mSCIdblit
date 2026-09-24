# mSCIdblit release v1.9.259

Release date: 2026-09-24

Graph identifier: `module20_24_mechanism_graph:2026-09-24-wnt3a-canonical-routes-382`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion382/`

## WNT3A canonical evidence routes

This release adds 15 source-linked full-layer evidence routes for WNT3A. The
routes cover five receptor-specific branches—FZD2, FZD4, FZD5, FZD7, and
FZD10—and three independently documented target-gene outputs: MYC, CCND1,
and CDKN1A.

The routes retain receptor-specific WNT3A activation evidence, the canonical
beta-catenin/LEF1 nuclear module, and WNT3A-associated target-gene expression.
The receptor-to-beta-catenin, beta-catenin-to-LEF1, and TF-to-target handoffs
remain explicitly unasserted where the source set does not demonstrate them as
direct causal edges in one experiment. No graph edges, causal assertions, or
database confidence scores were created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 341,033 |
| Literature-expansion annotations | 7,365 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 1,355 |
| Normalized route nodes | 1,311,270 |
| Normalized route edges | 1,287,907 |
| New WNT3A routes | 15 |

The mSCIdblit validator passed with zero errors. mSCS imported the bundle; its
derived-table contract passed and the mechanism-route test suite passed 18
tests.
