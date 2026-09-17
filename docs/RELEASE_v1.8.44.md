# mSCIdblit Module 20B–24B mechanism graph v1.8.44

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-039`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion039/`

This thirty-ninth selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations. These
records deliberately preserve the intracellular and TF layers as unresolved:

- SHH → BOC → Hedgehog receptor-complex and cerebellar progenitor proliferation output
- mature VEGF-C → FLT4/VEGFR3 → receptor dimerization/autophosphorylation output
- processed VEGF-C → KDR/VEGFR2 → receptor phosphorylation and endothelial migration output
- VEGF-D → KDR/VEGFR2 → receptor phosphorylation and endothelial output
- NRG2-beta → ERBB3 → receptor phosphorylation, MAPK and proliferation output
- NRG2-beta → ERBB4 → receptor phosphorylation, MAPK and proliferation output
- ephrin-B1 → EPHB2 → receptor phosphorylation and neuronal adaptor output
- pleiotrophin → PTPRZ1 → receptor-phosphatase inhibition and beta-catenin phosphorylation output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores, and they do
not assert SCI-specific effects. Receptor activation, reporter, phosphorylation,
neuronal, vascular, and cellular functional outputs are not treated as evidence
of a particular intracellular relay, TF, or target gene.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,283 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 236 |
| Unique covered queue candidates | 221 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 61 |
| Unused downstream queue candidates remaining | 3,110 |
| Unused P1 queue candidates remaining | 2,043 |

The graph topology and causal edge counts are unchanged from v1.8.43. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies represented in this batch include PMID 21664577 (BOC/Hedgehog),
PMID 23878260 and PMID 8617204 (VEGF-C/VEGFR3 and VEGFR2), PMID 11279005 and
PMID 15215251 (VEGF-D/VEGFR2), PMID 9742126, PMID 10214951 and PMID 9168114
(NRG2-ErbB3/ErbB4), PMID 16101278 and PMID 9233798 (ephrin-B1-EphB2), and
PMID 10706604 (pleiotrophin-PTPRZ1).
