# Genome-scale mouse TF-target prior release

The additive release `mscs_release_bundle:2026-10-01-nichenet-tf-target-prior-v1`
packages a response-independent mouse TF-target prior alongside the pinned
NicheNet resource and candidate universe. It does not modify the neutral
Module 20B–24B mechanism graph and does not create graph edges or route
confidence.

The broad prior is derived from the retained mouse TRRUST v2 source snapshot.
The source is licensed for non-commercial research under CC BY-SA 4.0; the
release records the official source URL, snapshot checksum, source-record
identifiers, record hashes, PMIDs, and source locators. The raw snapshot is
not redistributed. Source-supported activation/repression is retained; an
unknown or conflicting source sign remains `unknown`. TRRUST supplies no
association weights or ranks in this release, so those fields remain blank and
are explicitly marked `not_supplied`.

The release contains two deliberately separate evidence tiers:

* `tf_target_prior/tf_target_prior.tsv` is the broad 6,490-pair,
  response-independent prior over 827 TFs and 2,092 targets.
* `tf_target_prior/tf_target_direct_graph_tier.tsv` is a projection of the
  326 already-retained exportable TF-to-target mechanism-graph edges. It is an
  audit-preserving tier, not a graph update.

The source-level records remain in
`tf_target_prior/tf_target_prior_source_records.tsv`, with exact provenance in
`tf_target_prior/source_registry.tsv`. No GSE304399 response data or other
observed response was used to select the prior.

Build and validation are reproducible with:

```bash
python3 scripts/build_tf_target_prior.py
python3 scripts/build_mscs_tf_target_release.py
python3 scripts/validate_mscs_tf_target_release.py \
  --nichenet-artifact-root \
  /Users/derea/Documents/SCI/mSCIdblit-expand-23B/data/raw/method_resources/mscs_phase2_external_snapshot_2026-08-05
```

The prior is a method/resource input for downstream compatibility or
exploration. It is not a claim that a TF is active, that a target responds in
SCI, or that a source relationship is causal in the mSCS mechanism graph.
