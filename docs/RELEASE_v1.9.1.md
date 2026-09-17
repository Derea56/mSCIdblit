# mSCIdblit mechanism graph release v1.9.1

Release date: 2026-09-17

This release adds the 96th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new source-linked
ligand–receptor–output annotations for mSCS plausibility analysis. Nine routes
retain an independently curated receptor-proximal continuation through a
bounded intracellular signaling component; one route retains direct
ligand–receptor–output evidence without an asserted intracellular layer.
No transcription-factor or target-gene layer is asserted.

The routes cover reduced HMGB1/CXCL12–CXCR4, MIF–CXCR4, MIF–ACKR3,
resolvin D1–FPR2, neuromedin B–NMBR, NPFF–NPFFR1, NPFF–NPFFR2,
human beta-defensin-1–CCR6, oligomeric RPS19–C5AR1, and UDP–P2Y6.
Primary support includes receptor-specific binding, calcium or phosphorylation
readouts, beta-arrestin or G-protein continuation, chemotaxis, phagocytosis,
and bounded immune or neuroinflammatory function ([PMID:22370717](https://pubmed.ncbi.nlm.nih.gov/22370717/),
[PMID:17435771](https://pubmed.ncbi.nlm.nih.gov/17435771/),
[PMID:27226569](https://pubmed.ncbi.nlm.nih.gov/27226569/),
[PMID:26139098](https://pubmed.ncbi.nlm.nih.gov/26139098/),
[PMID:20080636](https://pubmed.ncbi.nlm.nih.gov/20080636/),
[PMID:1328611](https://pubmed.ncbi.nlm.nih.gov/1328611/),
[PMID:11024015](https://pubmed.ncbi.nlm.nih.gov/11024015/),
[PMID:25122636](https://pubmed.ncbi.nlm.nih.gov/25122636/),
[PMID:12651630](https://pubmed.ncbi.nlm.nih.gov/12651630/),
[PMID:28228558](https://pubmed.ncbi.nlm.nih.gov/28228558/),
[PMID:17410128](https://pubmed.ncbi.nlm.nih.gov/17410128/),
[PMID:38614103](https://pubmed.ncbi.nlm.nih.gov/38614103/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor, bounded intracellular continuation, and output evidence as
route-plausibility inputs while applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,741
- Cumulative literature-expansion route rows: 694
- Unique downstream queue candidates with literature coverage: 678
- Remaining downstream queue candidates: 2,653, including 1,591 P1 candidates
- Literature route tiers added: 9 receptor–intracellular–output routes and 1 direct receptor–output route

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing receptor-proximal outputs and
bounded intracellular continuations that improve plausible Ligand–Receptor–
Output traversal without overclaiming terminal transcriptional effects.
