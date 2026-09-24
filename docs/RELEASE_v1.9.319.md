# mSCIdblit release v1.9.319

Release ID: `module20_24_mechanism_graph:2026-09-24-all-ligand-tf-role-repair-queue-525`

This release applies a narrow semantic repair across the all-ligand route
catalog. Nine existing route nodes that are explicitly used in
`transcription_factor_node_id` fields and supported by existing evidence-gated
TF, transcriptional-complex, or pathway records now also carry a
`transcription_factor` role. The repair includes EGR1, LEF1, TCF7L2, AP-1,
STAT1, STAT2, and related composite TF programs. It does not add graph edges,
route evidence rows, causal assertions, or confidence scores.

The release contains 591,800 signaling route-evidence rows and 25,686
literature-expansion rows. The graph remains unchanged at 11,988 nodes,
14,831 graph edges, and 15,107 edge-source records. The all-ligand curation
queue contains 15,094 candidates across 1,862 ligands, including 9,302 P1
review candidates.

Role-aware coverage is 62 full target-gene ligands, 184 full
functional-output ligands, 1,559 partial downstream ligands, and 808
ligand–receptor-only ligands. HBEGF is now correctly classified as having a
full evidence route to CYP24A1 through the existing HBEGF→EGFR→ERK1/2→EGR1
route record. These are evidence-layer summaries, not confidence scores or
causal traversal permissions.

Validation passed with no errors. The only validator warning is the inherited
warning that some evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion525/`
- `scripts/repair_missing_transcription_factor_roles.py`
