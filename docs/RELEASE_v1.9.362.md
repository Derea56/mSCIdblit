# mSCIdblit release v1.9.362

This release adds three primary-literature route overlays: two receptor-
specific IL-37 branches through IL-18Rα/IL-1R8 or IL-1R8 with STAT3-linked
anti-inflammatory signaling and NF-κB inhibition, and an IL-17D→CD93→p38-
AKT→SMAD2/3 route for DDX5 suppression and IL-36R inflammatory amplification.

These are evidence-layer routes for mSCS plausibility analysis. They preserve
the inhibitory polarity of the IL-37 branches and retain receptor-specific
identities. Unresolved handoffs remain explicitly bounded; no causal graph
edges, confidence scores, or traversal permissions are created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,378 → 596,381
- Route nodes: 2,502,495 → 2,502,507
- Route edges: 2,301,884 → 2,301,893
- Literature-expansion rows: 30,264 → 30,267
- Full-sequence curation candidates: 15,487 → 15,490
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,738 → 9,741
- Coverage summary: 177 full functional-output, 168 full target-gene,
  1,463 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locators include [PMID:25729923](https://pubmed.ncbi.nlm.nih.gov/25729923/),
[PMID:19503107](https://pubmed.ncbi.nlm.nih.gov/19503107/),
[PMID:25654981](https://pubmed.ncbi.nlm.nih.gov/25654981/), and
[PMID:36271146](https://pubmed.ncbi.nlm.nih.gov/36271146/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion603/`
