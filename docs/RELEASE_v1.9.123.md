# mSCIdblit v1.9.123

## Gap-driven primary-literature expansion

This release adds ten bounded ligand→receptor→output annotations emphasizing
SCI-relevant glial, inflammatory, barrier, and axon-guidance outputs:

- MBP→LRP1→myelin-vesicle uptake and oligodendroglial repair-associated output
- LDL→TREM2→microglial lipoprotein uptake
- extracellular Synapsin-I→NCAM→neurite outgrowth
- Versican→NgR2→sensory-axon repulsion
- proNGF→SORCS2/p75NTR→growth-cone signaling
- SEMA6B→Plexin-A4→axon-growth suppression and repulsion
- SEMA3C→Plexin-D1:Plexin-A4→cytoskeletal collapse and repulsion
- Annexin A2→ROBO4→endothelial-barrier preservation
- CCN1→TLR2→MyD88-dependent inflammatory output
- BMP7→ACVR1:BMPR2→receptor-complex reporter output

These are evidence-layer routes for mSCS plausibility analysis. They do not
create graph edges, causal claims, or database confidence scores. Intracellular
continuation, TF, and target-gene layers remain explicitly unasserted, even
where the primary study reports a named adaptor or reporter. Species, receptor
complex, cell-model, and non-SCI comparator boundaries remain explicit.

## Release counts

- Route evidence records: 19,747 → 19,757
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 10

Primary locators include PMID:28549068, PMID:27477018, PMID:21593312,
PMID:24478347, PMID:24908487, PMID:15814794, PMID:29661844,
PMID:21238923, PMID:32144270, and PMID:7791754.

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion218`.
