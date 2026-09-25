# mSCIdblit release v1.9.368

This release adds a primary-literature CCL2→CCR2→PI3K/AKT→NF-κB route with
measured NF-κB nuclear translocation and astrocyte-survival outputs. The route
is retained as an evidence-layer overlay for mSCS plausibility analysis; it
does not establish a promoter-resolved target gene or direct causal graph
edges for every intermediate.

No causal graph edges, confidence scores, or traversal permissions are
created. The all-ligand curation queue is regenerated so mSCS can consume the
new route together with the existing evidence layers.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,393 → 596,394
- Route nodes: 2,502,563 (unchanged)
- Route edges: 2,301,936 (unchanged)
- Literature-expansion rows: 30,279 → 30,280
- Full-sequence curation candidates: 15,502 → 15,503
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,753 → 9,754
- Coverage summary: 182 full functional-output, 172 full target-gene,
  1,454 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locator: [PMID:17949991](https://pubmed.ncbi.nlm.nih.gov/17949991/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion609/`
