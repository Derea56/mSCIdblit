# mSCIdblit mechanism graph release v1.8.98

Release date: 2026-09-17

This release adds the 93rd selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new source-linked
ligand–receptor–output annotations for mSCS plausibility analysis. One route,
S100A7–RAGE, also retains the validated RAGE–DAP10 intracellular continuation;
the remaining nine routes retain direct receptor-output evidence. No
transcription-factor or target-gene layer is asserted for the batch.

The routes cover ALCAM–L1CAM, SLIT2–GPC1, NT-4–TrkB, GALP–GALR2,
S100A7–RAGE, KISS1–KISS1R, activated alpha2-macroglobulin–LRP1,
neuropeptide S–NPSR1, deoxycholic acid–MRGPRX4, and CART(55-102)–GPR162.
Primary support includes cellular growth assays, receptor-binding and
activation studies, second-messenger readouts, uptake or clearance assays,
and secretory functional readouts ([PMID:31300520](https://pubmed.ncbi.nlm.nih.gov/31300520/),
[PMID:11375980](https://pubmed.ncbi.nlm.nih.gov/11375980/),
[PMID:1375038](https://pubmed.ncbi.nlm.nih.gov/1375038/),
[PMID:10601261](https://pubmed.ncbi.nlm.nih.gov/10601261/),
[PMID:18606705](https://pubmed.ncbi.nlm.nih.gov/18606705/),
[PMID:11457843](https://pubmed.ncbi.nlm.nih.gov/11457843/),
[PMID:15910735](https://pubmed.ncbi.nlm.nih.gov/15910735/),
[PMID:15312648](https://pubmed.ncbi.nlm.nih.gov/15312648/),
[PMID:31500698](https://pubmed.ncbi.nlm.nih.gov/31500698/),
[PMID:38077141](https://pubmed.ncbi.nlm.nih.gov/38077141/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor, the bounded RAGE–DAP10 continuation, and output evidence
as route-plausibility inputs while applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,711
- Cumulative literature-expansion route rows: 664
- Unique downstream queue candidates with literature coverage: 648
- Remaining downstream queue candidates: 2,683, including 1,621 P1 candidates
- Literature route tiers added: 1 receptor–intracellular–output route and 9 direct receptor–output routes

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing receptor-proximal outputs and
bounded intracellular continuations that improve plausible Ligand–Receptor–
Output traversal without overclaiming terminal transcriptional effects.
