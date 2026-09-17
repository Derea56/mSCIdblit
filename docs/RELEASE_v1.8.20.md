# mSCIdblit Module 20B–24B mechanism graph v1.8.20

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-015`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion015/`

This fifteenth selective literature-expansion release adds five
source-linked ligand–receptor-to-TF/output annotations with the intracellular
relay explicitly unresolved:

- IL-4 → IL4RA:IL13RA1 type-II receptor complex → STAT6 → transcriptional output
- IL-4 → IL4RA:IL2RG type-I receptor complex → STAT6 → phosphorylation, DNA-binding and gene-expression output
- IL-10 → IL10RA:IL10RB receptor complex → STAT3-associated DNA-binding and reporter output
- IL-12 → IL12RB1:IL12RB2 receptor complex → STAT4 → phosphorylation output
- Tenascin-C → TLR4 receptor complex → NF-κB → reporter and cytokine output

The two IL-4 entries preserve receptor-complex composition as a biological
distinction rather than collapsing type-I and type-II signaling. The IL-10
entry retains the source record’s STAT1/STAT3 ambiguity while recording STAT3
as the represented TF-associated layer. The tenascin-C entry preserves FBG
domain, endotoxin-control and macrophage context without asserting a complete
TLR4 adaptor cascade. Each route remains an evidence record for mSCS rather
than a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,122 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 75 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 14 |
| Cumulative L→R→intracellular→output annotations missing TF | 22 |
| Cumulative L→R→TF→output annotations missing intracellular | 19 |
| Cumulative L→R→output-only annotations | 10 |

The graph topology and causal edge counts are unchanged from v1.8.19. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 18852293 (type-II IL-4
receptor and STAT6); PMID 9492265 (type-I IL-4 receptor and STAT6); PMID 8662928
(IL-10 receptor and STAT1/STAT3); PMID 8943050, PMID 9498755 and PMID 7638186
(IL-12 receptor and STAT4); and PMID 29150600 with PMCID PMC5693923
(tenascin-C FBG–TLR4–NF-κB/cytokine output).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
