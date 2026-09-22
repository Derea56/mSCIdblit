# mSCIdblit release v1.9.162

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-275`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion275/`

## Receptor-proximal signaling curation overlay

This release adds ten primary-literature receptor-proximal annotations for
mSCS plausibility analysis. The routes cover EGFR outputs through CBL, SHC1,
and SHP1; EPOR through SHP1; PDGFRB through PLCG1; EPHB1 through NCK1;
EPHB2 through SRC; and EPHA2 through VAV2/VAV3, PIK3R1, and NCK1. These
records preserve the observed intracellular continuation while leaving TF,
target-gene, causal, and confidence fields unresolved. No graph edges, causal
claims, or confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,331 |
| New literature-expansion rows | 10 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,668 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,407 |
| L→R→intracellular→TF→output | 129 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
7689724, PMID 7889566, PMID 9430661, PMID 9544989, PMID 9632142, PMID 9733788,
PMID 11823423, PMID 16782872, PMID 18387945, and PMID 23358419.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion275
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory. The
core graph tables are byte-for-byte unchanged from v1.9.161.
