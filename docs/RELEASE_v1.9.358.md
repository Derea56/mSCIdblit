# mSCIdblit release v1.9.358

This release adds three primary-literature route overlays for canonical
purinergic, neurotrophic, and growth-factor ligands. The new routes are
IGF1→IGF1R→PI3K/Akt→FOXO1→GPR17 expression and
NGF→TrkA→ERK/p38→CREB→BDNF expression, together with
ATP→P2Y11→PKA→CREB→BDNF promoter-IV expression. All preserve the full
proposed route layers for mSCS plausibility analysis while retaining unresolved
cross-study handoffs as explicit evidence gaps.

This is evidence-layer data only. It does not create graph edges, causal
assertions, confidence scores, or a claim that one experiment demonstrates the
complete sequence.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,359 → 596,362
- Route nodes: 2,502,411 → 2,502,425
- Route edges: 2,301,819 → 2,301,830
- Literature-expansion rows: 30,245 → 30,248
- Full-sequence curation candidates: 15,468 → 15,471
- Unique ligands in the curation queue: 1,867 (unchanged)
- P1 review candidates: 9,727 → 9,728

Primary locators include [PMID:35163437](https://pubmed.ncbi.nlm.nih.gov/35163437/),
[PMID:9528766](https://pubmed.ncbi.nlm.nih.gov/9528766/),
[PMID:9262478](https://pubmed.ncbi.nlm.nih.gov/9262478/),
[PMID:9334420](https://pubmed.ncbi.nlm.nih.gov/9334420/), and
[PMID:15207334](https://pubmed.ncbi.nlm.nih.gov/15207334/), and
[PMID:18649393](https://pubmed.ncbi.nlm.nih.gov/18649393/). Validation passed
with no errors; the inherited warning remains that some evidence sources lack
stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion598/`
