# mSCIdblit release v1.9.251

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-alias-target-routes-374`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion374/`

## Ligand-alias target-route expansion

This release adds 55 evidence routes for eight source-linked ligand aliases:

`Bdnf`, `Epo`, `Growth hormone`, `Il11`, `Il15`, `Il2`, `Il9`, and `Thpo`.

The routes reuse only existing primary-locator target-gene evidence from the
corresponding canonical ligand families. One route retains an exact
receptor-to-relay graph handoff. The remaining 54 routes expose the
alias-receptor-to-TF-to-target evidence as
`ligand>receptor>????>TF>target_gene_expression`, leaving the intracellular
continuation and its handoff explicitly unresolved. This makes the aliases
addressable to mSCS without treating alias composition as a new causal chain.

No graph edges, causal assertions, or database confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 340,117 |
| Literature-expansion annotations | 6,449 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 439 |
| Normalized route nodes | 1,306,735 |
| Normalized route edges | 1,284,288 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows.
