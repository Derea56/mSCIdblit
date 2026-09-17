# mSCIdblit Module 20B–24B mechanism graph v1.8.57

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-052`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion052/`

This fifty-second selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations for WNT3A:

- WNT3A → FZD3 → JNK activation and neurite-outgrowth output
- WNT3A → FZD10 → LRP6-dependent beta-catenin reporter and spinal-cord proliferation output
- WNT3A → FZD2 → LRP6 phosphorylation, beta-catenin stabilization and DVL output
- WNT3A → FZD7 → receptor-dependent canonical WNT reporter output
- WNT3A → FZD4 → LRP6 phosphorylation, beta-catenin stabilization and DVL output
- WNT3A → FZD5 → LRP6 phosphorylation, beta-catenin stabilization and DVL output
- WNT3A → RYK → WNT reporter and neurite-outgrowth output
- WNT3A → GPC5 → beta-catenin reporter and migration output

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. Receptor, species, cell-model, assay and
modulatory contexts are retained; intracellular continuation, TF and target-
gene layers remain unresolved in all eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,387 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 340 |
| Unique covered queue candidates | 325 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 165 |
| Unused downstream queue candidates remaining | 3,006 |
| Unused P1 queue candidates remaining | 1,939 |

The graph topology and causal edge counts are unchanged from v1.8.56. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented in this batch include WNT3A-FZD3 PMID 18212053,
WNT3A-FZD10 PMID 24599775, WNT-FZD2/FZD4/FZD5 PMID 25605717, WNT3A-FZD7
PMID 28733458, mammalian RYK/WNT3A PMID 15454084, and GPC5/WNT3A PMID 27157618.
