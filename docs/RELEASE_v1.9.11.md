# mSCIdblit mechanism graph release v1.9.11

Release date: 2026-09-17

This release adds the 106th selective primary-literature expansion batch for
Module 21B downstream curation. The evidence overlay adds ten source-linked
ligand-receptor-output annotations for previously unexpanded P1 candidates.
These routes deliberately retain the ligand and receptor input plus a bounded
functional or activation readout while leaving intracellular continuation and
TF layers unresolved.

The batch covers PDGFB-PDGFRB-associated SHP2/FAK and migration output;
netrin-1-DCC-associated RhoGTPase and growth-cone output; CCL24-CCR3
chemotaxis and fibroblast activation; vitronectin- and fibronectin-alphaVbeta3
adhesion; laminin-511-alpha3beta1 mast-cell adhesion and migration;
midkine-PTPRZ1 neuronal migration; FGF19-beta-Klotho-FGFR1c phosphorylation
and metabolic output; ephrin-B1-EPHB1 activation; and PF4-Mac-1 leukocyte
adhesion, migration, and phagocytosis. Primary locators retained in the
bundle include PMID:7691811, PMID:10318871, PMID:15788770, PMID:40955564,
PMID:23532518, PMID:9480902, PMID:1703545, PMID:19752234, PMID:10212223,
PMID:17623664, PMID:7973638, and PMID:29540475, together with the associated
PMCID and DOI locators.

All ten routes are classified as
`ligand_receptor_output_annotation_missing_intracellular_and_tf`: they retain
an exact ligand-receptor edge and source-linked output evidence, but do not
assign a receptor-proximal intracellular continuation or terminal TF. All
routes remain non-causal evidence routes with `evidence_route_not_causal`
traversal status. No graph edges, causal edges, or database confidence scores
are created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,841
- Cumulative literature-expansion route rows: 794
- Unique downstream queue candidates with literature-expansion coverage: 764
- Remaining downstream queue candidates: 2,567
- Remaining P1 candidates: 1,522

The release is an evidence-layer update only. mSCS can use the retained
ligand-receptor-output evidence as route-plausibility input while applying its
own confidence logic and treating the missing intracellular and TF layers as
uncertainty rather than as absent biology.
