# mSCIdblit release v1.9.212

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-primary-cytokine-routes-330`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion330/`

## Primary route expansion

This release carries forward the v329 graph and all-ligand curation queue and
adds 16 primary-evidence route annotations across IL-2, IL-4, IFN-gamma, and
IL-23. The routes expose shared JAK/STAT intermediates and target-gene outputs
for later perturbation analysis.

The annotations are evidence-layer routes, not new causal edges. Each route
retains the direct TF-to-target edge where present and marks the direct
intracellular-to-TF relay as unresolved when that exact edge is not asserted in
the graph. mSCS can therefore use the route as bounded plausibility evidence
without treating an assembled multi-paper path as a single demonstrated causal
chain.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 333,702 |
| Literature route annotations added | 16 |
| Full-sequence curation candidates | 7,742 |

The release validator passed with zero errors; the existing stable-locator
warning remains. No graph edges or database confidence scores were created.
mSCS imports the release identifier and the expanded literature-route table
alongside the normalized route artifacts.
