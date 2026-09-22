# mSCIdblit release v1.9.156

Release date: 2026-09-21

Graph identifier: `module20_24_mechanism_graph:2026-09-21-literature-expansion-269`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion269/`

## Cytokine, checkpoint, and opsonin route curation overlay

This release adds six primary-literature route annotations for mSCS
plausibility analysis: IL-34–CSF1R, GM-CSF–CSF2R, CD47–SIRPα–SHP-1,
IL-37–IL-18Rα/IL-1R8, and MFG-E8–αVβ3/αVβ5 phagocytosis routes. The CD47
route retains an intracellular SHP-1 continuation; the remaining routes retain
partial functional outputs without inferred TF or terminal target-gene links.
No graph edges, causal claims, or confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,285 |
| New literature-expansion rows | 6 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Intracellular/TF gap pairs prioritized for follow-up | 5,950 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,659 |
| L→R→TF→output | 338 |
| L→R→intracellular→output | 2,377 |
| L→R→intracellular→TF→output | 128 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
22579672, PMID 1460041, PMID 18657508, PMID 25729923, PMID 12000961, and
PMID 10821695.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion269
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release.
