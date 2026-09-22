# mSCIdblit release v1.9.191

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-305`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion305/`

## Manual disposition of the remaining queue

This release adds a machine-readable disposition ledger for the remaining 70
downstream queue records. The ledger distinguishes 62 direct-edge records and
8 contextual-association records where the stored primary-supported curation
does not retain an explicit downstream output. These records remain available
as entry/context evidence only and are not promoted to causal or output routes;
the ledger records full-text primary review as the next action if an output route
is needed.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 19,651 |
| Manual disposition rows | 70 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

Validation passed with zero errors, and the bundle imported successfully through
mSCS's `import_mechanism_bundle.py`. The graph core and route-evidence layer
remain unchanged.
