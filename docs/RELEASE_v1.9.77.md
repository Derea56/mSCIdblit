# mSCIdblit v1.9.77

## Gap-driven primary-literature expansion

This release upgrades two shared-beta-chain cytokine routes with named
intracellular continuations and target-gene outputs:

- GM-CSF > CSF2RA:CSF2RB > JAK2 > STAT5 > CISH
- IL-3 > IL3RA:CSF2RB > JAK2 > STAT5 > CISH

The routes are supported by primary studies reporting cytokine receptor
JAK2/STAT5 signaling and CIS/CISH induction or promoter activity
(PMID:10372132; PMID:17090651; PMID:36471114; PMID:7539031;
PMID:9129017). They remain evidence-layer routes rather than causal graph
traversals. Shared-beta-chain, species, cell-state and CIS/CISH nomenclature
limits are preserved. No database confidence score is added.

## Release counts

- Route evidence records: 19,456 -> 19,458
- Strict full-route annotations: 56 -> 58
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 2

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion172`.
