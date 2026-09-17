# mSCIdblit mechanism graph release v1.9.6

Release date: 2026-09-17

This release adds the 101st selective primary-literature expansion batch for
Module 21B downstream curation. The overlay adds ten source-linked routes for
mSCS plausibility analysis while preserving the distinction between observed
ligand–receptor output, bounded intracellular continuation, and unresolved
mechanistic layers.

The batch covers S100A8/A9, S100A12, and S100B through RAGE; PrP(C) through
ADGRG6/GPR126; LL-37 through FPR2/ALX; beta-defensin-3 through CCR6; RBP4 and
CCN1 through TLR4; IFN-lambda-4 through IFNLR1/IL10RB with STAT1 support; and
muramyl dipeptide through NOD2 with RIPK2 and NF-kappaB support. Primary
locators include [PMID:18339893](https://pubmed.ncbi.nlm.nih.gov/18339893/),
[PMID:17158877](https://pubmed.ncbi.nlm.nih.gov/17158877/),
[PMID:17660747](https://pubmed.ncbi.nlm.nih.gov/17660747/),
[PMID:27501152](https://pubmed.ncbi.nlm.nih.gov/27501152/),
[PMID:11015447](https://pubmed.ncbi.nlm.nih.gov/11015447/),
[PMID:12840147](https://pubmed.ncbi.nlm.nih.gov/12840147/),
[PMID:33214151](https://pubmed.ncbi.nlm.nih.gov/33214151/),
[PMID:32144270](https://pubmed.ncbi.nlm.nih.gov/32144270/),
[PMID:24169568](https://pubmed.ncbi.nlm.nih.gov/24169568/), and
[PMID:22857257](https://pubmed.ncbi.nlm.nih.gov/22857257/).

Eight routes retain receptor-proximal intracellular continuation without a
TF, one retains an intracellular continuation plus an exact NF-kappaB node
mention without a terminal target gene, and one retains an exact STAT1/output
annotation while leaving the JAK/adaptor relay unresolved. All ten remain
non-causal evidence routes with `evidence_route_not_causal` traversal status.
No graph edges, causal edges, or database confidence scores are created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,791
- Cumulative literature-expansion route rows: 744
- Unique downstream queue candidates with literature coverage: 728
- Remaining downstream queue candidates: 2,603, including 1,547 P1 candidates
- Literature route tiers added: 8 receptor–intracellular–output routes, 1
  receptor–intracellular–TF–output route, and 1 receptor–TF/output route

The release is an evidence-layer update only. mSCS can use the retained
receptor, intracellular, TF, and output evidence as route-plausibility inputs
while applying its own confidence logic.
