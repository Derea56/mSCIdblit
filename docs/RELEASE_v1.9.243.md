# mSCIdblit release v1.9.243

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-all-ligand-source-linked-366`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion366/`

## All-ligand source-linked route exposure

This release exposes curated historical Module 21B route annotations for known
ligand–receptor pairs across the graph. It adds 5,318 source-linked evidence
routes covering 1,844 ligand labels and 3,085 ligand–receptor edges. The
records span direct `ligand>receptor>output` observations, partial routes with
unresolved intracellular or TF layers, and 24 additional
`ligand>receptor>intracellular>TF>target_gene_expression` records.

Unknown layers remain explicit rather than being inferred. The imported routes
retain primary locators, source queue/evidence identifiers, model context,
limitations, `causal_status=not_asserted`, and
`traversal_status=evidence_route_not_causal`. They are available to mSCS as
route-plausibility evidence, while mSCS remains responsible for contextual
evaluation and confidence assignment.

The batch required an explicit ligand and receptor, valid current graph
references, source queue/evidence links, and a stable primary locator. The
2,178 historical records without an explicit ligand or receptor were not
promoted and remain available for later curation.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 339,546 |
| Literature-expansion annotations | 5,878 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,304,713 |
| Normalized route edges | 1,282,828 |

The release validator passed with zero errors. No graph edges, causal edges, or
database confidence scores were created by this release.
