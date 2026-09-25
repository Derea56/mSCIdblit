# mSCIdblit release v1.9.375

This release adds one primary-literature evidence route for glutamate/NMDA
signaling through ERK1/2 and Elk-1 to c-Fos gene expression. The route makes a
distinct transcription-factor branch retrievable alongside the existing
glutamate/CREB route.

The route is source-linked evidence for mSCS plausibility analysis. The
receptor-to-ERK, ERK-to-Elk-1, and Elk-1-to-c-Fos handoffs remain explicitly
unasserted because the cited studies use complementary primary-neuron models
and do not establish one end-to-end graph chain. No causal graph edges,
confidence scores, or traversal permissions are created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,411 → 596,412
- Route nodes: 2,502,632 → 2,502,637
- Route edges: 2,301,988 → 2,301,992
- Literature-expansion rows: 30,297 → 30,298
- Full-sequence curation candidates: 15,512 → 15,513
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,755 (unchanged)
- Coverage summary: 182 full functional-output, 173 full target-gene,
  1,453 partial downstream, and 805 ligand–receptor-only ligand rows

Primary sources: [NMDA receptor, ERK, Elk-1, and c-fos transcription in
primary cortical neurons](https://pubmed.ncbi.nlm.nih.gov/8757255/) and
[glutamate/NMDA-dependent CREB and c-fos responses in primary striatal
neurons](https://pubmed.ncbi.nlm.nih.gov/10414964/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion616/`
