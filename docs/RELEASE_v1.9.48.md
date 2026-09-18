# mSCIdblit v1.9.48

This release adds ten selective primary-literature route annotations covering
immune-receptor proximal biochemistry, mechanotransduction, inhibitory CNS
receptor complexes, adhesion, efferocytosis, trophic signaling, glycan-dependent
receptor recognition, and complement assembly. The evidence layer now retains
CD45–TCRζ, PCDH15–LHFPL5, NgR1–NgR3, Slitrk5–PTPδ, L1–VLA-5,
PtdSer–BAI1, microglial BDNF–TrkB, Dectin-1–CLEC-2, basigin–E-selectin, and
C1r–C1s continuations.

The annotations preserve important boundaries. Several routes are adhesion or
extracellular-complex continuations rather than canonical intracellular
cascades; the Slitrk5, L1, Dectin-1, and basigin records explicitly separate
the incoming graph edge from the ligand or assay used in the downstream primary
study. Transcription-factor and terminal target-gene layers remain unassayed
for this batch; no causal graph edges or confidence scores are created.

- Route evidence: 17,201 → 17,211 records
- Graph topology: 11,952 nodes and 14,722 edges, unchanged
- Downstream queue candidates covered: 1,124 → 1,134
- Remaining downstream queue candidates: 2,197
- Remaining P1 candidates: 1,165
- Primary locators: PMCID:PMC45139; PMID:30070639; PMID:22406547; PMID:26004511; PMID:8557754; PMID:24898390; PMID:24360280; PMID:36479973; PMID:19443639; PMID:19494295

All route annotations remain evidence-layer records and are not causal graph
edges. The corresponding bundle is
`mechanism_graph_module20_24_v2026_09_16_literature_expansion143`.
