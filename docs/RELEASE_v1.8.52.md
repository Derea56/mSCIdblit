# mSCIdblit Module 20B–24B mechanism graph v1.8.52

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-047`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion047/`

This forty-seventh selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations for
serotonin receptors:

- Serotonin → HTR1A/5-HT1A → Gi/o-linked cAMP modulation output
- Serotonin → HTR2A/5-HT2A → intracellular-calcium and phosphoinositide output
- Serotonin → HTR1D/5-HT1D → Gi-linked cAMP inhibition output
- Serotonin → HTR4/5-HT4 → Gs-linked cAMP activation output
- Serotonin → HTR6/5-HT6 → adenylyl-cyclase activation output
- Serotonin → HTR7/5-HT7 → cAMP activation output
- Serotonin → HTR1E/5-HT1E → cAMP modulation output
- Serotonin → HTR1F/5-HT1F → Gi-linked cAMP inhibition output

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. Recombinant expression systems, species,
host-cell and assay contexts, and assay boundaries are retained;
intracellular continuation, TF, and target-gene layers remain unresolved in
all eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,347 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 300 |
| Unique covered queue candidates | 285 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 125 |
| Unused downstream queue candidates remaining | 3,046 |
| Unused P1 queue candidates remaining | 1,979 |

The graph topology and causal edge counts are unchanged from v1.8.51. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

The inherited queue locator for the 5-HT2 row labeled `PMCID:PMC455123` was
checked against the primary record and corrected here to PMID 2854054; the
PMCID and PMID refer to the same 5-HT2 receptor study. This batch also retains
primary records for the 5-HT1A, 5-HT1D, 5-HT4, 5-HT6, 5-HT7, 5-HT1E, and 5-HT1F
functional readouts.

Primary studies represented in this batch include PMID 2549039, PMID 2854054
(PMCID PMC455123), PMID 1565658, PMID 9276448, PMID 9349523, PMID 8522988,
PMID 8397408 (PMCID PMC47394), PMID 1608964, PMID 7984278, PMID 8380639, and
PMID 8133900.
