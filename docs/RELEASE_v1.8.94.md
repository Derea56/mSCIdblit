# mSCIdblit mechanism graph release v1.8.94

Release date: 2026-09-17

This release adds the 89th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new direct
ligand–receptor–output annotations for mSCS plausibility analysis. The
intracellular continuation, transcription-factor, and target-gene layers are
explicitly unasserted for these routes.

The routes cover CCL22–CCR4, CXCL2–CXCR2, CXCL3–CXCR2, CXCL5–CXCR2,
CXCL6–CXCR1, CXCL6–CXCR2, CX3CL1–CX3CR1, CCL16–CCR2, RGMa–neogenin,
and netrin-1–DSCAM. Primary support includes chemokine-receptor calcium,
activation, arrest, and migration studies
([PMID:16614259](https://pubmed.ncbi.nlm.nih.gov/16614259/),
[PMID:15937099](https://pubmed.ncbi.nlm.nih.gov/15937099/),
[PMID:33688078](https://pubmed.ncbi.nlm.nih.gov/33688078/),
[PMID:9692902](https://pubmed.ncbi.nlm.nih.gov/9692902/),
[PMID:9390561](https://pubmed.ncbi.nlm.nih.gov/9390561/),
[PMID:11470772](https://pubmed.ncbi.nlm.nih.gov/11470772/)). Guidance-receptor
support includes RGMa–neogenin axonal repulsion
([PMID:15258590](https://pubmed.ncbi.nlm.nih.gov/15258590/)) and
netrin-1–DSCAM commissural-axon turning/outgrowth
([PMID:18585357](https://pubmed.ncbi.nlm.nih.gov/18585357/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor and output evidence as route-plausibility inputs while
applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,671
- Cumulative literature-expansion route rows: 624
- Unique downstream queue candidates with literature coverage: 607
- Remaining downstream queue candidates: 2,724, including 1,662 P1 candidates
- Literature route tiers added: 10 direct receptor–output routes missing intracellular continuation and TF layers

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing routes where primary studies can
add an output or a bounded intracellular continuation without overclaiming
terminal transcriptional effects.
