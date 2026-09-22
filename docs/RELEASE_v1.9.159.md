# mSCIdblit release v1.9.159

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-272`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion272/`

## Receptor-proximal intracellular route curation overlay

This release adds seven primary-literature route annotations for mSCS
plausibility analysis: CSF1–CSF1R–PI3K functional output, two VEGFA–VEGFR2
receptor-site branches through PLCγ1 and NCK, IL-9–IL9RA/IL2RG–STAT output,
WNT5A–ROR2/FZD7–DVL2 output, and separate CD200R1–DOK1 and CD200R1–DOK2
inhibitory branches. These routes preserve receptor-proximal intracellular
evidence and functional or reporter outputs while leaving terminal TF and
target-gene layers unresolved. No graph edges, causal claims, or confidence
scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,304 |
| New literature-expansion rows | 7 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,659 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,390 |
| L→R→intracellular→TF→output | 128 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
11387210, PMID 15557172, PMID 16966330, PMID 20457807, PMID 9535918, and
PMCID PMC86204 with its cited primary studies.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion272
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release.
