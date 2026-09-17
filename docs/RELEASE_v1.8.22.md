# mSCIdblit Module 20B–24B mechanism graph v1.8.22

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-017`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion017/`

This seventeenth selective literature-expansion release adds five
source-linked ligand–receptor-to-output annotations. Three include a
source-supported intracellular continuation but no resolved transcription
factor; two preserve ligand–receptor-to-output evidence while leaving both the
intracellular relay and transcription factor unresolved:

- TIMP-1 → CD63/ITGB1 receptor complex → PI3K–AKT1 → OPC maturation output
- ANGPTL2 → MAG → FYN → oligodendrocyte differentiation, myelination, and remyelination output
- TUB → MERTK → RAB7A/Rab7 → microglial phagocytosis output
- C1q → CD44 → CNS repair, microglial phagocytosis, and migration output
- Progranulin → SorCS2 → motor-neuron development, axon outgrowth, and nerve-regeneration output

The C1q annotation retains mouse T9 contusion spinal-cord-injury evidence
alongside human and iPSC comparator systems. The other annotations preserve
their source assay and model context in the evidence records. Each route
remains an evidence record for mSCS rather than a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,132 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 85 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 14 |
| Cumulative L→R→intracellular→output annotations missing TF | 25 |
| Cumulative L→R→TF→output annotations missing intracellular | 24 |
| Cumulative L→R→output-only annotations | 12 |

The graph topology and causal edge counts are unchanged from v1.8.21. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 30121936/PMCID
PMC6379156 (TIMP-1/CD63/ITGB1/PI3K–AKT1 and OPC maturation); PMID
36855057/PMCID PMC9976406/DOI 10.1186/s13578-023-00970-3 (ANGPTL2/MAG/FYN
and remyelination); PMID 22884297/PMCID PMC3466361/DOI
10.1016/j.jneuroim.2012.07.009 (TUB/MERTK/Rab7 and phagocytosis); PMID
32894219/PMCID PMC7476762/DOI 10.7554/eLife.55732 and PMID
42286716/PMCID PMC12633497/DOI 10.1186/s12974-026-03892-2
(C1q/CD44 and CNS repair); and PMID 37897724/DOI
10.1016/j.celrep.2023.113333 (progranulin/SorCS2 and motor-neuron/axon
outgrowth).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
