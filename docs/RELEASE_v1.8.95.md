# mSCIdblit mechanism graph release v1.8.95

Release date: 2026-09-17

This release adds the 90th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new direct
ligand–receptor–output annotations for mSCS plausibility analysis. The
intracellular continuation, transcription-factor, and target-gene layers are
explicitly unasserted for every route.

The routes cover CCL25–CCR9, CXCL7–CXCR2, XCL1–XCR1,
FGF19–FGFR4:beta-Klotho, FGF21–FGFR3c:beta-Klotho, IL-34–PTPRZ1,
IL-34–Syndecan-1, netrin-1–CD146, netrin-1–UNC5D, and GDNF–Syndecan-3.
Primary support includes chemokine trafficking, receptor activity and
chemotaxis studies ([PMID:11884450](https://pubmed.ncbi.nlm.nih.gov/11884450/),
[PMID:28245630](https://pubmed.ncbi.nlm.nih.gov/28245630/),
[PMID:19913446](https://pubmed.ncbi.nlm.nih.gov/19913446/));
beta-Klotho receptor-complex activation studies
([PMID:30944224](https://pubmed.ncbi.nlm.nih.gov/30944224/),
[PMID:18187602](https://pubmed.ncbi.nlm.nih.gov/18187602/));
IL-34 alternative-receptor binding and phosphorylation or migration studies
([PMID:23744080](https://pubmed.ncbi.nlm.nih.gov/23744080/),
[PMID:25662098](https://pubmed.ncbi.nlm.nih.gov/25662098/));
netrin-1 CD146 signaling and UNC5D processing studies
([PMID:25656845](https://pubmed.ncbi.nlm.nih.gov/25656845/),
[PMID:23778138](https://pubmed.ncbi.nlm.nih.gov/23778138/)); and
matrix-bound GDNF–Syndecan-3 neuronal-function evidence
([PMID:21200028](https://pubmed.ncbi.nlm.nih.gov/21200028/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor and output evidence as route-plausibility inputs while
applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,681
- Cumulative literature-expansion route rows: 634
- Unique downstream queue candidates with literature coverage: 617
- Remaining downstream queue candidates: 2,714, including 1,652 P1 candidates
- Literature route tiers added: 10 direct receptor–output routes missing intracellular continuation and TF layers

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing routes where primary studies can
add an output or a bounded intracellular continuation without overclaiming
terminal transcriptional effects.
