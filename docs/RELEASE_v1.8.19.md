# mSCIdblit Module 20B–24B mechanism graph v1.8.19

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-014`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion014/`

This fourteenth selective literature-expansion release adds five
source-linked route annotations with receptor-proximal intracellular support:

- Phosphatidylserine → TREM2 → DAP12/TYROBP → reporter and apoptotic-cell-recognition output
- S1P → TREM2 → DAP12/TYROBP → microglial phagocytosis output
- Microglia-derived TG2 → ADGRG1/GPR56 → RhoA → OPC proliferation and myelin/remyelination output
- Astrocyte-derived ET-1 → EDNRA/ETA → YAP1 nuclear signaling → microglial phenotype output after spinal-cord contusion
- Astrocyte-derived ET-1 → EDNRB/ETB → YAP1 nuclear signaling → microglial phenotype output after spinal-cord contusion

The annotations preserve receptor aliases, adaptor or signaling-state
context, assay model, perturbation context, and species or injury limits. The
TREM2 entries retain DAP12 only because the cited assays directly use or test
TREM2–DAP12 signaling. The TG2 entry retains RhoA because RhoA activation is
reported in the ADGRG1/OPC system. The ETA and ETB entries remain separate so
mSCS can evaluate receptor-specific plausibility. TF and target-gene layers
remain unresolved in all five routes. Each route remains an evidence record
for mSCS rather than a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,117 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 70 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 14 |
| Cumulative L→R→intracellular→output annotations missing TF | 22 |
| Cumulative L→R→TF→output annotations missing intracellular | 14 |
| Cumulative L→R→output-only annotations | 10 |

The graph topology and causal edge counts are unchanged from v1.8.18. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 31101881 with PMCID
PMC6525155 (phosphatidylserine–TREM2–DAP12); PMID 35847502 with PMCID
PMC9279640 and DOI 10.1016/j.apsb.2021.10.012 (S1P–TREM2–DAP12); PMID 29809138
with PMCID PMC5980231 and DOI 10.7554/eLife.33385 (microglial TG2–ADGRG1–RhoA);
and PMID 40443301 with PMCID PMC12376558 and DOI 10.1002/advs.202507215
(astrocytic ET-1, endothelin receptors and microglial YAP after spinal-cord
contusion).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
