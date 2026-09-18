# mSCIdblit v1.9.50

This release adds ten selective primary-literature route annotations spanning
glycoform-dependent immune recognition, complement–phagocyte modulation,
neuronal adhesion, checkpoint organization, neutrophil transmigration,
microglial synapse elimination, receptor-tyrosine-kinase activation and
extracellular-matrix adhesion. The evidence layer now retains
Galectin-1–CD43–Siglec1, Factor H–CR3/Mac-1, Properdin–NKp46,
Tenascin-R–Contactin-1–NrCAM, PD-L2–PD-L1–CD80, Proteinase-3–CD177–PECAM1,
CX3CL1–CX3CR1 microglial synapse elimination, C3–CR3 microglial synapse
elimination, NELL2–ROS1 activation and Perlecan–CSPG4/NG2 adhesion routes.

The records preserve the distinction between an existing ligand–receptor input
edge and separately curated receptor-proximal primary evidence. The NELL2–ROS1
record retains the structural and receptor-phosphorylation boundaries of the
recent primary study; the CX3CL1 and C3 records retain their developmental
microglial pruning contexts. Transcription-factor and terminal target-gene
layers remain unassayed for this batch; no causal graph edges or confidence
scores are created.

- Route evidence: 17,221 → 17,231 records
- Graph topology: 11,952 nodes and 14,722 edges, unchanged
- Downstream queue candidates covered: 1,144 → 1,154
- Remaining downstream queue candidates: 2,177
- Remaining P1 candidates: 1,145
- Primary locators: PMID:11238599; PMID:20826755; PMID:28480349; PMID:8274278; PMID:17580308; PMID:31209379; PMID:22632727; PMID:41698918; PMID:29462330

All route annotations remain evidence-layer records and are not causal graph
edges. The corresponding bundle is
`mechanism_graph_module20_24_v2026_09_16_literature_expansion145`.
