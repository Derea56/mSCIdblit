# mSCIdblit release v1.9.271

This release materializes the next all-ligand full-intermediate curation pass.
It restores the literature-expansion mapping carried by the prior route layer
and adds 98 source-linked, primary-locator-backed composed routes across IL1A,
IL17B, VIP, and WNT3A. The routes retain ligand, receptor, intracellular
continuation, TF, and target-gene layers while keeping unsupported handoffs
explicitly unresolved.

Graph identifier: `module20_24_mechanism_graph:2026-09-24-all-ligand-full-intermediate-promotion-402`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion402/`

The release contains 7,483 literature-expansion annotations: 7,385 carried
forward and 98 added in this pass. These are evidence-layer compositions only;
they do not create graph edges, causal assertions, or database confidence
scores. The 98 additions use exact same-ligand/same-receptor source-linked
components and preserve missing receptor-to-relay, relay-to-TF, and TF-to-target
links rather than inferring them.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 573,597
- Route nodes: 2,394,517
- Route edges: 2,217,068
- Full-sequence curation queue: 15,302
- Literature-expansion annotations: 7,483

The regenerated all-ligand queue contains 9,280 P1 candidates, 12,411 routes
with an intracellular continuation layer, and 9,654 with a transcription-factor
layer. Validation passed with no errors; the retained warning concerns evidence
sources without stable public locators.
