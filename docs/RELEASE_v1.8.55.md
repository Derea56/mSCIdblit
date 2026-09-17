# mSCIdblit Module 20B–24B mechanism graph v1.8.55

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-050`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion050/`

This fiftieth selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations:

- LPA → LPAR1/EDG2 → binding, G-protein activation, neurite-retraction and growth output
- LPA → LPAR2/EDG4 → binding and serum-response-element activation output
- LPA → LPAR3/EDG7 → calcium mobilization and cAMP-modulation output
- LPA → LPAR4/GPR23 → binding, calcium/cAMP, Rho and neurite-retraction output
- LPA → LPAR5/GPR92 → binding, receptor internalization, G-protein and cAMP output
- LPA → LPAR6/P2Y5 → binding, GTP binding, Rho-dependent morphology and cAMP output
- SST-14 → SSTR1 → pertussis-toxin-sensitive cAMP inhibition and Na+/H+ exchange output
- SST-14 → SSTR2 → pertussis-toxin-sensitive cAMP inhibition output

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
| Evidence-route records | 16,371 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 324 |
| Unique covered queue candidates | 309 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 149 |
| Unused downstream queue candidates remaining | 3,022 |
| Unused P1 queue candidates remaining | 1,955 |

The graph topology and causal edge counts are unchanged from v1.8.54. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented in this batch include the LPAR1/EDG2 functional
study PMID 9600933, the LPAR2/EDG4 study PMID 9525886, the LPAR3/EDG7 study
PMID 10488122, and the SSTR1/SSTR2 coupling study PMID 8144617.
