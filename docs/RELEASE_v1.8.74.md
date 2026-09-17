# mSCIdblit Module 20B–24B mechanism graph v1.8.74

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-069`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion069/`

This sixty-ninth selective literature-expansion release adds four
ligand–receptor–transcription-factor routes with the intracellular continuation
left unresolved:

- IL-23 → IL-12Rβ1/IL-23R → STAT3 → gene-expression output
- IL-3 → IL-3Rα/common β → STAT5 → gene-expression output
- IL-31 → IL-31RA/OSMRβ → STAT3 → growth and gene-induction output
- CNTF → CNTFRα/gp130/LIFR → STAT3 → phosphorylation and proliferative output

These are traversable evidence routes, not causal graph edges. The routes retain
receptor-complex, species and cell-system boundaries and do not claim a complete
JAK/adaptor sequence, terminal target gene, database confidence score or SCI
transfer. IL-23 is explicitly multi-STAT; IL-3, IL-31 and CNTF likewise retain
composite evidence from separate receptor-complex and downstream signaling
studies.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,474 |
| Literature-expansion annotations in this batch | 4 |
| Cumulative literature-expansion annotations | 427 |
| Unique covered queue candidates | 412 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 91 |
| Cumulative L→R→TF→output annotations missing intracellular | 60 |
| Cumulative L→R→output-only annotations | 239 |
| Unused downstream queue candidates remaining | 2,919 |
| Unused P1 queue candidates remaining | 1,854 |

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented include IL-23 receptor-complex and multi-STAT
signaling (PMID 12023369), IL-3 receptor activation and STAT5 recruitment
(PMIDs 8649415 and 9192755), IL-31 receptor STAT3/growth signaling (PMID
17148439), and CNTF receptor-complex assembly and STAT3 signaling (PMIDs
8390097, 8385113, 7500350 and 38569939).
