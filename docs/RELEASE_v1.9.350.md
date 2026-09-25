# mSCIdblit release v1.9.350

This release adds a primary-literature WNT5A→ROR2→JNK→c-Jun-associated
RANK-expression route. The route preserves a complete ligand, receptor,
intracellular and transcription-factor sequence while retaining the missing
dedicated RANK target-gene node as an explicit output-layer gap.

This is evidence-layer data only. It does not create graph edges, causal
assertions, confidence scores, or a claim that one experiment demonstrates the
complete sequence.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,346 → 596,347
- Route nodes: 2,502,346 → 2,502,351
- Route edges: 2,301,767 → 2,301,771
- Literature-expansion rows: 30,232 → 30,233
- Full-sequence curation candidates: 15,463 → 15,464
- Unique ligands in the curation queue: 1,867 (unchanged)
- P1 review candidates: 9,725 → 9,726

The route uses the
`ligand_receptor_intracellular_tf_output_missing_target_gene` tier and
remains `causal_status=not_asserted` with
`traversal_status=evidence_route_not_causal`. Validation passed with no
errors; the inherited warning remains that some evidence sources lack stable
public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion590/`
