# mSCIdblit release v1.9.149

## Primary-evidence harvest from public ligand-receptor comparisons

This release resolves the 25 highest-priority public-only ligand-receptor rows
against the current mSCIdblit graph and the primary literature. It adds three
new graph edges:

- GRP → NMBR, a primary mouse functional itch-circuit branch with behavioral
  and electrophysiological output. The evidence preserves that this branch is
  weaker than GRP → GRPR and does not assert an intracellular, TF, or target-
  gene layer.
- PTN → SDC1, a primary mouse biochemical glycosaminoglycan-binding layer.
- PTN → SDC4, a primary mouse biochemical glycosaminoglycan-binding layer.

The other public rows are retained as explicit dispositions rather than
duplicated edges. They resolve to mature ligand forms, aliases, processed
complement fragments, species-corrected receptor forms, existing noncanonical
interactions, reverse adhesion orientation, family-level evidence, or
unresolved boundaries. PTN → SDC2 remains conditional because the located
primary evidence is Y-P30-enhanced binding rather than native PTN-alone
binding. C4b → CR2 remains unresolved for the free-ligand edge.

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion243/`.
It contains 11,952 nodes, 14,725 graph edges, and 20,216 route-evidence
records. The route-evidence layer remains non-causal and evidence-only; no
mSCS confidence scores are created.

The row-level harvest is documented in
`docs/PRIMARY_EVIDENCE_HARVEST_TOP25_v1.9.149.md` and
`data/processed/public_database_comparison_v2/primary_evidence_harvest_resolution.tsv`.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion243
```
