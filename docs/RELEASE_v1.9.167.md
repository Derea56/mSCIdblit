# mSCIdblit release v1.9.167

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-280`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion280/`

## Chemokine and guidance-receptor output curation overlay

This release adds ten primary-literature direct L→R→output annotations for
CXCL9, CXCL10, and CXCL11 through CXCR3; CCL20 through CCR6; CCL24 through
CCR3; CCL1 through CCR8; SLIT2 through ROBO2; and CXCL2, CXCL3, and CXCL5
through CXCR2. The records preserve receptor activation, G-protein,
chemotaxis, adhesion, guidance, or inflammatory outputs while leaving
intracellular, TF, and target-gene layers unresolved. No graph edges, causal
claims, or confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,381 |
| New literature-expansion rows | 10 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,702 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,421 |
| L→R→intracellular→TF→output | 131 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
10102268, PMID 11259614, PMID 11884450, PMID 15150261, PMID 15483227, PMID
15937099, PMID 19234125, PMID 20363748, PMID 23532518, PMID 23878309, PMID
27882344, PMID 32541785, PMID 33688078, PMID 38040762, PMID 38625857, and
PMID 40955564.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion280
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory. The
core graph tables are byte-for-byte unchanged from v1.9.166.
