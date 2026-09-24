# mSCIdblit release v1.9.249

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-csf1-il34-erk-cfos-372`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion372/`

## CSF1 and IL-34 ERK/c-FOS route expansion

This release adds two evidence routes:

`CSF1 > CSF1R/c-Fms > MEK/ERK1/2 > ELK1 > c-FOS expression`

`IL-34 > CSF1R/c-Fms > MEK/ERK1/2 > ELK1 > c-FOS expression`

Primary studies support ligand-specific CSF1R engagement and c-FOS output, while
the existing primary-supported CSF1R-to-MEK/ERK component supplies the bounded
intracellular continuation. The ERK-to-ELK1 and ELK1-to-c-FOS handoffs remain
explicitly unasserted. These rows remain evidence-only and do not create graph
edges, causal assertions, or database confidence scores.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 340,061 |
| Literature-expansion annotations | 6,393 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 437 |
| Normalized route nodes | 1,306,509 |
| Normalized route edges | 1,284,118 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows.
