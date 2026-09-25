# mSCIdblit release v1.9.339

Release ID: `module20_24_mechanism_graph:2026-09-25-sost-bmp6-id1-queue-569`

This release adds one composite primary-literature evidence route for
SOST/Sclerostin. One primary study reports that sclerostin inhibits BMP6-induced
SMAD phosphorylation, while a separate primary study reports BMP6-induced
SMAD1/5/8 phosphorylation followed by Id1 expression. The route preserves the
source overlap and distinct cell-system contexts rather than presenting the
composition as a single end-to-end experiment.

This is an evidence-layer composition. Receptor-to-relay, relay-to-TF, and
TF-to-target handoffs remain explicit missing links. No graph edge, causal
assertion, or database confidence score was created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,264 -> 593,265
- Literature-expansion rows: 27,150 -> 27,151
- Full-sequence curation candidates: 15,131 -> 15,132
- Unique ligands in the curation queue: 1,863 (unchanged)
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 159 -> 160
- Full functional-output ligands: 110 (unchanged)
- Partial downstream ligands: 1,537 -> 1,536

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Primary sources: [PMID 14633986](https://pubmed.ncbi.nlm.nih.gov/14633986/) and
[PMID 15877825](https://pubmed.ncbi.nlm.nih.gov/15877825/).

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion569/`
- `scripts/build_primary_sost_bmp6_id1_route.py`
- `docs/RELEASE_v1.9.339.md`
