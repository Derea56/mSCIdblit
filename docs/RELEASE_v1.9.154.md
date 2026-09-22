# mSCIdblit release v1.9.154

Release date: 2026-09-21

Graph identifier: `module20_24_mechanism_graph:2026-09-21-literature-expansion-267`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion267/`

## EGFR and matrix-receptor route curation overlay

This release adds five primary-literature L→R→output annotations for mSCS
plausibility analysis: EpEX–EGFR, decorin–EGFR, EFEMP1–EGFR, L1CAM–EGFR,
and COMP–CD47. The intracellular and TF layers remain unresolved for these
routes. No graph edges, causal claims, or confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,274 |
| New literature-expansion rows | 5 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Intracellular/TF gap pairs prioritized for follow-up | 5,950 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,649 |
| L→R→TF→output | 338 |
| L→R→intracellular→output | 2,376 |
| L→R→intracellular→TF→output | 128 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMIDs
9988678, 12105206, 19804359, 20033473, 22815787, 29981429, 30261040 and
32978170.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion267
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release.
