# mSCIdblit release v1.9.359

This release adds five primary-literature route overlays for canonical immune
ligands. The new routes are IL-10→IL-10R→JAK1/TYK2→STAT3→SOCS3,
4-1BBL→4-1BB→TRAF2→NF-κB→IL-2 output,
OX40L→OX40→TRAF2→NF-κB→T-cell-survival output,
GITRL→GITR→TRAF2/JNK→AP-1→regulatory-T-cell output, and
RANKL→RANK→TRAF6/TAK1→AP-1→osteoclast output.

These are evidence-layer routes for mSCS plausibility analysis. They retain
graph-supported receptor-to-adaptor edges where available, but do not create
causal graph edges, confidence scores, or traversal permissions for unresolved
handoffs.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,362 → 596,367
- Route nodes: 2,502,425 → 2,502,446
- Route edges: 2,301,830 → 2,301,846
- Literature-expansion rows: 30,248 → 30,253
- Full-sequence curation candidates: 15,471 → 15,476
- Unique ligands in the curation queue: 1,867 → 1,869
- P1 review candidates: 9,728 → 9,732
- Coverage summary: 172 full functional-output, 164 full target-gene,
  1,472 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locators include [PMID:7543512](https://pubmed.ncbi.nlm.nih.gov/7543512/),
[PMID:11034314](https://pubmed.ncbi.nlm.nih.gov/11034314/),
[PMID:9464265](https://pubmed.ncbi.nlm.nih.gov/9464265/),
[PMID:9607925](https://pubmed.ncbi.nlm.nih.gov/9607925/),
[PMID:21282629](https://pubmed.ncbi.nlm.nih.gov/21282629/),
[PMID:22461627](https://pubmed.ncbi.nlm.nih.gov/22461627/),
[PMID:11809792](https://pubmed.ncbi.nlm.nih.gov/11809792/), and
[PMID:19112497](https://pubmed.ncbi.nlm.nih.gov/19112497/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion600/`
