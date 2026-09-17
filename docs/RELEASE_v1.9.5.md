# mSCIdblit mechanism graph release v1.9.5

Release date: 2026-09-17

This release adds the 100th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new source-linked
ligand–receptor–output annotations for mSCS plausibility analysis. Each route
also retains an independently curated receptor-proximal continuation through
an adaptor or G-protein layer. No transcription-factor or target-gene layer is
asserted.

The routes cover ficolin-2–TLR4, competence-stimulating peptide 1–MRGPRX2,
P17–MRGPRX2, Staphylococcus aureus delta-toxin–MRGPRX2, major-basic-protein
and eosinophil-cationic-protein fragments–MRGPRX2, PACAP1-38–MRGPRX2,
VIP–MRGPRX2, FAM19A4/TAFA4–FPR1, and WNT2B–FZD4. Primary support includes
TLR4-dependent immune activation, G-protein coupling, ERK phosphorylation,
mast-cell calcium/degranulation, macrophage phagocytosis, and epithelial
functional output ([PMID:28844702](https://pubmed.ncbi.nlm.nih.gov/28844702/),
[PMID:41924265](https://pubmed.ncbi.nlm.nih.gov/41924265/),
[PMID:34111449](https://pubmed.ncbi.nlm.nih.gov/34111449/),
[PMID:24172897](https://pubmed.ncbi.nlm.nih.gov/24172897/),
[PMID:32072023](https://pubmed.ncbi.nlm.nih.gov/32072023/),
[PMID:37516794](https://pubmed.ncbi.nlm.nih.gov/37516794/),
[PMID:16979137](https://pubmed.ncbi.nlm.nih.gov/16979137/),
[PMID:25109685](https://pubmed.ncbi.nlm.nih.gov/25109685/),
[PMID:31359032](https://pubmed.ncbi.nlm.nih.gov/31359032/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor, bounded intracellular continuation, and output evidence as
route-plausibility inputs while applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,781
- Cumulative literature-expansion route rows: 734
- Unique downstream queue candidates with literature coverage: 718
- Remaining downstream queue candidates: 2,613, including 1,551 P1 candidates
- Literature route tiers added: 10 receptor–intracellular–output routes

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing receptor-proximal outputs and
bounded intracellular continuations that improve plausible Ligand–Receptor–
Output traversal without overclaiming terminal transcriptional effects.
