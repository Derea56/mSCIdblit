# mSCIdblit release v1.9.337

Release ID: `module20_24_mechanism_graph:2026-09-25-bmp-antagonist-id-queue-565`

This release adds six primary-literature evidence routes for two soluble BMP
antagonists. NOG is connected to BMP4/BMPR signaling, SMAD1/5/8, and Id1/Id2/Id3
expression using a primary mouse loss-of-function study. CHRDL1 is connected to
BMP7/BMPR signaling, SMAD1/5/8, and Id1/Id2/Id3 expression using a primary renal
signaling study; its TWSG1-dependent context is retained explicitly.

These are evidence-layer compositions. Receptor-to-relay, relay-to-TF, and
TF-to-target handoffs remain explicit missing links. No graph edge, causal
assertion, or database confidence score was created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,256 -> 593,262
- Literature-expansion rows: 27,142 -> 27,148
- Full-sequence curation candidates: 15,127 -> 15,129
- Unique ligands in the curation queue: 1,862 -> 1,863
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 156 -> 158
- Full functional-output ligands: 110 (unchanged)
- Partial downstream ligands: 1,539 -> 1,538
- Ligand-receptor-only ligands: 808 -> 807

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Primary sources: [PMID 27573479](https://pubmed.ncbi.nlm.nih.gov/27573479/) and
[PMID 19357253](https://pubmed.ncbi.nlm.nih.gov/19357253/).

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion565/`
- `scripts/build_primary_bmp_antagonist_id_routes.py`
- `docs/RELEASE_v1.9.337.md`
