# mSCIdblit release v1.9.194

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-disposition-308`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion308/`

## Synchronized downstream disposition

This evidence-preserving release carries the five source-reviewed downstream
route annotations from the preceding literature-expansion release and
regenerates the manual disposition ledger against that updated route table.
The graph core remains unchanged. Remaining records are not claims that the
underlying papers lack additional findings; they identify records that still
require full-text primary review if a new output route is needed.

| Disposition | Count |
|---|---:|
| No explicit output in the stored curated record | 52 |
| Contextual association without explicit output | 4 |
| No new output in this record; pair has another output route | 9 |
| **Remaining disposition rows** | **65** |

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 19,656 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |

Validation passed with zero errors, and the bundle imported successfully through
mSCS's `import_mechanism_bundle.py`. No causal edges or confidence scores were
created.
