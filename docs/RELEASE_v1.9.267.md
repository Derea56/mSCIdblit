# mSCIdblit release v1.9.267

Release date: 2026-09-24

Graph identifier: `module20_24_mechanism_graph:2026-09-24-il17b-il36-cxcl1-routes-390`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion390/`

## IL-17B and IL-36 CXCL1 route curation

This release adds four bounded evidence routes ending in CXCL1 expression:

- IL-17B → IL17RB → TRAF6-ACT1-TAK1-ERK1/2 → NFKB p65/p50 → CXCL1
- IL-36A → IL1RL2:IL1RAP → ???? → NFKB p65/p50 → CXCL1
- IL-36B → IL1RL2:IL1RAP → ???? → NFKB p65/p50 → CXCL1
- IL-36G → IL1RL2:IL1RAP → ???? → NFKB p65/p50 → CXCL1

The IL-17B relay is supported by a ligand-level cascade observation, but the
receptor-to-relay and relay-to-TF handoffs remain unasserted. The IL-36
routes retain receptor and terminal TF/output evidence while explicitly
leaving the intracellular continuation unresolved. No graph edges, causal
assertions, or database confidence scores were created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 341,049 |
| Literature-expansion annotations | 7,381 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 1,368 |
| Normalized route nodes | 1,311,347 |
| Normalized route edges | 1,287,968 |
| New routes in this release | 4 |

The mSCIdblit validator passed with zero errors.
