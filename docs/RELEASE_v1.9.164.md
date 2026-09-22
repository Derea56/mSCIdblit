# mSCIdblit release v1.9.164

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-277`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion277/`

## Notch, TREM2, and inhibitory adaptor curation overlay

This release adds ten primary-literature route annotations for mSCS
plausibility analysis. Five records preserve direct L→R→output evidence for
JAG1/JAG2–NOTCH2 processing and reporter activity and for phosphatidylserine,
C1q, and S1P interactions with TREM2. Five records preserve receptor-proximal
SHIP1, DOK3, SHP1, and SHP2 branches connected to TREM2-DAP12, C1q-CD33, or
CD47-SIRPA evidence. These records leave unresolved layers explicit and do not
create graph edges, causal claims, or confidence scores.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,351 |
| New literature-expansion rows | 10 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,674 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,419 |
| L→R→intracellular→TF→output | 131 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
10958687, PMID 16055727, PMID 20484116, PMID 31101881, PMID 35847502, PMID
37442133, PMCID PMC1190262, and PMCID PMC3923308.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion277
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory. The
core graph tables are byte-for-byte unchanged from v1.9.163.
