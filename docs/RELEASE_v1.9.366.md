# mSCIdblit release v1.9.366

This release adds two primary-literature route overlays for thrombospondin
ligands: TSP1/THBS1→CD36→TLR4/MD2-MyD88-p38-NF-κB→TNF gene expression and
THBS2→NOTCH3:JAG1→NOTCH3/NICD3→RBPJ/CSL→HES1 target-gene expression.

These are evidence-layer routes for mSCS plausibility analysis. They preserve
the source-specific models and measured outputs, while unresolved handoffs
remain explicit. No causal graph edges, confidence scores, or traversal
permissions are created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,390 → 596,392
- Route nodes: 2,502,545 → 2,502,555
- Route edges: 2,301,922 → 2,301,930
- Literature-expansion rows: 30,276 → 30,278
- Full-sequence curation candidates: 15,499 → 15,501
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,750 → 9,752
- Coverage summary: 180 full functional-output, 172 full target-gene,
  1,456 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locators include [PMID:23954950](https://pubmed.ncbi.nlm.nih.gov/23954950/),
[PMID:19147503](https://pubmed.ncbi.nlm.nih.gov/19147503/), and
[PMID:20472562](https://pubmed.ncbi.nlm.nih.gov/20472562/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion607/`
