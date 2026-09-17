# mSCIdblit Module 20B–24B mechanism graph v1.8.73

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-068`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion068/`

This sixty-eighth selective literature-expansion release adds three
ligand–receptor routes with an explicitly supported intracellular continuation:

- LTB4 → BLT1 → Gi/o-family coupling → calcium/IP3, adenylyl-cyclase inhibition and chemotaxis output
- Factor Xa → PAR2 → Gq/11-family coupling → phosphoinositide hydrolysis and ERK1/2 phosphorylation
- CCL5 → GPR75 → Gq/11-family coupling → calcium/IP3, AKT/MAPK and neuronal survival output

The routes remain traversable evidence routes, not causal graph edges. The
first two combine ligand/receptor-specific functional studies with separate
receptor–transducer studies. The CCL5/GPR75 route is more explicitly composite:
its Gαq/11 continuation is supported by a separate 20-HETE–GPR75 study, not by
the CCL5 experiment itself. No TF, terminal target gene, causal graph edge,
database confidence score, or SCI transfer is asserted.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,470 |
| Literature-expansion annotations in this batch | 3 |
| Cumulative literature-expansion annotations | 423 |
| Unique covered queue candidates | 408 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 91 |
| Cumulative L→R→TF→output annotations missing intracellular | 56 |
| Cumulative L→R→output-only annotations | 239 |
| Unused downstream queue candidates remaining | 2,923 |
| Unused P1 queue candidates remaining | 1,858 |

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented include BLT1 cloning and LTB4 functional signaling
(PMID 9177352), BLT1 Gi/o reconstitution (PMID 12721292), Factor Xa/PAR2
endothelial signaling (PMID 11850418), PAR2 Gq/11 signaling (PMID 20215560),
CCL5/GPR75 functional signaling (PMID 17001303), and separate GPR75 Gαq/11
coupling evidence (PMID 28325781).
