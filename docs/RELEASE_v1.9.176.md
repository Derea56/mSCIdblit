# mSCIdblit release v1.9.176

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-289`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion289/`

## Curated receptor-proximal output evidence

This release adds ten primary-supported output annotations from the next
unresolved queue tranche. They retain topology-unlinked route semantics
(`????>????>????>????>output`): the records preserve experimentally observed
complex formation, sequestration, scavenging, chemotaxis, signaling, or
functional readouts without assigning unsupported ligand, receptor,
intracellular, or transcription-factor links. No graph edges, causal claims,
confidence scores, intracellular links, or TF links are created.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 18,692 |
| New literature-expansion rows | 10 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Prioritized route-gap pairs | 5,954 |

The direct L→R route categories remain unchanged because these annotations do
not assert a complete direct topology:

| Category | Records |
|---|---:|
| L→R→output | 4,394 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,421 |
| L→R→intracellular→TF→output | 131 |
| L→R entry only | 9,307 |

All ten rows retain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. Validation passed with zero
errors, and the bundle imported successfully through mSCS's
`import_mechanism_bundle.py` into a temporary active release directory.
