# mSCIdblit release v1.9.285

This release adds four primary-literature evidence routes across four ligand
labels: GDNF, FGF2, surfactant protein D, and ANGPTL2. The additions extend the
all-ligand route layer with GDNF→RET→Ras/ERK→CREB→cFos expression,
FGF2→FGFR1→ERK→JunD→uPA output, SFTPD→TLR4/MD-2→NF-κB attenuation→TNF/cytokine
output, and ANGPTL2→α5β1 integrin→MAPK/Akt/NF-κB→inflammatory-gene output.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-continuation-gap-441`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion441/`

All four rows retain primary locators, explicit limitations,
`causal_status=not_asserted`, and `traversal_status=evidence_route_not_causal`.
No graph edges or database confidence scores were created. FGF2, SFTPD, and
ANGPTL2 remain functional-output routes because the current graph does not
provide one clean terminal target-gene node for the source-supported output
sets. The SFTPD route preserves inhibitory polarity.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,209
- Route nodes: 2,463,789
- Route edges: 2,271,758
- Full-sequence curation queue: 15,400
- Literature-expansion annotations: 22,095
- Unique ligand candidates in queue: 1,862

The graph validator passed with no errors. The remaining warning concerns
legacy evidence sources without stable locators and is unchanged from the
previous release.
