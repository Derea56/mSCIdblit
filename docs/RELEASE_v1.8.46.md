# mSCIdblit Module 20B–24B mechanism graph v1.8.46

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-041`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion041/`

This forty-first selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations in a
chemokine-receptor pass:

- CXCL4/PF4 → CCR1 → calcium flux, receptor endocytosis and monocyte chemotaxis output
- CCL11/eotaxin-1 → CCR2 → partial-agonist calcium and monocyte chemotaxis output
- CCL26/eotaxin-3 → CCR3 → eosinophil/basophil chemotaxis and activation output
- CCL26/eotaxin-3 → CX3CR1 → calcium flux, chemotaxis and immune-cell recruitment output
- XCL2/SCM-1beta → XCR1 → monomeric-ligand calcium-flux and chemotaxis output
- CCL13/MCP-4 → CCR2 → calcium flux and monocyte chemotaxis output
- CCL13/MCP-4 → CCR3 → calcium flux, basophil chemotaxis and mediator-release output
- CCL15/MIP-5/HCC-2 → CCR1 → calcium flux and monocyte chemotaxis output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores, and they do
not assert SCI-specific effects. Chemokine concentration, ligand processing,
glycosaminoglycan presentation, receptor species, and agonist potency are
retained as context; intracellular continuation, TF, and target-gene layers
remain unresolved in these eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,299 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 252 |
| Unique covered queue candidates | 237 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 77 |
| Unused downstream queue candidates remaining | 3,094 |
| Unused P1 queue candidates remaining | 2,027 |

The graph topology and causal edge counts are unchanged from v1.8.45. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented in this batch include PMID 29930254
(CXCL4-CCR1), PMID 11559700 (CCL11-CCR2), PMID 16102831, PMID 35742962 and
PMID 9276730 (CCL26-CCR3), PMID 20974991 (CCL26-CX3CR1), PMID 25497737
(XCL2-XCR1), PMID 8955214, PMID 9062350 and PMID 9276730 (CCL13-CCR2/CCR3),
and PMID 9346309 and PMID 14984572 (CCL15-CCR1).
