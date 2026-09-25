# mSCIdblit release v1.9.324

Release ID: `module20_24_mechanism_graph:2026-09-24-growth-factor-tf-queue-537`

This release adds six primary-literature evidence routes for four canonical
ligands: two G-CSF/STAT3 routes to MMP2 and MMP9, two VEGFA/VEGFR2/STAT3
routes to MYC and SOX2, one PGE2/EP4/ERK/CREB route to EGR1, and one
PDGFB/PDGFR/ERK/Elk-1 route to EGR1. These routes retain explicit
receptor-to-intermediate, intermediate-to-TF, and TF-to-target missing-link
flags; no graph edges, causal assertions, or confidence scores are created.

The four ligands now have `full_target_gene_route` evidence-layer coverage.
The release contains 591,819 signaling route-evidence rows and 25,705
literature-expansion rows. The graph remains unchanged at 11,988 nodes,
14,831 graph edges, and 15,107 edge-source records. The full-sequence
curation queue contains 15,106 candidates across 1,862 ligands, including
9,302 P1 review candidates.

Role-aware coverage is now 146 full target-gene ligands, 110 full
functional-output ligands, 1,549 partial downstream ligands, and 808
ligand–receptor-only ligands. These are evidence-layer summaries, not
confidence scores or causal traversal permissions.

Primary locators for the new routes include PMID:7521688, PMID:10961983,
PMID:15003938, PMID:15492129, PMID:17631291, PMID:25151964, and
PMID:32242230.

Validation passed with no errors. The only validator warning is the inherited
warning that some evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion537/`
- `scripts/build_growth_factor_tf_routes.py`
