# mSCIdblit mechanism graph release v1.9.12

Release date: 2026-09-17

This release adds the 107th selective primary-literature expansion batch for
Module 21B downstream curation. The evidence overlay adds ten source-linked
ligand-receptor-output annotations for previously unexpanded P1 candidates,
focused on semaphorin receptor and holoreceptor contexts. These routes retain
the ligand and receptor input plus a bounded functional or activation readout
while leaving intracellular continuation and TF layers unresolved.

The batch covers SEMA3C-PLXNB1 RTK activation and growth; SEMA3C-NRP1:PlexinD1
endothelial and angiogenesis output; SEMA7A-PLXNC1 receptor-binding evidence;
SEMA7A-beta1-integrin spreading and axon-outgrowth output; SEMA4D-PLXNB2
neurite-outgrowth modulation; SEMA3G-NRP2:PlexinD1 lymphatic patterning;
SEMA3G-NRP2:PlexinA4 Rac1 and synaptic output; SEMA3F-NRP2:PLXNA3 CNS
functional output; SEMA3F-NRP2:PLXNA1 cytoskeletal and migration output; and
SEMA3E-PLXND1:NRP1:VEGFR2 phosphorylation and axonal-growth output. Primary
locators retained in the bundle include PMID:10520995, PMID:15330859,
PMID:17671519, PMID:12879062, PMID:18660502, PMID:20010807,
PMID:23063687, PMID:11683995, PMID:20434998, PMID:26194913,
PMID:27880905, PMID:30685224, PMCID:PMC2936782, PMCID:PMC2555994,
PMCID:PMC5801490, and the associated DOI locator.

All ten routes are classified as
`ligand_receptor_output_annotation_missing_intracellular_and_tf`: they retain
an exact ligand-receptor edge and source-linked output evidence, but do not
assign a receptor-proximal intracellular continuation or terminal TF. The
complex-level records preserve holoreceptor topology and do not collapse
ligand-binding and signal-transducing components into an unsupported binary
claim. All routes remain non-causal evidence routes with
`evidence_route_not_causal` traversal status. No graph edges, causal edges, or
database confidence scores are created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,851
- Cumulative literature-expansion route rows: 804
- Unique downstream queue candidates with literature-expansion coverage: 774
- Remaining downstream queue candidates: 2,557
- Remaining P1 candidates: 1,512

The release is an evidence-layer update only. mSCS can use the retained
ligand-receptor-output evidence as route-plausibility input while applying its
own confidence logic and treating the missing intracellular and TF layers as
uncertainty rather than as absent biology.
