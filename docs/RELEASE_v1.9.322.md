# mSCIdblit release v1.9.322

Release ID: `module20_24_mechanism_graph:2026-09-24-il24-jak-stat3-queue-531`

This release extends the all-ligand route-curation tranche with four IL-24
evidence routes covering the type-I and type-II IL-20 receptor branches and
the S100A7 and KRT16 target-gene outputs. The routes retain primary evidence
for receptor engagement, JAK1/STAT3 pathway activity, STAT3 nuclear activity,
and epithelial target expression. Receptor-to-JAK1, JAK1-to-STAT3, and
STAT3-to-target handoffs remain explicit missing links; no graph edges, causal
assertions, or confidence scores are created.

Together with the prior IL-36 tranche, the release contains 591,807 signaling
route-evidence rows and 25,693 literature-expansion rows. The graph remains
unchanged at 11,988 nodes, 14,831 graph edges, and 15,107 edge-source records.
The all-ligand curation queue contains 15,099 candidates across 1,862 ligands,
including 9,302 P1 review candidates.

Role-aware coverage is now 140 full target-gene ligands, 110 full
functional-output ligands, 1,555 partial downstream ligands, and 808
ligand–receptor-only ligands. These are evidence-layer summaries, not
confidence scores or causal traversal permissions.

Primary locators for the new IL-24 routes include PMID:17277128,
PMID:25168428, PMID:38752989, DOI:10.4049/jimmunol.178.4.2229, and
DOI:10.1016/j.taap.2014.08.019.

Validation passed with no errors. The only validator warning is the inherited
warning that some evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion531/`
- `scripts/build_il24_jak_stat3_routes.py`
