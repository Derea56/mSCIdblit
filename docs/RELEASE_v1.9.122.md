# mSCIdblit v1.9.122

## Gap-driven primary-literature expansion

This release adds ten bounded ligand→receptor→output annotations emphasizing
receptor-mediated uptake, scavenging, internalization, and neuronal outputs:

- proBDNF→SORCS2→growth-cone collapse
- L-ferritin→SCARA5→endocytosis and iron delivery
- LCN2/NGAL→SLC22A17→receptor-mediated internalization
- HTRA1→LRP1→internalization and vascular handling
- tPA→LRP1→endocytic clearance
- apoB-70.5 lipoprotein→LRP2/megalin→uptake and catabolism
- CS-E→Contactin-1→neurite extension
- ManLAM→DC-SIGN→BCG internalization and maturation output
- CCL20→ACKR4→beta-arrestin/scavenging output
- CXCL10→ACKR2→beta-arrestin, lysosomal routing, and depletion

These are evidence-layer routes for mSCS plausibility analysis. They do not
create graph edges, causal claims, or database confidence scores. Intracellular
continuation, TF, and target-gene layers remain explicitly unasserted. Uptake
and scavenging annotations are retained as receptor-dependent outputs but are
not labeled as canonical kinase cascades. Model, species, ligand-form,
receptor-complex, and non-SCI comparator boundaries remain explicit.

## Release counts

- Route evidence records: 19,737 → 19,747
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 10

Primary locators include PMID:24908487, PMID:19154717, PMID:16377569,
PMID:23868935, PMID:8063731, PMCID:PMC408451, PMID:19075012,
PMID:12515809, PMID:32533638, and PMID:33801414.

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion217`.
