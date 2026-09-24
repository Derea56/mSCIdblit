# mSCIdblit release v1.9.254

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-relay-target-promotion-377`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion377/`

## Source-linked relay promotion

This release adds 194 full-layer evidence routes across seven ligand labels.
Each new route starts from an existing source-linked
`ligand>receptor>????>TF>target_gene_expression` record and carries over an
intracellular relay already represented by a full route with the identical
ligand, receptor, and TF node identities. The original partial route remains
in the release, and the new route records whether receptor-to-relay,
relay-to-TF, and TF-to-target edges are actually asserted.

These are composed evidence routes for mSCS plausibility analysis. They do not
create graph edges, causal assertions, or database confidence scores, and they
do not claim that one primary source demonstrated every handoff.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 340,353 |
| Literature-expansion annotations | 6,685 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 675 |
| Normalized route nodes | 1,307,915 |
| Normalized route edges | 1,285,232 |
| New relay-promotion routes | 194 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows. The mSCS derived
table contract passed, and the mechanism-route test suite passed 18 tests.
