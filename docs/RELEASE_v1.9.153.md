# mSCIdblit release v1.9.153

Release date: 2026-09-21

Graph identifier: `module20_24_mechanism_graph:2026-09-21-literature-expansion-266`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion266/`

## Receptor-family route curation overlay

This release adds six primary-literature route annotations for mSCS
plausibility analysis. EPO contributes three JAK2–STAT5 target-gene routes
(BCL2L1, CISH, and PIM1). ANGPTL2 and tenascin-R retain receptor-to-NF-κB
annotations with unresolved intracellular and terminal-output layers. GAS6
retains a directly measured MERTK phosphorylation/MAPK output. No graph edges,
causal claims, or confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,269 |
| New literature-expansion rows | 6 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Intracellular/TF gap pairs prioritized for follow-up | 5,950 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,644 |
| L→R→TF→output | 338 |
| L→R→intracellular→output | 2,376 |
| L→R→intracellular→TF→output | 128 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMIDs
9160883, 9657743, 19723494, 28732065, and 31581797, plus the tenascin-R
primary report PMID 29150600/PMCID PMC5693923.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion266
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release.
