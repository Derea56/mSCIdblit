# mSCIdblit Module 20B–24B mechanism graph v1.8.13

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-008`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion008/`

This eighth selective literature-expansion release adds five source-linked
route annotations for mSCS plausibility analysis:

- IL-17B → IL-17RB → TRAF6/ACT1/TAK1/ERK1/2 → composite NF-κB/ATF2/AML1/AP-1 program → CCL20 expression
- IL-17C → IL-17RA/IL-17RE → HBD2/DEFB4A protein output, with intracellular and TF layers unresolved
- IL-17A → IL-17RA/IL-17RC → ACT1/CIKS → CCL20 inflammatory output, with the TF unresolved
- NT-3 → TrkC → MEK/ERK → astrocyte NGF mRNA output, with the TF unresolved
- OSM → gp130/OSMRβ → JAK/STAT → STAT3 → SOCS3 expression

The annotations preserve receptor-complex context, assay model, preparation or
cell-state caveats, and species or tissue limits. Unresolved layers are not
interpreted as biological absence. Each route remains an evidence record for
mSCS rather than a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,087 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 40 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 7 |
| Cumulative L→R→intracellular→output annotations missing TF | 11 |
| Cumulative L→R→TF→output annotations missing intracellular | 8 |
| Cumulative L→R→output-only annotations | 4 |

The graph topology and causal edge counts are unchanged from v1.8.12. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 10749887 and PMID 25732306
(IL-17B/IL-17RB); PMID 21993849 and PMID 31793105 (IL-17C/IL-17RE); PMID
17911633, PMID 17035243, PMID 17277779, and PMID 16272323 (IL-17A/IL-17RA);
PMID 1653651, PMID 8344249, PMID 39508056, and PMID 22387236 (NT-3/TrkC);
and PMID 8999038, PMID 18571793, and PMID 16718380 (OSM/JAK-STAT3/SOCS3).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
