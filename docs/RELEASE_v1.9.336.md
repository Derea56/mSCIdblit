# mSCIdblit release v1.9.336

Release ID: `module20_24_mechanism_graph:2026-09-25-twsg1-bmp7-id1-route-queue-563`

This release adds one primary-literature TWSG1 route through the BMP7/BMPR
signaling layer, SMAD1/5/8, and ID1 expression. In primary Ishikawa
endometrial-cancer cells, recombinant TWSG1 suppresses BMP7-induced
SMAD1/5/8 phosphorylation and ID1 mRNA expression. The route therefore
retains inhibitory polarity and does not represent TWSG1 as a productive BMP
receptor agonist.

The record is an evidence-layer composition. Receptor-to-relay,
relay-to-TF, and TF-to-target handoffs remain explicit missing links; no graph
edge, causal assertion, or database confidence score was created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,255 -> 593,256
- Literature-expansion rows: 27,141 -> 27,142
- Full-sequence curation candidates: 15,126 -> 15,127
- Unique ligands in the curation queue: 1,862 (unchanged)
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 155 -> 156
- Full functional-output ligands: 110 (unchanged)
- Partial downstream ligands: 1,540 -> 1,539

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Primary source: [PMID 34360647](https://pubmed.ncbi.nlm.nih.gov/34360647/).

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion563/`
- `scripts/build_primary_twsg1_id1_route.py`
- `docs/RELEASE_v1.9.336.md`
