# mSCIdblit Module 20B–24B mechanism graph v1.8.16

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-011`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion011/`

This eleventh selective literature-expansion release adds five source-linked
JAK/STAT5 and receptor-proximal route annotations:

- IL-2 → IL2RB/IL2RG → JAK1/JAK3 → STAT5 → phosphorylation, DNA-binding and reporter output, with the terminal gene unresolved
- TPO → MPL → JAK2 → STAT5 → phosphorylation, DNA-binding and hematopoietic output, with the terminal gene unresolved
- GH → GHR → JAK2 → STAT5 → phosphorylation and DNA-binding output, with the terminal gene unresolved
- Prolactin → PRLR → JAK2 → STAT5 → phosphorylation, DNA binding and beta-casein reporter output, with the terminal gene unresolved
- FGF1 → FGFR3 → SH2-Bβ → STAT5 → phosphorylation and nuclear-translocation output, with the terminal gene unresolved

The annotations preserve receptor aliases, receptor-proximal kinase or
phosphosite context, assay model, perturbation context, and species or tissue
limits. The FGF1–FGFR3 route explicitly treats the ligand-receptor register
edge and activated-FGFR3 phosphosite study as complementary evidence rather
than claiming that FGF1 caused every mutant readout. Unresolved layers are not
interpreted as biological absence. Each route remains an evidence record for
mSCS rather than a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,102 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 55 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 14 |
| Cumulative L→R→intracellular→output annotations missing TF | 13 |
| Cumulative L→R→TF→output annotations missing intracellular | 13 |
| Cumulative L→R→output-only annotations | 4 |

The graph topology and causal edge counts are unchanged from v1.8.15. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 7777534 and PMID 9382798
(IL-2/JAK/STAT5); PMID 7796811 (TPO/MPL); PMID 9231797 (GH/GHR); PMID 7925280
(prolactin/PRLR); and PMID 11827956 with DOI 10.1074/jbc.M102777200
(FGFR3/SH2-Bβ/STAT5).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
