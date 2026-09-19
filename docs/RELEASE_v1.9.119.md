# mSCIdblit v1.9.119

## Gap-driven primary-literature expansion

This release adds ten bounded ligand→receptor→output annotations from
primary-supported records that previously had receptor-entry evidence but no
explicit route-level output annotation:

- FGF8b→FGFR2c→mid-hindbrain patterning
- FGF10→FGFR2b→biological activity
- FGF3→FGFR2b→mitogenic response
- CCL26/eotaxin-3→CCR2→inhibition of CCR2 chemotaxis/signaling
- CCL8/MCP-2→CCR3→receptor internalization and chemotaxis
- tenascin-C→αVβ1 integrin→EMT-like cellular response
- SEMA7A→αVβ1 integrin→IL-10 production
- ANGPTL4→αVβ3 integrin→Src/junction stabilization
- JAM2/JAM-B→α4β1 integrin→T-cell rolling and sticking
- CCL11/eotaxin-1→CCR3→calcium flux and eosinophil chemotaxis

These are evidence-layer routes for mSCS plausibility analysis. They do not
create graph edges, causal claims, or database confidence scores. Intracellular
continuation, TF, and target-gene layers remain explicitly unasserted. The
annotations retain splice-isoform, receptor-complex, cofactor, cell-model,
and non-SCI comparator boundaries from the primary studies.

## Release counts

- Route evidence records: 19,707 → 19,717
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 10

Primary locators include PMID:16384934, PMID:12591959, PMID:7592624,
PMID:15039444, PMID:29281969, PMID:23958855, PMID:22198947,
PMID:27577973, PMID:12070135, and PMID:8642344.

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion214`.
