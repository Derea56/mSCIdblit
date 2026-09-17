# mSCIdblit Module 20B–24B mechanism graph v1.8.11

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-006`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion006/`

This sixth selective literature-expansion release adds five source-linked
route annotations for mSCS plausibility analysis:

- SAA1 → TLR2 → NF-κB/MAPK and inflammatory gene-expression output, with the intracellular layer unresolved
- Biglycan → TLR2 → MyD88/p38/ERK → NF-κB → TNF-α/MIP-2 inflammatory output, with the target gene unresolved
- extracellular NAMPT → TLR4 → NF-κB and inflammatory cytokine/lung-injury output, with the intracellular layer unresolved
- soluble GPNMB extracellular domain → CD44 → NF-κB suppression and inflammatory cytokine output, with the intracellular layer unresolved
- ANGPTL2 → MCAM/CD146 → CREB phosphorylation and adipocyte metabolic/adipogenesis output, with the intracellular layer unresolved

The annotations preserve activation versus inhibition, receptor or co-receptor
context, assay model, preparation caveats, and species or cell-state limits.
An unresolved intracellular or target-gene layer is not interpreted as
biological absence. Each route remains an evidence record for mSCS rather than
a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,077 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 30 |
| Cumulative full literature-supported route annotations | 8 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 5 |
| Cumulative L→R→intracellular→output annotations missing TF | 8 |
| Cumulative L→R→TF→output annotations missing intracellular | 6 |
| Cumulative L→R→output-only annotations | 3 |

The graph topology and causal edge counts are unchanged from v1.8.10. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 11160347 and PMID
26290589 (SAA1/TLR2); PMID 16025156 and PMID 29777767
(biglycan/TLR2/TLR4/MyD88 and CD14 context); PMID 26272519
(extracellular NAMPT/TLR4); PMID 34582891 (soluble GPNMB/CD44); and PMID
33747748 (ANGPTL2/MCAM-CD146/CREB).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
