# mSCIdblit release v1.9.326

Release ID: `module20_24_mechanism_graph:2026-09-25-tgfb2-target-queue-543`

This release adds three primary-literature evidence routes for the TGF-beta
family: TGFβ3→TGFBR1/2→SMAD2/3-SMAD4→CTGF, TGFβ3→TGFBR1/2→SMAD2/3-SMAD4→SMAD7,
and TGFβ2→TGFBR1/2→SMAD2/3-SMAD4→COL1A1. The routes are supported by
ligand-specific fibroblast or epithelial-cell studies and retain explicit
receptor-to-relay, relay-to-TF, and TF-to-target missing-link flags.

The annotations remain evidence-only: no graph edges, causal assertions, or
confidence scores are created. Primary support is provided by PMID:16772929
for TGFβ3-induced CTGF and SMAD7 expression in mouse fibroblasts and
PMID:24755068 for TGFβ2-induced collagen-I expression with SMAD2/3 dependence
in human lens epithelial cells.

The final bundle contains 591,825 signaling route-evidence rows and 25,711
literature-expansion rows. The graph remains unchanged at 11,988 nodes,
14,831 graph edges, and 15,107 edge-source records. The full-sequence
curation queue contains 15,111 candidates across 1,862 ligands, including
9,302 P1 review candidates.

Role-aware coverage is now 149 full target-gene ligands, 110 full
functional-output ligands, 1,546 partial downstream ligands, and 808
ligand–receptor-only ligands. These are evidence-layer summaries, not
confidence scores or causal traversal permissions.

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion543/`
- `scripts/build_primary_tgfb3_target_routes.py`
- `scripts/build_primary_tgfb2_target_routes.py`
