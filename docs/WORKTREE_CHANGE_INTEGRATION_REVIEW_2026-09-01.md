# Worktree change integration review — 2026-09-01

## Scope

The pre-existing worktree contained 37 modified tracked files. This review
classifies them by whether they are reproducible, release-relevant, or blocked
by an unresolved input or schema decision. No file was deleted or reverted.

## Integrated group

The Module 2–7 evidence and materialization group was validated and committed
as `8544866` (`integrate validated module 2-7 evidence upgrades`). It includes
the six evidence bundles, six generated SQL materializations, the corresponding
Module 2A–7B tracker updates, the materialized-integrity report, the two
exporter changes, and the README changes. The current builders reproduce all
six JSON bundles and all six SQL files byte-for-byte; exporter checks pass for
Modules 2–7. The file-level audit reports 791 observations, 773 SQL
experiments, and 128 consensus statements, with ten documented non-blocking
warnings about expected claim-link gaps and B rows not represented in parsed A
tables.

## Integrated public-TF workflow group

The following remaining changes are coherent public-TF workflow/design changes
and were committed as `907b8cf` (`integrate public TF workflow updates`):

- `scripts/screen_public_tf_module_integration.py`
- `docs/PUBLIC_TF_EXPANSION_TRIAGE_SUMMARY_2026-08-26.md`
- `modules/ROADMAP.md`

The updated screening script was run against the correct staging directory and
passed with 4,174 input rows, 2,821 provisional module-owner candidates, 49
noncanonical module-context candidates, and no canonical materialization. The
noncanonical output agrees with the existing staged output. The context
adjudication and C-tier queue builders also pass in temporary output locations.

## Hold groups

### Public-TF snapshot validation

`data/processed/public_tf_union_v1/public_tf_union_validation.json` is
preserved as an explicit failing validation record, not as release-passing
evidence. It fails because the four exact registered snapshots are missing
from `/private/tmp`:

- `omnipath_dorothea_human.tsv`
- `omnipath_dorothea_mouse.tsv`
- `trrust_human.tsv`
- `trrust_mouse.tsv`

The validation result must not be converted to pass or released without those
exact source snapshots and their registered SHA-256 digests.

### Schema and schema documentation

`schema/schema.sql` and `docs/SCHEMA_DOCUMENTATION.md` were validated as a
fresh-load schema/documentation pair in an isolated rolled-back PostgreSQL
schema. The live database already contains the signaling layer and its
evidence-grade/context-level extensions: 3,399 edges, 3,399 register edges,
4,937 register-source records, and 7,432 canonical edge-source records. The
fresh-load definition and documentation are therefore integrated in the
current follow-up commit. The separate additive grading migration remains the
authoritative path for upgrading an existing database.

### Module 22B tracker status

`modules/Module_22B_TRACKER.md` states that 221 public TF-target pairs are
canonicalized across 198 species-qualified TF entries. The linked
`data/processed/module22b_database_comparison_v1/` directory was not found in
the repository file inventory, so the tracker has been corrected to report the
independent local-database count reconciliation without claiming that missing
comparison artifact.

### Path-linkage batch

`work/cross_module_synthesis/path_linkage_batches/module20_24_path_linkage_batch09_matrix_adhesion_yap_fak.tsv`
was normalized in its SEMA7A row. The M20B relay and functional evidence IDs
are preserved, and the duplicate source locators were reduced to their exact
union and rechecked against the source registers.

### Module 12B

`modules/Module_12B_TRACKER.md` contains a separate full-text/comparator update
and is not required for the current Module 20–24 promotion workflow. It remains
untouched and uncommitted pending a dedicated Module 12 review.

## Current status

No canonical schema migration or public-TF snapshot repair was performed by
this review. The remaining held files are intentionally preserved for their
respective follow-up tasks; the Module 22B tracker, path-linkage cleanup, and
fresh-load schema/documentation pair are now integrated in the current review
commit.
