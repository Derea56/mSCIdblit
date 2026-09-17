# mSCIdblit Module 20B–24B mechanism graph v1.8.64

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-059`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion059/`

This fifty-ninth selective literature-expansion release adds seven
source-linked annotations:

- Galectin-3 → TLR4 → microglial inflammatory activation/readout
- Galectin-3 → CD146 → glycan-dependent clustering and AKT-linked function
- Galectin-3 → VEGFR2 → receptor retention/phosphorylation and angiogenesis
- Galectin-3 → αVβ3 integrin → glycan-dependent clustering, FAK and angiogenesis
- Galectin-3 → α3β1 integrin → glycan cross-linking, Rac1/FAK and lamellipodia
- Galectin-3 → MerTK → opsonized bacterial uptake by microglia
- WNT5A → ROR2/FZD7 receptor complex → Dishevelled/Rac1 and AP-1 reporter output

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores. The
release preserves glycan-dependent receptor modulation, opsonin-mediated
phagocytosis, and the distinction between an explicit pathway-level AP-1
readout and an unresolved intracellular relay. No terminal target gene is
asserted in this batch.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,434 |
| Literature-expansion annotations in this batch | 7 |
| Cumulative literature-expansion annotations | 387 |
| Unique covered queue candidates | 372 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 54 |
| Cumulative L→R→output-only annotations | 211 |
| Unused downstream queue candidates remaining | 2,959 |
| Unused P1 queue candidates remaining | 1,893 |

The graph topology and causal edge counts are unchanged from v1.8.63. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented include galectin-3/TLR4 neuroinflammatory
evidence (PMIDs 25753426 and 28128358), galectin-3/CD146 binding and function
(PMID 28364041; PMCID PMC5437243; PMID 29741757), galectin-3/VEGFR2
retention and angiogenesis (PMID 21715322; PMCID PMC3191032), galectin-3
integrin glycan-clustering studies (PMID 20713592; PMCID PMC2931172; PMID
19755493; PMCID PMC2758802), galectin-3/MerTK phagocytosis (PMID 31781126;
PMCID PMC6861381), and WNT5A/ROR2/FZD7 receptor-complex signaling (PMID 20457807; PMCID
PMC6509336).
