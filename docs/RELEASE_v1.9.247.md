# mSCIdblit release v1.9.247

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-gh-jak2-stat5-cish-370`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion370/`

## Growth-hormone STAT5 target route expansion

This release adds two parallel evidence routes for the two current growth
hormone ligand labels:

`GH1/growth hormone (GH) > GHR/growth hormone receptor > JAK2 > STAT5 > Cish expression`

`Growth hormone > GHR/growth hormone receptor > JAK2 > STAT5 > Cish expression`

Primary-linked evidence supports the receptor, GHR-associated JAK2, GH-induced
STAT5 activity, and GH-induced Cish expression. The STAT5-to-Cish component is
retained from the existing evidence-gated graph; the JAK2-to-STAT5 handoff
remains explicitly unasserted. These rows therefore support mSCS route
plausibility without creating graph edges, causal assertions, or database
confidence scores.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 340,053 |
| Literature-expansion annotations | 6,385 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 429 |
| Normalized route nodes | 1,306,469 |
| Normalized route edges | 1,284,080 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows.
