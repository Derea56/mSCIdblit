# mSCIdblit release v1.9.317

Release ID: `module20_24_mechanism_graph:2026-09-24-bmp-smad-id1-route-queue-521`

This release adds four source-linked BMP-family route annotations ending in
ID1 gene expression: BMP9/GDF2→ACVRL1/ALK1→SMAD transcriptional program→SMAD1/5/8→ID1,
BMP10→ACVRL1/ACVR2A→the same SMAD layer→ID1, GDF6/BMP13→BMPR1A/ALK3→the
same SMAD layer→ID1, and GDF7/BMP12→BMPR1A→the same SMAD layer→ID1. The
receptor-to-SMAD and SMAD-program-to-TF handoffs remain explicit missing-link
fields; the SMAD1/5/8→ID1 target edge is graph-linked evidence.

The cumulative release contains 591,799 signaling route-evidence rows and
25,685 literature-expansion rows. The graph remains unchanged at 11,988 nodes,
14,831 graph edges, and 15,107 edge-source records. The rebuilt all-ligand
curation queue contains 15,093 candidates across 1,862 ligands, including
9,302 P1 review candidates.

Role-aware coverage is now 63 full target-gene ligands, 182 full
functional-output ligands, 1,564 partial downstream ligands, and 804
ligand–receptor-only ligands. These are evidence-layer summaries, not
confidence scores or causal traversal permissions.

Validation passed with no errors. The only validator warning is the inherited
warning that some evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion521/`
- `work/module_b_consolidation/module21b/module21b_literature_expansion_batch286_bmp_smads_id1.json`

