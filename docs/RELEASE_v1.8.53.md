# mSCIdblit Module 20B–24B mechanism graph v1.8.53

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-048`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion048/`

This forty-eighth selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations for
norepinephrine/adrenergic receptors:

- Norepinephrine → ADRA1A/α1A → phosphoinositide, intracellular-calcium and MAPK output
- Norepinephrine → ADRA1B/α1B → phosphoinositide, intracellular-calcium and subtype-dependent kinase output
- Norepinephrine → ADRA1D/α1D → subtype-dependent signaling output
- Norepinephrine → ADRA2A/α2A → Gi-linked cAMP-inhibition output
- Norepinephrine → ADRA2B/α2B → context-dependent cAMP output
- Norepinephrine → ADRA2C/α2C → receptor-density-dependent cAMP output
- Norepinephrine → ADRB2/β2 → ligand-selective cAMP and ERK output
- Norepinephrine → ADRB3/β3 → neural-precursor activation and proliferation output

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. Receptor subtype, recombinant-expression,
host-cell, receptor-density, ligand-bias, pharmacological-assignment and
assay contexts are retained; intracellular continuation, TF and target-gene
layers remain unresolved in all eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,355 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 308 |
| Unique covered queue candidates | 293 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 133 |
| Unused downstream queue candidates remaining | 3,038 |
| Unused P1 queue candidates remaining | 1,971 |

The graph topology and causal edge counts are unchanged from v1.8.52. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented in this batch include PMID 11358336 for cloned
human α1-subtype signaling, PMID 9371546 for α2-subtype adenylyl-cyclase
regulation, PMID 22241475 for β2 ligand-selective cAMP/ERK responses, and
PMID 20164362 for β3-mediated neural-precursor activation.
