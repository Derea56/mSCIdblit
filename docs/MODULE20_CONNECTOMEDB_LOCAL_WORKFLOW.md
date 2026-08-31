# Module 20A ConnectomeDB Local Workflow

Use this workflow when we want a broad, low-credit database-first cast for Module 20A and want the local model to do repeatable triage work without inventing biology.

## Principles

- Treat ConnectomeDB rows as seed candidates, not final mechanistic truth.
- Keep mouse support explicit. Use human context only when it is clearly labeled.
- Never let the local model invent receptor complexes, species support, or downstream signaling.
- Salvage local-model output only when the repair is mechanical and source-controlled.
- Push malformed or incomplete rows into rerun rather than guessing.

## Current Direct-Seed Workflow

1. Build a source master from `ConnectomeDB2025_mouse.csv`.
2. Filter to the current Module 20A priority families.
3. Split the filtered direct-only set into small microchunks.
4. Generate one prompt per microchunk.
5. Run the local model on each prompt.
6. Validate and normalize the outputs before any curator review or evidence follow-up.

## Run The Validator

From the repo root:

```bash
python3 scripts/validate_connectomedb_lr_batch.py
```

Default inputs:

- source chunks:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/`
- raw local-model outputs:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/outputs/`

Default review outputs:

- normalized per-chunk TSVs:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/normalized_outputs/`
- merged validated TSV:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/connectomedb_mouse_priority_direct_validated_merged.tsv`
- machine-readable audit:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/connectomedb_mouse_priority_direct_validation.json`
- human-readable audit:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/connectomedb_mouse_priority_direct_validation.md`
- rerun helper:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/rerun_failed_chunks.sh`

## Export Curator Review Slices

After validation is clean enough for review, materialize stable triage queues:

```bash
python3 scripts/export_connectomedb_lr_review_slices.py
```

Default review-slice outputs:

- merged passthrough copy:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/all_rows.tsv`
- bucket slices:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/by_bucket/`
- action slices:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/by_action/`
- family slices:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/by_family/`
- curator-first priority queues:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/priority_queues/`
- machine-readable summary:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/summary.json`
- human-readable summary:
  `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/summary.md`

The export is still mechanical only. It does not promote any pair into the graph and it does not clean or reinterpret biology-facing text.

## What The Validator Repairs

Safe repairs only:

- strips ANSI noise and blank wrapper lines
- reattaches source-controlled fields from the original chunk row:
  `interaction_id`, `lr_pair`, `evidence`, `matched_families`
- recovers controlled-vocabulary fields when they can be parsed mechanically:
  `module20a_bucket`, `species_note`, `next_action`
- preserves the local model's short reason only when it can be isolated without guessing

The validator does not:

- infer missing biology
- rewrite a row whose prefix no longer matches the source chunk
- guess between multiple possible controlled-vocabulary parses
- promote rows into `SignalingEdge` curation

## Rerun Policy

Rerun a chunk when any of these occur:

- missing source interaction IDs
- malformed rows that cannot be parsed mechanically
- duplicate interaction IDs
- visibly truncated output

Use the generated helper script to rerun only the failed chunk set:

```bash
bash work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/rerun_failed_chunks.sh
```

## Recommended Loop

1. Run the local-model batch.
2. Run `validate_connectomedb_lr_batch.py`.
3. Rerun failed chunks until the validation report is clean enough for curator review.
4. Run `export_connectomedb_lr_review_slices.py`.
5. Review the exported priority queues instead of the raw merged file.
6. Only then start review-backed or primary-source evidence escalation on retained pairs.

## Current Curator-First Queue Order

For the current ConnectomeDB2025 mouse direct-seed pass, use this review order:

1. `priority_queues/01_keep_direct_seed_review_then_primary.tsv`
2. `priority_queues/02_keep_direct_seed_with_caution_review_then_primary.tsv`
3. `priority_queues/04_primary_first.tsv`
4. `priority_queues/03_boundary_review.tsv`
5. `priority_queues/05_hold_for_later_family_pass.tsv`

This ordering keeps the highest-yield direct LR seeds in front while preserving the caution and boundary sets for explicit later review rather than silent exclusion.
