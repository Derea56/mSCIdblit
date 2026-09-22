# mSCIdblit release v1.9.181

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-294`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion294/`

## Continued explicit output curation

This release adds 100 additional topology-unlinked output annotations from
stored primary-supported summaries. The evidence layer now retains a broader
set of experimentally observed cellular, localization, processing, and
receptor-proximal readouts without inferring unsupported complete signaling
chains.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 19,192 |
| New literature-expansion rows | 100 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The graph core and direct L→R route categories are unchanged. Validation passed
with zero errors, and the bundle imported successfully through mSCS's
`import_mechanism_bundle.py`.
