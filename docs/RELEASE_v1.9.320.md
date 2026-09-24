# mSCIdblit release v1.9.320

Release ID: `module20_24_mechanism_graph:2026-09-24-target-gene-role-repair-queue-527`

This release applies a bounded target-gene role repair across the all-ligand
route catalog. It adds `target_gene` roles to 314 existing endpoint nodes that
are supported by evidence-gated TF-target edges or locator-bearing
literature-expansion routes. Program, pathway, branch, and complex nodes are
excluded from the repair, as are nodes that remain ligand or receptor inputs.
No graph edges, route evidence rows, causal assertions, or confidence scores
are created.

The release contains 591,800 signaling route-evidence rows and 25,686
literature-expansion rows. The graph remains unchanged at 11,988 nodes,
14,831 graph edges, and 15,107 edge-source records. The all-ligand curation
queue contains 15,094 candidates across 1,862 ligands, including 9,302 P1
review candidates.

Role-aware coverage is now 136 full target-gene ligands, 110 full
functional-output ligands, 1,559 partial downstream ligands, and 808
ligand–receptor-only ligands. The increase reflects endpoint role repair of
existing evidence routes, not new biological claims. These are evidence-layer
summaries, not confidence scores or causal traversal permissions.

Validation passed with no errors. The only validator warning is the inherited
warning that some evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion527/`
- `scripts/repair_missing_target_gene_roles.py`
