# mSCIdblit release v1.9.284

This release adds four primary-literature evidence routes across four ligand
labels: Osteopontin/SPP1, Galectin-3/LGALS3, dopamine, and ATP. The additions
extend the all-ligand route layer with SPP1→integrin αVβ3→NF-κB→HIF-1→BMI1
expression, Galectin-3→TLR4→MAPK/NF-κB→IL-6/CCL5 output,
dopamine→DRD1→PKA/CREB→cFos expression, and ATP→P2X7→NF-κB output.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-next-gap-438`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion438/`

All four rows retain primary locators, explicit limitations,
`causal_status=not_asserted`, and `traversal_status=evidence_route_not_causal`.
No graph edges or database confidence scores were created. The Galectin-3 and
ATP rows remain functional-output routes because the current graph does not
contain clean terminal target-gene nodes for those source-supported readouts.
The SPP1 and dopamine rows retain target-gene nodes, while their intermediate
handoffs remain explicitly unasserted.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,205
- Route nodes: 2,463,772
- Route edges: 2,271,745
- Full-sequence curation queue: 15,396
- Literature-expansion annotations: 22,091
- Unique ligand candidates in queue: 1,862

The graph validator passed with no errors. The remaining warning concerns
legacy evidence sources without stable locators and is unchanged from the
previous release.
