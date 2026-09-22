# mSCIdblit release v1.9.175

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-288`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion288/`

## Remaining P1 output evidence curation

This release adds ten manually curated primary-supported downstream output
annotations from the highest-priority unresolved queue records. The evidence
records retain the observed output and its primary locator, but remain
topology-unlinked (`????>????>????>????>output`) where the source does not
support assigning ligand, receptor, intracellular, or transcription-factor
roles. No graph edges, causal claims, confidence scores, intracellular links,
or TF links are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 18,682 |
| New literature-expansion rows | 10 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories remain unchanged because the ten new records do
not support direct L→R topology assignment:

| Category | Records |
|---|---:|
| L→R→output | 4,394 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,421 |
| L→R→intracellular→TF→output | 131 |
| L→R entry only | 9,307 |

All ten rows retain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. The graph core is unchanged.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion288
```

The bundle passes validation with zero errors and the existing stable-locator
warning. It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory.
