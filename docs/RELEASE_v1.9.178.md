# mSCIdblit release v1.9.178

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-291`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion291/`

## Continued explicit output curation

This release adds the next 100 topology-unlinked output annotations selected
from stored primary-supported evidence summaries and assay fields. The rows
retain explicit functional observations while leaving ligand, receptor,
intracellular, TF, and target-gene roles unassigned unless separately
supported. Binding/structure-only records remain outside the overlay.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 18,892 |
| New literature-expansion rows | 100 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The direct L→R route categories remain unchanged; these are evidence-only
topology-unlinked annotations.

| Category | Records |
|---|---:|
| L→R→output | 4,394 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,421 |
| L→R→intracellular→TF→output | 131 |
| L→R entry only | 9,307 |

Validation passed with zero errors, and the bundle imported successfully through
mSCS's `import_mechanism_bundle.py` into a temporary active release directory.
