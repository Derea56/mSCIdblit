# mSCIdblit v1.9.121

## Gap-driven primary-literature expansion

This release adds ten bounded ligand→receptor→output annotations from
primary-supported records with direct functional readouts:

- SEMA4A→Plexin-B2→Rnd1-linked contraction and growth-cone collapse
- SEMA4A→Plexin-B3→Rnd1-linked contraction and growth-cone collapse
- TIMP1→LRP1→internalization and neurite-growth effects
- Glycine→GlyRalpha2→strychnine-sensitive chloride current
- Protons→ASIC1→acid-gated cation current
- Glutamate→GluA1/AMPA receptor→ligand-gated current
- Acetylcholine→nicotinic ACh receptor→ligand-gated cation current
- C5a→C5L2→beta-arrestin2 recruitment and receptor internalization
- ephrin-A5→EphB2→receptor autophosphorylation and growth-cone collapse
- SEMA3A→NRP1:Plexin-A2→growth-cone collapse and repulsion

These are evidence-layer routes for mSCS plausibility analysis. They do not
create graph edges, causal claims, or database confidence scores. Intracellular
continuation, TF, and target-gene layers remain explicitly unasserted. The
annotations retain receptor-complex, heterologous-expression, electrophysiology,
endocytosis, structural, and neuronal-comparator boundaries from the primary
studies.

## Release counts

- Route evidence records: 19,727 → 19,737
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 10

Primary locators include PMID:20043131, PMID:25075518, PMID:7752562,
PMID:9062189, PMID:1699805, PMID:3834076, PMID:19641221, PMID:15107857,
PMID:23104057, and PMID:10781943.

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion216`.
