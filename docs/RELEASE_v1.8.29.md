# mSCIdblit Module 20B–24B mechanism graph v1.8.29

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-024`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion024/`

This twenty-fourth selective literature-expansion release adds five
source-linked ligand–receptor–transcription-factor/output annotations. The
intracellular continuation and terminal target-gene layers remain unresolved:

- Leptin → LEPRb Tyr1138-associated STAT3 → hypothalamic energy-balance output
- GDF6/BMP13 → BMPR1A/ALK3 with type-II receptor context → SMAD1/5/8 output
- GDF7/BMP12 → BMPR1B/ALK6 with type-II receptor context → SMAD1/5/8 output
- BMP10 → ACVRL1:BMPR2 → SMAD1/5/8 output
- BMP9/GDF2 → ACVRL1/ALK1 with endoglin context → SMAD1/5/8 output

The leptin entry preserves Tyr1138 site-specific genetic evidence. The BMP
entries preserve type-I/type-II receptor dependence, the primary model
contexts and pathway-level SMAD output; the BMP9 entry also retains the
reported SMAD2 branch. None of these routes asserts a causal graph edge or a
database confidence score.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,167 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 120 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 18 |
| Cumulative L→R→intracellular→output annotations missing TF | 33 |
| Cumulative L→R→TF→output annotations missing intracellular | 45 |
| Cumulative L→R→output-only annotations | 14 |

The graph topology and causal edge counts are unchanged from v1.8.28. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies reviewed for this batch include PMID 12594516
(leptin–LEPRb Tyr1138–STAT3), PMID 16049014 (GDF6/GDF7/BMP10 receptor-
dependent SMAD1/5/8 activation), and PMID 19366699 with PMCID PMC2708876
(BMP9/ALK1/endoglin-dependent endothelial SMAD1/5/8 phosphorylation).
