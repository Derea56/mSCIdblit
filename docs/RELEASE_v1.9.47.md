# mSCIdblit v1.9.47

This release adds ten selective primary-literature route annotations focused on
adhesion-complex, clearance, receptor-cofactor, and cross-cell signaling
continuations. The evidence layer now retains contactin-1/CASPR1,
contactin-1/NF155, contactin-1/PTPRZ1, PtdSer/TIM4, CD47/SIRPalpha,
VEGFB/NRP1, PtdSer/TIM1/CD300B, TAG1/L1CAM/ErbB3, WNT3A/biglycan/LRP6, and
RAMP2/PTH1R routes.

The annotations preserve model and topology limits. Several records represent
adhesion or accessory-complex modulation rather than direct ligand occupancy;
the NRP1 record is a cross-cell microglia-to-OPC relay, and the RAMP2 record
explicitly separates adrenomedullin-RAMP2 input from PTH/PTHrP testing at
PTH1R. Transcription-factor and terminal target-gene layers remain unassayed
for this batch; no causal graph edges or confidence scores are created.

- Route evidence: 17,191 → 17,201 records
- Graph topology: 11,952 nodes and 14,722 edges, unchanged
- Downstream queue candidates covered: 1,114 → 1,124
- Remaining downstream queue candidates: 2,207
- Remaining P1 candidates: 1,175
- Primary locators: PMID:12972410; PMCID:PMC2173730; PMID:21969550; PMID:24898390; PMID:33795678; PMID:33859199; PMID:20566714; PMID:22815787; PMID:21969569; PMID:35914163

All route annotations remain evidence-layer records and are not causal graph
edges. The corresponding bundle is
`mechanism_graph_module20_24_v2026_09_16_literature_expansion142`.
