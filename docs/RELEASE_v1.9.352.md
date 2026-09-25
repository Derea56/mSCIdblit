# mSCIdblit release v1.9.352

This release adds a primary-literature acetylcholine→M1 muscarinic
receptor→ERK→EGR1 transcription-factor output route. The route records the
observed TF-level endpoint while preserving the lack of a dedicated terminal
target-gene node for this composition.

This is evidence-layer data only. It does not create graph edges, causal
assertions, confidence scores, or a claim that one experiment demonstrates the
complete sequence.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,348 → 596,349
- Route nodes: 2,502,356 → 2,502,361
- Route edges: 2,301,775 → 2,301,779
- Literature-expansion rows: 30,234 → 30,235
- Full-sequence curation candidates: 15,465 → 15,466
- Unique ligands in the curation queue: 1,867 (unchanged)
- P1 review candidates: 9,726 → 9,727

The route uses the
`ligand_receptor_intracellular_tf_output_missing_target_gene` tier and
remains `causal_status=not_asserted` with
`traversal_status=evidence_route_not_causal`. Validation passed with no
errors; the inherited warning remains that some evidence sources lack stable
public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion592/`
