# mSCIdblit v1.9.53

This release adds ten selective primary-literature route annotations covering
lectin-complement recognition, CD47 receptor-proximal continuations,
desmosomal and neuron–glia adhesion, microglial activation, and extracellular
synaptic-organizing complexes. The evidence layer now retains
MBL–CR1/CD35, CD47–SIRPγ, CD47–α2β1 integrin, MBL–LAIR2, E-cadherin–DSG2–DSC2,
E-cadherin–DSG2–DSC3, CD200–microglial activation,
N-cadherin–astrotactin-1, syndecan–MADD-4–neuroligin-1, and
syndecan–MADD-4–neurexin-1 routes.

The records preserve the distinction between an existing ligand–receptor input
edge and separately curated receptor-proximal primary evidence. Soluble
lectin, checkpoint, adhesion and microglial records retain their source-specific
topology and assay boundaries; none are promoted to causal intracellular
relays. Transcription-factor and terminal target-gene layers remain unassayed
for this batch; no causal graph edges or confidence scores are created.

- Route evidence: 17,251 → 17,261 records
- Graph topology: 11,952 nodes and 14,722 edges, unchanged
- Downstream queue candidates covered: 1,174 → 1,184
- Remaining downstream queue candidates: 2,147
- Remaining P1 candidates: 1,115
- Primary locators: PMID:11120776; PMID:18524990; PMID:10397731; PMID:24192271; PMID:27298358; PMID:11099416; PMID:30262652; PMID:26028574; PMID:32928959

All route annotations remain evidence-layer records and are not causal graph
edges. The corresponding bundle is
`mechanism_graph_module20_24_v2026_09_16_literature_expansion148`.
