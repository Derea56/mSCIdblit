# mSCIdblit release v1.9.256

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-output-template-promotion-379`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion379/`

## Output-template route promotion

This release adds 122 full-layer evidence routes across 11 ligand labels. The
new routes begin with source-linked target-gene records that lack a relay or
TF and use a primary-supported full output route for the same ligand and
receptor as an intracellular/TF template. Eighty-seven retain a TF already
present in the target route; 35 add both the relay and TF identities from the
output template.

The output-template source is not treated as evidence for the target-specific
gene handoff. Original partial routes remain in the release, and each route
records asserted and missing edges explicitly. No graph edges, causal
assertions, or database confidence scores are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 340,553 |
| Literature-expansion annotations | 6,885 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 875 |
| Normalized route nodes | 1,308,883 |
| Normalized route edges | 1,286,000 |
| New output-template routes | 122 |

The release validator passed with zero errors. The only warning remains the
stable-locator audit warning for some evidence-source rows. mSCS import and
contract validation are the next release gate.
