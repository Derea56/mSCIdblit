# mSCIdblit release v1.9.335

Release ID: `module20_24_mechanism_graph:2026-09-25-grem1-bmp4-id2-route-queue-561`

This release adds one primary-literature GREM1 route through the BMP4/BMPR
signaling layer, SMAD1/5/8, and ID2 expression. The route records GREM1's
inhibitory BMP-antagonist behavior: primary human fetal-ovarian somatic-cell
experiments show that GREM1 suppresses BMP4-mediated SMAD1/5/8
phosphorylation and abolishes the BMP4-induced ID2 response.

The route is an evidence-layer composition. The receptor-to-relay,
relay-to-TF, and TF-to-target handoffs remain explicit missing links, and no
graph edge, causal assertion, or database confidence score was created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,254 -> 593,255
- Literature-expansion rows: 27,140 -> 27,141
- Full-sequence curation candidates: 15,125 -> 15,126
- Unique ligands in the curation queue: 1,862 (unchanged)
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 154 -> 155
- Full functional-output ligands: 110 (unchanged)
- Partial downstream ligands: 1,541 -> 1,540

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Primary source: [PMID 27385727](https://pubmed.ncbi.nlm.nih.gov/27385727/).

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion561/`
- `scripts/build_primary_grem1_id2_route.py`
- `docs/RELEASE_v1.9.335.md`
