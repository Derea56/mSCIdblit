# mSCIdblit release v1.9.155

Release date: 2026-09-21

Graph identifier: `module20_24_mechanism_graph:2026-09-21-literature-expansion-268`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion268/`

## CD36 and TAM-receptor route curation overlay

This release adds five primary-literature L→R→output annotations for mSCS
plausibility analysis: PROS1–MERTK efferocytosis, TSP1–CD36 antiangiogenic
output, Aβ–CD36 microglial migration, SAA1–CD36 inflammatory signaling, and
S100A12–CD36 receptor-translocation/regulatory output. Intracellular and TF
layers remain unresolved. No graph edges, causal claims, or confidence scores
are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,279 |
| New literature-expansion rows | 5 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Intracellular/TF gap pairs prioritized for follow-up | 5,950 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,654 |
| L→R→TF→output | 338 |
| L→R→intracellular→output | 2,376 |
| L→R→intracellular→TF→output | 128 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
18250462, PMID 23640500, PMID 17623670, PMCID PMC2832998, and PMID 27734162.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion268
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release.
