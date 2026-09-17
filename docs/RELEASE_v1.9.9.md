# mSCIdblit mechanism graph release v1.9.9

Release date: 2026-09-17

This release adds the 104th selective primary-literature expansion batch for
Module 21B downstream curation. The evidence overlay adds ten receptor-
proximal route annotations for mSCS plausibility analysis. Nine routes cover
previously unexpanded queue candidates; one strengthens the existing CSF1–
CSF1R–PI3K annotation by adding the explicit receptor-to-PI3K edge.

The batch includes CSF1–CSF1R–PI3K p85/p110; HBD3–CXCR4–GNAI/O/Z;
B7-H6–NKp30–CD3ζ; MICB–NKG2D–DAP10; ULBP1–NKG2D–DAP10;
SIGLEC4/MAG–4-1BB–TRAF1; ATRA–MRGPRX2–GNAQ/GNA11;
LPC–GPR119–GNAS; Teneurin-2–ADGRL3–GNAS; and FLRT3–ADGRL3–GNAS.
Primary locators retained in the bundle include PMID:10958675, PMID:16818731,
PMID:23659571, PMID:19528259, PMID:11239445, PMID:11777960,
PMID:38354234, PMID:31006867, PMID:35970999, PMID:24273166, and
PMID:22405201, together with the associated PMCID and DOI locators.

All ten routes are classified as
`ligand_receptor_intracellular_output_missing_tf`: they retain a ligand,
receptor, receptor-proximal intracellular continuation, and bounded output,
while leaving TF and terminal target-gene fields empty. Effects include
activating, inhibitory, and unknown annotations where supported by the
underlying evidence. All routes remain non-causal evidence routes with
`evidence_route_not_causal` traversal status. No graph edges, causal edges, or
database confidence scores are created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,821
- Cumulative literature-expansion route rows: 774
- Unique downstream queue candidates with literature coverage: 750
- Remaining downstream queue candidates: 2,581
- Remaining P1 candidates: 1,536

The release is an evidence-layer update only. mSCS can use the retained
receptor, intracellular, and output evidence as route-plausibility inputs while
applying its own confidence logic.
