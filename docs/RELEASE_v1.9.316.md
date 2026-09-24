# mSCIdblit release v1.9.316

Release ID: `module20_24_mechanism_graph:2026-09-24-wnt3a-output-route-queue-519`

This release adds seven bounded primary-literature WNT3A route annotations: six
WNT3A→FZD8:LRP6→target-gene-expression records for MYC, CCND1, CDKN1A, TFRC,
PLF1, and RAMP3, plus one WNT3A→FZD8:LRP6→LRP6-signalosome→TCF-reporter
functional-readout record. The receptor-to-signalosome, signalosome-to-TF,
and TF-to-target handoffs remain explicit missing-link fields where the
exported graph does not contain a direct edge.

The release also includes the preceding all-ligand source-linked composition
tranche: 608 annotations across IL4, TNF, and Il34. The rebuilt curation queue
contains 15,089 deduplicated candidates across 1,862 ligands, with 9,302 P1
review candidates. The graph remains unchanged: 11,988 nodes, 14,831 graph
edges, and 15,107 edge-source records. The release contains 591,795 signaling
route-evidence rows and 25,681 literature-expansion rows.

The semantic coverage status counts remain 182 full functional-output ligands,
59 full target-gene ligands, 1,568 partial downstream ligands, and 804
ligand–receptor-only ligands. These counts are role-aware summaries, not
confidence scores or causal traversal permissions.

Validation passed with no errors. The only validator warning is the inherited
warning that some evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion519/`
- `work/module_b_consolidation/module21b/module21b_literature_expansion_batch284_source_linked_full_sequence.json`
- `work/module_b_consolidation/module21b/module21b_literature_expansion_batch285_wnt3a_outputs.json`

