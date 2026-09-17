# mSCIdblit Module 20B–24B mechanism graph v1.8.63

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-058`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion058/`

This fifty-eighth selective literature-expansion release adds seven
source-linked Fibulin-5/FBLN5 annotations:

- Fibulin-5 → α5β1 integrin → smooth-muscle-cell adhesion and behavior readout
- Fibulin-5 → α4β1 integrin → smooth-muscle-cell adhesion and behavior readout
- Fibulin-5 → αVβ3 integrin → elastic-fiber anchorage/organization readout
- Fibulin-5 → αVβ5 integrin → elastic-fiber anchorage/organization readout
- Fibulin-5 → α9β1 integrin → elastic-fiber anchorage/organization readout
- Fibulin-5 → uPA/PLAU → proteolytic matrix-remodeling and β1-integrin-dependent migration readout
- Fibulin-5 → elastin/ELN → elastic-fiber organization readout

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores. The
release preserves the distinction between cell-surface integrin receptors,
the extracellular protease partner uPA, and the structural matrix partner
elastin. Intracellular continuation, TF and target-gene layers remain
unresolved in all seven records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,427 |
| Literature-expansion annotations in this batch | 7 |
| Cumulative literature-expansion annotations | 380 |
| Unique covered queue candidates | 365 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 205 |
| Unused downstream queue candidates remaining | 2,966 |
| Unused P1 queue candidates remaining | 1,899 |

The graph topology and causal edge counts are unchanged from v1.8.62. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented include human aortic smooth-muscle-cell
fibulin-5 binding and functional assays (PMID 17472576; PMCID PMC2267297),
fibulin-5 integrin-ligand and elastogenesis experiments (PMID 11805835), and
fibulin-5/uPA binding, cleavage and migration experiments (PMID 22280367;
PMCID PMC4591041; DOI 10.1042/BJ20111751).
