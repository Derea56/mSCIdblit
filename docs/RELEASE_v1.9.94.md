# mSCIdblit v1.9.94

## Gap-driven primary-literature expansion

This release adds nine bounded receptor-proximal route annotations:

- Netrin-4/NEO1 > UNC5B > endothelial migration and tube formation
- syndecan-4 > VEGFR3 > VEGF-C-dependent receptor signaling and lymphangiogenesis
- TAG1/CNTN2 > NRP1 > Sema3A-dependent receptor trafficking and CRMP2/growth-cone output
- SCRG1 > BST1-containing receptor context > FAK/ERK/PI3K-AKT-associated MSC output
- GPNMB > EGFR heterocomplex > BRK/HIF1A phosphorylation output
- NPTX2 > NPTXR > neuronal-pentraxin complex organization
- CSPG4/NG2 > FGFR1 or FGFR3 > FGF2 receptor-phosphorylation output
- cleaved Hevin/SPARCL1 > TLR4 > microglial response/processing output

The routes use primary studies including PMID:18719102, PMID:27225479,
PMID:22836270, PMID:24413464, PMID:26751287, PMID:10748068,
PMID:23124902 and DOI:10.1016/j.neuron.2025.12.028. Coreceptor, cis-complex,
cleavage, cell-context and composite-topology limitations remain explicit.
No graph edges, causal traversals, confidence scores, terminal TFs, target
genes or SCI-specific transfers are asserted.

## Release counts

- Route evidence records: 19,505 -> 19,514
- Strict full-route annotations: 77 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 9

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion189`.
