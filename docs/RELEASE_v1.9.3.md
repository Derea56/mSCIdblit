# mSCIdblit mechanism graph release v1.9.3

Release date: 2026-09-17

This release adds the 98th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new source-linked
ligand–receptor–output annotations for mSCS plausibility analysis. Each route
also retains an independently curated receptor-proximal G-protein continuation
through GNAI/O/Z, GNAQ/GNA11, or related coupling evidence. No
transcription-factor or target-gene layer is asserted.

The routes cover soluble GPNMB–GPR39, processed CCL14a–CCR1,
GPR15LG–CXCR4, cortistatin–MRGPRX2, PAMP-12–MRGPRX2, human beta-defensin-3–
MRGPRX2, LL-37–MRGPRX2, human beta-defensin-2–MRGPRX2, CXCL17–MRGPRX2,
and Substance P–MRGPRX2. Primary support includes receptor binding or
activation, calcium and cAMP signaling, AKT/ERK readouts, degranulation,
mediator release, chemotaxis, and context-dependent immune or cardiac
function ([PMID:39455836](https://pubmed.ncbi.nlm.nih.gov/39455836/),
[PMID:19553544](https://pubmed.ncbi.nlm.nih.gov/19553544/),
[PMID:11085751](https://pubmed.ncbi.nlm.nih.gov/11085751/),
[PMID:9687537](https://pubmed.ncbi.nlm.nih.gov/9687537/),
[PMID:40394646](https://pubmed.ncbi.nlm.nih.gov/40394646/),
[PMID:12915402](https://pubmed.ncbi.nlm.nih.gov/12915402/),
[PMID:15823563](https://pubmed.ncbi.nlm.nih.gov/15823563/),
[PMID:23698749](https://pubmed.ncbi.nlm.nih.gov/23698749/),
[PMID:22069323](https://pubmed.ncbi.nlm.nih.gov/22069323/),
[PMID:38279626](https://pubmed.ncbi.nlm.nih.gov/38279626/),
[PMID:31652731](https://pubmed.ncbi.nlm.nih.gov/31652731/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor, bounded intracellular continuation, and output evidence as
route-plausibility inputs while applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,761
- Cumulative literature-expansion route rows: 714
- Unique downstream queue candidates with literature coverage: 698
- Remaining downstream queue candidates: 2,633, including 1,571 P1 candidates
- Literature route tiers added: 10 receptor–intracellular–output routes

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing receptor-proximal outputs and
bounded intracellular continuations that improve plausible Ligand–Receptor–
Output traversal without overclaiming terminal transcriptional effects.
