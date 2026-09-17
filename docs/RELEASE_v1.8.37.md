# mSCIdblit Module 20B–24B mechanism graph v1.8.37

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-032`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion032/`

This thirty-second selective literature-expansion release adds eight unused
P1 candidates as source-linked `ligand → receptor → intracellular continuation
→ output` annotations. The batch extends receptor-proximal coverage across
Eph, TAM, inhibitory immune-receptor and purinergic systems:

- ephrin-B1 → EPHB1 → NCK1 → JNK/cell-attachment output
- ephrin-A1 → EPHA2 → NCK1 → migration output
- Gas6 → TYRO3 → GRB2 → ERK/PI3K neuronal output
- HLA-G1 → LILRB2/ILT4 → SHP1 → inhibitory Fc-receptor output
- ATP → P2X7 → PANX1 → pore/IL-1β-processing output
- ATP → P2X7 → paxillin → NLRP3-complex output
- ATP → P2X7 → NLRP2 → astrocytic inflammasome output
- ATP → P2X7 → NLRP1 → neuronal inflammasome-complex output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges, database confidence scores or SCI-specific
claims. The TF and terminal target-gene layers remain explicitly unresolved
in all eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,227 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 180 |
| Unique covered queue candidates | 165 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 71 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 19 |
| Unused downstream queue candidates remaining | 3,166 |
| Unused P1 queue candidates remaining | 2,099 |

The graph topology and causal edge counts are unchanged from v1.8.36. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies represented in this batch include PMID 9430661 (EphB1
pY594-Nck), PMID 23358419 (EphA2 pY930-Nck), PMCID PMC2231337 (TYRO3-GRB2),
PMID 9842885 (LILRB2/ILT4-SHP1), PMID 17036048 and PMID 28495860 (P2X7-PANX1),
PMID 33243234 (P2X7-paxillin-NLRP3), PMID 23625868 (P2X7-NLRP2), and PMID
19416975 (P2X7-NLRP1).
