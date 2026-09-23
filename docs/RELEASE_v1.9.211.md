# mSCIdblit release v1.9.211

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-all-ligand-full-sequence-queue-329`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion329/`

## All-ligand full-sequence curation queue

This release retains the v328 graph and route-evidence snapshot and adds
`mechanism_full_sequence_curation_queue.tsv.gz`. The queue collapses repeated
route-evidence records into distinct ligand→receptor→intracellular→TF route
cores while retaining the contributing route IDs, source chains, evidence IDs,
pathways, and stable primary locators.

It contains 7,742 curation candidates covering 1,840 ligands and 1,600
receptors. The candidates are review work items, not confidence scores: missing
links remain explicit, and no causal or traversable graph edge is created.

The queue is grouped at the intracellular/TF core level, so multiple target
genes or generic outputs remain attached to the same shared signaling core.
This preserves overlap for later perturbation analysis, including shared-node
queries such as MYD88, while keeping primary-literature verification as the
gate for promoting any missing link.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 333,686 |
| Full-sequence curation candidates | 7,742 |
| Ligands represented in the queue | 1,840 |
| Receptors represented in the queue | 1,600 |
| P1 core candidates | 2,535 |

The release validator passed with zero errors; the existing stable-locator
warning remains. The queue is evidence-layer data only and does not assign
database confidence. mSCS imports it as
`mechanism_full_sequence_curation_queue.tsv` alongside the normalized route
artifacts.
