# mSCIdblit release v1.9.188

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-302`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion302/`

## Functional readout curation

This release adds 14 topology-unlinked output annotations for primary-supported
transport, excitability, cross-presentation, receptor clustering, cell-death,
and intracellular localization readouts. No complete ligand→receptor→intracellular→TF
route is inferred.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 19,611 |
| New literature-expansion rows | 14 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

Validation passed with zero errors, and the bundle imported successfully through
mSCS's `import_mechanism_bundle.py`. The graph core remains unchanged.
