# mSCIdblit release v1.9.222

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-catalogued-full-routes-340`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion340/`

## Full-route catalog completion

This release exposes 14 previously retained, source-linked full-route records
through the literature-expansion catalog. The records cover IL-21, IL-23,
IL-15, IL-6, EPO, BDNF, CSF1, and FGF2. No route-evidence record or graph edge
was added; each catalog row reuses its existing route identifier, downstream
evidence record, primary locator, context, and limitations.

The full route sequence remains represented as ligand → receptor → intracellular
continuation → TF → target-gene expression or functional output. Existing
unresolved handoffs remain explicitly marked, and no causal edge or confidence
score is created.

The bundle now contains 358 literature-expansion annotations across 102 ligand
labels and 334,026 normalized signaling-route evidence records.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,026 |
| Literature-expansion annotations | 358 |
| Ligand labels represented in literature annotations | 102 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,188 |
| Normalized route edges | 1,275,189 |

The release validator passed with zero errors; the existing stable-locator
warning remains.
