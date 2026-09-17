# mSCIdblit mechanism graph release v1.9.2

Release date: 2026-09-17

This release adds the 97th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new source-linked
ligand–receptor–output annotations for mSCS plausibility analysis. Each route
also retains an independently curated receptor-proximal G-protein continuation
through GNAI, GNAQ/GNA11, GNAI/O/Z, or related coupling evidence. No
transcription-factor or target-gene layer is asserted.

The routes cover DADLE–OPRD1, Dynorphin A–OPRK1, sulfated CCK-8–CCKBR,
GRP–GRPR, extracellular ubiquitin–CXCR4, kynurenic acid–GPR35,
PROK1–PROKR1, PROK1–PROKR2, PROK2–PROKR1, and PROK2–PROKR2.
Primary support includes receptor-specific binding, cAMP inhibition,
phosphoinositide and calcium signaling, MAPK phosphorylation, receptor
internalization, chemotaxis, and bounded endothelial or recombinant-receptor
function ([PMID:7808419](https://pubmed.ncbi.nlm.nih.gov/7808419/),
[PMID:8170987](https://pubmed.ncbi.nlm.nih.gov/8170987/),
[PMID:7681836](https://pubmed.ncbi.nlm.nih.gov/7681836/),
[PMID:7723750](https://pubmed.ncbi.nlm.nih.gov/7723750/),
[PMID:20228059](https://pubmed.ncbi.nlm.nih.gov/20228059/),
[PMID:28455789](https://pubmed.ncbi.nlm.nih.gov/28455789/),
[PMID:16754668](https://pubmed.ncbi.nlm.nih.gov/16754668/),
[PMID:12054613](https://pubmed.ncbi.nlm.nih.gov/12054613/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor, bounded intracellular continuation, and output evidence as
route-plausibility inputs while applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,751
- Cumulative literature-expansion route rows: 704
- Unique downstream queue candidates with literature coverage: 688
- Remaining downstream queue candidates: 2,643, including 1,581 P1 candidates
- Literature route tiers added: 10 receptor–intracellular–output routes

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing receptor-proximal outputs and
bounded intracellular continuations that improve plausible Ligand–Receptor–
Output traversal without overclaiming terminal transcriptional effects.
