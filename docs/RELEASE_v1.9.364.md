# mSCIdblit release v1.9.364

This release adds three primary-literature route overlays for unresolved
canonical ligands: HMGB1→RAGE→NF-κB/p65 phosphorylation→NF-κB→tissue-factor
output, VEGFA→KDR→ERK1/2→EGR1→tissue-factor output, and
IGF1→IGF1R→PI3K-AKT1→NF-κB→VEGFA gene expression.

These are evidence-layer routes for mSCS plausibility analysis. They preserve
the source-specific models and measured outputs, while unresolved handoffs
remain explicit. No causal graph edges, confidence scores, or traversal
permissions are created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,385 → 596,388
- Route nodes: 2,502,523 → 2,502,536
- Route edges: 2,301,905 → 2,301,915
- Literature-expansion rows: 30,271 → 30,274
- Full-sequence curation candidates: 15,494 → 15,497
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,745 → 9,748
- Coverage summary: 179 full functional-output, 169 full target-gene,
  1,460 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locators include [PMID:25490770](https://pubmed.ncbi.nlm.nih.gov/25490770/),
[PMID:19652887](https://pubmed.ncbi.nlm.nih.gov/19652887/),
[PMID:10339488](https://pubmed.ncbi.nlm.nih.gov/10339488/),
[PMID:11149911](https://pubmed.ncbi.nlm.nih.gov/11149911/), and
[PMID:15277220](https://pubmed.ncbi.nlm.nih.gov/15277220/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion605/`
