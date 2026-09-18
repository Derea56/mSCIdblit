# mSCIdblit mechanism graph release v1.9.14

Release date: 2026-09-17

This release adds the 109th selective primary-literature expansion batch for
Module 21B downstream curation. The evidence overlay adds ten source-linked
ligand-receptor-output annotations for previously unexpanded P1 candidates.
These routes retain bounded binding, activation, trafficking, adhesion,
transcriptional, or cellular readouts while leaving intracellular
continuation and terminal TF layers unresolved.

The batch covers collagen-I GFOGER recognition by alpha1beta1 and alpha2beta1;
CCL25-ACKR4 chemokine scavenging and beta-arrestin recruitment; ANGPT2-
alpha5beta1 endothelial function; FGF19-beta-Klotho complexes with FGFR2c and
FGFR3c; SEMA7A-alpha1beta1 immune-inflammatory function; MIF-CD74:CD44 ERK
signaling; IL-19-IL20RA:IL20RB receptor-complex output; and SLIT3-ROBO4
endothelial angiogenic function. Primary locators retained in the bundle
include PMID:10617582, PMID:32391018, PMID:16791897, PMID:25635707,
PMID:17623664, PMID:17377534, PMID:12782713, PMID:17045821, PMID:12351624,
PMID:17083366, and PMID:19741192, together with the associated PMCID and DOI
locators.

All ten routes are classified as
`ligand_receptor_output_annotation_missing_intracellular_and_tf`: they retain
an exact ligand-receptor edge and source-linked output evidence, but do not
assign a receptor-proximal intracellular continuation or terminal TF. The
ACKR4 record preserves its atypical-scavenging boundary and reported lack of
Erk1/2, Akt, or Src activation. The FGF19 records preserve beta-Klotho and
FGFR-isoform requirements, and the MIF record preserves CD74 as the
ligand-binding component and CD44 as the signaling component. All routes
remain non-causal evidence routes with `evidence_route_not_causal` traversal
status. No graph edges, causal edges, or database confidence scores are
created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,871
- Cumulative literature-expansion route rows: 824
- Unique downstream queue candidates with literature-expansion coverage: 794
- Remaining downstream queue candidates: 2,537
- Remaining P1 candidates: 1,492

The release is an evidence-layer update only. mSCS can use the retained
ligand-receptor-output evidence as route-plausibility input while applying its
own confidence logic and treating the missing intracellular and TF layers as
uncertainty rather than as absent biology.
