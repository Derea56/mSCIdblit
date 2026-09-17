# mSCIdblit Module 20B–24B mechanism graph v1.8.56

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-051`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion051/`

This fifty-first selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations:

- S1P → S1PR1/EDG1 → Gi/o-linked phospholipase-C, calcium, MAPK and cAMP output
- S1P → S1PR2/EDG5 → serum-response-element reporter and calcium-efflux output
- S1P → S1PR3/EDG3 → binding, calcium, phosphoinositide, MAPK and cAMP output
- S1P → S1PR4/EDG6 → pertussis-toxin-sensitive ERK, calcium and phosphoinositide output
- S1P → S1PR5/EDG8 → GTP-binding, Gi/o-linked cAMP and oligodendrocyte-process output
- SST-14 → SSTR3 → PLC-beta3, IP3, calcium, contraction and cAMP output
- SST-14 → SSTR4 → preferential-binding and adenylyl-cyclase-inhibition output
- SST-14 → SSTR5 → preferential-binding and pertussis-toxin-sensitive cAMP-inhibition output

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. Receptor-expression, species, ligand-form,
assay and subtype-specific coupling contexts are retained; intracellular
continuation, TF and target-gene layers remain unresolved in all eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,379 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 332 |
| Unique covered queue candidates | 317 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 157 |
| Unused downstream queue candidates remaining | 3,014 |
| Unused P1 queue candidates remaining | 1,947 |

The graph topology and causal edge counts are unchanged from v1.8.55. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented in this batch include S1PR1/EDG1 PMID 9765227,
S1PR2/EDG5 PMID 9409733, S1PR3/EDG3 PMID 10381367, S1PR4/EDG6 PMID 10679247,
S1PR5/EDG8 PMID 11705398, SSTR3 PMID 8798553, SSTR4 PMID 1362243, and SSTR5
PMID 7908405.
