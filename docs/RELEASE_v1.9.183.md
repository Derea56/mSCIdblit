# mSCIdblit release v1.9.183

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-296`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion296/`

## Final explicit-output batch from the automated tranche

This release adds the remaining 20 records identified by the reproducible
stored-summary readout filter. They remain topology-unlinked evidence routes;
no unsupported intracellular, TF, or target-gene links are asserted.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 19,312 |
| New literature-expansion rows | 20 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The graph core and direct L→R route categories are unchanged. Validation passed
with zero errors, and the bundle imported successfully through mSCS's
`import_mechanism_bundle.py`.
