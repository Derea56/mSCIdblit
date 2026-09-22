# mSCIdblit release v1.9.151

Release date: 2026-09-21

Graph identifier: `module20_24_mechanism_graph:2026-09-21-literature-expansion-264`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion264/`

## Curated literature-expansion overlay

This release adds seven primary-literature route annotations for mSCS
plausibility analysis. Five records connect TGFA–EGFR evidence to cellular or
SCI-relevant outputs while leaving intracellular and TF layers unresolved. Two
records capture primary EROS/CYBC1–P2X7 and HSP90–P2X7 receptor-proximal
support; they are explicitly not treated as extracellular ligand inputs. The
overlay does not create graph edges, causal claims, or confidence scores.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,257 |
| New literature-expansion rows | 7 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Intracellular/TF gap pairs prioritized for follow-up | 5,950 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,643 |
| L→R→TF→output | 336 |
| L→R→intracellular→output | 2,376 |
| L→R→intracellular→TF→output | 120 |
| L→R entry only | 9,306 |

All seven new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include
PMIDs 12869560, 17234735, 18647603, 19965678, 22016551, 24159173, 27301716,
2755700, 31862710 and 36421765.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion264
```

The bundle passes validation with zero errors and was imported successfully
through mSCS's `import_mechanism_bundle.py` into a temporary active release.
