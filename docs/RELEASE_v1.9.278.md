# mSCIdblit release v1.9.278

This release promotes 1,602 additional source-linked route annotations across
731 ligand labels. The additions expose receptor-proximal intracellular,
transcription-factor, generic-output, and target-gene evidence already present
in the retained route-evidence layer. Unresolved handoffs remain explicit as
`????`; no missing intermediate is inferred.

Graph identifier: `module20_24_mechanism_graph:2026-09-24-source-linked-route-queue-421`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion421/`

The promoted rows require a source queue ID, a downstream evidence-record ID,
a stable public locator, and a ligand-role input. They remain evidence-only
(`causal_status=not_asserted`, `traversal_status=evidence_route_not_causal`),
with no new graph edges or database confidence scores.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 580,977
- Route nodes: 2,427,856
- Route edges: 2,243,045
- Full-sequence curation queue: 15,325
- Literature-expansion annotations: 14,863
- Unique ligand candidates in queue: 1,862

Validation passed with no errors. The retained warning concerns evidence
sources without stable public locators. The queue remains a curation worklist,
not a confidence layer or a claim that every missing link has been resolved.
