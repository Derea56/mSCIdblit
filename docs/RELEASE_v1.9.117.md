# mSCIdblit v1.9.117

## Gap-driven primary-literature expansion

This release adds ten bounded ligand→receptor→output annotations from
primary-supported records that were already present in the downstream
curation queue:

- annexin A1/ANXA1→FPR2/ALX→receptor activation and calcium/ERK/MAPK readout
- MIF→CD74:CD44→phosphorylation, ERK, and apoptosis-protection readout
- S100A8/A9→RAGE/AGER→MAPK/NF-κB and inflammatory proliferation readout
- S100B→RAGE/AGER→neuronal survival and growth readout
- decorin/DCN→EGFR→receptor autophosphorylation, MAPK, and p21 readout
- adiponectin/ADIPOQ→LAIR1/CD305→inhibitory T-cell activation and SHP-2 readout
- surfactant protein D/SFTPD→SIRPA→suppressed macrophage phagocytosis
- FGL1→LAG3/CD223→inhibited antigen-specific T-cell activation
- tenascin-R/TNR→TLR4→NF-κB reporter and cytokine readout
- surfactant protein D/SFTPD→OSCAR→NFAT reporter and TNF-α release

These are evidence-layer routes for mSCS plausibility analysis. They do not
create graph edges, causal claims, or database confidence scores. Intracellular
continuation, TF, and target-gene layers remain explicitly unasserted, while
the measured receptor-proximal or cellular outputs and their context limits
are retained for downstream confidence evaluation.

## Release counts

- Route evidence records: 19,687 → 19,697
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 10

Primary locators include PMID:22610094, PMID:12782713, PMID:18339893,
PMID:17660747, PMID:9988678, PMID:34403808, PMID:22511785, PMID:30580966,
PMID:29150600, and PMCID:PMC4369396.

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion212`.
