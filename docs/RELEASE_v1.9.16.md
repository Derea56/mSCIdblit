# mSCIdblit mechanism graph release v1.9.16

Release date: 2026-09-17

This release adds the 111th selective primary-literature expansion batch for
Module 21B downstream curation. The evidence overlay adds ten previously
unexpanded ligand-receptor routes with receptor-specific outputs while keeping
their unresolved intracellular and transcription-factor layers explicit.

The batch covers DDT/MIF-2-CD74:CD44 ERK1/2 activation; netrin-4-alpha6beta1
endothelial responses; SP-D-EGFR regulation; IL-20 and IL-24 signaling through
the IL20RA:IL20RB and IL22RA1:IL20RB receptor complexes; IL-25-
IL17RA:IL17RB receptor-complex signaling; Jagged2-Notch2 processing; and
ATP-P2X4 channel activation. Primary locators are retained for
PMID:21817065/PMCID:PMC3161582, PMID:21799154/PMCID:PMC3552560,
PMID:24608429, PMID:22802649/PMCID:PMC3412030, PMID:12351624,
PMID:17083366, PMCID:PMC9477748, PMID:10958687/PMCID:PMC88767, and
PMID:8622997/PMCID:PMC39672.

All ten routes are classified as
`ligand_receptor_output_annotation_missing_intracellular_and_tf`: they retain
exact ligand-receptor evidence and observed receptor or cellular outputs while
leaving graph-linked intracellular and TF layers unresolved. The Jagged2-Notch2
record preserves cleavage, nuclear-translocation, hyperphosphorylation and
RBP-Jkappa reporter observations as output evidence without asserting a
terminal TF route. All ten routes remain non-causal evidence routes. No graph
edges, causal edges, or database confidence scores are created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,891
- Cumulative literature-expansion route rows: 844
- Unique downstream queue candidates covered by the expansion inputs: 814
- Remaining downstream queue candidates: 2,517
- Remaining P1 candidates: 1,472

The release is an evidence-layer update only. mSCS can use the retained
ligand-receptor and output evidence for route-plausibility analysis while
applying its own confidence logic and treating unresolved layers as uncertainty
rather than as absent biology.
