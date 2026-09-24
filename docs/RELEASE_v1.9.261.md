# mSCIdblit release v1.9.261

Release date: 2026-09-24

Graph identifier: `module20_24_mechanism_graph:2026-09-24-pacap-pac1-routes-384`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion384/`

## PACAP route curation

This release carries forward the 15 WNT3A routes and two VIP/VPAC2 routes and
adds two PACAP/PAC1 evidence routes that preserve parallel receptor-proximal
branches converging on a CREB-associated Bdnf promoter-IV output:

- PACAP → PAC1 → GNAS → CREB → Bdnf promoter IV
- PACAP → PAC1 → GNAQ/GNA11 → CREB → Bdnf promoter IV

The PACAP routes compose primary receptor-coupling, neuronal transcription, and
PAC1-dependent BDNF evidence layers. The G-protein-to-CREB and CREB-to-target
handoffs remain explicitly unasserted. These are evidence-layer annotations
only; no graph edges, causal assertions, or database confidence scores were
created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 341,037 |
| Literature-expansion annotations | 7,369 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 1,359 |
| Normalized route nodes | 1,311,290 |
| Normalized route edges | 1,287,923 |
| New routes in this release | 2 |

The mSCIdblit validator passed with zero errors. The route audit reports 141
edge-chain instances and 95 unique four-node topologies; the increase in this
release is in the evidence-route layer and does not change the causal graph.
