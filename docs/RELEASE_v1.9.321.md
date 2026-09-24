# mSCIdblit release v1.9.321

Release ID: `module20_24_mechanism_graph:2026-09-24-il36-shared-relay-queue-529`

This release begins the next all-ligand route-curation tranche by adding
three evidence-layer sequences for IL-36α, IL-36β, and IL-36γ. Each route
retains the ligand–IL1RL2:IL1RAP receptor record, the shared
MyD88/IRAK/NF-κB/MAPK intracellular layer, the NF-κB p65/p50 transcription
factor layer, and the CXCL1 target-gene output. The receptor-to-relay and
relay-to-TF handoffs remain explicitly unresolved because the supporting
primary studies establish complementary layers rather than one asserted
end-to-end chain. No graph edges, causal assertions, or confidence scores are
created.

The release contains 591,803 signaling route-evidence rows and 25,689
literature-expansion rows. The graph remains unchanged at 11,988 nodes,
14,831 graph edges, and 15,107 edge-source records. The all-ligand curation
queue contains 15,097 candidates across 1,862 ligands, including 9,302 P1
review candidates.

Role-aware coverage is now 139 full target-gene ligands, 110 full
functional-output ligands, 1,556 partial downstream ligands, and 808
ligand–receptor-only ligands. These are evidence-layer summaries, not
confidence scores or causal traversal permissions.

Primary locators for the new IL-36 relay routes include PMID:14734551,
PMID:24829417, PMID:29180446, DOI:10.1074/jbc.M400117200, and
DOI:10.1074/jbc.M117.805739.

Validation passed with no errors. The only validator warning is the inherited
warning that some evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion529/`
- `scripts/build_il36_shared_relay_full_routes.py`
