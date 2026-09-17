# mSCIdblit mechanism graph release v1.8.89

Release date: 2026-09-17

This release adds the 84th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten previously unexpanded
ligand–receptor output annotations as source-linked evidence routes for mSCS
plausibility analysis. Seven routes retain an existing receptor-to-G-protein
continuation, while three retain ligand–receptor–output evidence without an
asserted intracellular layer. The routes include orexin–HCRTR2/OX2R,
relaxin-3–RXFP3, adrenomedullin–CALCRL:RAMP3, LysoPS–GPR34 and GPR174,
LPI–GPR55, RvD2–GPR18, proton–GPR68, LTD4–CysLT1 and LTC4/LTD4–CysLT2.
Primary support includes the orexin receptor discovery study
([PMID:9491897](https://pubmed.ncbi.nlm.nih.gov/9491897/)), relaxin-3/RXFP3
work ([PMID:14522967](https://pubmed.ncbi.nlm.nih.gov/14522967/)),
GPR174/LysoPS pharmacology
([PMID:25970039](https://pubmed.ncbi.nlm.nih.gov/25970039/)), and
proton-sensing GPR68/OGR1 studies
([PMID:12955148](https://pubmed.ncbi.nlm.nih.gov/12955148/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status, and the TF and target
gene fields remain unasserted. mSCS can therefore use the retained output and
intracellular evidence as route-plausibility inputs while applying its own
confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,621
- Cumulative literature-expansion rows: 574
- Unique downstream queue candidates with literature coverage: 557
- Remaining downstream queue candidates: 2,774, including 1,709 P1 candidates
- Literature route tiers: 15 full routes; 22 with ligand–receptor–intracellular–TF and missing target output; 224 with ligand–receptor–intracellular–output and missing TF; 62 with ligand–receptor–TF–output and missing intracellular continuation; and 251 ligand–receptor–output routes missing intracellular and TF layers

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing routes where primary studies can
add an output or a bounded intracellular continuation without overclaiming
terminal transcriptional effects.
