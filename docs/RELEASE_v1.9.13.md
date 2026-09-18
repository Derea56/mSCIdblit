# mSCIdblit mechanism graph release v1.9.13

Release date: 2026-09-17

This release adds the 108th selective primary-literature expansion batch for
Module 21B downstream curation. The evidence overlay adds ten source-linked
ligand-receptor-output annotations for previously unexpanded P1 candidates.
These routes retain the ligand and receptor input plus a bounded functional or
activation readout while leaving intracellular continuation and TF layers
unresolved.

The batch covers ATP/ADP-P2Y-associated Rac and microglial chemotaxis; Reelin
with VLDLR and ApoER2/LRP8, including Dab1 phosphorylation; noncanonical
Reelin-EPHB2 clustering and neuronal retraction; persephin-GFRA4:RET
autophosphorylation and sympathetic-neuron survival; mature MSP-MST1R/RON
phosphorylation and migration; netrin-4-neogenin antiangiogenic function;
high- versus low-molecular-weight hyaluronan-CD44 ERK/Rac and cyclin-D1
output; IL-27-WSX-1:gp130 cytokine induction; and IL-36α-IL1RL2:IL1RAP
CXCL1 output. Primary locators retained in the bundle include PMID:11245682,
PMID:10571240, PMID:10571241, PMID:23318582, PMID:11116144, PMID:7939629,
PMID:9202013, PMID:18719102, PMID:18806267, PMID:14764690, and
PMID:29180446, together with the associated PMCID locators.

All ten routes are classified as
`ligand_receptor_output_annotation_missing_intracellular_and_tf`: they retain
an exact ligand-receptor edge and source-linked output evidence, but do not
assign a receptor-proximal intracellular continuation or terminal TF. The
Reelin records distinguish canonical lipoprotein-receptor signaling from
noncanonical EphB2 crosstalk, and the netrin-4 record preserves the recruited
Unc5B functional context. All routes remain non-causal evidence routes with
`evidence_route_not_causal` traversal status. No graph edges, causal edges, or
database confidence scores are created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,861
- Cumulative literature-expansion route rows: 814
- Unique downstream queue candidates with literature-expansion coverage: 784
- Remaining downstream queue candidates: 2,547
- Remaining P1 candidates: 1,502

The release is an evidence-layer update only. mSCS can use the retained
ligand-receptor-output evidence as route-plausibility input while applying its
own confidence logic and treating the missing intracellular and TF layers as
uncertainty rather than as absent biology.
