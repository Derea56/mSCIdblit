# mSCIdblit Module 20B–24B mechanism graph v1.8.36

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-031`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion031/`

This thirty-first selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → intracellular continuation
→ output` annotations. The batch fills receptor-proximal signaling gaps across
growth-factor, axon-guidance, cytokine and purinergic systems:

- EGF → EGFR → SHC1 → Grb2-SOS/Ras activation output
- ephrin-B1 → EPHB2 → SRC → receptor-activation output
- ephrin-A1 → EPHA2 → VAV2/VAV3 → Rac1/migration output
- ephrin-A1 → EPHA2 → PI3K p85 → Rac1/migration output
- EGF → EGFR → SHP1 → receptor dephosphorylation/MAPK attenuation output
- FGF1 → FGFR3 → PLCG1 → activation/transformation output
- prolactin → PRLR → JAK2 → kinase-activation output
- ATP → P2X7 → NLRP3 → inflammasome-recruitment output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges, database confidence scores or SCI-specific
claims. The TF and terminal target-gene layers remain explicitly unresolved in
all eight records. All eight source queue identifiers are unique within the
cumulative literature-expansion set.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,219 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 172 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 63 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 19 |
| Unused downstream queue candidates remaining | 3,174 |
| Unused P1 queue candidates remaining | 2,107 |

The graph topology and causal edge counts are unchanged from v1.8.35. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies reviewed for this batch include PMID 9544989 (EGFR
pY1148-SHC1/Ras), PMID 9632142 (EPHB2 pY611-SRC), PMID 18387945 and PMID
16782872 (EPHA2 phosphosite-VAV/PI3K branches), PMID 9733788 (EGFR
pY992-SHP1), PMID 15784730 (FGFR3 pY760-PLCG1), PMID 7515493
(PRLR-associated JAK2), and PMID 25690658 (P2X7-NLRP3 interaction).
