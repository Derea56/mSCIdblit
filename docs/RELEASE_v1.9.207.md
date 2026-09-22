# mSCIdblit release v1.9.207

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-cross-record-route-linkage-324`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion324/`

## Conservative cross-record route composition

This release adds 215 evidence-route records across 66 exact ligand–receptor
edges. A route was added only when the receptor-proximal intracellular record
and the TF/output record shared both the exact exported ligand–receptor edge
and a stored evidence identifier. These records are retained as
`ligand_receptor_intracellular_tf_output_missing_target_gene` evidence routes.

The new rows do not create graph edges, assert an intracellular-to-TF causal
edge, or assign database confidence. mSCS can score them as four-layer route
support while retaining their non-causal, coobserved provenance.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 19,928 |
| L→R→output records | 4,394 |
| L→R→TF→output records | 344 |
| L→R→intracellular→output records | 2,421 |
| L→R→intracellular→TF→output records | 346 |
| Full graph edge-chain instances | 141 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |

The full graph-chain count remains 141 because this release expands the
evidence-route layer only. The downstream queue is fully represented in the
route audit; remaining work is primarily topology resolution, context
curation, and additional primary-evidence harvesting rather than unprocessed
unknown-output records.

Validation passed with zero errors. The bundle was imported successfully
through mSCS's `import_mechanism_bundle.py`. The mSCIdblit test suite passed
176 tests, and the mSCS route-scoring tests passed 4 tests.
