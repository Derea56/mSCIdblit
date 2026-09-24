# mSCIdblit release v1.9.269

Release date: 2026-09-24

Graph identifier: `module20_24_mechanism_graph:2026-09-24-all-ligand-route-expansion-392`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion392/`

## All-ligand graph-supported route expansion

This release adds 213,835 evidence-only route compositions across 206 exact
ligand–receptor edges and 174 ligand labels. The compositions require an exact
exported ligand–receptor edge plus compatible downstream components with a
shared pathway or evidence anchor. They expose 198,096 routes with a
target-gene layer and 15,739 routes that end at a supported downstream output
without target-gene attribution.

The new routes retain their component evidence IDs and stable graph references.
They leave every relay-to-TF handoff unasserted, create no graph edges, make no
causal assertions, and assign no database confidence scores. mSCS can therefore
use them as plausible evidence routes while evaluating context and confidence
itself.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 554,888 |
| Literature-expansion annotations | 7,385 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 1,368 |
| Normalized route nodes | 2,302,921 |
| Normalized route edges | 2,141,150 |
| New graph-supported routes | 213,835 |

The release validator passed with zero errors. The only warning is the
existing stable-locator audit for a small number of inherited evidence rows.
