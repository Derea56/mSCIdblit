# mSCIdblit release v1.9.192

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-306`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion306/`

## Corrected manual disposition ledger

This release corrects the remaining-queue ledger to identify nine records whose
specific downstream claim has no new output annotation but whose ligand–receptor
pair already has separate output routes elsewhere in the evidence layer. The
other 61 records remain entry/context evidence only in this release. No route or
graph edge is promoted by the ledger.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 19,651 |
| Manual disposition rows | 70 |
| Records with existing pair-level output routes | 9 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |

Validation passed with zero errors, and the bundle imported successfully through
mSCS's `import_mechanism_bundle.py`. The graph core and route-evidence layer
remain unchanged.
