# mSCIdblit Module 20B–24B mechanism graph v1.8.54

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-049`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion049/`

This forty-ninth selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations for the
human bitter-receptor family:

- Denatonium → hTAS2R47 → calcium and receptor-catalysed G-protein activation output
- Denatonium → hTAS2R4 → calcium and receptor/G-protein activation output
- Denatonium → hTAS2R8 → calcium and receptor/G-protein activation output
- Denatonium → hTAS2R10 → calcium and receptor/G-protein activation output
- Denatonium → hTAS2R13 → calcium and receptor/G-protein activation output
- Denatonium → hTAS2R39 → calcium and receptor/G-protein activation output
- Denatonium → hTAS2R43 → calcium and receptor/G-protein activation output
- Denatonium → hTAS2R46 → calcium and receptor/G-protein activation output

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. Heterologous receptor-panel,
concentration and assay contexts are retained; intracellular continuation, TF
and target-gene layers remain unresolved in all eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,363 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 316 |
| Unique covered queue candidates | 301 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 141 |
| Unused downstream queue candidates remaining | 3,030 |
| Unused P1 queue candidates remaining | 1,963 |

The graph topology and causal edge counts are unchanged from v1.8.53. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

The eight annotations are supported by the quantitative human TAS2R ligand
panel study PMID 20022913 (DOI 10.1093/chemse/bjp092), which challenged 25
human bitter receptors with a broad bitter-compound panel and measured
receptor-linked functional responses.
