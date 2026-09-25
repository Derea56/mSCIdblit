# mSCIdblit release v1.9.340

Release ID: `module20_24_mechanism_graph:2026-09-25-notch-hes1-queue-571`

This release adds two primary-literature evidence routes through the NOTCH1
relay. CCN3/NOV and SERPINA4/Kallistatin are linked to NOTCH1-associated HES1
observations, and those ligand-specific records are composed with the exported
NOTCH1 -> NICD -> RBPJ/CSL -> HES1 relay. The canonical relay handoffs remain
distinct from the ligand-specific primary claims.

These are evidence-layer compositions. Receptor-to-relay, relay-to-TF, and
TF-to-target handoffs remain explicit missing links. No graph edge, causal
assertion, or database confidence score was created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,265 -> 593,267
- Literature-expansion rows: 27,151 -> 27,153
- Full-sequence curation candidates: 15,132 -> 15,134
- Unique ligands in the curation queue: 1,863 (unchanged)
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 160 -> 162
- Full functional-output ligands: 110 (unchanged)
- Partial downstream ligands: 1,536 -> 1,534

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Primary sources: [CCN3/NOV study](https://pubmed.ncbi.nlm.nih.gov/12050162/)
and [Kallistatin study](https://elifesciences.org/articles/99462).

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion571/`
- `scripts/build_primary_notch_hes1_routes.py`
- `docs/RELEASE_v1.9.340.md`
