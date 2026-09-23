# mSCIdblit release v1.9.236

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-all-ligand-output-linked-359`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion359/`

## Primary-supported ligand-to-output route expansion

This release adds 75 non-causal evidence-route annotations that explicitly
link existing ligand–receptor and intracellular observations to existing
transcription-factor and target-gene output edges. The batch covers IL-13,
IL-4, IL-10, IL-7, IL-9, IL-21, IFN-γ, IL-6, IL-15, IL-17A, and IL-31.
Where the graph contains a receptor-associated kinase or adaptor edge, it is
retained in the route. The intracellular-to-TF handoff remains explicitly
unasserted unless a traversable graph edge already exists.

The route rows preserve overlapping outputs and relay alternatives rather than
collapsing them into one pathway. They therefore allow mSCS to use shared
intermediates and alternative receptor-proximal branches as plausibility
evidence while keeping causality and confidence scoring in mSCS.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Linked graph-source rows | 17,242 |
| Evidence-route records | 334,184 |
| Literature-expansion annotations | 516 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,972 |
| Normalized route edges | 1,275,845 |

The release validator passed with zero errors; the existing stable-locator
warning remains. No graph edges, causal assertions, or database confidence
scores were created.
