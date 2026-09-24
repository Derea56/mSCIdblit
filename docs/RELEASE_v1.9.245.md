# mSCIdblit release v1.9.245

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-all-ligand-target-routes-368`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion368/`

## All-ligand target-gene route promotion

This release adds 441 individually addressable target-gene evidence routes
across 44 ligand labels. The routes are restricted to full-sequence queue rows
with a linked downstream curation record and retained primary locators. They
are emitted at the highest supported layer: 104 include a TF with the
intracellular step unresolved, while 337 retain both intracellular and TF
steps as unresolved.

These rows preserve missing layers as `????` and remain evidence-only. The
promotion creates no graph edges, causal assertions, or confidence scores. The
target-gene list is carried from an explicitly named queue component and is
not treated as proof that one paper demonstrated every handoff; mSCS should
evaluate source context and layer linkage when assessing route plausibility.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 340,048 |
| Literature-expansion annotations | 6,380 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 424 |
| Normalized route nodes | 1,306,444 |
| Normalized route edges | 1,284,057 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows.
