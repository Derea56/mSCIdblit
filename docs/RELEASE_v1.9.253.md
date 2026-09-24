# mSCIdblit release v1.9.253

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-alias-full-target-routes-376`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion376/`

## Alias full-layer route curation

This release adds 42 full-layer evidence routes for four ligand aliases with
distinct current graph nodes: `Bdnf`, `Il15`, `Il2`, and `Thpo`.

The routes retain source-supported intracellular nodes from the corresponding
canonical primary routes. Where the alias receptor does not have an exact
current graph edge to that relay, the route records
`receptor_to_intracellular_edge_not_asserted` rather than dropping the relay
or creating a new graph edge. The existing TF and target-gene handoffs remain
independently represented and are marked in `missing_layers` when not asserted.

No graph edges, causal assertions, or database confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 340,159 |
| Literature-expansion annotations | 6,491 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 481 |
| Normalized route nodes | 1,306,945 |
| Normalized route edges | 1,284,456 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows.
