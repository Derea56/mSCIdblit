# mSCIdblit Module 20B–24B mechanism graph v1.8.48

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-043`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion043/`

This forty-third selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations in a
glutamatergic receptor pass:

- Glutamate → GRM5/mGluR5 → inositol-phosphate and intracellular-calcium output
- Glutamate → GRM2/mGluR2 → forskolin-stimulated cAMP inhibition output
- Glutamate → GRM3/mGluR3 → forskolin-stimulated cAMP inhibition output
- Glutamate → GRM4/mGluR4 → forskolin-stimulated cAMP inhibition output
- Glutamate → GRM6/mGluR6 → pertussis-toxin-sensitive cAMP inhibition output
- Glutamate → GRM7/mGluR7 → high-concentration cAMP inhibition output
- Glutamate → GRM8/mGluR8 → forskolin-stimulated adenylyl-cyclase inhibition output
- Glutamate → GRIA2/GluA2Q → homomeric AMPA calcium-flux output

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. Recombinant expression systems, receptor
isoforms/editing states, species, agonist potency, and assay boundaries are
retained; intracellular continuation, TF, and target-gene layers remain
unresolved in all eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,315 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 268 |
| Unique covered queue candidates | 253 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 93 |
| Unused downstream queue candidates remaining | 3,078 |
| Unused P1 queue candidates remaining | 2,011 |

The graph topology and causal edge counts are unchanged from v1.8.47. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented in this batch include PMID 8532169 (mGluR5), PMID
7620613 (mGluR2), PMID 8887960 and PMID 7643921 (mGluR3), PMID 7617140 (mGluR4),
PMID 9144651 (mGluR6), PMID 8145723 (mGluR7), PMID 7722646 (mGluR8), and PMID
16475972 (GluA2/GluR2).
