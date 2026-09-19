# mSCIdblit v1.9.118

## Gap-driven primary-literature expansion

This release adds ten bounded ligand→receptor→output annotations from
primary-supported records that previously had receptor-entry evidence but no
explicit route-level output annotation:

- FGF3→FGFR1b→mitogenic response
- FGF7→FGFR2b→biological potency and mitogenic response
- FGF2→FGFR4→mitogenic response
- FGF8b→FGFR1c→mid-hindbrain patterning
- ANGPT1→αVβ5 integrin→directional retinal angiogenesis
- tenascin-C→αVβ6 integrin→EMT-like cellular response
- osteopontin/SPP1→CD44→chemotaxis and attachment
- IL-37→IL1R8/SIGIRR→suppression of inflammatory cytokine output
- netrin-1→UNC5A→growth-cone repulsion
- CCL28→CCR3→chemotaxis and mucosal recruitment

These are evidence-layer routes for mSCS plausibility analysis. They do not
create graph edges, causal claims, or database confidence scores. Intracellular
continuation, TF, and target-gene layers remain explicitly unasserted. The
annotations preserve splice-isoform, receptor-complex, cofactor, cell-model,
and non-SCI comparator boundaries from the primary studies.

## Release counts

- Route evidence records: 19,697 → 19,707
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 10

Primary locators include PMID:7592624, PMID:10950949, PMID:16597617,
PMID:16384934, PMID:24048525, PMID:23958855, PMID:8560266,
PMID:25654981, PMID:25123307, and PMID:17912348.

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion213`.
