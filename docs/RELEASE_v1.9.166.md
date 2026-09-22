# mSCIdblit release v1.9.166

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-279`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion279/`

## Early chemokine, integrin, and receptor-output curation overlay

This release adds ten primary-literature direct L→R→output annotations from
the next sequential queue block. The routes cover ATP/ADP-P2Y microglial
chemotaxis, SPP1-alphaVbeta3 adhesion, fibrinogen-Mac-1 adhesion, VEGF165-
NRP1/KDR endothelial function, latent TGF-beta1-alphaVbeta6 activation,
VCAM1-alpha4beta1 adhesion, CCL2-CCR2, CCL17-CCR4, CCL22-CCR4, and CCL25-
CCR9. Intracellular, TF, and target-gene layers remain explicitly unresolved;
no graph edges, causal claims, or confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,371 |
| New literature-expansion rows | 10 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,692 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,421 |
| L→R→intracellular→TF→output | 131 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
10025398, PMID 11245682, PMID 11884450, PMID 12390020, PMID 15325806, PMID
15920019, PMID 16614259, PMID 20427772, PMID 22863617, PMID 24534492, PMID
35570218, PMID 7511143, and PMCID PMC2290915.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion279
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory. The
core graph tables are byte-for-byte unchanged from v1.9.165.
