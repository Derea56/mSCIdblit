# mSCIdblit v1.9.116

## Gap-driven primary-literature expansion

This release adds ten bounded ligand→receptor→output annotations from
primary-supported records that were already present in the downstream
curation queue:

- CXCL12→CXCR4→migration
- CD47→SIRPA→inhibition of macrophage phagocytosis
- MFG-E8→αVβ3→phosphatidylserine-bridging phagocytosis
- MFG-E8→αVβ5→phosphatidylserine-bridging phagocytosis
- CCL2→CCR2→chemotaxis
- CCL5→CCR5→receptor activation
- CXCL2→CXCR2→leukocyte arrest and neutrophil chemotaxis
- tenascin-C→TLR4→NF-κB reporter/cytokine response
- TSP1→CD36→inhibition of endothelial migration and tube formation
- osteopontin/SPP1→αVβ3→cell adhesion

These are evidence-layer routes for mSCS plausibility analysis. They do not
create graph edges, causal claims, or database confidence scores. Intracellular
continuation, TF, and target-gene layers remain explicitly unasserted.
Context boundaries such as opsonin bridging, membrane-bound CD47 geometry,
TLR4 FBG-domain fragments, and non-SCI comparator models are retained in the
route annotations.

## Release counts

- Route evidence records: 19,677 → 19,687
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 10

Primary locators include PMID:11283158, PMID:12000961, PMID:15325806,
PMID:15937099, PMID:18657508, PMID:20427772, PMID:23640500,
PMID:28325822, PMID:29150600, PMID:34134983, and PMID:35570218.

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion211`.
