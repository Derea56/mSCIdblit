# mSCIdblit release v1.9.323

Release ID: `module20_24_mechanism_graph:2026-09-24-il19-jak-stat3-queue-535`

This release extends the all-ligand route-curation tranche with four IL-20
evidence routes and two IL-19 evidence routes. The routes cover the relevant
IL-20 receptor branches, JAK1/STAT3 pathway activity, and epithelial
target-gene outputs. The receptor-to-JAK1, JAK1-to-STAT3, and STAT3-to-target
handoffs remain explicit missing links; no graph edges, causal assertions, or
confidence scores are created.

Together with the prior IL-36 and IL-24 tranches, the release contains 591,813
signaling route-evidence rows and 25,699 literature-expansion rows. The graph
remains unchanged at 11,988 nodes, 14,831 graph edges, and 15,107 edge-source
records. The all-ligand full-sequence curation queue contains 15,102
candidates across 1,862 ligands, including 9,302 P1 review candidates.

Role-aware coverage is now 142 full target-gene ligands, 110 full
functional-output ligands, 1,553 partial downstream ligands, and 808
ligand–receptor-only ligands. These are evidence-layer summaries, not
confidence scores or causal traversal permissions.

Primary locators for the new routes include PMID:11564763,
PMID:12351624, PMID:17277128, PMID:25046339, PMID:37884352,
DOI:10.4049/jimmunol.167.7.3545, and
DOI:10.4049/jimmunol.178.4.2229.

Validation passed with no errors. The only validator warning is the inherited
warning that some evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion535/`
- `scripts/build_il19_jak_stat3_routes.py`
- `scripts/build_il20_jak_stat3_routes.py`
