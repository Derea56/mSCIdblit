# mSCIdblit Module 20B–24B mechanism graph v1.8.2

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-network-coverage`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_network_coverage/`

This patch extends the v1.8.1 evidence-route audit so mSCS can use existing
receptor-proximal intracellular evidence when an exact ligand–receptor entry
resolves to the same receptor node. The graph edges and source registers are
unchanged. These additional rows are retained as non-causal, context-bound
evidence routes and do not assert that every ligand for a receptor produces
the same intracellular response.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Strict edge-chain instances | 141 |
| Strict four-node topologies | 95 |
| Partial chain records | 6,118 |
| Evidence-route records | 13,743 |
| Exact-shared-receptor route records | 2,625 |
| Receptor-proximal records still missing an LR pair | 735 |

The new route layer contains 1,340 `ligand>receptor>intracellular` evidence
records without an extracted TF or output, 1,262 intracellular-plus-generic-
output records missing TF support, and 23 intracellular-plus-TF records
missing a terminal output. The strict complete-chain count remains 141 because
these additions are evidence routes rather than newly asserted causal edges.

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
The mSCS import contract accepts the new route tiers. Generic outputs, missing
TFs, and unresolved terminal layers remain explicit for downstream confidence
scoring.
