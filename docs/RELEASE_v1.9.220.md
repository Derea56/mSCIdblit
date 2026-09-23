# mSCIdblit release v1.9.220

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-primary-full-sequence-routes-338`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion338/`

## Graph-linked receptor-relay expansion

This release adds 21 nonduplicate evidence-route annotations: one corrected
full-intermediate IL-15 route and 20 graph-linked receptor-relay routes across
nine ligand labels. The new relay routes use stable, primary-locator-backed receptor-to-relay
edges for JAK1/2/3, TYK2, and related receptor-proximal kinase branches, then
connect them to already retained TF and output evidence. The newly represented
ligand label is LIF; other additions extend existing cytokine ligand labels.

These rows are explicitly marked as graph-linked compositions because their
route records do not originate in the downstream manual-evidence table. They
remain evidence-only and non-causal: the receptor-to-relay edge is source-linked,
the relay-to-TF handoff remains unasserted, and no database confidence score or
graph edge is created.

The bundle now contains 339 literature route annotations across 101 ligand
labels and 334,021 normalized signaling-route evidence records.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,021 |
| Full-sequence literature annotations | 339 |
| Ligand labels represented in literature annotations | 101 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,163 |
| Normalized route edges | 1,275,169 |

The release validator passed with zero errors; the existing stable-locator
warning remains.
