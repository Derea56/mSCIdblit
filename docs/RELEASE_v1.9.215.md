# mSCIdblit release v1.9.215

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-primary-full-sequence-routes-333`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion333/`

## Full-sequence route expansion

This release adds 28 reconciled primary-literature route annotations to the
v331 graph snapshot. The additions recover explicit receptor aliases,
composite JAK1/JAK3 branches, and primary Biglycan–TLR–MyD88/NF-kappaB
routes. Together with the earlier curated rows, the release contains 68
full-sequence annotations across 20 ligand labels.

These are evidence-layer routes. Receptor aliases and composite relay
reconciliations are recorded in `route_linkage_status`; unresolved
intermediate-to-TF handoffs remain marked as missing rather than becoming
causal graph edges. No database confidence scores are assigned.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 333,750 |
| Full-sequence literature annotations | 68 |
| Ligand labels represented in full-sequence annotations | 20 |
| Full-sequence curation candidates | 7,742 |

The release validator passed with zero errors; the existing stable-locator
warning remains. mSCS imports the release identifier and all 68 literature
route annotations.
