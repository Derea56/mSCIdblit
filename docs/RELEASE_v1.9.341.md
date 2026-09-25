# mSCIdblit release v1.9.341

Release ID: `module20_24_mechanism_graph:2026-09-25-fam3c-stat3-socs3-queue-573`

This release adds one composite primary-literature route for FAM3C/ILEI.
Primary mammary epithelial and breast-cancer studies support FAM3C/ILEI
interaction with LIFR and LIFR-dependent STAT3 phosphorylation. The route
composes that observation with the exported JAK1 relay and STAT3 -> SOCS3
target-gene relation, while preserving the missing handoffs and the bounded
mammary/tumor context.

This is an evidence-layer composition. No graph edge, causal assertion, or
database confidence score was created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,267 -> 593,268
- Literature-expansion rows: 27,153 -> 27,154
- Full-sequence curation candidates: 15,134 -> 15,135
- Unique ligands in the curation queue: 1,863 (unchanged)
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 162 -> 163
- Full functional-output ligands: 110 (unchanged)
- Partial downstream ligands: 1,534 -> 1,533

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Primary sources: [PMID 30692635](https://pubmed.ncbi.nlm.nih.gov/30692635/)
and [PMID 37927213](https://pubmed.ncbi.nlm.nih.gov/37927213/).

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion573/`
- `scripts/build_primary_fam3c_stat3_socs3_route.py`
- `docs/RELEASE_v1.9.341.md`
