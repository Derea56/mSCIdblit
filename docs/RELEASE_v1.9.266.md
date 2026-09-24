# mSCIdblit release v1.9.266

Release date: 2026-09-24

Graph identifier: `module20_24_mechanism_graph:2026-09-24-il1a-il33-il18-routes-389`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion389/`

## Corrected IL-1A, IL-33, and IL-18 route snapshot

This corrected snapshot carries forward the three v387 routes and adds one
new IL-1A route:

- IL-1A → IL1R1-IL1RAP → MYD88 → RELA → IL6

The preceding v388 build was superseded before mSCS import because its batch
input re-emitted the three carried-forward route IDs. v389 was rebuilt from
the clean v387 source with only the new IL-1A row; all literature-expansion
IDs are unique and the mSCS importer accepts the bundle.

The MYD88-to-TF handoff remains explicitly unasserted. Existing TF-to-target
and direct ligand-associated output evidence are retained as separate layers.
No graph edges, causal assertions, or database confidence scores were created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 341,045 |
| Literature-expansion annotations | 7,377 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 1,367 |
| Normalized route nodes | 1,311,330 |
| Normalized route edges | 1,287,955 |
| New routes in this release | 1 |

The mSCIdblit validator passed with zero errors.
