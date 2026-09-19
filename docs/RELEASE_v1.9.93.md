# mSCIdblit v1.9.93

## Gap-driven primary-literature expansion

This release adds four bounded output-bearing annotations for unresolved
ligand/receptor or matrix-receptor records:

- SCUBE2 > VEGFR2 coreceptor context > VEGFR2 phosphorylation/MAPK-AKT and endothelial angiogenic response
- SPON2 > alpha5beta1 integrin > RhoA-associated relay > adhesion and migration/invasion output
- SPARC > beta1-integrin-associated complex > ILK activity and stress-survival output
- laminin alpha4 G-domain > alpha6beta1 integrin > endothelial attachment and angiogenic response

The routes are based on primary studies (PMID:27834687; PMID:16917498;
PMID:29440144; PMID:18503049; PMID:12454288; PMCID:PMC138567). Coreceptor,
matrix-adhesion, cell-context and composite-study limitations remain explicit.
No terminal TF, target gene, causal traversal, confidence score or SCI-specific
transfer is asserted.

No graph edges or confidence scores are added.

## Release counts

- Route evidence records: 19,501 -> 19,505
- Strict full-route annotations: 77 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 4

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion188`.
