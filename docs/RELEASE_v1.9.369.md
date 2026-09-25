# mSCIdblit release v1.9.369

This release adds the canonical `Thbs1` route
Thbs1→CD36→TLR4/MyD88/p38/NF-κB→TNF expression. It preserves the existing
graph-linked Thbs1–CD36 pair and the existing relay, while retaining the
primary macrophage evidence as an evidence-layer route for mSCS plausibility
analysis.

No causal graph edges, confidence scores, or traversal permissions are
created. The all-ligand curation queue is regenerated so the canonical and
alias ligand records remain available to downstream review.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,394 → 596,395
- Route nodes: 2,502,568 (unchanged)
- Route edges: 2,301,940 (unchanged)
- Literature-expansion rows: 30,280 → 30,281
- Full-sequence curation candidates: 15,503 → 15,504
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,754 → 9,755
- Coverage summary: 182 full functional-output, 173 full target-gene,
  1,453 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locator: [PMID:23954950](https://pubmed.ncbi.nlm.nih.gov/23954950/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion610/`
