# mSCIdblit Module 20B–24B mechanism graph v1.8.38

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-033`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion033/`

This thirty-third selective literature-expansion release adds eight unused
P1 candidates as source-linked `ligand → receptor → intracellular continuation
→ output` annotations. The batch expands receptor-proximal coverage across
immune, purinergic and prolactin systems:

- CD47 → SIRPA → SHP1 → macrophage redox/NO output
- CD47 → SIRPA → SHP2 → macrophage redox/NO output
- ATP → P2X2 → VILIP1 → calcium/surface-expression output
- ATP → P2X2 → FE65 → synaptic receptor-function output
- ATP → P2X7 → RPTPβ → phosphorylation/blebbing-feedback output
- ATP → P2Y1 → NHERF2 → calcium-signal-duration output
- ADP → P2Y12 → NHERF1 → internalization output
- prolactin → PRLR → SHP2 → receptor-proximal output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores, and they do
not assert SCI-specific effects. The TF and terminal target-gene layers remain
explicitly unresolved in all eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,235 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 188 |
| Unique covered queue candidates | 173 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 79 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 19 |
| Unused downstream queue candidates remaining | 3,158 |
| Unused P1 queue candidates remaining | 2,091 |

The graph topology and causal edge counts are unchanged from v1.8.37. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies represented in this batch include PMID 11283158 and PMID
16055727 (SIRPα signaling), PMID 18922787 and PMID 22090499 (P2X2–VILIP1),
PMID 16330549 (P2X2–FE65), PMID 11707406 (P2X7–RPTPβ), PMID 15901899
(P2Y1–NHERF2), PMID 22610101 (P2Y12–NHERF1), and PMID 10991949
(PRLR–SHP2).
