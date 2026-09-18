# mSCIdblit mechanism graph release v1.9.15

Release date: 2026-09-17

This release adds the 110th selective primary-literature expansion batch for
Module 21B downstream curation. The evidence overlay adds ten previously
unexpanded ligand-receptor routes. Nine retain bounded receptor-output
annotations, and one retains an explicitly source-supported LRP1-NPVY-Akt1/Akt2
continuation for extracellular HSP90alpha.

The batch covers EPO-EPOR receptor orientation and proliferation; FGF1-FGFR3
mitogenic activation; SEMA4D-CD72 B-cell signaling; FGL1-LAG3 immune
checkpoint inhibition; hyaluronan-fragment recognition by the
TLR4-MD2-CD44 complex; extracellular S100A4-RAGE MAPK/ERK motility; JAG1-
NOTCH2 processing; H-ferritin-TfR1 uptake; PGE2-EP2 cAMP coupling; and the
extracellular HSP90alpha-LRP1-Akt motility relay. Primary locators are retained
for PMID:9774108, PMID:10388848, PMID:16597617/PMCID:PMC2080618,
PMID:11114375, PMID:30580966/PMCID:PMC6365968, PMID:17400552,
PMID:24952599/PMCID:PMC4102805, PMID:24126057/PMCID:PMC3889557,
PMID:10958687/PMCID:PMC88767, PMID:20133674/PMCID:PMC2840523, and
PMID:8163486.

Nine routes are classified as
`ligand_receptor_output_annotation_missing_intracellular_and_tf`: they retain
exact ligand-receptor evidence and observed outputs while leaving intracellular
and TF layers unresolved. The HSP90alpha route is classified as
`ligand_receptor_intracellular_output_missing_tf`: it uses the existing
cross-module HSP90alpha-LRP1 binding and LRP1-NPVY-Akt relay edges as bounded
evidence annotations, without asserting a new causal edge. All ten routes
remain non-causal evidence routes. No graph edges, causal edges, or database
confidence scores are created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,881
- Cumulative literature-expansion route rows: 834
- Unique downstream queue candidates covered by the expansion inputs: 804
- Remaining downstream queue candidates: 2,527
- Remaining P1 candidates: 1,482

The release is an evidence-layer update only. mSCS can use the retained
ligand-receptor, intracellular, and output evidence for route-plausibility
analysis while applying its own confidence logic and treating unresolved layers
as uncertainty rather than as absent biology.
