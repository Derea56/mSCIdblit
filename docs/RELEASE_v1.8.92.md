# mSCIdblit mechanism graph release v1.8.92

Release date: 2026-09-17

This release adds the 87th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten newly curated
ligand–receptor route annotations for mSCS plausibility analysis. Five routes
retain a bounded receptor-to-intracellular continuation, three retain a
receptor-to-STAT5/STAT3 pathway annotation with the intracellular continuation
unresolved, and two retain direct ligand–receptor–output evidence with both
intermediate layers unasserted.

The routes cover PGD2–DP1, PYY(3-36)–Y2R, nicotinic acid–HCAR2, medium/long-chain
fatty acids–FFAR1, apelin-13–APLNR, IL-5–IL5RA:CSF2RB–STAT5,
IL-13–IL4RA:IL13RA1–STAT3, IL-6–IL-6R-gp130–STAT3, FGF23–FGFR1c:alpha-Klotho,
and TPO–MPL. Primary support includes DP1 cAMP/calcium activation
([PMID:7642548](https://pubmed.ncbi.nlm.nih.gov/7642548/)), PYY/Y2R Gi
signaling ([PMID:36525977](https://pubmed.ncbi.nlm.nih.gov/36525977/)),
HCAR2/Gi-cAMP signaling ([PMID:12646212](https://pubmed.ncbi.nlm.nih.gov/12646212/)),
FFAR1/Gq signaling ([PMID:12496284](https://pubmed.ncbi.nlm.nih.gov/12496284/)),
and APLNR signaling ([PMID:27671350](https://pubmed.ncbi.nlm.nih.gov/27671350/)).
The cytokine pathway annotations retain IL-5/STAT5 support
([PMID:9363920](https://pubmed.ncbi.nlm.nih.gov/9363920/)), IL-13 receptor
complex support ([PMID:18243101](https://pubmed.ncbi.nlm.nih.gov/18243101/)),
and IL-6/gp130/STAT3 support
([PMID:11412113](https://pubmed.ncbi.nlm.nih.gov/11412113/)). Direct receptor
output evidence includes FGF23–FGFR1c:alpha-Klotho FRS2/ERK signaling
([PMID:29342138](https://pubmed.ncbi.nlm.nih.gov/29342138/)) and TPO–MPL
activation architecture ([PMID:37633268](https://pubmed.ncbi.nlm.nih.gov/37633268/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor, intracellular, TF, and output evidence as route-plausibility
inputs while applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,651
- Cumulative literature-expansion route rows: 604
- Unique downstream queue candidates with literature coverage: 587
- Remaining downstream queue candidates: 2,744, including 1,682 P1 candidates
- Literature route tiers added: 5 receptor–intracellular–output routes missing TF; 3 receptor–TF–output routes missing intracellular continuation; and 2 receptor–output routes missing intracellular and TF layers

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing routes where primary studies can
add an output or a bounded intracellular continuation without overclaiming
terminal transcriptional effects.
