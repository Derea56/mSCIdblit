# mSCIdblit Module 20B–24B mechanism graph v1.8.8

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-003`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion003/`

This third selective literature-expansion release adds five source-linked
partial route annotations for mSCS plausibility analysis. Each route has
ligand, receptor, intracellular-continuation, and output support, while the
terminal transcription-factor and target-gene layers remain unresolved:

- ATP → P2X7 → caspase-1 → mature IL-1β processing/release
- CCL2 → CCR2 → Gαi2 → monocyte/macrophage chemotaxis
- osteopontin/SPP1 → αVβ3 integrin → Src-associated relay → migration
- TNF → TNFR2 → TRAF2/alternative NF-κB relay → activation output
- RANKL/TNFSF11 → RANK → TRAF6 relay → osteoclastogenic output

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,062 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 15 |
| Cumulative full literature-supported route annotations | 7 |
| Cumulative L→R→intracellular→output annotations missing TF | 7 |
| Cumulative L→R→output-only annotations | 1 |

The graph topology and causal edge counts are unchanged from v1.8.7. The
overlay is evidence-layer data: it preserves primary locators, assay context,
effect direction, and limitations, but it does not create causal graph edges,
database confidence scores, or SCI-transfer claims. mSCS receives these route
annotations and remains responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 10779799 (ATP/P2X7,
caspase-1 and IL-1β release), PMID 22706085 (CCL2/Gαi2 chemotaxis), PMID
28397850 (osteopontin/αV-integrin/Src migration), PMID 20038584
(membrane-TNF/TNFR2 alternative NF-κB), and PMID 15678102
(RANKL/RANK/TRAF6 osteoclastogenesis).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
