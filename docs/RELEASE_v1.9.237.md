# mSCIdblit release v1.9.237

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-all-ligand-output-linked-360`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion360/`

## Expanded cytokine relay-to-output curation

This clean cumulative release contains 103 unique primary-supported
ligand-to-output route annotations. Relative to v1.9.236, it adds 28 routes
for IL-2, GM-CSF, IL-3, IL-5, OSM, IL-12/23, and LIF. Each route links
existing ligand–receptor and receptor-proximal evidence to an existing TF and
target-gene output edge. The intracellular-to-TF handoff remains explicitly
unasserted unless a traversable graph edge already exists.

The release was rebuilt from the v353 baseline to ensure that the cumulative
overlay contains no duplicate expansion identifiers. These rows are evidence
routes for mSCS plausibility analysis; they do not create graph edges, causal
assertions, or database confidence scores.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Linked graph-source rows | 17,242 |
| Evidence-route records | 334,212 |
| Literature-expansion annotations | 544 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,293,112 |
| Normalized route edges | 1,275,971 |

The release validator passed with zero errors; the existing stable-locator
warning remains.
