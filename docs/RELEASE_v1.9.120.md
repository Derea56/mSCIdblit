# mSCIdblit v1.9.120

## Gap-driven primary-literature expansion

This release adds ten bounded ligand→receptor→output annotations from
primary-supported receptor-entry records that now have explicit functional
readouts:

- Substance P→TACR1/NK1R→phosphatidylinositol metabolism
- 5-oxo-ETE→OXER1/OXE→Gi-linked granulocyte chemotaxis
- UTP→P2Y4/P2RY4→PLC-linked inositol-phosphate signaling
- Galanin→GALR1→adenylyl-cyclase inhibition
- ATP→P2X2/P2RX2→ligand-gated cation current
- ATP→P2X1/P2RX1→ligand-gated cation current
- ATP→P2X3/P2RX3→fast-desensitizing cation current
- Glycine→GLRA1/GlyRalpha1→strychnine-sensitive chloride current
- GABA→GABA-A receptor complex→ligand-gated chloride current
- Serotonin/5-HT→HTR3A/5-HT3→ligand-gated inward cation current

These are evidence-layer routes for mSCS plausibility analysis. They do not
create graph edges, causal claims, or database confidence scores. Intracellular
continuation, TF, and target-gene layers remain explicitly unasserted. The
annotations retain heterologous-expression, electrophysiology, receptor
pharmacology, cell-model, and non-SCI comparator boundaries from the primary
studies.

## Release counts

- Route evidence records: 19,717 → 19,727
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 10

Primary locators include PMID:1657150, PMID:12065583, PMID:16567419,
PMID:8537336, PMID:8700127, PMCID:PMC44900, PMID:8730726, PMID:12719485,
PMID:9221902, PMID:2155780, PMID:9422818, and PMID:7606430.

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion215`.
