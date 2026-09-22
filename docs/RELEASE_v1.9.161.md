# mSCIdblit release v1.9.161

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-274`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion274/`

## Direct ligand–receptor functional-output curation overlay

This release adds nine primary-literature L→R→output annotations for mSCS
plausibility analysis: CD47–SIRPA phagocytosis inhibition,
NLGN1–NRXN1B synaptic adhesion, P-selectin–PSGL1 rolling,
CXCL8–CXCR1/2 activation, CCL3–CCR1/CCR5 chemotaxis, CCL5–CCR5 activation,
and CXCL1–CXCR2 recruitment. These routes retain documented outputs while
explicitly leaving intracellular, TF, and target-gene layers unresolved. No
graph edges, causal claims, or confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,321 |
| New literature-expansion rows | 9 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,668 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,397 |
| L→R→intracellular→TF→output | 129 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
9289016, PMID 9829984, PMID 11404385, PMID 15567066, PMID 15831559, PMID
18093521, PMID 18657508, PMID 20630874, PMID 23479735, and PMID 34134983.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion274
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release.
