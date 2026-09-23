# mSCIdblit release v1.9.213

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-primary-full-sequence-routes-331`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion331/`

## Full-sequence route expansion

This release adds 20 reconciled primary-literature route annotations to the
v330 snapshot. Together with the earlier curated rows, the release contains 40
full-sequence annotations across 16 ligands. Every row includes a resolved
ligand, receptor, receptor-proximal intracellular intermediate, TF, and target
gene node in the current graph.

The routes are evidence-layer annotations. The intermediate-to-TF relay is
marked unresolved unless the exact graph edge is present, so these records are
usable for mSCS plausibility analysis without becoming causal or traversable
graph edges. Historical route rows were reconciled by current graph labels and
retained only when the receptor-proximal intermediate could be resolved
unambiguously.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 333,722 |
| Full-sequence literature annotations | 40 |
| Ligands represented in full-sequence annotations | 16 |
| Full-sequence curation candidates | 7,742 |

The release validator passed with zero errors; the existing stable-locator
warning remains. No graph edges or database confidence scores were created.
mSCS imports the release identifier and all 40 literature-route annotations.
