# mSCIdblit Module 20B–24B mechanism graph v1.8.10

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-005`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion005/`

This fifth selective literature-expansion release adds five source-linked
route annotations for mSCS plausibility analysis:

- IL-12 → IL-12Rβ1/β2 → JAK2/TYK2 → STAT4 → IFNG expression
- IL-15 → IL-2Rβ/γc → JAK1/JAK3 → STAT5 → lymphocyte output
- IL-4 → type-II IL-4Rα/IL-13Rα1 → STAT6/output, with the intracellular layer unresolved
- myostatin → ACVR2B:ALK4 → SMAD2/3 → reporter/adipogenesis output
- maresin-1 → LGR6 → ERK1/2 → CREB → phagocyte-resolution output

The annotations preserve different evidence depths and do not imply that an
unresolved layer is absent biologically. They provide mSCS with explicit
ligand–receptor-to-output evidence, intracellular continuation where supported,
and transcription-factor or target-gene evidence where available.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,072 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 25 |
| Cumulative full literature-supported route annotations | 8 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 4 |
| Cumulative L→R→intracellular→output annotations missing TF | 8 |
| Cumulative L→R→TF→output annotations missing intracellular | 2 |
| Cumulative L→R→output-only annotations | 3 |

The graph topology and causal edge counts are unchanged from v1.8.9. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 12893768, PMID 9558063,
and PMID 11120802 (IL-12/STAT4/IFNG); PMID 18458113, PMID 18523252, and PMID
19553528 (IL-15 trans-presentation and lymphocyte output); PMID 18852293
(type-I/type-II IL-4 receptor and STAT6 response); PMID 14517293
(myostatin/ActRIIB/ALK4/SMAD2/3); and PMID 31657786 (maresin-1/LGR6/ERK/CREB
and phagocyte output).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
