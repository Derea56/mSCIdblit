# mSCIdblit release v1.9.338

Release ID: `module20_24_mechanism_graph:2026-09-25-sostdc1-id2-queue-567`

This release adds two primary-literature evidence routes for
USAG1/SOSTDC1. A primary transgenic-rat study links persistent Sertoli-cell
Sostdc1 expression with increased BMP4/BMP7-associated SMAD1/5/8
phosphorylation and Id2 expression in testis. The BMP4 and BMP7 alternatives
are retained separately, and the context-dependent activating observation is
not generalized to the inhibitory SOSTDC1 behavior reported in other tissues.

These are evidence-layer compositions. Receptor-to-relay, relay-to-TF, and
TF-to-target handoffs remain explicit missing links. No graph edge, causal
assertion, or database confidence score was created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,262 -> 593,264
- Literature-expansion rows: 27,148 -> 27,150
- Full-sequence curation candidates: 15,129 -> 15,131
- Unique ligands in the curation queue: 1,863 (unchanged)
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 158 -> 159
- Full functional-output ligands: 110 (unchanged)
- Partial downstream ligands: 1,538 -> 1,537

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Primary source: [PMID 31391487](https://pubmed.ncbi.nlm.nih.gov/31391487/).

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion567/`
- `scripts/build_primary_sostdc1_id2_route.py`
- `docs/RELEASE_v1.9.338.md`
