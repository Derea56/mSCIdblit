# mSCIdblit release v1.9.248

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-pdgfb-stat3-fos-371`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion371/`

## PDGF-BB STAT3 target route expansion

This release adds six parallel evidence routes for PDGF-BB/PDGFRB:

`PDGF-BB > PDGFRB receptor dimer > {ABL2, GRB2, PLCG1, PLCgamma1, PTPN11/SHP2, SHP2/PTPN11} > STAT3 > FOS gene expression`

The receptor-proximal branches are independently source-linked, while primary
PDGF-treated systems support STAT3 activation and an existing graph component
supports STAT3-associated FOS transcription. The branch-to-STAT3 handoff is
explicitly unasserted in every route. These rows remain evidence-only and do
not create graph edges, causal assertions, or database confidence scores.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 340,059 |
| Literature-expansion annotations | 6,391 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 435 |
| Normalized route nodes | 1,306,499 |
| Normalized route edges | 1,284,110 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows.
