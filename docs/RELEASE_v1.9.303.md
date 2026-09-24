# mSCIdblit release v1.9.303

This release adds two primary-literature evidence routes for IL-18 signaling
through IL18R1/IL18RAP, MyD88 and NF-kB-associated signaling to distinct IFN-
gamma protein and IFNG-transcription outputs in IL-12-stimulated natural killer
cells. The routes preserve intracellular and output layers while keeping
unresolved handoffs explicit for mSCS route-plausibility evaluation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-il18-myd88-498`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion498/`

The routes retain PMID:10229825 with `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. The IL-18 receptor and receptor-
to-MyD88 layers are linked to existing graph evidence; intracellular-to-NF-kB
and NF-kB-to-output handoffs remain unasserted. Protein and transcriptional
outputs remain separate. No graph edges or database confidence scores were
created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,261
- Route nodes: 2,464,042
- Route edges: 2,271,961
- Full-sequence curation queue: 15,423
- Literature-expansion annotations: 22,147
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors, and all compressed route artifacts
passed gzip integrity checks. The remaining warning concerns legacy evidence
sources without stable locators and is unchanged from prior releases.
