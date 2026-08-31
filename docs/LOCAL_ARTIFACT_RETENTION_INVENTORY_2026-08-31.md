# Local artifact retention inventory — 2026-08-31

This report is a non-destructive inventory of files reported by Git as
untracked. It does not imply that an artifact is safe to delete. The
database-link status means only that the exact path occurs in current
database provenance notes; database rows do not contain the source file.

- Inventory TSV: `data/processed/local_artifact_inventory_v1.tsv`
- Untracked files inventoried: 3,423

| Artifact class | Files | Bytes | Recommendation |
|---|---:|---:|---|
| `derived_output` | 104 | 531,244,473 | `review_reproducibility_then_archive` |
| `local_cache` | 112 | 29,822,499 | `safe_to_remove_after_index_review` |
| `local_configuration` | 4 | 9,184 | `keep_local_do_not_publish` |
| `local_helper` | 6 | 14,765 | `review_for_archive_or_removal` |
| `reference_snapshot` | 11 | 34,069,041 | `retain_externally_with_manifest` |
| `reproducibility_code` | 261 | 1,969,897 | `review_for_commit_or_archive` |
| `research_documentation` | 27 | 279,242 | `review_for_commit_or_archive` |
| `source_evidence` | 2,898 | 327,557,923 | `retain_until_release_freeze` |

| Database link status | Files |
|---|---:|
| `exact_path_referenced` | 697 |
| `not_referenced_by_current_db_notes` | 2,726 |

Recommended next action: retain source evidence and reference
snapshots through release freeze; review derived outputs and code
for reproducibility; then archive or remove only explicitly approved
superseded files. Local caches and configuration should not enter the
public release.

The repository now ignores local-only `.repowise/`, `.mcp.json`, `.vscode/`,
and `AGENTS.md` paths. This changes Git visibility only; the files were not
deleted or moved.

## Derived-output review

The 67 files under `data/processed/module20_24_database_intake_v1/` remain
staging inputs and review provenance. Its README explicitly says that these
records do not modify the frozen mechanism graph; they must be retained until
their leads are either adjudicated into the database or formally closed.

The older mechanism bundles, database-comparison outputs, and standalone seed
bundles under `data/processed/` are derived snapshots. The tracked
`data/processed/mechanism_graph_module20_24_v2026_08_30/` and the reproducible
database exporter are the current graph path. The older snapshots are marked
as archive candidates, not deletion candidates, until release history and
reproducibility checks are complete.

## Archive action completed

On 2026-08-31, six exact superseded/comparison-only directories were moved to
`/Users/derea/Documents/SCI/mSCIdblit_local_archive/derived_snapshots_2026-08-31/`.
They were moved, not deleted. The archive contains a README and the original
inventory retains their pre-move sizes and SHA-256 values. Raw evidence,
database-intake staging, and the current tracked mechanism graph were not
moved.

Preservation incident: two archived helper files shared the basename
`_20a_tlrs_full.py`. Because the archive destination was initially flat, the
second move overwrote the first. The surviving `modules/` copy was renamed in
the archive to `modules__20a_tlrs_full.py`. The original repository-root copy
was not recoverable from the workspace or temporary directories; its original
size and SHA-256 remain documented in the inventory for possible recovery from
an external filesystem backup. No further cleanup will proceed using flat
archive destinations.

On 2026-08-31, 107 historical Module 20A/20B batch-specific scripts were
moved to
`/Users/derea/Documents/SCI/mSCIdblit_local_archive/historical_batch_scripts_2026-08-31/scripts/`.
The handoff-linked `scripts/curate_module20_external_recovery_batch19.py`
was retained in the repository. The archived files were verified against the
pre-move SHA-256 inventory, and their original relative `scripts/` names are
preserved without flattening collisions.

On 2026-08-31, the remaining 104 untracked historical Module 20A/20B
search, audit, recovery, and batch-review scripts were moved to
`/Users/derea/Documents/SCI/mSCIdblit_local_archive/historical_module20_workflows_2026-08-31/scripts/`.
All 104 checksums passed. The current Module 20–24, noncanonical, and
public-TF pipeline scripts remain tracked; raw evidence and processed staging
artifacts were not moved.
