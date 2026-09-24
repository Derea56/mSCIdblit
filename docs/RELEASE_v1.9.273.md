# mSCIdblit release v1.9.273

This release completes the next source-linked all-ligand expansion pass. It
adds 2,390 evidence-layer route annotations relative to v1.9.272 across 50
ligand labels, including 2,125 additional
`ligand>receptor>intracellular>TF>target_gene_expression` records. The
remaining additions retain either the TF or intracellular layer as unresolved
when the primary evidence did not support that handoff.

Graph identifier: `module20_24_mechanism_graph:2026-09-24-all-ligand-full-intermediate-second-pass-408`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion408/`

The release contains 10,545 literature-expansion annotations. Every new
annotation has source linkage and a primary literature locator. All annotations
remain evidence-only (`causal_status=not_asserted`,
`traversal_status=evidence_route_not_causal`); no graph edges, causal
assertions, or database confidence scores are created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 576,659
- Route nodes: 2,409,529
- Route edges: 2,229,034
- Full-sequence curation queue: 15,313
- Literature-expansion annotations: 10,545

The queue contains 9,280 P1 candidates across 1,862 unique ligands. It
contains 12,422 routes with an intracellular continuation layer and 9,665 with
a transcription-factor layer. The current automated source-linked selectors
produce no further eligible rows on this release; deeper progress requires
paper-level review of the remaining queue. Validation passed with no errors;
the retained warning concerns evidence sources without stable public locators.
