# mSCIdblit v1.9.45

This release adds ten selective primary-literature route annotations for mSCS
signaling plausibility analysis. The evidence layer now retains explicit
ligand–receptor–output routes for NRG1β–HER2/HER3, eCIRP–TLR4/MD2,
endostatin–VEGFR2, PAI-1–LRP1, FGF5–FGFR1c, NT3–TrkA, NT3–TrkB,
DLL4–NOTCH1, FSTL1–TLR4, and CYTL1–CCR2B.

The routes preserve receptor-dependent, inhibitory, atypical-ligand, and
model-specific caveats. Intracellular continuation, transcription-factor, and
terminal target-gene layers remain explicitly unassayed for this batch; no
causal graph edges or confidence scores are created.

- Route evidence: 17,171 → 17,181 records
- Graph topology: 11,952 nodes and 14,722 edges, unchanged
- Downstream queue candidates covered: 1,094 → 1,104
- Remaining downstream queue candidates: 2,227
- Remaining P1 candidates: 1,195
- Primary locators: PMID:9693119; PMID:24097189; PMID:12029087; PMID:15001579; PMID:8663044; PMID:9015308; PMID:1649702; PMID:30289388; PMID:22265692; PMID:27084102

All route annotations remain evidence-layer records and are not causal graph
edges. The corresponding bundle is
`mechanism_graph_module20_24_v2026_09_16_literature_expansion140`.
