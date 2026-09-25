# mSCIdblit release v1.9.348

This release adds a primary-literature FGF2→FGFR1→ERK/Elk-1→c-Fos evidence
route to the all-ligand route layer. The route composes complementary primary
studies and preserves the receptor-to-relay and relay-to-TF handoffs as
unresolved for mSCS evaluation.

The addition is evidence-layer data only. It does not create graph edges,
causal assertions, confidence scores, or a claim that one experiment
demonstrates the complete sequence.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,344 → 596,345
- Route nodes: 2,501,966 → 2,502,341
- Route edges: 2,301,759 → 2,301,763
- Literature-expansion rows: 30,230 → 30,231
- Full-sequence curation candidates: 15,461 → 15,462
- Unique ligands in the curation queue: 1,867 (unchanged)
- P1 review candidates: 9,725 (unchanged)

The route uses the
`ligand_receptor_intracellular_tf_target_missing_direct_tf_edges` tier and
remains `causal_status=not_asserted` with
`traversal_status=evidence_route_not_causal`. Validation passed with no
errors; the inherited warning remains that some evidence sources lack stable
public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion588/`
