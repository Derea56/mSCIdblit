# mSCIdblit Module 20B–24B mechanism graph v1.8.43

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-038`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion038/`

This thirty-eighth selective literature-expansion release adds eight unused
P1 candidates as source-linked `ligand → receptor → output` annotations. These
records deliberately preserve the intracellular and TF layers as unresolved:

- NT4 → TrkB → receptor phosphorylation and neuronal differentiation output
- IL9 → IL9RA:IL2RG → receptor-complex proliferation output
- neurturin → GFRA2:RET → receptor-complex/MAPK reporter output
- artemin → GFRA3:RET → neuronal survival and receptor-activation output
- SEMA3E → PLXND1 → endothelial repulsion and vascular-patterning output
- SEMA6D → PLXNA1 → morphogenetic and gene-expression output
- TGF-β3 → TGFBR1:TGFBR2 → Smad reporter output
- Activin A → ACVR1B:ACVR2B → receptor phosphorylation and reporter output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores, and they do
not assert SCI-specific effects. Receptor activation, reporter, neuronal,
vascular, and cellular functional outputs are not treated as evidence of a
particular intracellular relay, TF, or target gene.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,275 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 228 |
| Unique covered queue candidates | 213 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 53 |
| Unused downstream queue candidates remaining | 3,118 |
| Unused P1 queue candidates remaining | 2,051 |

The graph topology and causal edge counts are unchanged from v1.8.42. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies represented in this batch include PMID 1375038 (NT4-TrkB),
PMID 7718508 (IL9 receptor complex), PMID 31392261 and PMID 29414779
(NRTN-GFRA2-RET), PMID 9883723, PMID 17013378 and PMID 16765900
(ARTN-GFRA3-RET), PMID 15550623 and PMID 20385769 (SEMA3E-PLXND1), PMID
14977921 and PMID 36156831 (SEMA6D-PLXNA1), PMID 18243111 (TGF-β3
receptor complex), and PMID 8622651 (Activin receptor complex).
