# mSCIdblit release v1.9.275

This release begins the next all-ligand primary-literature tranche. It adds
four bounded evidence routes for FGF2, LPA, VEGFA, and norepinephrine, while
preserving unresolved handoffs instead of inferring a complete chain from a
ligand–receptor pair.

Graph identifier: `module20_24_mechanism_graph:2026-09-24-next-all-ligand-primary-routes-415`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion415/`

The release contains 12,925 literature-expansion annotations, including 6,308
`ligand>receptor>intracellular>TF>target_gene_expression` records. The new
routes include one full molecular sequence for FGF2→FGFR1→ERK/JNK→EGR1→GDNF,
plus partial routes with explicit missing TF or target-gene layers for LPA,
VEGFA, and norepinephrine. All annotations remain evidence-only
(`causal_status=not_asserted`, `traversal_status=evidence_route_not_causal`);
no graph edges, causal assertions, or database confidence scores are created.

Bundle counts:

- Nodes: 11,988
- Graph edges: 14,831
- Edge-source records: 15,107
- Signaling-route evidence rows: 579,039
- Route nodes: 2,421,410
- Route edges: 2,238,535
- Full-sequence curation queue: 15,316
- Literature-expansion annotations: 12,925

Validation passed with no errors. The retained warning concerns evidence
sources without stable public locators. The queue still requires broader
paper-level review across the remaining ligands.
