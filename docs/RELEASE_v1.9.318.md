# mSCIdblit release v1.9.318

Release ID: `module20_24_mechanism_graph:2026-09-24-gdf11-smad-fst-route-queue-523`

This release adds one source-linked GDF11 route ending in FST gene expression:
GDF11→ACVR2B:ALK5→SMAD transcriptional program→SMAD2/3→FST. The
receptor-to-SMAD and SMAD-program-to-TF handoffs remain explicit missing-link
fields; the SMAD2/3→FST target-gene edge is graph-linked evidence.

The cumulative release contains 591,800 signaling route-evidence rows and
25,686 literature-expansion rows. The graph remains unchanged at 11,988 nodes,
14,831 graph edges, and 15,107 edge-source records. The rebuilt all-ligand
curation queue contains 15,094 candidates across 1,862 ligands, including
9,302 P1 review candidates.

Role-aware coverage is now 64 full target-gene ligands, 182 full
functional-output ligands, 1,563 partial downstream ligands, and 804
ligand–receptor-only ligands. These are evidence-layer summaries, not
confidence scores or causal traversal permissions.

Validation passed with no errors. The only validator warning is the inherited
warning that some evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion523/`
- `work/module_b_consolidation/module21b/module21b_literature_expansion_batch287_gdf11_smads_fst.json`

