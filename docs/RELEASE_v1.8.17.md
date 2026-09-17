# mSCIdblit Module 20B–24B mechanism graph v1.8.17

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-012`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion012/`

This twelfth selective literature-expansion release adds five direct
ligand–receptor output annotations:

- DLL4 → NOTCH4 → HES1/HES-HERP endothelial transcriptional output, with the intracellular and TF layers unresolved
- S100A8/S100A9 complex → CD69 → STAT3-associated SOCS3 regulatory output, with the intracellular relay unresolved
- Kallistatin → NOTCH1 → HES1 neuronal output, with the intracellular and TF layers unresolved
- CCN3/NOV → NOTCH1 → HES1/HES5 myogenic output, with the intracellular and TF layers unresolved
- JAG1 → NOTCH3 → HES1 Notch output, with the intracellular and TF layers unresolved

These annotations make measured ligand–receptor–output relationships
available to mSCS without fabricating a receptor-proximal cascade or terminal
TF link. Receptor context, assay model, perturbation context, species or tissue
limits, and negative scope are retained. Each route remains an evidence record
for mSCS rather than a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,107 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 60 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 14 |
| Cumulative L→R→intracellular→output annotations missing TF | 13 |
| Cumulative L→R→TF→output annotations missing intracellular | 14 |
| Cumulative L→R→output-only annotations | 9 |

The output-only count is recomputed from all twelve bounded expansion inputs;
the v1.8.16 note omitted one earlier output-only annotation. The earlier
v1.8.13 intra­cellular-output count was also corrected in v1.8.14.

The graph topology and causal edge counts are unchanged from v1.8.16. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 12814948 (DLL4-NOTCH4),
PMID 26296369 with DOI 10.1096/fj.15-273987 (S100A8/S100A9-CD69), DOI
10.7554/eLife.99462.3 (kallistatin-NOTCH1), PMID 12050162 with DOI
10.1074/jbc.M203727200 (CCN3/NOV-NOTCH1), and PMID 18632624 and PMID 23530123
(JAG1-NOTCH3).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
