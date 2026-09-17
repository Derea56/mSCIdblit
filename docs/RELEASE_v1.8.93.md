# mSCIdblit mechanism graph release v1.8.93

Release date: 2026-09-17

This release adds the 88th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten new ligand–receptor
route annotations for mSCS plausibility analysis. Three routes retain a
bounded receptor-to-G-protein continuation, while seven retain direct
ligand–receptor–output evidence with the intracellular and transcriptional
layers explicitly unasserted.

The routes cover GDNF–GFRA2:RET, neurturin–GFRA1:RET, UCN2–CRHR2,
PACAP–PAC1, secretin–SCTR, UCN1–CRHR1, UCN1–CRHR2, Reelin–ApoER2,
and astrocyte-derived ET-1 through EDNRA or EDNRB on microglia. Primary
support includes GDNF-family receptor-complex and RET phosphorylation studies
([PMID:9407096](https://pubmed.ncbi.nlm.nih.gov/9407096/),
[PMID:9608533](https://pubmed.ncbi.nlm.nih.gov/9608533/)), UCN2–CRHR2
binding and cAMP activation ([PMID:11226328](https://pubmed.ncbi.nlm.nih.gov/11226328/)),
PAC1 second-messenger assays
([PMID:7796937](https://pubmed.ncbi.nlm.nih.gov/7796937/)), UCN1 receptor
binding and signaling ([PMID:8612563](https://pubmed.ncbi.nlm.nih.gov/8612563/)),
and Reelin–ApoER2/Dab1 phosphorylation
([PMID:10571241](https://pubmed.ncbi.nlm.nih.gov/10571241/)). The endothelin
routes preserve a primary rat spinal-cord-contusion astrocyte–microglia
context ([PMID:40443301](https://pubmed.ncbi.nlm.nih.gov/40443301/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status. mSCS can use the
retained receptor, intracellular, and output evidence as route-plausibility
inputs while applying its own confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,661
- Cumulative literature-expansion route rows: 614
- Unique downstream queue candidates with literature coverage: 597
- Remaining downstream queue candidates: 2,734, including 1,672 P1 candidates
- Literature route tiers added: 3 receptor–intracellular–output routes missing TF and 7 receptor–output routes missing intracellular and TF layers

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing routes where primary studies can
add an output or a bounded intracellular continuation without overclaiming
terminal transcriptional effects.
