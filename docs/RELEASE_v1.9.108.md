# mSCIdblit v1.9.108

## Gap-driven primary-literature expansion

This release adds 11 bounded route annotations selected from unresolved
ligand–receptor gaps with primary downstream support:

- GDNF > GFRα1/RET > Ras–ERK–CREB/c-Fos and neuronal output
- IFN-β > IFNAR1/IFNAR2 > ISRE and antiviral-transcript output
- IFN-γ > IFNGR1/IFNGR2 > STAT1 phosphorylation and responsive-gene output
- Thrombin > PAR1/PAR4 > calcium, MAPK and platelet or permeability-related output
- Endothelin-1 > EDNRA/EDNRB > PLC/Ca2+-associated signaling output
- Vasopressin > AVPR1A > PLC/IP3/Ca2+ and second-messenger output
- CRH > CRHR2 > cAMP–CREB-associated VEGF-A output
- GDF5 > BMPR1B/ACVR2A > receptor activation and phosphorylation output
- WNT5A > FZD3 > PI3K/AKT-associated adhesion and cellular output

The routes use primary studies including PMID:7969820, PMID:8649432,
PMID:8702914, PMID:12145101, PMID:15878870, PMID:17303636, PMID:17804197,
PMID:22574190, PMID:26350463 and PMID:31892516. Model-specific outputs,
receptor-complex boundaries and unresolved transcription-factor or target-gene
layers remain explicit. These are evidence-layer annotations only: no graph
edges, causal traversals or confidence scores are asserted.

## Release counts

- Route evidence records: 19,579 -> 19,590
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 11

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion203`.
