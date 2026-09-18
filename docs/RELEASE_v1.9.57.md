# mSCIdblit v1.9.57

This release completes the remaining 500 P1 Module 21B downstream curation
entries. The evidence layer retains 236 receptor-like ligand/output routes,
257 topology-unresolved relations, six receptor-proximal non-ligand–receptor
continuations, and one ligand–receptor entry with no downstream output
annotation.

The batch closes the P1 queue without collapsing these evidence classes into a
single confidence score. Canonical or receptor-like output routes remain
usable as plausible evidence-layer routes; ambiguous topology remains marked
for manual pair resolution; receptor-proximal records retain the missing
upstream ligand–receptor layer; and the entry-only record retains its missing
output layer. Intracellular, TF, target-gene, causal and confidence fields are
not inferred.

- Route evidence: 17,876 → 18,376 records
- Graph topology: 11,952 nodes and 14,722 edges, unchanged
- Downstream queue candidates covered: 1,799 → 2,299
- Remaining downstream queue candidates: 1,032
- Remaining P1 candidates: 0
- Added route tiers: 236 L→R→O; 257 topology-unresolved; 6 receptor-proximal; 1 entry-only

The corresponding bundle is
`mechanism_graph_module20_24_v2026_09_16_literature_expansion152`.
