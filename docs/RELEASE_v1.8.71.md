# mSCIdblit Module 20B–24B mechanism graph v1.8.71

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-066`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion066/`

This sixty-sixth selective literature-expansion release adds one
source-linked E-selectin–DR3 route. Primary studies support E-selectin
engagement of DR3/TNFRSF25 on colon-carcinoma cells and downstream p38, ERK,
PI3K-Akt and NF-κB responses associated with adhesion, migration and survival.

The route is retained as:

`SELE/E-selectin → TNFRSF25/DR3 → ???? → NF-kB → survival/migration output`

The intracellular adaptor ordering and terminal target gene remain unresolved.
The record therefore adds TF/output evidence without asserting a specific
TRADD/TRAF sequence, a causal graph edge, a database confidence score, or SCI
transfer. E-selectin presentation and DR3 splice-variant context remain
explicit.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,464 |
| Literature-expansion annotations in this batch | 1 |
| Cumulative literature-expansion annotations | 417 |
| Unique covered queue candidates | 402 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 56 |
| Cumulative L→R→output-only annotations | 239 |
| Unused downstream queue candidates remaining | 2,929 |
| Unused P1 queue candidates remaining | 1,864 |

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies: Gout et al., “Death receptor-3, a new E-Selectin
counter-receptor that confers migration and survival advantages to colon
carcinoma cells by triggering p38 and ERK MAPK activation,” PMID 16982754; and
Porquet et al., “Survival advantages conferred to colon cancer cells by
E-selectin-induced activation of the PI3K-NFκB survival axis downstream of
Death receptor-3,” PMID 21722370, PMCID PMC3177907.
