# mSCIdblit Module 20B–24B mechanism graph v1.8.51

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-046`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion046/`

This forty-sixth selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations for
acetylcholine receptors:

- Acetylcholine → CHRM3/M3 → T-type calcium-current modulation output
- Acetylcholine → CHRM5/M5 → T-type calcium-current modulation output
- Acetylcholine → CHRNA3:CHRNB2 → intracellular-calcium and nAChR-current output
- Acetylcholine → CHRNA4:CHRNB2 → intracellular-calcium and nAChR-current output
- Acetylcholine → CHRNA3:CHRNB4 → whole-cell and single-channel-current output
- Acetylcholine → CHRNA4:CHRNB4 → whole-cell-current and desensitization output
- Acetylcholine → CHRNA2:CHRNB4 → intracellular-calcium and nAChR-current output
- Acetylcholine → CHRNA3:CHRNB3:CHRNB4 → gating and concentration-response output

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. Recombinant expression systems, receptor
assembly, species, host-cell and stoichiometry contexts, and assay boundaries
are retained; intracellular continuation, TF, and target-gene layers remain
unresolved in all eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,339 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 292 |
| Unique covered queue candidates | 277 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 117 |
| Unused downstream queue candidates remaining | 3,054 |
| Unused P1 queue candidates remaining | 1,987 |

The graph topology and causal edge counts are unchanged from v1.8.50. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented in this batch include PMID 10954332 (M3/M5
muscarinic calcium-current modulation), PMID 11044726 and PMID 8987816
(alpha3beta2 and alpha4beta2 nicotinic receptors), PMID 7707862 and PMID
12912995 (alpha3beta4 and beta3-containing alpha3beta4), PMID 16825297
(alpha4beta4), PMID 9454827 (alpha2beta4), and PMID 11118490
(alpha3beta3beta4 stoichiometry).
