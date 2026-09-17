# mSCIdblit Module 20B–24B mechanism graph v1.8.49

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-044`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion044/`

This forty-fourth selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations for
ionotropic glutamate receptors:

- Glutamate → GRIA3/GluA3 → homomeric AMPA calcium-flux output
- Glutamate → GRIA4/GluA4 → homomeric AMPA calcium-flux output
- Glutamate → GRIK2/GluK2/GluR6 → kainate-channel current and calcium output
- Glutamate → GluN1/GluN2D → glutamate-plus-glycine channel-gating output
- Glutamate → GluK2/GluK5 → heteromeric kainate current and desensitization output
- Glutamate → GluN1/GluN2C → glutamate-plus-glycine channel-current output
- Glutamate → GluA2/GluA4 → heteromeric AMPA current and binding output
- Glutamate → GluK1/GluK4 → heteromeric kainate current and desensitization output

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. Recombinant expression systems, receptor
assembly, species, co-agonist requirements, editing/splice states, and assay
boundaries are retained; intracellular continuation, TF, and target-gene
layers remain unresolved in all eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,323 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 276 |
| Unique covered queue candidates | 261 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 101 |
| Unused downstream queue candidates remaining | 3,070 |
| Unused P1 queue candidates remaining | 2,003 |

The graph topology and causal edge counts are unchanged from v1.8.48. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented in this batch include PMID 16475972 (GluA3/GluA4),
PMID 7536611 and PMID 7528929 (GluK2/GluR6), PMID 22641781 (GluN1/GluN2D),
PMID 22114280 (GluK2/GluK5), PMID 18635641 (GluN1/GluN2C), PMID 10952090
(GluA2/GluA4), and PMID 25139762 (GluK1/GluK4).
