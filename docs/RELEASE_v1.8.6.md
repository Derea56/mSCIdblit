# mSCIdblit Module 20B–24B mechanism graph v1.8.6

Release date: 2026-09-16
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-001`
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion001/`

This selective literature-expansion release adds five source-linked route
annotations for mSCS plausibility analysis. Four annotations retain a bounded
IL-4, IL-10, IL-21, or TSLP route through an intracellular/JAK layer, a
transcription factor, and a gene-expression output. One annotation retains the
TWEAK–Fn14 retinogeniculate functional output as L→R→output evidence while
leaving the intracellular and TF layers unknown.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,052 |
| Literature-expansion annotations | 5 |
| Full literature-supported route annotations | 4 |
| L→R→output-only literature annotations | 1 |

The graph topology and causal edge counts are unchanged from v1.8.5. The
overlay is evidence-layer data: it preserves primary locators, assay context,
effect direction, and limitations, but it does not create causal graph edges,
database confidence scores, or SCI-transfer claims. mSCS receives the route
annotations and remains responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 18852293 (IL-4/STAT6/Arg1),
PMID 22851691 (IL-10/STAT3/LCN2), PMID 17884812 (IL-21/STAT3/IL-17), PMID
10570284 (TSLP/STAT5/CIS), and PMID 32931754 (microglial TWEAK/Fn14 spine
remodeling).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
