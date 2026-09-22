# mSCIdblit release v1.9.152

Release date: 2026-09-21

Graph identifier: `module20_24_mechanism_graph:2026-09-21-literature-expansion-265`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion265/`

## Cytokine route curation overlay

This release adds six primary-literature route annotations for mSCS
plausibility analysis: IL-23 to STAT3/IL17A, IL-15 to STAT5/BCL2 or BCL2L1,
IL-6 to STAT3/SOCS3 or MYC, and CNTF to receptor-associated STAT3 activation.
The JAK-to-STAT links that are not represented as exact graph edges remain
explicitly unresolved. No graph edges, causal claims, or confidence scores are
created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,263 |
| New literature-expansion rows | 6 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Intracellular/TF gap pairs prioritized for follow-up | 5,950 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,643 |
| L→R→TF→output | 336 |
| L→R→intracellular→output | 2,376 |
| L→R→intracellular→TF→output | 125 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include
PMIDs 7568001, 8390097, 8612579, 9794795, 9874564, 12023369, 20440074,
20584990 and 23673666.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion265
```

The bundle passes validation with zero errors and was imported successfully
through mSCS's `import_mechanism_bundle.py` into a temporary active release.
