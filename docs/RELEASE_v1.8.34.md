# mSCIdblit Module 20B–24B mechanism graph v1.8.34

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-029`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion029/`

This twenty-ninth selective literature-expansion release adds eight unused
P1 candidates as source-linked `ligand → receptor → intracellular
continuation → output` annotations. The batch broadens receptor-proximal
coverage across vascular, erythroid, growth-factor and neurotrophin signaling:

- VEGFA → VEGFR2 → NCK → FYN/PAK2/p38 and endothelial-migration output
- EPO → EPOR → PI3K p85 → MAPK-linked erythroid output
- PDGF-BB → PDGFRB → PLCG1 → phosphoinositide/PKC-associated output
- FGF1 → FGFR1 → PLCG1 → phosphoinositide/calcium output
- EGF → EGFR → CBL → ubiquitination/endocytic signal attenuation
- BDNF → TrkB → SHC1/FRS2 → neuronal migration/differentiation output
- EPO → EPOR → SHP1 → JAK2/proliferative-signal termination output
- EGF → EGFR → SHP2 → Ras/ERK regulatory output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges, database confidence scores or SCI-specific
claims. All eight source queue identifiers are unique within the cumulative
literature-expansion set.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,203 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 156 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 55 |
| Cumulative L→R→TF→output annotations missing intracellular | 45 |
| Cumulative L→R→output-only annotations | 19 |
| Unused downstream queue candidates remaining | 3,190 |

The graph topology and causal edge counts are unchanged from v1.8.33. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies reviewed for this batch include PMID 16966330 (VEGFR2
pY1214/NCK/FYN/p38), PMID 9096338 (EPOR pY479/PI3K/MAPK), PMID 7689724 and
PMID 9507012 (PDGFRB pY1021/PLCG1), PMID 1656221, PMID 1379697 and PMID
1379698 (FGFR1/PLCG1), PMID 11823423 (EGFR pY1045/CBL), PMID 15372074
(TrkB pY515/Shc), PMID 7889566 (EPOR pY429/SHP1/JAK2 termination), and PMID
14560030 (EGFR pY992/SHP2/Ras-ERK).
