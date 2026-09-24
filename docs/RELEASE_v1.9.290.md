# mSCIdblit release v1.9.290

This release adds one primary-literature evidence route for IL-34→CSF1R→
MEK/ERK/JNK→AP-1→c-FOS expression. The route is based on IL-34 stimulation,
CSF1R dependence, kinase-phosphorylation measurements, and c-Fos/c-Jun
promoter and AP-1 transactivation assays in mouse epidermal and human breast-
cancer cell models.

Graph identifier:
`module20_24_mechanism_graph:2026-09-24-il34-ap1-gap-459`

Bundle:
`data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion459/`

The route retains PMID:33800170, `causal_status=not_asserted`, and
`traversal_status=evidence_route_not_causal`. CSF1R-to-relay, relay-to-AP-1,
and AP-1-to-c-FOS handoffs remain explicitly unasserted; no graph edges or
database confidence scores were created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 588,223
- Route nodes: 2,463,853
- Route edges: 2,271,808
- Full-sequence curation queue: 15,414
- Literature-expansion annotations: 22,109
- Unique ligand candidates in queue: 1,862
- Unique receptor candidates in queue: 1,633

The graph validator passed with no errors. The remaining warning concerns
legacy evidence sources without stable locators and is unchanged from prior
releases.
