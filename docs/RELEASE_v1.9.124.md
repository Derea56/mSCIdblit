# mSCIdblit v1.9.124

## Gap-driven primary-literature expansion

This release adds ten bounded ligand→receptor→output annotations spanning
signaling, endocytic handling, and glial homeostasis:

- HMGB1→RAGE:heparan sulfate→Erk/p38 and chemotaxis
- TSP1→LRP1→binding, endocytosis, and degradation
- diferric transferrin→TfR1→internalization, recycling, and iron delivery
- GABA→GABA-rho2→ligand-gated chloride current
- progranulin→sortilin→neuronal uptake and lysosomal trafficking
- CCL3→ACKR2/D6→internalization, recycling, and degradation
- decorin→LRP1→uptake and lysosomal degradation
- DLL4→NOTCH3→Notch proteolysis and macrophage inflammatory output
- granzyme B→IGF2R/CI-MPR→uptake and perforin-independent apoptosis
- Maresin 1→GPR37L1→satellite-glial potassium-current and pain-homeostasis output

These are evidence-layer routes for mSCS plausibility analysis. They do not
create graph edges, causal claims, or database confidence scores. Intracellular
continuation, TF, and target-gene layers remain explicitly unasserted, even
where a named adaptor or reporter appears in the primary assay. Endocytic
clearance and scavenging routes are retained as receptor-dependent outputs but
are not mislabeled as canonical kinase cascades.

## Release counts

- Route evidence records: 19,757 → 19,767
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 10

Primary locators include PMID:21990362, PMID:7775583, PMID:6300098,
PMID:15733087, PMID:21092856, PMID:15004236, PMID:16936287,
PMID:17533181, PMID:11081635, and PMID:38530364.

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion219`.
