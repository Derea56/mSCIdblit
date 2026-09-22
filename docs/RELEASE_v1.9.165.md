# mSCIdblit release v1.9.165

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-278`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion278/`

## Early queue direct-output and PDGFRB curation overlay

This release adds ten primary-literature route annotations from the earliest
unexpanded portion of the downstream queue. Two records preserve PDGFRB
Y1009-SHP2 and Y1021-PLCG1 receptor-proximal branches. Eight records preserve
direct L→R→output observations for HMGB1–MD-2/TLR4, hemopexin-heme–LRP1,
DLL1–NOTCH2, CXCL12–CXCR4, CXCL13–CXCR5, mature HGF–MET, CX3CL1–CX3CR1,
and ATP–P2X7. Unresolved intracellular, TF, and target-gene layers remain
explicit. No graph edges, causal claims, or confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,361 |
| New literature-expansion rows | 10 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,682 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,421 |
| L→R→intracellular→TF→output | 131 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
10958687, PMID 11688722, PMID 11943809, PMID 15218027, PMID 15947085, PMID
20547845, PMID 25395671, PMID 28325822, PMID 7678051, and PMID 7691811.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion278
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory. The
core graph tables are byte-for-byte unchanged from v1.9.164.
