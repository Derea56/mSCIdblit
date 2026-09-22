# mSCIdblit release v1.9.177

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-290`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion290/`

## Batch curation of explicit output readouts

This release adds 100 topology-unlinked output annotations from the remaining
unknown-output queue. Selection used a reproducible, conservative language
filter over the stored primary-supported evidence summary and assay fields.
Rows were retained only when those fields contained explicit functional
readouts such as chemotaxis, migration, cellular activation, internalization,
second-messenger activity, phosphorylation, gene induction, or related
phenotypes. Binding/structure-only records were not promoted. No ligand,
receptor, intracellular, TF, or target-gene roles are assigned by this batch.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 18,792 |
| New literature-expansion rows | 100 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The direct L→R route categories remain unchanged because these additions are
evidence-only topology-unlinked annotations:

| Category | Records |
|---|---:|
| L→R→output | 4,394 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,421 |
| L→R→intracellular→TF→output | 131 |
| L→R entry only | 9,307 |

All new rows retain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Validation passed with zero
errors, and the bundle imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory.
