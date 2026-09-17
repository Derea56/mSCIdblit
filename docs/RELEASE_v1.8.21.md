# mSCIdblit Module 20B–24B mechanism graph v1.8.21

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-016`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion016/`

This sixteenth selective literature-expansion release adds five
source-linked ligand–receptor-to-TF/output annotations with the intracellular
relay and terminal target gene explicitly unresolved:

- IL-9 → IL9RA:IL2RG receptor complex → STAT5 → proliferative/survival output
- BAFF → TACI/TNFRSF13B → NF-κB → activation output
- IL-21 → IL21R:IL2RG receptor complex → STAT3 → lymphoid functional output
- IL-21 → IL21R:IL2RG receptor complex → STAT5 → lymphoid functional output
- IL-11 → IL11Rα:gp130 hexamer → STAT3 → phosphorylation output

The two IL-21 annotations preserve separate STAT3 and STAT5 evidence records
from the same receptor-complex studies; the source also reports STAT1. This
keeps multiple supported transcription-factor-associated responses available
to mSCS without presenting one as exclusive. The BAFF entry retains TACI
isoform and NF-κB reporter context, while the IL-11 entry retains the
2:2:2 ligand–receptor-complex stoichiometry. Each route remains an evidence
record for mSCS rather than a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,127 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 80 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 14 |
| Cumulative L→R→intracellular→output annotations missing TF | 22 |
| Cumulative L→R→TF→output annotations missing intracellular | 24 |
| Cumulative L→R→output-only annotations | 10 |

The graph topology and causal edge counts are unchanged from v1.8.20. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 9535918 and PMID 9261146
(IL-9 receptor/JAK–STAT); PMID 30333819 (BAFF–TACI/NF-κB); PMID 11418623 and
PMID 12093291 (IL-21 receptor/common-gamma-chain signaling); and PMID 10948192
and PMID 11141475 (IL-11 receptor/gp130/STAT3 signaling).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
