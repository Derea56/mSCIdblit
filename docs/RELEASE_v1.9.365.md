# mSCIdblit release v1.9.365

This release adds two primary-literature route overlays for partial ligand
coverage: CX3CL1→CX3CR1→RAF/MEK/ERK→NF-κB→MMP3 gene expression and
FN1→ITGA5:ITGB1→ILK→AP-1 reporter activity.

These are evidence-layer routes for mSCS plausibility analysis. They preserve
the source-specific models and measured outputs, while unresolved handoffs
remain explicit. No causal graph edges, confidence scores, or traversal
permissions are created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,388 → 596,390
- Route nodes: 2,502,536 → 2,502,545
- Route edges: 2,301,915 → 2,301,922
- Literature-expansion rows: 30,274 → 30,276
- Full-sequence curation candidates: 15,497 → 15,499
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,748 → 9,750
- Coverage summary: 180 full functional-output, 170 full target-gene,
  1,458 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locators include [PMID:29268768](https://pubmed.ncbi.nlm.nih.gov/29268768/)
and [PMID:10523630](https://pubmed.ncbi.nlm.nih.gov/10523630/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion606/`
