# mSCIdblit release v1.9.360

This release adds four primary-literature route overlays for canonical ligands:
IL-25→IL-17RA/IL-17RB→Act1→NF-κB→IL-13 output,
IL-27→IL-27R/gp130→JAK/TYK2→STAT1→TBX21,
HGF→MET→MAPK→EGR1→motility output, and
VEGF165→NRP1/KDR→ERK→AP-1→JUNB/endothelial output.

These are evidence-layer routes for mSCS plausibility analysis. They retain
graph-linked ligand–receptor and TF–target components where available, while
unresolved handoffs remain explicitly bounded. The release does not create
causal graph edges, confidence scores, or traversal permissions.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,367 → 596,371
- Route nodes: 2,502,446 → 2,502,464
- Route edges: 2,301,846 → 2,301,860
- Literature-expansion rows: 30,253 → 30,257
- Full-sequence curation candidates: 15,476 → 15,480
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,732 → 9,734
- Coverage summary: 173 full functional-output, 166 full target-gene,
  1,469 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locators include [PMID:22045852](https://pubmed.ncbi.nlm.nih.gov/22045852/),
[PMID:19155512](https://pubmed.ncbi.nlm.nih.gov/19155512/),
[PMID:14565860](https://pubmed.ncbi.nlm.nih.gov/14565860/),
[PMID:15356135](https://pubmed.ncbi.nlm.nih.gov/15356135/),
[PMID:23452095](https://pubmed.ncbi.nlm.nih.gov/23452095/),
[PMID:16858414](https://pubmed.ncbi.nlm.nih.gov/16858414/),
[PMID:20357818](https://pubmed.ncbi.nlm.nih.gov/20357818/),
[PMID:26860974](https://pubmed.ncbi.nlm.nih.gov/26860974/),
[PMID:17549302](https://pubmed.ncbi.nlm.nih.gov/17549302/), and
[PMID:22828632](https://pubmed.ncbi.nlm.nih.gov/22828632/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion601/`
