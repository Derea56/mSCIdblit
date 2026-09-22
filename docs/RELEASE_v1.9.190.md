# mSCIdblit release v1.9.190

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-304`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion304/`

## Manual functional-readout curation

This release adds 26 topology-unlinked output annotations for explicit
functional outcomes including receptor activity, synaptic clustering, receptor
insertion, complement control, microbial attachment/penetration, membrane
clustering, BMP patterning, and cytoplasmic sequestration. Pure binding and
structure records remain unresolved. No complete ligand→receptor→intracellular→TF
route is inferred.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 19,651 |
| New literature-expansion rows | 26 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

Validation passed with zero errors, and the bundle imported successfully through
mSCS's `import_mechanism_bundle.py`. The graph core remains unchanged.
