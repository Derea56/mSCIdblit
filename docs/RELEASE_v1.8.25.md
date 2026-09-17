# mSCIdblit Module 20B–24B mechanism graph v1.8.25

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-020`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion020/`

This twentieth selective literature-expansion release adds five
source-linked ligand–receptor-to-transcription-factor/output annotations.
Each preserves the missing intracellular continuation and terminal target
gene as unresolved evidence layers for mSCS plausibility analysis:

- MSTN → ACVR2B:ALK5 → SMAD2/3 → reporter/phosphorylation output
- Activin E/INHBE → ACVR1C/ALK7 → SMAD2 → adipocyte gene-expression output
- BMP15/GDF9B → BMPR1B/ALK6 → SMAD1/5/8 → reporter output
- BMP9 → ACVR1/ALK2 → SMAD1/5/8 → ovarian-cell functional output
- High-mannose/alpha-mannan → CLEC6A/Dectin-2 → NF-κB → inflammatory activation output

The BMP9/ALK2 entry remains explicitly bounded to the reported ovarian-cell
context and does not generalize to endothelial ALK1. The BMP15 entry preserves
the covalently dimerized S356C ligand form, BMPR2 co-receptor context and
granulosa-cell assays. The Activin E entry preserves the adipocyte and mouse
genetic contexts. None of these routes asserts a causal graph edge or a
database confidence score.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,147 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 100 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 15 |
| Cumulative L→R→intracellular→output annotations missing TF | 28 |
| Cumulative L→R→TF→output annotations missing intracellular | 33 |
| Cumulative L→R→output-only annotations | 14 |

The graph topology and causal edge counts are unchanged from v1.8.24. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies reviewed for this batch include PMID 14517293
(myostatin/ActRIIB–ALK5 and SMAD2/3 reporter signaling), PMCID PMC11873131,
PMID 37523551 and PMCID PMC10410708 (activin E/ALK7, SMAD2 and adipocyte
outputs), PMID 22294741 and DOI 10.1210/en.2010-1390 (BMP15/BMPR1B and
SMAD1/5/8 reporter output), PMID 2892305, PMCID PMC2892305 and DOI
10.1016/j.ymgme.2009.04.004 (context-bounded BMP9/ALK2 and SMAD1/5/8), and
PMIDs 16423983 and 17050534 (Dectin-2 mannan recognition, FcRγ-associated
activation and NF-κB output).
