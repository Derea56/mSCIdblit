# mSCIdblit Module 20B–24B mechanism graph v1.8.61

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-056`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion056/`

This fifty-sixth selective literature-expansion release adds seven source-linked
myelin-associated glycoprotein (`MAG`) ligand–receptor/recognition annotations:

- MAG → PirB/LILRB2 → myelin-inhibitory neurite-growth output
- MAG → NgR2/RTN4R2 → sialic-acid-dependent neurite-inhibition output
- MAG → NgR1/RTN4R → neurite-outgrowth inhibition
- MAG → LRP1/CD91 → p75NTR/RhoA-associated neurite-inhibition output
- MAG → GT1b → neuronal glycan recognition and neurite inhibition
- MAG → GD1a → neuronal glycan recognition and neurite inhibition
- MAG → beta1 integrin → FAK phosphorylation and growth-cone turning output

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. The evidence preserves receptor competition,
sialic-acid dependence, ganglioside presentation, LRP1/p75NTR association and
FAK/RhoA readouts where reported, while leaving a complete intracellular-to-TF
route unresolved.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,413 |
| Literature-expansion annotations in this batch | 7 |
| Cumulative literature-expansion annotations | 366 |
| Unique covered queue candidates | 351 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 191 |
| Unused downstream queue candidates remaining | 2,980 |
| Unused P1 queue candidates remaining | 1,913 |

The graph topology and causal edge counts are unchanged from v1.8.60. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented include MAG-PirB (PMID 18988857), MAG-NgR2
(PMID 15673660; PMCID PMC6725623), MAG-NgR1 (PMID 12160746), MAG-LRP1
(PMID 23132925; PMCID PMC3603516), MAG-GT1b/GD1a (PMID 8570640;
PMCID PMC40139; PMID 12060784), and MAG-beta1 integrin (PMID 18922173;
PMCID PMC2576245). The receptor-linked neurite-inhibition interpretation is
consistent with the primary PirB, NgR2, LRP1 and beta1-integrin studies.
