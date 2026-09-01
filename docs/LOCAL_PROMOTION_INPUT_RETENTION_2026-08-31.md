# Local promotion-input retention — 2026-08-31

This note defines what remains available locally for future evidence promotion
while keeping the public Git history focused on reproducible code, curated
ledgers, and release bundles. The ignore rules in `.gitignore` change Git
visibility only; they do not move or delete any input.

## Retained public-TF staging

The public-TF module-integration staging layer remains the authoritative
candidate-review surface. The tracked staging ledgers preserve the reviewed
A–E evidence tiers, independent L0–L4 context levels, module routes, and
source-record identifiers. The ten current noncanonical owner/context files
are also retained as tracked staging outputs:

- `noncanonical_gene_expression_regulators.tsv`
- `noncanonical_module_context_adjudication.tsv` and its summary
- `noncanonical_module_context_triage.tsv` and its summary
- `noncanonical_module_owner_prescreen.tsv` and its summary
- `noncanonical_module_owner_review.tsv`
- `noncanonical_module_owner_review_rubric.md`
- `noncanonical_module_owner_review_summary.json`

These files are review inputs, not canonical graph edges. Owner decisions remain
pending unless explicitly adjudicated in a later promotion pass.

## Retained local-only evidence inputs

The following inputs remain on the workstation because they support open
extraction or promotion lanes:

| Path | Observed contents | Policy |
|---|---:|---|
| `data/processed/module20_24_database_intake_v1/` | 67 untracked files, about 490 MB | Retain until database leads are adjudicated or formally closed; not part of the frozen graph |
| `data/raw/evidence/module2_fulltext_upgrade/` | 108 local files, including one ignored PDF | Retain for Module 2 full-text extraction and tracker repair |
| `data/raw/evidence/module4_fulltext_upgrade/` | 3 local files | Retain for Module 4 evidence review |
| `data/raw/evidence/module6_7_fulltext_upgrade/` | 8 local files | Retain for Modules 6–7 evidence review |
| `data/raw/evidence/module_fulltext_queue_20260731/` | 53 local files, including `SOURCE_MANIFEST.tsv` | Retain for the queued Module 3/5 full-text pass |
| `data/raw/public_database_snapshots/module20_24_intake_v1/` | 9 source snapshots | Retain with the processed source registry and SHA-256 inventory |
| `data/raw/public_database_snapshots/tf_identity_intake_v1/` | 2 identity snapshots | Retain for reproducible public-TF identity rebuilding |
| `data/processed/module20_24_source_anchor_registry.tsv` | 32,232 derived anchor rows, about 5.2 MB | Retain locally as an audit derivative; rebuild only from the corresponding source registers |

The raw full-text files are not copied into the public release bundle. Their
local retention is necessary because the derived claims and evidence links do
not contain the source-file bytes. The public database and TF identity
snapshots are likewise local working inputs; their hashes remain recorded in
the tracked inventory and source registries.

## Cleanup boundary

No raw evidence or promotion input is deleted by this cleanup. Exact duplicate
raw snapshots are retained until the associated extraction lane is closed and a
checksum-preserving archive decision is made. Future cleanup may move a closed
input to the sibling local archive, but must preserve its original relative
path, size, SHA-256 digest, and a manifest before removal from the repository
working tree.
