# mSCIdblit release v1.9.179

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-292`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion292/`

## Continued explicit output curation

This release adds another 100 topology-unlinked output annotations from
primary-supported evidence summaries. The batch includes explicit cellular,
receptor-proximal, intracellular-association, localization, and functional
readouts while preserving unresolved route topology. No unsupported ligand,
receptor, TF, or target-gene link is inferred, and the graph core is unchanged.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 18,992 |
| New literature-expansion rows | 100 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The direct L→R route categories remain unchanged because these annotations are
evidence-only and topology-unlinked. Validation passed with zero errors, and
the bundle imported successfully through mSCS's `import_mechanism_bundle.py`.
