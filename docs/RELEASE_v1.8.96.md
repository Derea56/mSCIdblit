# mSCIdblit mechanism graph release v1.8.96

Release date: 2026-09-17

This release adds the 91st selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new source-linked
ligand–receptor–output annotations for mSCS plausibility analysis. Nine routes
remain direct receptor-output annotations; one route also retains an existing
FGFR1–PLCγ1 continuation. No transcription-factor or target-gene layer is
asserted for the batch.

The routes cover cyclophilin A–CD147, uromodulin–TRPM6, FAM3B–FGFR1,
FAM3B–FGFR2, FAM3B–FGFR3, FAM3B–FGFR4, DLK2–NOTCH1, L1CAM–FGFR1,
TFF2–CXCR4, and SVEP1–PEAR1. Primary support includes receptor binding,
ERK or receptor-phosphorylation, trafficking, reporter, chemotaxis,
neurite, and platelet-activation studies ([PMID:11943775](https://pubmed.ncbi.nlm.nih.gov/11943775/),
[PMID:30139743](https://pubmed.ncbi.nlm.nih.gov/30139743/),
[PMID:33975953](https://pubmed.ncbi.nlm.nih.gov/33975953/),
[PMID:21419176](https://pubmed.ncbi.nlm.nih.gov/21419176/),
[PMID:18222703](https://pubmed.ncbi.nlm.nih.gov/18222703/),
[PMID:19064997](https://pubmed.ncbi.nlm.nih.gov/19064997/),
[PMID:36792666](https://pubmed.ncbi.nlm.nih.gov/36792666/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor, intracellular-continuation, and output evidence as
route-plausibility inputs while applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,691
- Cumulative literature-expansion route rows: 644
- Unique downstream queue candidates with literature coverage: 627
- Remaining downstream queue candidates: 2,704, including 1,642 P1 candidates
- Literature route tiers added: 1 receptor–intracellular–output route and 9 direct receptor–output routes

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing routes where primary studies can
add an output or a bounded intracellular continuation without overclaiming
terminal transcriptional effects.
