# mSCIdblit Module 20B–24B mechanism graph v1.8.12

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-007`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion007/`

This seventh selective literature-expansion release adds five source-linked
route annotations for mSCS plausibility analysis:

- Biglycan → TLR4 → MyD88/p38/ERK → NF-κB → TNF-α/MIP-2 inflammatory output, with the target gene unresolved
- ANGPTL2 → α5β1 integrin → MAPK/Akt/NF-κB → inflammatory cytokine output, with the target gene unresolved
- IL-22 → IL-22Rα1/IL-10R2 → STAT3-associated signaling output, with the intracellular continuation unresolved
- leptin → LEPR → STAT3-associated activation output, with the intracellular continuation unresolved
- FGF21 → β-Klotho/FGFR1c → ERK/MAPK and adipocyte metabolic output, with the intracellular and TF layers unresolved

The annotations preserve receptor or co-receptor context, receptor-complex
assembly, assay model, preparation caveats, and species or cell-state limits.
Unresolved layers are not interpreted as biological absence. Each route remains
an evidence record for mSCS rather than a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,082 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 35 |
| Cumulative full literature-supported route annotations | 8 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 7 |
| Cumulative L→R→intracellular→output annotations missing TF | 9 |
| Cumulative L→R→TF→output annotations missing intracellular | 8 |
| Cumulative L→R→output-only annotations | 3 |

The graph topology and causal edge counts are unchanged from v1.8.11. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 16025156 (biglycan/TLR4);
PMID 19723494, PMID 31581797, PMID 27402837, and PMID 28934245
(ANGPTL2/α5β1); PMID 12513909, PMID 12087100, PMID 15327950, and PMID
18599299 (IL-22 receptor); PMID 37002197 (leptin/LEPR); and PMID 29342135,
PMID 22523080, and PMID 18187602 (FGF21/β-Klotho/FGFR1c).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
