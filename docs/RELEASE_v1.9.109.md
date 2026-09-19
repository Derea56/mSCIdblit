# mSCIdblit v1.9.109

## Gap-driven primary-literature expansion

This release adds 15 bounded route annotations selected from canonical
ligand–receptor entries with source-linked downstream readouts:

- CXCL12 > CXCR4 and CCL2 > CCR2 chemokine-receptor functional outputs
- GM-CSF > CSF2RA/CSF2RB and IL-21 > IL21R/IL2RG cytokine-receptor outputs
- IL-22 > IL22RA1/IL10RB JAK/STAT activation
- IL-37 > IL18R1/SIGIRR anti-inflammatory transcriptional output
- BDNF > TrkB and NRTN/ARTN > GFRα/RET receptor-complex outputs
- TGF-β3, Activin A and NODAL receptor-complex assembly and Smad-related outputs
- NRG1β > ERBB3 phosphorylation and AKT/ERK output
- FGF18 > FGFR2c and FGFR3c receptor-selectivity and cartilage-function outputs

The routes use primary studies including PMID:11950254, PMID:12513909,
PMID:1460041, PMID:1649702, PMID:18089557, PMID:18243111, PMID:20682778,
PMID:25729923, PMID:28325822, PMID:31392261, PMID:35570218,
PMID:37339051 and PMID:8622651. Receptor-complex stoichiometry, splice
variants, model-specific outputs and unresolved intracellular or TF layers
remain explicit. These are evidence-layer annotations only: no graph edges,
causal traversals or confidence scores are asserted.

## Release counts

- Route evidence records: 19,590 -> 19,605
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 15

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion204`.
