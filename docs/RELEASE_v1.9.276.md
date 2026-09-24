# mSCIdblit release v1.9.276

This release extends the all-ligand primary-literature route overlay with six
evidence-layer routes for IL-27, IL-17A, HBEGF, and PDGFA. The additions
prioritize intracellular continuation and transcriptional output coverage while
retaining unresolved handoffs explicitly.

Graph identifier: `module20_24_mechanism_graph:2026-09-24-high-yield-primary-routes-417`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion417/`

The new routes include IL-27→STAT1/STAT3→IL10, IL-27→STAT1→TBX21,
IL-17A→ACT1/CIKS→NF-kB program→DEFB4, IL-17A→ACT1/CIKS→NF-kB
program→CCL20, HBEGF→EGFR→ERK→EGR1→CYP24A1, and
PDGFA→PDGFRA→ERK→ELK1→EGR1 promoter. These are composed primary-evidence
routes; they do not imply that every handoff was demonstrated in one study.
All annotations remain evidence-only (`causal_status=not_asserted`,
`traversal_status=evidence_route_not_causal`), and no graph edges or database
confidence scores are created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 579,045
- Route nodes: 2,421,440
- Route edges: 2,238,559
- Full-sequence curation queue: 15,321
- Literature-expansion annotations: 12,931
- Unique ligand candidates in queue: 1,862

Validation passed with no errors. The retained warning concerns evidence
sources without stable public locators. The queue remains a curation worklist,
not a confidence layer or a claim that every missing link has been resolved.
