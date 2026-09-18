# mSCIdblit mechanism graph release v1.9.10

Release date: 2026-09-17

This release adds the 105th selective primary-literature expansion batch for
Module 21B downstream curation. The evidence overlay adds ten source-linked
route annotations across four previously unexpanded P1 receptor-proximal
queue candidates: CD300B/LMIR5, SIGLEC14, SIGLEC15, and TREM2 routes that
continue through DAP12/TYROBP.

The batch retains PtdSer-CD300B-DAP12 efferocytosis evidence; HSP70-,
cardiolipin-, and vimentin-SIGLEC14-DAP12 paired-receptor evidence; CD44 and
CD11b glycoform-SIGLEC15-DAP12 evidence; and APOE-, PtdSer-, C1q-, and
S1P-TREM2-DAP12 evidence with the independently supported DAP12-DOK3
macrophage output layer. Primary locators retained in the bundle include
PMID:25034781, PMID:17012248, PMID:24446437, PMID:26459514, PMID:31551352,
PMID:31805552, PMID:28899088, PMID:37311743, PMID:26374897, PMID:31101881,
PMID:37442133, PMID:35847502, and the associated PMCID and DOI locators.

All ten routes are classified as
`ligand_receptor_intracellular_output_missing_tf`: they retain a ligand,
receptor, DAP12/TYROBP continuation, and bounded output while leaving TF and
terminal target-gene fields empty. The SIGLEC15 glycoform routes remain
unknown-polarity because the primary signaling study used receptor clustering;
the APOE-TREM2 route remains unknown-polarity because its ligand study is
binding-focused. All routes remain non-causal evidence routes with
`evidence_route_not_causal` traversal status. No graph edges, causal edges, or
database confidence scores are created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,831
- Cumulative literature-expansion route rows: 784
- Unique downstream queue candidates with literature-expansion coverage: 754
- Remaining downstream queue candidates: 2,577
- Remaining P1 candidates: 1,532

The release is an evidence-layer update only. mSCS can use the retained
ligand, receptor, intracellular, and output evidence as route-plausibility
inputs while applying its own confidence logic and context filters.
