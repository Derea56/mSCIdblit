# mSCIdblit mechanism graph release v1.8.99

Release date: 2026-09-17

This release adds the 94th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new source-linked
ligand–receptor–output annotations for mSCS plausibility analysis. All ten
routes also retain independently curated receptor-to-G-protein continuations:
HRH2–GNAS, PROKR1/2–GNAQ/GNA11, GALR3–GNAI/O/Z, OXGR1–GNAQ/GNA11,
FFAR2–GNAQ/GNA11, FFAR3–GNAI/O/Z, FFAR4–GNAQ/GNA11, and NMUR1/2–
GNAQ/GNA11. No transcription-factor or target-gene layer is asserted.

The routes cover histamine–HRH2, prokineticin-2–PROKR1, prokineticin-2–
PROKR2, galanin–GALR3, alpha-ketoglutarate–OXGR1, acetate/propionate/
butyrate–FFAR2, acetate/propionate/butyrate–FFAR3, DHA/EPA–FFAR4,
neuromedin U–NMUR1, and neuromedin U–NMUR2. Primary support includes cloned
receptor binding and second-messenger assays, receptor-coupling studies,
GIRK activation, and receptor-expression pharmacology ([PMID:1313563](https://pubmed.ncbi.nlm.nih.gov/1313563/),
[PMID:15772293](https://pubmed.ncbi.nlm.nih.gov/15772293/),
[PMID:9722565](https://pubmed.ncbi.nlm.nih.gov/9722565/),
[PMID:15141213](https://pubmed.ncbi.nlm.nih.gov/15141213/),
[PMID:12711604](https://pubmed.ncbi.nlm.nih.gov/12711604/),
[PMID:20813258](https://pubmed.ncbi.nlm.nih.gov/20813258/),
[PMID:10999960](https://pubmed.ncbi.nlm.nih.gov/10999960/),
[PMID:11010960](https://pubmed.ncbi.nlm.nih.gov/11010960/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor, bounded G-protein continuation, and output evidence as
route-plausibility inputs while applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,721
- Cumulative literature-expansion route rows: 674
- Unique downstream queue candidates with literature coverage: 658
- Remaining downstream queue candidates: 2,673, including 1,611 P1 candidates
- Literature route tiers added: 10 receptor–intracellular–output routes

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing receptor-proximal outputs and
bounded intracellular continuations that improve plausible Ligand–Receptor–
Output traversal without overclaiming terminal transcriptional effects.
