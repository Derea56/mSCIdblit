# mSCIdblit release v1.9.184

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-297`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion297/`

## Expanded functional-output curation

This release adds 100 topology-unlinked output annotations using the expanded
stored-summary filter for explicit inhibition, clearance, developmental
activity, receptor-current, entry, and other functional outcomes. Structure-
only exclusions remain unresolved. No complete ligand→receptor→intracellular→TF
route is inferred.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 19,412 |
| New literature-expansion rows | 100 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

Validation passed with zero errors, and the bundle imported successfully through
mSCS's `import_mechanism_bundle.py`. The graph core remains unchanged.
