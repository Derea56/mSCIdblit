# mSCIdblit release v1.9.163

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-276`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion276/`

## Receptor-proximal and direct expression curation overlay

This release adds ten primary-literature route annotations for mSCS
plausibility analysis. Nine records preserve receptor-proximal signaling
branches involving EGFR, FGFR1, CSF1R, PDGFRB, and FGFR3. The CSF1R and FGFR3
branches also retain explicit STAT5 observations without asserting a TF-target
edge. One direct DLL4–NOTCH4 record preserves HES1/HERP/ephrin-B2 expression
as an L→R→output observation while leaving the intracellular relay and TF
identity unresolved. No graph edges, causal claims, or confidence scores are
created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,341 |
| New literature-expansion rows | 10 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,669 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,414 |
| L→R→intracellular→TF→output | 131 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
10391677, PMID 11827956, PMID 12814948, PMID 14560030, PMID 15297464, PMID
15784730, PMID 1656221, PMID 34144039, PMID 7691811, and PMID 7935391.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion276
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory. The
core graph tables are byte-for-byte unchanged from v1.9.162.
