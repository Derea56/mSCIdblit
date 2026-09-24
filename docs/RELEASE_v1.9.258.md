# mSCIdblit release v1.9.258

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-component-promotion-381`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion381/`

## Same-receptor component promotion

This release adds 453 full-layer evidence routes across 24 ligand labels. The
routes use source-linked intracellular and TF components from other routes with
the exact same ligand and receptor node identities. Forty-six add relay
variants to TF-known target routes; 407 add relay and TF identities to
target-gene routes missing both layers.

The component sources may terminate at different outputs or unresolved
endpoints, so direct relay-to-TF and TF-to-target handoffs remain explicitly
qualified. Original partial routes remain in the release. No graph edges,
causal assertions, or database confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 341,018 |
| Literature-expansion annotations | 7,350 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 1,340 |
| Normalized route nodes | 1,311,195 |
| Normalized route edges | 1,287,847 |
| New component-promotion routes | 453 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows. mSCS imported the
release successfully; its derived-table contract passed and the mechanism-route
test suite passed 18 tests.
