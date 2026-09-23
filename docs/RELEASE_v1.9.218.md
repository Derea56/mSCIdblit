# mSCIdblit release v1.9.218

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-primary-full-sequence-routes-336`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion336/`

## Receptor-proximal relay expansion

This release adds 14 nonduplicate source-linked route annotations across seven
ligand labels. The additions promote primary-locator-backed receptor-proximal
relays including JAK1/2/3, TYK2, MYD88, TRAF6, TICAM2/TRAM, RIPK2/RICK,
heterotrimeric G-protein branches, and a TRAF2:cIAP adaptor complex. The
routes connect those relays to already source-linked TF and downstream layers.

The receptor-to-relay edge is source-linked, while the relay-to-TF handoff
remains explicitly unasserted. These are composed, non-causal evidence routes;
they do not create graph edges or confidence scores and are not claims that a
single paper demonstrated every handoff. Duplicate signatures already present
in v335 were not re-added.

Together with v335, the release contains 318 literature route annotations
across 100 ligand labels and 334,000 normalized signaling-route evidence
records.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,000 |
| Full-sequence literature annotations | 318 |
| Ligand labels represented in literature annotations | 100 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,292,058 |
| Normalized route edges | 1,275,085 |

The release validator passed with zero errors; the existing stable-locator
warning remains.
