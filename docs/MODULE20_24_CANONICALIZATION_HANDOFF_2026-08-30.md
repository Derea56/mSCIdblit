# Module 20B–24B canonicalization handoff — 2026-08-30

## Current checkpoint

The existing high-confidence promotion pack was applied to the local
canonical PostgreSQL database `mscidblit_local` through the Unix socket
`/private/tmp/mscidblit_pg_socket`.

- Input: `work/module_b_consolidation/staging_round_2026_08_26/`
- Promotion rows: 108
- Non-self-loop canonical register updates: 107
- Intentional self-loop boundary rows skipped: 1
- Promotion-specific evidence rows in staging: 108
- Linked register provenance rows confirmed after the write: 271
- New register-source rows inserted: 0; the provenance rows were already
  present and were preserved without duplication

The exact candidate and evidence rows remain in:

- `work/module_b_consolidation/staging_round_2026_08_26/all_promoted_edge_candidates.tsv`
- `work/module_b_consolidation/staging_round_2026_08_26/all_promoted_evidence_candidates.tsv`

Post-write database counts for the affected register modules are:

| Module | Register edges | High-tier edges |
|---|---:|---:|
| 20B | 1,108 | 142 |
| 21B | 115 | 85 |
| 23B | 1,069 | 242 |
| 24B | 149 | 83 |

The mechanism-role, mechanism-database-release, and regulon validators all
passed with zero issues.

## Important materialization boundary

The current database contains register-backed graph rows, but the full
evidence hierarchy is not yet populated:

| Canonical table | Current rows |
|---|---:|
| `Paper` | 0 |
| `Experiment` | 0 |
| `Observation` | 0 |
| `AuthorClaim` | 0 |
| `EvidenceLink` | 0 |

The Phase-2 audit layer is substantially prepared, but it is not itself a
canonical write. It contains 4,722 integrated extraction rows and a 23,610-row
import manifest. The readiness report currently identifies unresolved or
deferred routes and explicitly states that canonical materialization remains
blocked until stable Paper records and validated atomic Observation/
AuthorClaim routes exist.

## Resumable next steps

1. Seed or verify the controlled evidence and outcome vocabularies from the
   repository’s authoritative vocabulary definitions. Do not create generic
   vocabulary terms solely to satisfy a foreign key.
2. Resolve the 582 paper-ready metadata records in
   `work/cross_module_synthesis/module20_24_canonical_paper_metadata.tsv`.
   Keep the 102 URL-only or otherwise unresolved records out of canonical
   Paper insertion until their identifiers are established.
3. For 20B and 21B, import only rows with an exact stable paper anchor and a
   separately validated experiment/observation route. 20B frozen LR-manifest
   anchors are not Paper or Observation records by themselves.
4. Repeat the same gate for 23B and 24B.
5. For remaining 22B rows, import only distinct TF/program claims. Do not
   turn receptor, pathway, promoter, enhancer, or functional-context rows
   into canonical TF-target claims.
6. Link canonical observations and claims to the existing graph edges while
   retaining independent ABC/D/E/U evidence grades and L0–L4 context grades.
7. Run the validation queries, database release validators, and a fresh
   mechanism-bundle export before creating a new release.

No Paper, Experiment, Observation, AuthorClaim, or EvidenceLink rows were
created at this checkpoint. No schema change was made.
