# mSCIdblit release v1.9.308

This release extends the all-ligand evidence layer with one composite primary
route and a conservative repair of uniquely resolvable node-ID aliases in the
literature-expansion and signaling-route tables. The graph itself is
unchanged.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-all-ligand-route-repair-and-dadle-creb-509`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion509/`

The added route is DADLE→OPRD1/DOR→GNAI→CREB phosphorylation. DADLE/DOR and
DOR/GNAI are directly source-linked; the CREB layer is a bounded
delta-opioid-agonist overlay and the target-gene layer remains explicit as
missing. It is evidence-only and does not create a causal edge or confidence
score.

The alias repair changed 11,215 evidence-layer node-ID cells where the stored
label mapped uniquely to one node and any explicit edge endpoint agreed with
the replacement. Ambiguous or edge-conflicting cells remain unchanged and are
reported in `route_node_id_repair_summary.json`.

All-ligand coverage:

- Ligand nodes indexed: 2,613
- Full target-gene route: 59
- Full intracellular–TF functional-output route: 174
- Partial downstream route: 1,576
- Ligand–receptor-only: 804

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 591,166
- Route nodes: 2,478,540
- Route edges: 2,283,137
- Full-sequence curation queue: 15,452
- Literature-expansion annotations: 25,052

The graph validator and gzip integrity checks passed. The existing validator
warning concerning legacy evidence sources without stable locators remains.
