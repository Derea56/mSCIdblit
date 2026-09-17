# mSCIdblit Module 20B–24B mechanism graph v1.8.47

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-042`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion042/`

This forty-second selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations:

- CCL15/MIP-5/HCC-2 → CCR3 → calcium flux and chemotaxis output
- CCL7/MCP-3 → CCR1 → monocyte activation output
- CCL7/MCP-3 → CCR2 → monocyte activation output
- CCL7/MCP-3 → CCR3 → calcium and eosinophil chemotaxis output
- CCL7/MCP-3 → CCR5 → binding and agonist-inhibition output
- CCL27/CTACK → CCR10 → calcium flux, skin-homing T-cell chemotaxis and recruitment output
- CCL8/MCP-2 → CCR1 → calcium and monocyte chemotaxis output
- CCL8/MCP-2 → CCR2B → calcium and monocyte chemotaxis output

The CCL7–CCR5 annotation is explicitly inhibitory/non-signaling: the cited
study supports high-affinity binding without productive activation and
inhibition of another CCR5 agonist. These records remain evidence-layer
annotations for mSCS route plausibility. They do not create causal graph edges
or database confidence scores, and they do not assert SCI-specific effects.
Intracellular continuation, TF, and target-gene layers remain unresolved in
all eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,307 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 260 |
| Unique covered queue candidates | 245 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 85 |
| Unused downstream queue candidates remaining | 3,086 |
| Unused P1 queue candidates remaining | 2,019 |

The graph topology and causal edge counts are unchanged from v1.8.46. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented in this batch include PMID 9346309 and PMID 14984572
(CCL15–CCR3), PMID 14733956 and PMID 9005985 (CCL7–CCR1/CCR2/CCR3), PMID 10477718
(CCL7–CCR5), PMID 10725697 and PMID 11821900 (CCL27–CCR10), and PMID 9115216
(CCL8–CCR1/CCR2B).
