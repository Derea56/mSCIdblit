# mSCIdblit Module 20B–24B mechanism graph v1.8.59

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-054`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion054/`

This fifty-fourth selective literature-expansion release adds ten source-linked
phosphatidylserine (`PtdSer`) ligand–receptor/recognition annotations with
bounded functional outputs:

- PtdSer → TIM4 → calcium-dependent apoptotic-cell recognition and efferocytosis
- PtdSer → BAI1 → ELMO/DOCK180/Rac-associated apoptotic-cell engulfment
- PtdSer → stabilin-2 → apoptotic-cell binding, engulfment and TGF-beta output
- PtdSer → CD300B → DAP12/ITAM-associated apoptotic-cell engulfment
- PtdSer → TIM3 → calcium-coordinated apoptotic-cell recognition and phagocytosis
- PtdSer → LOX1 → calcium-dependent apoptotic-body recognition
- PtdSer → CD300A → inhibitory dead-cell uptake and reporter output
- PtdSer → CD300F → metal-dependent recognition and efferocytosis
- PtdSer → GPR56 S4 → microglial synaptic-pruning output
- PtdSer → stabilin-1 → EGF-like-domain binding and efferocytosis

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. Some source studies report adaptor or
second-messenger involvement, but no complete intracellular-to-TF route was
materialized in this batch; those layers remain unresolved for all ten records.
Membrane presentation, apoptotic-cell, myeloid, developmental and receptor-
isoform contexts are retained in the evidence fields.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,399 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 352 |
| Unique covered queue candidates | 337 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 177 |
| Unused downstream queue candidates remaining | 2,994 |
| Unused P1 queue candidates remaining | 1,927 |

The graph topology and causal edge counts are unchanged from v1.8.58. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented include PtdSer/TIM4 (PMID 17960135), PtdSer/BAI1
(PMID 17960134), PtdSer/stabilin-2 (PMID 17962816; PMCID PMC2519725),
PtdSer/CD300B (PMCID PMC4211373), PtdSer/TIM3 (PMID 20083673), PtdSer/LOX1
(PMID 16146427), PtdSer/CD300A (PMID 22302738; PMCID PMC3327458),
PtdSer/CD300F (PMID 21865548; PMCID PMC3178745), PtdSer/GPR56
(PMID 32452062; PMCID PMC7429740), and PtdSer/stabilin-1 (PMID 19726632;
DOI 10.1242/jcs.049569).
