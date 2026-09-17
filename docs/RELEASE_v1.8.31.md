# mSCIdblit Module 20B–24B mechanism graph v1.8.31

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-026`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion026/`

This twenty-sixth selective literature-expansion release adds five
source-linked routes with receptor-proximal continuation evidence:

- PDGF-BB → PDGFRB → JAK1/JAK2/TYK2 → STAT3 activation output
- PDGF-BB → PDGFRB Tyr1021 → PLCγ1 → inositol-phosphate/DNA-synthesis output
- BDNF → TrkB Tyr515 → FRS2A → MAPK-associated output
- GAS6 → MERTK → VAV3 → phagocytic output
- GAS6 → MERTK → SRC → phagocytic output

The PDGFRB/JAK entry retains JAK association and STAT activation without
asserting a fully ordered relay. The PDGFRB/PLCγ1 and TrkB/FRS2A entries
preserve receptor-site boundaries. The two MERTK entries retain association
evidence from phosphorylated receptor-domain and RPE/phagocytosis systems.
Terminal transcription-factor or target-gene layers remain unresolved where
not directly supported. None of these routes asserts a causal graph edge or a
database confidence score.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,177 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 130 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 19 |
| Cumulative L→R→intracellular→output annotations missing TF | 37 |
| Cumulative L→R→TF→output annotations missing intracellular | 45 |
| Cumulative L→R→output-only annotations | 19 |

The graph topology and causal edge counts are unchanged from v1.8.30. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies reviewed for this batch include PMID 8657151 (PDGFRβ-
associated JAK/STAT signaling), PMID 7678051 with PMCID PMC358893 (PDGFRβ
PLCγ1 docking and output), PMID 10196222 (TrkB/FRS2A/MAPK), and PMCID
PMC3563642 (MERTK-associated VAV3 and SRC phagocytic signaling).
