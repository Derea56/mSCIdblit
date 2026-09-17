# mSCIdblit Module 20B–24B mechanism graph v1.8.30

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-025`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion025/`

This twenty-fifth selective literature-expansion release adds five
source-linked ligand–receptor/output annotations. The intracellular
continuation, transcription-factor and terminal target-gene layers remain
unresolved:

- BDNF → TrkB → receptor phosphorylation output
- NGF → TrkA → receptor phosphorylation/kinase output
- MFG-E8 → αVβ3 integrin → phagocytosis output
- TSP1 → CD36 → antiangiogenic endothelial output
- SLIT2 → ROBO2 → developmental guidance/adhesion output

These records make experimentally observed outputs available to mSCS without
turning them into causal graph edges or database confidence scores. The
annotations preserve ligand form, receptor-complex, assay-system and model
boundaries, including the MFG-E8 phosphatidylserine-bridging role, TSP1
TSR2/CD36 scope, and SLIT2 processing/Robo-family caveats.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,172 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 125 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 18 |
| Cumulative L→R→intracellular→output annotations missing TF | 33 |
| Cumulative L→R→TF→output annotations missing intracellular | 45 |
| Cumulative L→R→output-only annotations | 19 |

The graph topology and causal edge counts are unchanged from v1.8.29. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies reviewed for this batch include PMID 1710174 and PMID
1649702 (BDNF–TrkB receptor activation), PMID 1706478 (NGF–TrkA receptor
activation), PMID 12000961 (MFG-E8–αVβ3 phagocytosis), PMID 23640500 with
PMCID PMC3737738 (TSP1–CD36 antiangiogenic activity), and PMID 10102268,
15130495 and 27882344 (SLIT2–ROBO2 signaling and functional outputs).
