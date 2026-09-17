# mSCIdblit Module 20B–24B mechanism graph v1.8.42

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-037`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion037/`

This thirty-seventh selective literature-expansion release adds eight unused
P1 candidates as source-linked `ligand → receptor → output` annotations. These
records deliberately preserve the intracellular and TF layers as unresolved:

- CXCL9 → CXCR3 → G-protein/calcium and T-cell chemotaxis output
- CXCL10 → CXCR3 → G-protein/calcium and T-cell chemotaxis output
- CXCL11 → CXCR3 → G-protein/calcium and T-cell chemotaxis output
- CCL20 → CCR6 → G-protein/receptor-signaling output
- CXCL16 → CXCR6 → calcium, adhesion, chemotaxis and shedding output
- CCL19 → CCR7 → G-protein/β-arrestin/calcium and dendritic-cell chemotaxis output
- CCL21 → CCR7 → G-protein/β-arrestin/calcium and dendritic-cell chemotaxis output
- netrin-1 → UNC5C → receptor phosphorylation and axon-guidance output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores, and they do
not assert SCI-specific effects. Receptor activation, second-messenger,
adhesion, migration, and phosphorylation outputs are not treated as evidence
of a particular intracellular relay, TF, or target gene.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,267 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 220 |
| Unique covered queue candidates | 205 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 45 |
| Unused downstream queue candidates remaining | 3,126 |
| Unused P1 queue candidates remaining | 2,059 |

The graph topology and causal edge counts are unchanged from v1.8.41. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies represented in this batch include PMID 11259614 and PMID
15150261 (CXCL9/CXCL10/CXCL11-CXCR3), PMID 20363748 (CXCL11-CXCR3), PMID
32541785 and PMID 15483227 (CCL20-CCR6), PMID 11290797 and PMID 17363916
(CXCL16-CXCR6), PMID 25614627 and PMID 28018341 (CCL19/CCL21-CCR7), and
PMID 15574733 (netrin-1-UNC5C).
