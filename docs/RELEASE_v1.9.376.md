# mSCIdblit release v1.9.376

This release adds one primary-literature evidence route for NT-3/TrkC
signaling through ERK and CREB to BCL2 gene expression. It expands the
retrievable transcription-factor evidence for NT-3 alongside the existing
partial route records.

The route is source-linked evidence for mSCS plausibility analysis. The
TrkC-to-ERK, ERK-to-CREB, and CREB-to-BCL2 handoffs remain explicitly
unasserted because the cited primary studies use complementary cell models and
do not establish one end-to-end graph chain. No causal graph edges, confidence
scores, or traversal permissions are created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,412 → 596,413
- Route nodes: 2,502,637 → 2,502,642
- Route edges: 2,301,992 → 2,301,996
- Literature-expansion rows: 30,298 → 30,299
- Full-sequence curation candidates: 15,513 (unchanged after deduplication)
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,755 (unchanged)
- Coverage summary: 182 full functional-output, 173 full target-gene,
  1,453 partial downstream, and 805 ligand–receptor-only ligand rows

Primary sources: [NT-3/TrkC signaling through ERK and CREB in cultured
neurons](https://pubmed.ncbi.nlm.nih.gov/27122038/) and [CREB-dependent
NT-3 regulation of BCL2 in oligodendrocyte progenitors](https://pubmed.ncbi.nlm.nih.gov/15140194/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion617/`
