# mSCIdblit release v1.9.274

This release materializes an additional shared-anchor curation pass for the
all-ligand route queue. It adds 2,376 evidence-layer annotations across 47
ligand labels by joining target-gene output records with intracellular/TF
records that share an exact route-evidence identifier for the same ligand and
receptor. The resulting full-route annotations retain the shared anchor and
the component provenance so mSCS can evaluate the linkage explicitly.

Graph identifier: `module20_24_mechanism_graph:2026-09-24-all-ligand-shared-route-full-sequence-410`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion410/`

The release contains 12,921 literature-expansion annotations, including 6,307
`ligand>receptor>intracellular>TF>target_gene_expression` records. All new
annotations have stable primary literature locators and remain evidence-only
(`causal_status=not_asserted`, `traversal_status=evidence_route_not_causal`);
no graph edges, causal assertions, or database confidence scores are created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 579,035
- Route nodes: 2,421,394
- Route edges: 2,238,523
- Full-sequence curation queue: 15,313
- Literature-expansion annotations: 12,921

The queue contains 9,280 P1 candidates across 1,862 unique ligands. It
contains 12,422 routes with an intracellular continuation layer and 9,665 with
a transcription-factor layer. The automated source-linked and exact shared-
anchor selectors produce no further eligible rows on this release; remaining
progress requires deeper paper-level review. Validation passed with no errors;
the retained warning concerns evidence sources without stable public locators.
