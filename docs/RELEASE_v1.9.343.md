# mSCIdblit release v1.9.343

Release ID: `module20_24_mechanism_graph:2026-09-25-cross-record-route-promotions-580`

This release adds 565 evidence-route records across 112 ligands by promoting
exact ligand-receptor-endpoint signatures that were already supported by
curated full routes elsewhere in the evidence corpus. The additions comprise
419 target-gene route records and 146 functional-output route records. They
retain the source partial-route evidence and explicitly leave the intermediate
handoffs unasserted; they are intended for mSCS plausibility evaluation and
future primary-literature review.

This is an evidence-layer composition. No graph edge, causal assertion,
confidence score, or missing-link assertion was created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 594,049 -> 594,614
- Literature-expansion rows: 27,935 -> 28,500
- Full-sequence curation candidates: 15,139 (unchanged after signature deduplication)
- Unique ligands in the curation queue: 1,863 (unchanged)
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 163 (unchanged)
- Full functional-output ligands: 110 (unchanged)
- Partial downstream ligands: 1,533 (unchanged)

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion580/`
- `scripts/build_cross_record_route_promotions.py`
- `docs/RELEASE_v1.9.343.md`
