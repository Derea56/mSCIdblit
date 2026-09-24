# mSCIdblit release v1.9.283

This release adds four primary-literature evidence routes across three ligand
labels: HGF, CXCL12, and WNT5A. The additions extend the all-ligand route layer
with HGF→MET→STAT3→TWIST1 expression, CXCL12→CXCR4→PLCβ3/Ras–ERK→AP-1→IL10
transcription, CXCL12→CXCR4→NOS2 transcriptional output with unresolved
intracellular and TF layers, and WNT5A→ROR2→JNK→JUN/ATF2→MMP13 output with
the terminal target-gene node left unresolved.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-gap-full-sequences-435`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion435/`

All four rows retain primary locators, explicit limitations,
`causal_status=not_asserted`, and `traversal_status=evidence_route_not_causal`.
No graph edges or database confidence scores were created. The WNT5A MMP13
row remains an output route because the current graph does not contain a clean
MMP13 target-gene node; the CXCL12 NOS2 row similarly preserves the missing
intracellular and TF layers rather than inferring them.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,201
- Route nodes: 2,463,754
- Route edges: 2,271,731
- Full-sequence curation queue: 15,392
- Literature-expansion annotations: 22,087
- Unique ligand candidates in queue: 1,862

The graph validator passed with no errors. The remaining warning concerns
legacy evidence sources without stable locators and is unchanged from the
previous release.
