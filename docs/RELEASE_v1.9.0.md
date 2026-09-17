# mSCIdblit mechanism graph release v1.9.0

Release date: 2026-09-17

This release adds the 95th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new source-linked
ligand–receptor–output annotations for mSCS plausibility analysis. Every route
also retains an independently curated receptor-proximal continuation through a
G protein or beta-arrestin: FPR1/FPR2, CCR1/CCR8, APLNR, MRGPRX2, TSHR and
ACKR3. No transcription-factor or target-gene layer is asserted.

The routes cover FAM3D–FPR1, FAM3D–FPR2, processed CCL23–CCR1,
Elabela/APELA–APLNR, N-terminal Annexin A1 peptide–FPR1, Apelin-36–APLNR,
CXCL14–MRGPRX2, CCL17–CCR8, thyrostimulin/GPHA2:GPHB5–TSHR, and
DKK3–ACKR3. Primary support includes receptor-specific binding, calcium and
second-messenger assays, chemotaxis, receptor internalization, ERK or GIRK
readouts, and bounded vascular or endocrine function ([PMID:26966188](https://pubmed.ncbi.nlm.nih.gov/26966188/),
[PMID:9886417](https://pubmed.ncbi.nlm.nih.gov/9886417/),
[PMID:15927850](https://pubmed.ncbi.nlm.nih.gov/15927850/),
[PMID:17513790](https://pubmed.ncbi.nlm.nih.gov/17513790/),
[PMID:25639753](https://pubmed.ncbi.nlm.nih.gov/25639753/),
[PMID:10882119](https://pubmed.ncbi.nlm.nih.gov/10882119/),
[PMID:12603839](https://pubmed.ncbi.nlm.nih.gov/12603839/),
[PMID:38184723](https://pubmed.ncbi.nlm.nih.gov/38184723/),
[PMID:12045258](https://pubmed.ncbi.nlm.nih.gov/12045258/),
[PMID:29980568](https://pubmed.ncbi.nlm.nih.gov/29980568/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor, bounded intracellular continuation, and output evidence as
route-plausibility inputs while applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,731
- Cumulative literature-expansion route rows: 684
- Unique downstream queue candidates with literature coverage: 668
- Remaining downstream queue candidates: 2,663, including 1,601 P1 candidates
- Literature route tiers added: 10 receptor–intracellular–output routes

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing receptor-proximal outputs and
bounded intracellular continuations that improve plausible Ligand–Receptor–
Output traversal without overclaiming terminal transcriptional effects.
