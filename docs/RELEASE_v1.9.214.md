# mSCIdblit release v1.9.214

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-primary-full-sequence-routes-332`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion332/`

## Full-sequence route expansion

This release adds 14 reconciled primary-literature route annotations to the
v331 snapshot. The additions recover explicit JAK1 and JAK3 branches from
historical IL-4 and IL-15 route records that reported a composite JAK1/JAK3
continuation. Together with the earlier curated rows, the release contains
54 full-sequence annotations across 17 ligand labels.

The routes are evidence-layer annotations. The intermediate-to-TF relay is
marked unresolved unless the exact graph edge is present, so these records are
usable for mSCS plausibility analysis without becoming causal or traversable
graph edges. Composite intermediates were split only when each branch was
represented by a current receptor-proximal graph edge and the source record
explicitly named the composite continuation.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 333,736 |
| Full-sequence literature annotations | 54 |
| Ligand labels represented in full-sequence annotations | 17 |
| Full-sequence curation candidates | 7,742 |

The release validator passed with zero errors; the existing stable-locator
warning remains. No graph edges or database confidence scores were created.
mSCS imports the release identifier and all 54 literature-route annotations.
