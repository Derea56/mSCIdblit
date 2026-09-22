# mSCIdblit release v1.9.169

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-282`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion282/`

## Notch, integrin, and selectin output curation overlay

This release adds ten primary-literature direct L→R→output annotations for DLL1
through NOTCH1; vitronectin and fibronectin through ITGAV:ITGB3; collagen I
through ITGA1:ITGB1 and ITGA2:ITGB1; laminin-511 through ITGA3:ITGB1;
E-selectin through CD44/HCELL and ESL-1/GLG1; CD43 through E-selectin; and
endoglycan through P-selectin. The records preserve reporter, binding,
adhesion, rolling, migration, glycan-dependent, and co-stimulation outputs
while leaving intracellular, TF, and target-gene layers unresolved. No graph
edges, causal claims, or confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,401 |
| New literature-expansion rows | 10 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,722 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,421 |
| L→R→intracellular→TF→output | 131 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
10617582, PMID 11402070, PMID 16339541, PMID 1703545, PMID 18606703, PMID
19752234, PMID 23839946, PMID 7531823, and PMID 9480902.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion282
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory. The
core graph tables are byte-for-byte unchanged from v1.9.168.
