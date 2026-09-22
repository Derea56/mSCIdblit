# mSCIdblit release v1.9.174

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-287`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion287/`

## Contextual and pathway-scoped output evidence curation

This release adds the remaining 69 queue records with controlled output
classes, including contextual-support and pathway-membership evidence. They
remain topology-unlinked (`????>????>????>????>output`) because the queue does
not support assigning a direct ligand-receptor route. This preserves the
observed outputs without promoting contextual evidence to a direct L→R claim.
No graph edges, causal claims, confidence scores, intracellular links, or TF
links are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 18,672 |
| New literature-expansion rows | 69 |
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

The 69 new records are intentionally excluded from those L→R category counts.
They retain source locators, queue evidence summaries, and
`causal_status=not_asserted` with
`traversal_status=evidence_route_not_causal`. Selection is reproducible with
`scripts/generate_unlinked_output_evidence_batch.py`.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion287
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory. The
graph core remains unchanged from v1.9.173.
