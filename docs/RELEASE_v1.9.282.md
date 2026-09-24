# mSCIdblit release v1.9.282

This release adds 456 all-ligand full-sequence evidence-route annotations
across 21 ligand labels. The annotations compose source-linked
ligand→receptor→intracellular continuation→TF→target-gene observations while
retaining the primary locators and unresolved molecular handoffs for mSCS to
evaluate.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-all-ligand-full-sequence-432`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion432/`

All new rows use
`ligand>receptor>intracellular>TF>target_gene_expression`, retain
`causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`, and do not create graph edges or
database confidence scores. A deterministic layer-identity deduplication step
prevents repeated graph compositions within one source queue from producing a
Cartesian-product explosion.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,197
- Route nodes: 2,463,737
- Route edges: 2,271,718
- Full-sequence curation queue: 15,389
- Literature-expansion annotations: 22,083
- Unique ligand candidates in queue: 1,862

The full-sequence queue remains a primary-literature curation worklist. It does
not imply that every composed handoff was demonstrated in one paper, and the
graph validator passed with no errors.
