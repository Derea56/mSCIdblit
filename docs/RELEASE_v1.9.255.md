# mSCIdblit release v1.9.255

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-tf-target-promotion-378`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion378/`

## Exact target-template promotion

This release adds 78 full-layer evidence routes across 14 ligand labels. Each
new route starts from an existing source-linked
`ligand>receptor>????>????>target_gene_expression` record and uses a full route
with the identical ligand, receptor, and target-gene node identities to supply
the intracellular and TF identities. The original partial route remains in the
release, and every edge handoff is still represented as asserted or missing.

This is composed evidence for mSCS plausibility analysis. It does not create
graph edges, causal assertions, or database confidence scores, and it does not
claim that one primary source demonstrated every handoff. Partial routes with
no exact full-route template remain unresolved for later literature review.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 340,431 |
| Literature-expansion annotations | 6,763 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 753 |
| Normalized route nodes | 1,308,305 |
| Normalized route edges | 1,285,544 |
| New TF/relay-promotion routes | 78 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows. mSCS imported the
release successfully; its derived-table contract passed and the mechanism-route
test suite passed 18 tests.
