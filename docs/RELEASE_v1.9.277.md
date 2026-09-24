# mSCIdblit release v1.9.277

This release promotes 330 source-linked `Il15` alias routes onto the existing
canonical IL-15 TF-to-target evidence layer. The routes expose the alias as a
separate ligand input while retaining exact receptor, TF, and target-gene
identifiers from the existing evidence layer.

Graph identifier: `module20_24_mechanism_graph:2026-09-24-alias-target-promotion-419`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion419/`

All 330 additions use the full route shape
`ligand>receptor>intracellular>TF>target_gene_expression`. They retain the
receptor-to-intracellular handoff as unresolved when no exact alias-receptor
edge exists, and preserve the unresolved intracellular-to-TF layer. Stable
public locators are retained separately from internal evidence identifiers.
All annotations remain evidence-only (`causal_status=not_asserted`,
`traversal_status=evidence_route_not_causal`); no graph edges or database
confidence scores are created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 579,375
- Route nodes: 2,423,090
- Route edges: 2,239,879
- Full-sequence curation queue: 15,325
- Literature-expansion annotations: 13,261
- Unique ligand candidates in queue: 1,862

Validation passed with no errors. The retained warning concerns evidence
sources without stable public locators. The queue remains a curation worklist,
not a confidence layer or a claim that every missing link has been resolved.
