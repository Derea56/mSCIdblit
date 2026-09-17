# mSCIdblit Module 20B–24B mechanism graph v1.8.7

Release date: 2026-09-16
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-002`
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion002/`

This second selective literature-expansion release adds five source-linked
route annotations for mSCS plausibility analysis. Three annotations support a
bounded ligand-to-receptor-to-intracellular-to-transcription-factor-to-output
route for GM-CSF/STAT5/CISH, DLL1/NOTCH1/RBPJ/HES1, or HMGB1/TLR4/NF-kB/IL6.
Two annotations add intracellular evidence to CXCL12/CXCR4 and HGF/MET
functional routes while leaving terminal TF and target-gene layers unresolved.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,057 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 10 |
| Cumulative full literature-supported route annotations | 7 |
| Cumulative L→R→intracellular→output annotations missing TF | 2 |
| Cumulative L→R→output-only annotations | 1 |

The graph topology and causal edge counts are unchanged from v1.8.6. The
overlay is evidence-layer data: it preserves primary locators, assay context,
effect direction, and limitations, but it does not create causal graph edges,
database confidence scores, or SCI-transfer claims. mSCS receives the route
annotations and remains responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 9292509 (GM-CSF/STAT5
gene expression), PMID 9819428 (Delta-1/NOTCH1/HES1), PMID 30273982
(HMGB1/TLR4/NF-kB/IL6), PMID 25466898 (CXCL12/CXCR4/Gi/mTORC1 migration),
PMID 10871282 (HGF/MET/GAB1 coupling), and PMID 15385963 (HGF/c-Met/ERK
signaling and migration).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
