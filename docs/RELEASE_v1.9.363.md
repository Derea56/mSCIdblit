# mSCIdblit release v1.9.363

This release adds four primary-literature route overlays for canonical ligand
gaps: two CXCL12→CXCR4 branches through PI3K-AKT1→NF-κB→SHH output or
JAK2→STAT3 anti-apoptotic output, a GAS6→AXL→PI3K-AKT1→NF-κB→Bcl-xL
survival-output route, and an SPP1→CD44v→NF-κB/p65→IL-6 microglial-output
route in an SCI model.

These are evidence-layer routes for mSCS plausibility analysis. They preserve
the source-specific models and functional outputs, while unresolved handoffs
remain explicit. No causal graph edges, confidence scores, or traversal
permissions are created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,381 → 596,385
- Route nodes: 2,502,507 → 2,502,523
- Route edges: 2,301,893 → 2,301,905
- Literature-expansion rows: 30,267 → 30,271
- Full-sequence curation candidates: 15,490 → 15,494
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,741 → 9,745
- Coverage summary: 178 full functional-output, 168 full target-gene,
  1,462 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locators include [PMID:22995914](https://pubmed.ncbi.nlm.nih.gov/22995914/),
[PMID:28721072](https://pubmed.ncbi.nlm.nih.gov/28721072/),
[PMID:11425860](https://pubmed.ncbi.nlm.nih.gov/11425860/), and
[PMID:40797111](https://pubmed.ncbi.nlm.nih.gov/40797111/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion604/`
