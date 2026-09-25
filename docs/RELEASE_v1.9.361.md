# mSCIdblit release v1.9.361

This release adds seven primary-literature route overlays for canonical ligand
branches: IL-17C→IL-17RA/IL-17RE→Act1→NF-κB→NFKBIZ,
CD40L→CD40→TRAF2→NF-κB→IL-6 and
CD40L→CD40→TRAF2→AP-1→IL-6,
TRAIL→DR4 or DR5→FADD→NF-κB output, and
VEGF-C→VEGFR3 or VEGFR2→ERK→AP-1 endothelial output.

These are evidence-layer routes for mSCS plausibility analysis. They retain
graph-linked ligand–receptor and receptor-proximal components where available,
while unresolved handoffs remain explicitly bounded. The release does not
create causal graph edges, confidence scores, or traversal permissions.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,371 → 596,378
- Route nodes: 2,502,464 → 2,502,495
- Route edges: 2,301,860 → 2,301,884
- Literature-expansion rows: 30,257 → 30,264
- Full-sequence curation candidates: 15,480 → 15,487
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,734 → 9,738
- Coverage summary: 175 full functional-output, 168 full target-gene,
  1,465 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locators include [PMID:21982598](https://pubmed.ncbi.nlm.nih.gov/21982598/),
[PMID:23944933](https://pubmed.ncbi.nlm.nih.gov/23944933/),
[PMID:11886848](https://pubmed.ncbi.nlm.nih.gov/11886848/),
[PMID:16260598](https://pubmed.ncbi.nlm.nih.gov/16260598/),
[PMID:9430227](https://pubmed.ncbi.nlm.nih.gov/9430227/),
[PMID:12207174](https://pubmed.ncbi.nlm.nih.gov/12207174/),
[PMID:23096115](https://pubmed.ncbi.nlm.nih.gov/23096115/),
[PMID:8617204](https://pubmed.ncbi.nlm.nih.gov/8617204/),
[PMID:11532940](https://pubmed.ncbi.nlm.nih.gov/11532940/),
[PMID:25281926](https://pubmed.ncbi.nlm.nih.gov/25281926/),
[PMID:25524775](https://pubmed.ncbi.nlm.nih.gov/25524775/), and
[PMID:9506953](https://pubmed.ncbi.nlm.nih.gov/9506953/).

The materializer now writes route evidence directly to the canonical gzip
artifact, avoiding a duplicate uncompressed intermediate during release builds.

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion602/`
