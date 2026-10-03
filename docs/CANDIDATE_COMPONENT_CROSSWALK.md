# Candidate LR component crosswalk

Release `mscs_release_bundle:2026-10-02-nichenet-tf-prior-candidate-components-v1`
adds an explicit component crosswalk to the method-resource candidate universe.
The canonical ligand/receptor name remains unchanged; component fields are
additional source-backed metadata and do not create mechanism edges, alter
route status, or change evidence strength.

The crosswalk is built by exact ligand/receptor pair lookup in the frozen
`master_lr_registry.tsv`. It uses the registry's explicit pipe-delimited
`ligand_components` and `receptor_components` fields and never splits an
underscore-joined canonical name. It records the registry ID, source methods,
resources, source-record IDs, evidence notes, source path, and source checksum.
Malformed, duplicate, ambiguous, or disagreeing mappings remain unresolved.

The corrected projection contains 9,099 candidate pairs:

* 3,359 agree with explicit component rows already present in the method
  migration layer;
* 239 receive an explicit source-complex mapping from the master registry;
* 5,501 receive a source-registry single-gene identity or exact fallback.

No unresolved component mappings remain in this frozen registry-backed
projection. This means component resolvability is complete for the candidate
catalog, not that every candidate is measured in an experiment.

The coordinator-reported downstream audit of 88 missing pairs was not present
in this repository, so exact pair-level recovery was not claimed. The machine-
readable handoff records that limitation in
`candidate_universe/candidate_component_handoff.json`; supplying the 88-row
audit with ligand, receptor, missing reason, and measured-feature requirement
will allow the 48-pair potentially recoverable subset to be checked directly.

Build and validation:

```bash
python3 scripts/build_mechanism_lr_candidate_universe.py \
  --output-dir data/processed/mechanism_lr_candidate_universe_v3_component_crosswalk_v1
python3 scripts/build_mscs_candidate_component_release.py
python3 scripts/validate_mscs_tf_target_release.py \
  --bundle-dir data/processed/mscs_release_bundle_v1_8_0_nichenet_tf_prior_candidate_components_v1 \
  --nichenet-artifact-root \
  /Users/derea/Documents/SCI/mSCIdblit-expand-23B/data/raw/method_resources/mscs_phase2_external_snapshot_2026-08-05
```
