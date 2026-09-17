# mSCIdblit mechanism graph release v1.8.97

Release date: 2026-09-17

This release adds the 92nd selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new source-linked
ligand–receptor–output annotations for mSCS plausibility analysis. Three routes
also retain existing receptor-to-G-protein continuations for HCAR3, ADGRD1,
and ADGRG2; the remaining seven routes retain direct receptor-output evidence.
No transcription-factor or target-gene layer is asserted for the batch.

The routes cover JAG2–NOTCH1, JAG2–NOTCH3,
3-hydroxyoctanoate–HCAR3, beta-phenylethylamine–TAAR1, tyramine–TAAR1,
tryptamine–TAAR1, trimethylamine–TAAR5, dimethylethylamine–TAAR5,
5alpha-DHT–ADGRD1, and DHEA–ADGRG2. Primary support includes receptor-specific
Notch reporters, GPCR second-messenger assays, receptor-bound cryo-EM
structures, and cell or animal functional readouts ([PMID:23530123](https://pubmed.ncbi.nlm.nih.gov/23530123/),
[PMID:19561068](https://pubmed.ncbi.nlm.nih.gov/19561068/),
[PMID:11459929](https://pubmed.ncbi.nlm.nih.gov/11459929/),
[PMID:11723224](https://pubmed.ncbi.nlm.nih.gov/11723224/),
[PMID:23393561](https://pubmed.ncbi.nlm.nih.gov/23393561/),
[PMID:39884271](https://pubmed.ncbi.nlm.nih.gov/39884271/),
[PMID:35982227](https://pubmed.ncbi.nlm.nih.gov/35982227/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor, intracellular-continuation, and output evidence as
route-plausibility inputs while applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,701
- Cumulative literature-expansion route rows: 654
- Unique downstream queue candidates with literature coverage: 637
- Remaining downstream queue candidates: 2,694, including 1,632 P1 candidates
- Literature route tiers added: 3 receptor–intracellular–output routes and 7 direct receptor–output routes

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing routes where primary studies can
add an output or a bounded intracellular continuation without overclaiming
terminal transcriptional effects.
