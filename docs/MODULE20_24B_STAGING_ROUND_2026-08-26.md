# Module 20B/21B/23B/24B staging round — 2026-08-26

The remaining B-module material is assembled as an audit-only staging pack.
No canonical `Paper`, `Observation`, `AuthorClaim`, `SignalingEdge`, or
`SignalingEdgeSource` rows were written, and the frozen Module 20–24 releases
were not modified.

This is the pre-write staging record. The subsequent canonical write is
documented in
[MODULE20_24B_CANONICAL_MATERIALIZATION_2026-08-26.md](/Users/derea/Documents/SCI/mSCIdblit/docs/MODULE20_24B_CANONICAL_MATERIALIZATION_2026-08-26.md).

## Staged coverage

| Module | B edges | B evidence | boundaries | high B edges | new high candidates | linked candidate evidence | source-format repairs |
|---|---:|---:|---:|---:|---:|---:|---:|
| 20B | 5,906 | 7,630 | 4,796 | 143 | 44 | 108 | 20 |
| 21B | 111 | 60 | 0 | 85 | 6 | 12 | 4 |
| 23B | 1,075 | 1,501 | 289 | 313 | 34 | 104 | 33 |
| 24B | 151 | 224 | 31 | 85 | 24 | 49 | 19 |

The staging pack contains 108 new high-confidence edge candidates in total:
44 for 20B, 6 for 21B, 34 for 23B, and 24 for 24B. Every candidate is
exportable, has a matching high-tier promotion-evidence record, and retains
the original module-specific evidence layer and limitations.

The 20B, 21B, 23B, and 24B source edge registers initially had 76 detached
carriage-return annotations. They were repaired in the normalized staging
copies for the write, and the same formatting-only cleanup was then applied to
the tracked source registers before commit; no data fields or IDs changed.

## Materialization boundary

Each candidate is marked `staged_high_confidence_pending_canonical_review` with
`canonical_entity_role_gate=pending`. The next decision is therefore whether
to run the canonical entity/role and source-anchor gates, not whether the
literature promotion itself occurred. Module 22B remains in its existing
public-TF staging ledger and was not duplicated here.

## Files

- [staging manifest](/Users/derea/Documents/SCI/mSCIdblit/work/module_b_consolidation/staging_round_2026_08_26/staging_manifest.json)
- [module summary](/Users/derea/Documents/SCI/mSCIdblit/work/module_b_consolidation/staging_round_2026_08_26/module_summary.tsv)
- [all promoted edge candidates](/Users/derea/Documents/SCI/mSCIdblit/work/module_b_consolidation/staging_round_2026_08_26/all_promoted_edge_candidates.tsv)
- [all linked evidence candidates](/Users/derea/Documents/SCI/mSCIdblit/work/module_b_consolidation/staging_round_2026_08_26/all_promoted_evidence_candidates.tsv)
- [isolated staging SQL](/Users/derea/Documents/SCI/mSCIdblit/work/module_b_consolidation/staging_round_2026_08_26/module20_24b_staging_round.sql)
- [builder and validator](/Users/derea/Documents/SCI/mSCIdblit/scripts/build_module20_24_b_staging_round.py)

The staging TSVs passed structural, ID, evidence-link, locator, tier, and
promotion-PMID checks. A disposable sandbox PostgreSQL startup test was blocked
by shared-memory permissions, but the canonical local PostgreSQL materialization
completed successfully and passed the role/release gates.
