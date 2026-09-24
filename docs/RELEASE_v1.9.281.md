# mSCIdblit release v1.9.281

This release adds 37 source-linked composed full intermediate routes across
three ligand labels. Eighteen routes join relay, TF, and measured-output
observations from one source queue; 19 additional routes retain at least one
pairwise public-locator overlap. These routes end in measured outputs rather
than asserting a named target-gene edge, so they extend plausible signaling
coverage without converting an output readout into target-gene causality.

Graph identifier: `module20_24_mechanism_graph:2026-09-24-pairwise-full-output-queue-429`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion429/`

The new rows use `ligand>receptor>intracellular>TF>output`, preserve the
measured output label and public locators, and leave the target-gene layer
empty. They retain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`; no graph edge or database
confidence score is created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 587,741
- Route nodes: 2,461,495
- Route edges: 2,269,920
- Full-sequence curation queue: 15,388
- Literature-expansion annotations: 21,627
- Unique ligand candidates in queue: 1,862

Graph validation passed with no errors; the retained warning concerns evidence
sources without stable public locators. The queue remains a curation worklist,
not a confidence layer.
