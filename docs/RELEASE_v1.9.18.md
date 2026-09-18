# mSCIdblit mechanism graph release v1.9.18

Release date: 2026-09-17

This release adds the 113th selective primary-literature expansion batch for
Module 21B downstream curation. The evidence overlay adds ten previously
unexpanded ligand-receptor routes with receptor-specific adhesion, tethering,
rolling, secretion, or receptor-proximal signaling outputs while keeping
intracellular and transcription-factor layers explicit.

The batch covers GlyCAM1-L-selectin beta2-integrin activation; nepmucin-
L-selectin rolling and shear-resistant adhesion; underglycosylated MUC1-
E-selectin rolling and MUC1-P-selectin tethering; CD24-E-selectin rolling;
cell-surface nucleolin-P-selectin phosphorylation/PI3K-p38 signaling; L1CAM-
E-selectin adhesion; LAMP1-E-selectin adhesion; and CEACAM5/CEA interactions
with E-selectin and L-selectin. Primary locators are retained for
PMID:7679207, PMID:9422729, PMID:8879206, PMID:16754720, PMID:23805168,
PMID:22866263, PMID:21207944/PMCID:PMC3059340, PMID:18504038/PMCID:PMC2504360,
PMID:33167483/PMCID:PMC7672641, PMID:10639580, PMID:7685349, and
PMID:18375392.

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
- Signaling route-evidence rows: 16,911
- Cumulative literature-expansion route rows: 864
- Unique downstream queue candidates covered by the expansion inputs: 834
- Remaining downstream queue candidates: 2,497
- Remaining P1 candidates: 1,452

The release is an evidence-layer update only. mSCS can use the retained
ligand-receptor and output evidence for route-plausibility analysis while
applying its own confidence logic and treating unresolved layers as uncertainty
rather than as absent biology.
