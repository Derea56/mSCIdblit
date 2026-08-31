# Public TF mechanism evidence layer — 2026-08-30

This layer carries the reviewed public-TF relationships alongside the
Module 20B–24B mechanism graph without treating every catalog association as
a traversable mechanism edge.

## Layer contents

The generated bundle is
`data/processed/public_tf_mechanism_layer_v2026_08_30/`.

| Artifact | Meaning |
|---|---|
| `public_tf_candidate_layer.tsv` | All reviewed public-TF module-screening rows, including A/B/C/D/E evidence, L0–L4 context, role class, module route, provenance, and limitations. |
| `public_tf_validated_edge_layer.tsv` | Rows that passed the explicit validated-edge gate and received manual literature adjudication. |
| `layer_metadata.json` | Counts, policy, and gate definition. |

The layer is additive and does not modify canonical database tables. Candidate
rows remain queryable even when their traversal status is
`not_traversable`. Evidence tier (A–E) and context level (L0–L4) remain
independent fields.

## Validated-edge gate

A public-TF row can enter the validated-edge subset only when all of the
following are present:

- A- or B-tier reviewed evidence;
- an exportable source and explicit module assignment;
- `canonical_role_status=canonical_tf`;
- `mechanism_evidence_type=direct_sequence_specific_tf_binding`;
- exact-pair context scope; and
- an explicit literature adjudication with citations and limitations.

The current adjudicated subset contains three module rows representing two
unique mouse TF-target relationships:

| Regulator | Target | Modules | Relation | Context boundary |
|---|---|---|---|---|
| MSGN1 | Dll3 | 20B | induces target gene | L1, presomitic mesoderm; not SCI |
| OVOL2 | Cdh2 | 20B, 23B | represses target gene | L1, mammary-cell model; not SCI |

The MSGN1/Dll3 decision is supported by the primary developmental study's
Msgn1 occupancy and reporter/perturbation evidence
([primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3622708/)). The
OVOL2/Cdh2 decision is supported by primary mouse ChIP-seq, ChIP validation,
and deletion-expression evidence
([primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4062651/)). These
are validated general mouse mechanisms, not claims of spinal-cord or SCI
activity.

All other relationships remain in the candidate layer until they receive the
same explicit adjudication. D/E, unresolved, noncanonical, catalog-only, and
component-context-only rows remain available for screening but are not
traversable mechanism edges.

Build or rebuild the layer with:

```bash
python3 scripts/build_public_tf_mechanism_layer.py
```

The builder is deterministic, preserves the source and screening fields, and
does not perform database writes or alter the existing mechanism graph.

## Graph-release candidate

The corresponding combined graph candidate is
`data/processed/mechanism_graph_module20_24_v2026_08_30/`. It copies the
validated `2026-08-26` Module 20B–24B graph and adds only the three explicitly
adjudicated public-TF module rows. The candidate validates with zero errors and
contains:

- 2,786 nodes;
- 3,154 traversable edges;
- 4,487 evidence-source rows;
- 4,339 role assignments; and
- 947 pathway summaries.

The three added rows are `Msgn1 → Dll3` in 20B and `Ovol2 ┤ Cdh2` in 20B and
23B. They are general mouse mechanisms with L1 exact-pair context, not SCI
claims. The full candidate layer remains beside the graph, and all other
public-TF rows remain non-traversable until individually adjudicated.

The candidate is intentionally dated rather than assigned a new semantic
project version. The root `VERSION` file and the frozen `1.0.0` tag remain
unchanged.
