# mSCIdblit mechanism graph release v1.9.4

Release date: 2026-09-17

This release adds the 99th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new source-linked
ligand–receptor–output annotations for mSCS plausibility analysis. Each route
also retains an independently curated receptor-proximal G-protein continuation
through GNAQ/GNA11, GNAS, GNAI/O/Z, GNA15, or GNAI. No transcription-factor or
target-gene layer is asserted.

The routes cover processed PK2beta–PROKR1, processed PK2beta–PROKR2,
spexin–GALR3, FSH–FSHR, GnRH-I–GNRHR, PDYN-derived dynorphin–GPR139,
AGRP–MC3R, AGRP–MC5R, ASIP–MC4R, and PAMP-20–MRGPRX2. Primary support
includes calcium and cAMP signaling, receptor-selective pharmacology,
prolactin release, medial-habenula responses, competitive melanocortin
antagonism, and bounded peptide GPCR outputs ([PMID:15772293](https://pubmed.ncbi.nlm.nih.gov/15772293/),
[PMID:24517231](https://pubmed.ncbi.nlm.nih.gov/24517231/),
[PMID:2126341](https://pubmed.ncbi.nlm.nih.gov/2126341/),
[PMID:8013367](https://pubmed.ncbi.nlm.nih.gov/8013367/),
[PMID:40701991](https://pubmed.ncbi.nlm.nih.gov/40701991/),
[PMID:9892020](https://pubmed.ncbi.nlm.nih.gov/9892020/),
[PMID:9058374](https://pubmed.ncbi.nlm.nih.gov/9058374/),
[PMID:15823563](https://pubmed.ncbi.nlm.nih.gov/15823563/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor, bounded intracellular continuation, and output evidence as
route-plausibility inputs while applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,771
- Cumulative literature-expansion route rows: 724
- Unique downstream queue candidates with literature coverage: 708
- Remaining downstream queue candidates: 2,623, including 1,561 P1 candidates
- Literature route tiers added: 10 receptor–intracellular–output routes

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing receptor-proximal outputs and
bounded intracellular continuations that improve plausible Ligand–Receptor–
Output traversal without overclaiming terminal transcriptional effects.
