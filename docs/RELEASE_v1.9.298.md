# mSCIdblit release v1.9.298

This release adds one primary-literature evidence route for CSF1 signaling
through the existing CSF1R/c-Fms and MEK/ERK layers to Elk-1-associated c-Fos
transcription. The route preserves the intracellular continuation and
transcription-factor layers while keeping unresolved handoffs explicit for
mSCS route-plausibility evaluation.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-csf1-erk-elk1-483`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion483/`

The route retains PMID:15812575, PMID:10958675, and PMID:9514945, with
`causal_status=not_asserted` and `traversal_status=evidence_route_not_causal`.
The CSF1→CSF1R/c-Fms and CSF1R/c-Fms→MEK/ERK layers are linked to existing
graph evidence; the ERK-to-Elk-1 and Elk-1-to-c-Fos handoffs remain
unasserted. No graph edges or database confidence scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,245
- Route nodes: 2,463,962
- Route edges: 2,271,895
- Full-sequence curation queue: 15,419
- Literature-expansion annotations: 22,131
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors, and all compressed route artifacts
passed gzip integrity checks. The remaining warning concerns legacy evidence
sources without stable locators and is unchanged from prior releases.
