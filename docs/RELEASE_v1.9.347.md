# mSCIdblit release v1.9.347

This release applies the all-ligand full-intermediate route-composition pass
to the current graph snapshot. It adds 74 evidence-layer routes across 23
ligands and 23 ligand–receptor pairs. Each route records the ordered
ligand→receptor→intracellular continuation→TF→target-gene expression shape,
while preserving any unsupported handoffs as unresolved for mSCS.

The routes are composed only from existing source-linked primary-literature
components. They do not create graph edges, causal assertions, confidence
scores, or universal ligand-specific signaling claims.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,270 → 596,344
- Route nodes: 2,501,966
- Route edges: 2,301,759
- Literature-expansion rows: 30,156 → 30,230
- Full-sequence curation candidates: 15,457 → 15,461
- Unique ligands in the curation queue: 1,867 (unchanged)
- P1 review candidates: 9,725 (unchanged)

All 74 additions use the `ligand_receptor_intracellular_tf_target_missing_direct_tf_edges`
route tier and remain `causal_status=not_asserted` with
`traversal_status=evidence_route_not_causal`. Validation passed with no
errors; the inherited warning remains that some evidence sources lack stable
public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion587/`
