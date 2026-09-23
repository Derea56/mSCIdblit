# mSCIdblit release v1.9.217

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-primary-full-sequence-routes-335`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion335/`

## All-ligand full-intermediate route expansion

This release promotes 192 additional source-linked route annotations from the
full-sequence curation queue. Each selected record has explicit ligand,
receptor, intracellular continuation, transcription-factor, and downstream
output labels plus stable primary locators. The additions cover 70 ligand
labels and add 187 `ligand>receptor>intracellular>TF>output` routes and five
routes with target-gene labels.

These are composed evidence routes, not claims that one paper demonstrated
every handoff. The route linkage records retain the source-linked layers and
explicitly state `end_to_end_chain_not_asserted_by_single_source`. They remain
non-causal, non-traversable evidence records for mSCS evaluation; no graph
edges or confidence scores are created. Of 537 queue candidates with all
intermediate and downstream labels, 344 were withheld because the normalized
route lacked a downstream evidence-record anchor.

Together with v334, the release contains 304 literature route annotations
across 97 ligand labels.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 333,986 |
| Full-sequence literature annotations | 304 |
| Ligand labels represented in literature annotations | 97 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,291,998 |
| Normalized route edges | 1,275,039 |

The release validator passed with zero errors; the existing stable-locator
warning remains. mSCS imports the release identifier and the evidence-only
route annotations without materializing causal graph edges.
