# mSCIdblit Module 20B–24B mechanism graph v1.8.45

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-040`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion040/`

This fortieth selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations in an
EGFR/ERBB receptor-family pass:

- epiregulin → EGFR → receptor tyrosine-phosphorylation and mitogenic signaling output
- epiregulin → ERBB4/HER4 → receptor tyrosine-phosphorylation and signaling output
- HB-EGF → EGFR → receptor-associated smooth-muscle migration output
- HB-EGF → ERBB4/HER4 → receptor activation, PI3K association and chemotaxis output
- betacellulin → EGFR → receptor tyrosine-phosphorylation and activation output
- betacellulin → ERBB4/HER4 → receptor activation and cellular-response output
- amphiregulin → EGFR → receptor autophosphorylation and epithelial mitogenic output
- CSPG5/neuroglycan C/NRG6 → ERBB3/HER3 → receptor-family phosphorylation and growth output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores, and they do
not assert SCI-specific effects. The HB-EGF–HER4 PI3K association is retained
as assay-linked context, not promoted to a causal intermediate edge. All other
intracellular continuation, TF, and target-gene layers remain unresolved in
these eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,291 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 244 |
| Unique covered queue candidates | 229 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 69 |
| Unused downstream queue candidates remaining | 3,102 |
| Unused P1 queue candidates remaining | 2,035 |

The graph topology and causal edge counts are unchanged from v1.8.44. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors, and
the release preserves all prior `LITEXP` overlay records.

Primary studies represented in this batch include PMID 9419975
(epiregulin-EGFR/ErbB4), PMID 8349739 and PMID 9135143 (HB-EGF-EGFR/ErbB4),
PMID 8570211 (betacellulin-EGFR/ErbB4), PMID 7929459 (amphiregulin-EGFR), and
PMID 15358134 (neuroglycan C/ErbB3).
