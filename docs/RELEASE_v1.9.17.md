# mSCIdblit mechanism graph release v1.9.17

Release date: 2026-09-17

This release adds the 112th selective primary-literature expansion batch for
Module 21B downstream curation. The evidence overlay adds ten previously
unexpanded ligand-receptor routes with receptor-specific adhesion or cellular
outputs while keeping intracellular and transcription-factor layers explicit.

The batch covers neuroligin-1-beta-neurexin-1 trans-synaptic adhesion;
P-selectin-PSGL1 binding and leukocyte rolling; E-selectin interactions with
CD44/HCELL, ESL1/GLG1 and glycoform-dependent CD43; endoglycan-P-selectin
rolling; HEV-glycoform CD34-L-selectin adhesion; and MUC16-E-selectin,
MUC16-L-selectin and PODXL-E-selectin tumor-cell adhesion. Primary locators
are retained for PMID:18093521/PMCID:PMC2703725, PMID:9829984,
PMID:7532174, PMID:11402070, PMID:17442598, PMID:7531823,
PMID:16339541, PMID:18714037, PMID:18606703/PMCID:PMC2700822,
PMID:7692600, PMID:7559783, PMID:22159147/PMCID:PMC3289508, and
PMCID:PMC3468350.

All ten routes are classified as
`ligand_receptor_output_annotation_missing_intracellular_and_tf`: they retain
exact ligand-receptor evidence and observed adhesion or cellular outputs while
leaving graph-linked intracellular and TF layers unresolved. All ten routes
remain non-causal evidence routes. No graph edges, causal edges, or database
confidence scores are created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,901
- Cumulative literature-expansion route rows: 854
- Unique downstream queue candidates covered by the expansion inputs: 824
- Remaining downstream queue candidates: 2,507
- Remaining P1 candidates: 1,462

The release is an evidence-layer update only. mSCS can use the retained
ligand-receptor and output evidence for route-plausibility analysis while
applying its own confidence logic and treating unresolved layers as uncertainty
rather than as absent biology.
