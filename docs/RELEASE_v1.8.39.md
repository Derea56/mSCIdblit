# mSCIdblit Module 20B–24B mechanism graph v1.8.39

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-034`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion034/`

This thirty-fourth selective literature-expansion release adds eight unused
P1 candidates as source-linked route annotations. Six records add
receptor-proximal intracellular continuation evidence, and two preserve
functional outputs where the intracellular layer remains unassayed:

- CD200 → CD200R1 → DOK1 → inhibitory myeloid output
- CD200 → CD200R1 → DOK2/RasGAP → inhibitory myeloid output
- haptoglobin → CD22 → SHP1 → B-cell signaling output
- haptoglobin → CD22 → PLCG1 → B-cell calcium/signaling output
- Agrin → LRP4 → MuSK → phosphorylation/AChR-clustering output
- CD177 → PECAM1/CD31 → CD38 → adhesion/calcium output
- CD47 → SIRPA → myelin phagocytosis-brake output
- CD200 → CD200R1 → microglial activation/inflammatory-priming output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores, and they do
not assert SCI-specific effects. The haptoglobin→CD22 and CD177→PECAM1 input
edges are explicitly kept separate from the cited downstream assays; the
records do not claim that those ligands alone reproduced the downstream
experimental stimulus. TF and terminal target-gene layers remain unresolved.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,243 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 196 |
| Unique covered queue candidates | 181 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 21 |
| Unused downstream queue candidates remaining | 3,150 |
| Unused P1 queue candidates remaining | 2,083 |

The graph topology and causal edge counts are unchanged from v1.8.38. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies represented in this batch include PMID 15557172 (CD200R-Dok
adaptor signaling), PMID 8627166 (CD22-SHP1/PLCG1), PMID 18848351 and PMID
18957220 (Agrin-LRP4-MuSK), PMID 9551996 and PMID 9494077 (CD31-CD38), PMID
21401967 (myelin CD47-SIRPA phagocytosis), and PMID 29104062 (CD200R1-linked
microglial inflammatory priming).
