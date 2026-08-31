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
