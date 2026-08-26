# Module 20B/21B/23B/24B canonical materialization — 2026-08-26

The reviewed B-module promotion staging was written to the local canonical
PostgreSQL database `mscidblit_local` after the pre-write backup and release
gates passed.

## Write result

| Measure | Before | After | Change |
|---|---:|---:|---:|
| Canonical `SignalingEntity` rows | 2,792 | 2,792 | 0 |
| Canonical `SignalingEdge` rows | 3,172 | 3,172 | 0 |
| `SignalingEdgeRegister` rows | 3,172 | 3,172 | 0 |
| `SignalingEdgeRegisterSource` rows | 4,398 | 4,505 | +107 |

The write upgraded 107 valid staged B-module candidates and materialized their
reviewed register-level provenance:

| Module | Written candidates | Promotion sources |
|---|---:|---:|
| 20B | 44 | 44 |
| 21B | 6 | 6 |
| 23B | 34 | 34 |
| 24B | 23 | 23 |

One staged candidate, `M24B-E000087` (`FLRT3 → FLRT3`), was intentionally not
written because canonical graph constraints prohibit self-loops. It remains
available in the staging ledger.

Canonical role validation and the database release gate both passed with zero
issues. Raw noncanonical staging labels for species/scope/confidence were
normalized into bounded canonical fields where necessary and retained in
register-source notes; no Paper, Observation, or AuthorClaim foreign keys were
fabricated.

The public TF/22B ledger remains separate staging and was not inserted by this
write; its canonical entity/role gate is a distinct decision.

## Outputs

- [register-backed graph bundle](/Users/derea/Documents/SCI/mSCIdblit/data/processed/mechanism_graph_module20_24_v2026_08_26/)
- [canonical database bundle](/Users/derea/Documents/SCI/mSCIdblit/data/processed/mechanism_bundle_module20_24_db_v2026_08_26/)
- [materialization script](/Users/derea/Documents/SCI/mSCIdblit/scripts/materialize_module20_24_b_promotions.py)
- [pre-write PostgreSQL backup](/private/tmp/mscidblit_canonical_prewrite_20260826.dump)

The canonical export contains 2,792 nodes, 4,358 node roles, 3,172 edges, and
4,505 edge-source records.
