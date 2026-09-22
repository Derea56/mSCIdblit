# mSCIdblit release v1.9.187

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-301`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion301/`

## Functional readout curation

This release adds 20 topology-unlinked output annotations for primary-supported
complement-regulatory, developmental, receptor-pharmacology, transport, and
cellular functional readouts. No complete ligand→receptor→intracellular→TF
route is inferred.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 19,597 |
| New literature-expansion rows | 20 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

Validation passed with zero errors, and the bundle imported successfully through
mSCS's `import_mechanism_bundle.py`. The graph core remains unchanged.
