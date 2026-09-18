# mSCIdblit v1.9.52

This release adds ten selective primary-literature route annotations covering
thrombin–platelet receptor context, microglial and astrocyte engulfment,
collagen/glypican–APP association, desmosomal adhesion, APP–LRP10 trafficking,
and lectin-complement protease continuations. The evidence layer now retains
thrombin–GPIb-IX-V, CD47–microglial synapse pruning, PLTP–ABCA1–reactive
astrocyte phagocytosis, collagen V–GPC1–APP, E-cadherin–DSG2–DSC3,
E-cadherin–DSG2–ephrin-B1, APP–LRP10, MBL–MASP2, MBL–MASP1 and
L-ficolin–MASP2 routes.

The records preserve the distinction between an existing ligand–receptor input
edge and separately curated receptor-proximal primary evidence. Complement
records retain soluble lectin-complex and protease-activation boundaries;
phagocytic records retain their developmental or ischemic model contexts; and
the adhesion/APP records remain bounded molecular or functional continuations,
not inferred canonical intracellular cascades. Transcription-factor and
terminal target-gene layers remain unassayed for this batch; no causal graph
edges or confidence scores are created.

- Route evidence: 17,241 → 17,251 records
- Graph topology: 11,952 nodes and 14,722 edges, unchanged
- Downstream queue candidates covered: 1,164 → 1,174
- Remaining downstream queue candidates: 2,157
- Remaining P1 candidates: 1,125
- Primary locators: PMID:8022782; PMID:30308165; PMID:28642575; PMID:8940123; PMID:33229577; PMID:22734645; PMID:9087411; PMID:10925294; PMID:12421953; PMID:18031558; PMID:10679061

All route annotations remain evidence-layer records and are not causal graph
edges. The corresponding bundle is
`mechanism_graph_module20_24_v2026_09_16_literature_expansion147`.
