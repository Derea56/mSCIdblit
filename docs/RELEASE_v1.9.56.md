# mSCIdblit v1.9.56

This release resolves the first large canonical ligand–receptor tranche by
adding 594 evidence-layer `ligand>receptor>output` route annotations. Every
route is backed by a canonical ligand–receptor edge, a primary downstream
evidence record, and a non-unknown output classification. The tranche includes
cellular, phosphorylation/activation, transcriptional, secreted, localization,
reporter, phagocytic, cleavage and target-gene-expression readouts.

These records deliberately stop at the observed output. Intracellular relays,
transcription factors and target genes are left unmapped unless explicitly
identified in the source evidence; no causal traversal, confidence score or
new graph edge is created. The primary locators, context qualifiers and
limitations remain attached to each route for downstream mSCS evaluation.

- Route evidence: 17,282 → 17,876 records
- Graph topology: 11,952 nodes and 14,722 edges, unchanged
- Downstream queue candidates covered: 1,205 → 1,799
- Remaining downstream queue candidates: 1,532
- Remaining P1 candidates: 500
- Added route tier: 594 `ligand_receptor_output_annotation_missing_intracellular_and_tf` records

The corresponding bundle is
`mechanism_graph_module20_24_v2026_09_16_literature_expansion151`.
