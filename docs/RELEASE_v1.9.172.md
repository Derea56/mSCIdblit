# mSCIdblit release v1.9.172

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-285`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion285/`

## Final direct-output selector correction

This release adds 49 additional validated direct L→R→output records after
correcting the reproducible selector to aggregate all prior release overlays
and to use boundary-aware receptor-source detection. This prevents duplicate
queue curation and avoids mistaking ligand names such as ephrin and CD40LG for
receptor sources. The records remain evidence-only and do not assert
intracellular continuation, TF or target-gene links, graph edges, causality, or
database confidence scores.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 18,073 |
| New literature-expansion rows | 49 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 4,394 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,421 |
| L→R→intracellular→TF→output | 131 |
| L→R entry only | 9,307 |

All new rows retain source locators and queue evidence summaries, with
`causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Selection is reproducible with
`scripts/generate_literature_expansion_batch_from_queue.py`; the selector
aggregates all prior release overlays before generating a new batch.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion285
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory. The
graph core remains unchanged from v1.9.171.
