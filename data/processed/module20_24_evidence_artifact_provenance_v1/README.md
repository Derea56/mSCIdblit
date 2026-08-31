# Module 20–24 evidence-artifact provenance layer

This bundle records the retained raw artifacts from:

`data/raw/evidence/module20_24_supervised_cli_phase2/`

It is an audit/provenance layer, not a biological-evidence promotion layer.
Each artifact is represented by its repository-relative path, byte size, and
SHA-256 digest. Filename identifiers are recorded separately. Register
crosswalk rows are conservative filename-token candidates only; they do not
assert that a file validates an edge, paper, observation, or claim.

The materialization SQL requires the additive migration
`schema/module20_24_evidence_artifacts.sql` and is idempotent. It does not
modify existing graph rows or create `Paper`, `Experiment`, `Observation`,
`AuthorClaim`, `EvidenceLink`, or `SignalingEdgeSource` records.

Generated files:

- `artifact_manifest.tsv`: one row per retained artifact;
- `artifact_identifiers.tsv`: explicit identifiers in filenames only;
- `register_crosswalk_candidates.tsv`: conservative candidate links to
  register evidence sources;
- `module20_24_evidence_artifacts_materialization.sql`: database inserts;
- `bundle_metadata.json`: reproducibility counts and scope note;
- `database_load_audit.md`: observed local-load counts and integrity checks.

Content-level citations are intentionally not converted into source links
because article reference lists and metadata payloads can mention unrelated
papers. Promotion still requires the existing exact source-unit gates and
independent A–E/U and L0–L4 grading.
