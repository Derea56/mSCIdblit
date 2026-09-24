# mSCIdblit release v1.9.272

This release extends the all-ligand full-intermediate curation pass with 672
additional source-linked route annotations spanning 138 ligand labels. The
annotations preserve ligand, receptor, intracellular continuation, TF, and
target-gene/output layers while leaving unsupported handoffs unresolved.

Graph identifier: `module20_24_mechanism_graph:2026-09-24-all-ligand-full-intermediate-curation-404`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion404/`

The release contains 8,155 literature-expansion annotations: 7,483 carried
forward and 672 added in this pass. Every new annotation has a stable primary
literature locator. All 672 remain evidence-only (`causal_status=not_asserted`,
`traversal_status=evidence_route_not_causal`); no graph edges, causal
assertions, or database confidence scores are created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 574,269
- Route nodes: 2,397,857
- Route edges: 2,219,752
- Full-sequence curation queue: 15,302
- Literature-expansion annotations: 8,155

The queue still contains 9,280 P1 candidates across 1,862 unique ligands. It
contains 12,411 routes with an intracellular continuation layer and 9,654 with
a transcription-factor layer. Validation passed with no errors; the retained
warning concerns evidence sources without stable public locators.
