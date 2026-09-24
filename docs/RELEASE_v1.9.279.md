# mSCIdblit release v1.9.279

This release adds 6,655 source-linked composed full-sequence route records
across 34 ligand labels. Each record joins a relay, TF, and target-gene
observation for the same ligand/receptor pair and downstream source queue, with
public literature locators retained for audit. The records are intended to
make plausible routes traversable by mSCS while preserving the distinction
between shared-source evidence and a single-paper causal chain.

Graph identifier: `module20_24_mechanism_graph:2026-09-24-source-linked-full-sequence-queue-423`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion423/`

The new rows use
`ligand>receptor>intracellular>TF>target_gene_expression`, retain
`causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`, and leave unresolved
intracellular-to-TF and TF-to-target handoffs explicit unless an existing graph
edge is present. No graph edges or database confidence scores are created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 587,632
- Route nodes: 2,460,959
- Route edges: 2,269,493
- Full-sequence curation queue: 15,359
- Literature-expansion annotations: 21,518
- Unique ligand candidates in queue: 1,862

The full-sequence queue remains a primary-literature curation worklist. It does
not assign confidence and does not imply that every composed handoff has been
demonstrated experimentally. Graph validation passed with no errors; the
retained warning concerns evidence sources without stable public locators.
