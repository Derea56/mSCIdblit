# mSCIdblit release v1.9.367

This release adds a primary-literature SPP1/Spp1→ITGAV:ITGB3→PI3K-AKT1→NF-κB
route with a measured NF-κB-dependent migration output. The route is retained
as an evidence-layer overlay for mSCS plausibility analysis; the study does
not establish a promoter-resolved target gene or direct causal handoffs for
every intermediate.

No causal graph edges, confidence scores, or traversal permissions are
created. The all-ligand curation queue is regenerated so mSCS can consume the
new route together with the existing evidence layers.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,392 → 596,393
- Route nodes: 2,502,559 (unchanged)
- Route edges: 2,301,933 (unchanged)
- Literature-expansion rows: 30,278 → 30,279
- Full-sequence curation candidates: 15,501 → 15,502
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,752 → 9,753
- Coverage summary: 181 full functional-output, 172 full target-gene,
  1,455 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locator: [PMID:18996613](https://pubmed.ncbi.nlm.nih.gov/18996613/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion608/`
