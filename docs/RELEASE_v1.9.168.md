# mSCIdblit release v1.9.168

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-281`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion281/`

## Chemokine, scavenging, guidance, and leukocyte-receptor output curation overlay

This release adds ten primary-literature direct L→R→output annotations for
CXCL6 through CXCR1 and CXCR2; CXCL7 through CXCR2; CXCL16 through CXCR6;
CX3CL1 through CX3CR1; XCL1 through XCR1; CCL19 and CCL21 through CCR7;
CXCL11 through ACKR3/CXCR7; and netrin-1 through UNC5C. The records preserve
measured calcium, migration, adhesion, G-protein, beta-arrestin, scavenging,
processing, phosphorylation, and guidance outputs while leaving intracellular,
TF, and target-gene layers unresolved. No graph edges, causal claims, or
confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,391 |
| New literature-expansion rows | 10 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,712 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,421 |
| L→R→intracellular→TF→output | 131 |
| L→R entry only | 9,307 |

All new rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Primary locators include PMID
9692902, PMID 10382755, PMID 11290797, PMID 15574733, PMID 17197447, PMID
17363734, PMID 19913446, PMID 25614627, PMID 28018341, PMID 28245630, and
PMCID PMC5217689, PMCID PMC6730211.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion281
```

The bundle passes validation with zero errors and one stable-locator warning.
It was also imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory. The
core graph tables are byte-for-byte unchanged from v1.9.167.
