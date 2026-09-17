# mSCIdblit Module 20B–24B mechanism graph v1.8.72

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-067`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion067/`

This sixty-seventh selective literature-expansion release adds three
chemokine receptor routes with an explicitly supported intracellular
G-protein continuation:

- CCL3 → CCR1 → Gi-family coupling → neutrophil migration/inflammatory output
- CCL3 → CCR5 → GNAZ coupling → ERK/p38-associated neutrophil migration output
- CCL5 → CCR5 → GNAZ coupling → receptor activation output

The routes combine ligand/receptor-specific primary evidence with separate
receptor-transducer studies. That composite structure is explicit: the CCR5
GNAZ profile used MIP-1alpha stimulation, not CCL3 or CCL5, and therefore does
not establish exclusive ligand-specific GNAZ coupling. No TF, terminal target
gene, causal graph edge, database confidence score, or SCI transfer is
asserted.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,467 |
| Literature-expansion annotations in this batch | 3 |
| Cumulative literature-expansion annotations | 420 |
| Unique covered queue candidates | 405 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 88 |
| Cumulative L→R→TF→output annotations missing intracellular | 56 |
| Cumulative L→R→output-only annotations | 239 |
| Unused downstream queue candidates remaining | 2,926 |
| Unused P1 queue candidates remaining | 1,861 |

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented include CCL3/CCR1 neutrophil migration and
inflammatory mediator release (PMIDs 11404385 and 15831559), CCL3/CCR5
ERK/p38-dependent neutrophil migration (PMID 15567066), CCL5 receptor-specific
binding/activation (PMID 9289016), active CCL5–CCR5–Gi structural signaling
(PMID 34134983), and CCR5 GNAZ subtype coupling (DOI
10.7554/eLife.74101; PMCID PMC9005190).
