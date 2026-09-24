# mSCIdblit release v1.9.286

This release adds two primary-literature evidence routes for TSP1/THBS1 and
C1q. The additions preserve TSP1→CD47→NF-κB/AP-1→IL-1β modulation and
C1q→LAIR1→CREB/NF-κB→IL-10/anti-inflammatory output, while explicitly
retaining the unresolved intracellular handoffs.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-receptor-output-gap-447`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion447/`

Both rows retain primary locators, explicit limitations,
`causal_status=not_asserted`, and `traversal_status=evidence_route_not_causal`.
No graph edges or database confidence scores were created. The C1q route uses
the established annotation tier for a ligand–receptor–TF–output route with the
intracellular continuation unresolved.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,211
- Route nodes: 2,463,796
- Route edges: 2,271,763
- Full-sequence curation queue: 15,402
- Literature-expansion annotations: 22,097
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,632

The graph validator passed with no errors. The remaining warning concerns
legacy evidence sources without stable locators and is unchanged from the
previous release.
