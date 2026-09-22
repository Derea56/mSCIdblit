# mSCIdblit release v1.9.158

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-271`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion271/`

## Cytokine, matrix, and growth-factor TF/output curation overlay

This release adds six primary-literature route annotations for mSCS
plausibility analysis: IL-21–IL21R/IL2RG–STAT3, IL-4–IL4Rα/IL13Rα1–STAT6,
tenascin-C–TLR4–NF-κB, Nodal–Cripto/ACVR1B/ACVR2B–SMAD2/3,
IL-2–IL2Rβ/IL2RG–STAT5, and PDGF-BB–PDGFRB–STAT3. These routes retain
transcription-factor and functional or reporter outputs while leaving the
intervening intracellular relay and terminal target-gene layer unresolved.
No graph edges, causal claims, or confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,297 |
| New literature-expansion rows | 6 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,659 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,383 |
| L→R→intracellular→TF→output | 128 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
11418623, PMID 18852293, PMID 29150600, PMID 18089557, PMID 7777534, and
PMID 8657151.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion271
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release.
