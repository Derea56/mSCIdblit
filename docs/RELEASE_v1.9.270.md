# mSCIdblit release v1.9.270

This release extends the all-ligand mechanism graph with primary-evidence
JAK→STAT pathway handoffs and rematerializes the evidence-route layer so
mSCS can traverse ligand→receptor→intracellular continuation→TF→output
routes where the intermediate handoff is supported.

Graph identifier: `module20_24_mechanism_graph:2026-09-24-all-ligand-jak-stat-handoff-394`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion394/`

The source-register batch adds 30 pathway-specific JAK→STAT handoff edges and
30 primary evidence records. These are exported as `supports` pathway-handoff
edges with explicit limitations; they do not assert a universal binary
kinase–substrate reaction, causality, or confidence.

The route layer adds 18,611 graph-supported compositions across 58 ligand–receptor
edges. Of those additions, 13,643 contain explicit receptor→intracellular and
intracellular→TF edge identifiers. Route-to-target output linkage remains an
evidence layer for mSCS evaluation.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 573,499
- Route nodes: 2,394,027
- Route edges: 2,216,676
- Full-sequence curation queue: 7,742

Validation passed with no errors. The only retained warning is the existing
stable-locator audit for evidence records whose provenance is local or
otherwise unresolved.
