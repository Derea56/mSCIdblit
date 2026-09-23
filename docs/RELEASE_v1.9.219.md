# mSCIdblit release v1.9.219

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-primary-full-sequence-routes-337`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion337/`

## Full-intermediate route completion

This release adds two nonduplicate source-linked full-intermediate route
annotations across two ligand labels:

- IL-6 > IL-6R-gp130 > JAK1 > STAT3 > MYC/output program
- IL-15 > IL15RA:IL2RB:IL2RG > JAK3 > STAT5 > BCL2/IL17A output

These are composed evidence routes. The component layers retain their primary
locators, while the release does not assert that one source demonstrated every
handoff, causal activation, or a database confidence score. No graph edges were
created or changed.

Together with earlier releases, the bundle contains 320 literature route
annotations across 102 ligand labels and 334,002 normalized signaling-route
evidence records.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,002 |
| Full-sequence literature annotations | 320 |
| Ligand labels represented in literature annotations | 102 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,068 |
| Normalized route edges | 1,275,093 |

The release validator passed with zero errors; the existing stable-locator
warning remains.
