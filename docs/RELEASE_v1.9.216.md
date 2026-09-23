# mSCIdblit release v1.9.216

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-primary-full-sequence-routes-334`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion334/`

## Full-sequence route expansion

This release adds 60 branch- and alias-aware primary-literature route
annotations to the v333 snapshot. The additions recover named intermediate
and TF/target layers from all remaining historical full-route source records,
including routes where the current graph does not contain one or more explicit
handoff edges. Together with earlier curated rows, the release contains 128
full-sequence annotations across 42 ligand labels.

Missing handoffs are retained in `missing_layers` and
`route_linkage_status`; these rows remain evidence-only and non-causal. The
release does not create graph edges or database confidence scores. All 89
unique historical full-route source records are now represented: 43 were
already materialized and 60 new branch/alias-aware rows were added.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 333,810 |
| Full-sequence literature annotations | 128 |
| Ligand labels represented in full-sequence annotations | 42 |
| Full-sequence curation candidates | 7,742 |

The release validator passed with zero errors; the existing stable-locator
warning remains. mSCS imports the release identifier and all 128 literature
route annotations.
