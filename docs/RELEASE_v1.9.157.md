# mSCIdblit release v1.9.157

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-270`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion270/`

## Axon-guidance receptor-proximal route curation overlay

This release adds six primary-literature route annotations for mSCS
plausibility analysis: two Netrin-1–DCC routes, Netrin-1–UNC5B, Slit2–Robo1,
SEMA3A–Plexin-A2, and ephrin-A1–EphA4. These rows retain FAK/Src,
RhoGTPase/PAK/WASL, PIKE-L/PI3K, srGAP1/Cdc42, Fyn/Cdk5, and
Ephexin1/RhoA as receptor-proximal intracellular continuations with
functional guidance outputs. No TF, terminal target-gene, causal, or
confidence-score claims are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,291 |
| New literature-expansion rows | 6 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Intracellular/TF gap pairs prioritized for follow-up | 5,950 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,659 |
| L→R→TF→output | 338 |
| L→R→intracellular→output | 2,383 |
| L→R→intracellular→TF→output | 128 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
15494734, PMID 15788770, PMID 18469807, PMID 11672528, PMID 12372285, and
PMID 15848799.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion270
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release.
