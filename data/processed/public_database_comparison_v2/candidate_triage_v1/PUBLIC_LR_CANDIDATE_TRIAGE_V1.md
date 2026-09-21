# Public ligand--receptor candidate triage v1

This report reduces `7,753` public-only rows to `7,753` normalized candidate units against `6,060` direct ligand--receptor graph edges from `module20_24_mechanism_graph:2026-09-20`.

## Results

| Triage lane | Candidate units | Meaning |
|---|---:|---|
| Resolved graph match | 5 | Exact label or exact component match; no new edge is implied. |
| Completed prior harvest | 25 | Present in the existing primary-evidence harvest ledger; excluded from new review batches. |
| Completed batch review | 100 | Resolved in a batch-specific evidence ledger; excluded from new review batches while retaining the resolution record. |
| Represented graph alias | 943 | Conservative one-component/one-edge representation match; no new evidence or edge is inferred. |
| Alias adjudication | 46 | Component overlap suggests an alias or composite representation; curator confirmation is required. |
| Primary-evidence review | 1,589 | No automatic graph match and a public primary-paper locator is present. |
| Discovery review | 5,045 | No automatic graph match and no primary locator in the frozen public snapshot. |

The actionable review queue contains `6,680` units, of which `1,594` have a primary locator and `5,086` require discovery or broader evidence search.

## Review batches

Novel and alias-adjudication units are ranked using the existing public-source/locator priority fields and divided into batches of `100`. This rank is an effort-ordering value, not a confidence score.

## Reproduction

```bash
python3 scripts/triage_public_lr_candidates_v1.py
```

Outputs: `candidate_normalization.tsv` contains every normalized unit; `candidate_review_queue.tsv` excludes automatic graph matches and completed review-ledger rows; `candidate_triage_summary.json` contains input hashes and counts.
