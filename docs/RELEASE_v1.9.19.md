# mSCIdblit mechanism graph release v1.9.19

Release date: 2026-09-17

This release adds the 114th selective primary-literature expansion batch for
Module 21B downstream curation. The evidence overlay adds ten previously
unexpanded ligand-receptor routes with receptor-specific adhesion,
chemokine-binding, migration, or functional readouts while keeping
intracellular and transcription-factor layers explicit.

The batch covers Mac-2BP-E-selectin adhesion; human L-selectin-E-selectin
binding and neutrophil rolling; CCL2-ACKR1/DARC chemokine sequestration;
hyaluronan-layilin adhesion; laminin-411 and laminin-421 interactions with
MCAM/CD146 and alpha6beta1 integrin; and fibronectin interactions with
alpha4beta1 and alpha4beta7 integrins. Primary locators are retained for
PMID:22970241, PMID:9024699, PMID:13679391, PMID:11294894/PMCID:PMC32274,
PMID:22792325/PMCID:PMC3391262, PMID:24951930,
PMID:8598221, PMID:7689608, and PMID:7523506.

All ten routes are classified as
`ligand_receptor_output_annotation_missing_intracellular_and_tf`: they retain
exact ligand-receptor evidence and preserve the distinct observed outputs
without asserting graph-linked intracellular or TF layers. All ten routes
remain non-causal evidence routes. No graph edges, causal edges, or database
confidence scores are created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,921
- Cumulative literature-expansion route rows: 874
- Unique downstream queue candidates covered by the expansion inputs: 844
- Remaining downstream queue candidates: 2,487
- Remaining P1 candidates: 1,442

The release is an evidence-layer update only. mSCS can use the retained
ligand-receptor and output evidence for route-plausibility analysis while
applying its own confidence logic and treating unresolved layers as
uncertainty rather than as absent biology.
