# mSCIdblit mechanism graph release v1.9.7

Release date: 2026-09-17

This release adds the 102nd selective primary-literature expansion batch for
Module 21B downstream curation. The overlay adds ten source-linked routes for
mSCS plausibility analysis while retaining explicit distinctions between
ligand–receptor output, bounded intracellular continuation, and unresolved
transcriptional layers.

The batch covers heparin and progastrin through GPR56/GNA12; LXA4 through
FPR2/GNAI; RvE1 through BLT1/GNAI/O/Z; MICA and ULBP2 through NKG2D/DAP12;
NMS through NMUR1/GNAQ/GNA11; 5-HIAA through GPR35/GNA13; Tri-DAP through
NOD1/RIPK2; and cytosolic dsDNA through AIM2/ASC. Primary locators include
[PMID:27068534](https://pubmed.ncbi.nlm.nih.gov/27068534/),
[PMID:28380450](https://pubmed.ncbi.nlm.nih.gov/28380450/),
[PMID:8006586](https://pubmed.ncbi.nlm.nih.gov/8006586/),
[PMID:17339491](https://pubmed.ncbi.nlm.nih.gov/17339491/),
[PMID:10426993](https://pubmed.ncbi.nlm.nih.gov/10426993/),
[PMID:11239445](https://pubmed.ncbi.nlm.nih.gov/11239445/),
[PMID:15976061](https://pubmed.ncbi.nlm.nih.gov/15976061/),
[PMID:35148838](https://pubmed.ncbi.nlm.nih.gov/35148838/),
[PMID:21757725](https://pubmed.ncbi.nlm.nih.gov/21757725/), and
[PMID:19158676](https://pubmed.ncbi.nlm.nih.gov/19158676/).

All ten routes retain receptor-proximal or sensor-proximal intracellular
continuation without asserting a TF or target gene. RvE1/BLT1 is recorded as
an inhibitory counter-regulatory output relative to LTB4 signaling, while
heparin/GPR56 remains context-dependent. All ten remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. No graph edges,
causal edges, or database confidence scores are created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,801
- Cumulative literature-expansion route rows: 754
- Unique downstream queue candidates with literature coverage: 738
- Remaining downstream queue candidates: 2,593, including 1,545 P1 candidates
- Literature route tiers added: 10 receptor–intracellular–output routes

The release is an evidence-layer update only. mSCS can use the retained
receptor, intracellular, and output evidence as route-plausibility inputs
while applying its own confidence logic.
