# mSCIdblit v1.1.0 mechanism-graph release

This release extends the frozen v1.0.0 graph with an explicit public-TF
evidence layer and the small subset of public-TF relationships that passed the
validated mechanism-edge gate.

## Release identity

- Project version: `mSCIdblit v1.1.0`
- Mechanism graph version: `v1.1.0`
- Graph release identifier: `module20_24_mechanism_graph:v1.1.0`
- Release date: `2026-08-30`
- Prior frozen release: `mSCIdblit-v1.0.0`

## Graph contents

The released bundle is
`data/processed/mechanism_graph_module20_24_v2026_08_30/` and passed the
deterministic graph validator with zero errors.

| Measure | Count |
|---|---:|
| Nodes | 2,786 |
| Traversable edges | 3,154 |
| Evidence-source rows | 4,487 |
| Role assignments | 4,339 |
| Pathway summaries | 947 |
| Non-exportable boundaries | 9,825 |
| Public-TF candidate rows retained as an evidence layer | 4,174 |

The public-TF layer retains all evidence tiers A/B/C/D/E and context levels
L0–L4. Only three module rows, representing two unique general mouse
relationships, were added as traversable edges:

- `Msgn1 → Dll3` in Module 20B;
- `Ovol2 ┤ Cdh2` in Module 20B; and
- `Ovol2 ┤ Cdh2` in Module 23B.

These are general mouse mechanisms with L1 exact-pair context. They are not
claims of spinal-cord or SCI activity. The primary evidence is documented in
the [MSGN1/Dll3 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3622708/)
and the [OVOL2/Cdh2 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4062651/).

All remaining public-TF rows are retained for audit and future review but are
not traversable edges. D/E, unresolved, noncanonical, catalog-only, and
component-context-only rows remain explicitly gated out.

## Scope boundary

The release does not modify the frozen v1.0.0 bundle. It does not perform new
database writes. Future public-TF promotion work should begin from a fresh
branch and use the retained candidate layer plus explicit adjudications.
