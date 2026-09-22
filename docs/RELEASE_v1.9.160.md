# mSCIdblit release v1.9.160

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-273`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion273/`

## Axon-guidance, erythropoietin, and BDNF receptor-proximal curation overlay

This release adds eight primary-literature route annotations for mSCS
plausibility analysis: Netrin-1–UNC5B–PIKE-L/PI3K, Slit2–ROBO1–SRGAP1/Cdc42,
SEMA3A–NRP1/PLXNA2–FYN/CDK5, ephrin-A1–EPHA4–Ephexin1/RhoA,
EPO–EPOR–PIK3R1/p85, and three BDNF–TrkB receptor-site branches through
SHC1, PLCG1, and FRS2A. The PLCG1 branch also retains co-observed CREB
evidence while leaving terminal target-gene linkage unresolved. No graph edges,
causal claims, or confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,312 |
| New literature-expansion rows | 8 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,659 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,397 |
| L→R→intracellular→TF→output | 129 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
10196222, PMID 11672528, PMID 12367511, PMID 12372285, PMID 15372074, PMID
15848799, PMID 18469807, and PMID 9096338.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion273
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release.
