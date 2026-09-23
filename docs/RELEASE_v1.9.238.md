# mSCIdblit release v1.9.238

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-all-ligand-output-linked-361`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion361/`

## Growth-hormone and prolactin target-output curation

This release adds two primary-supported evidence routes that were previously
represented only as full-sequence queue candidates:

- GH → GHR → JAK2 → STAT5 → BCL2 expression
- prolactin → PRLR → JAK2 → STAT5 → BCL2 expression

The target-gene and receptor-proximal components are linked to existing graph
edges. No direct ligand→BCL2 output graph edge was asserted; the route records
mark that output linkage as primary-evidence-only and retain the missing layer
explicitly. The cumulative clean overlay now contains 105 unique added route
annotations and 546 literature-expansion rows.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,214 |
| Literature-expansion annotations | 546 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,293,122 |
| Normalized route edges | 1,275,979 |

The release validator passed with zero errors, and the focused mSCS route tests
passed 18/18. No graph edges, causal assertions, or database confidence scores
were created.
