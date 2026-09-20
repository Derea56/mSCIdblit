# Public ligand--receptor candidate triage v1

This report reduces `7,753` public-only rows to `7,753` normalized candidate units against `6,059` direct ligand--receptor graph edges from `module20_24_mechanism_graph:2026-09-19-literature-expansion-243`.

## Results

| Triage lane | Candidate units | Meaning |
|---|---:|---|
| Resolved graph match | 7 | Exact label or exact component match; no new edge is implied. |
| Alias adjudication | 1,071 | Component overlap suggests an alias or composite representation; curator confirmation is required. |
| Primary-evidence review | 1,630 | No automatic graph match and a public primary-paper locator is present. |
| Discovery review | 5,045 | No automatic graph match and no primary locator in the frozen public snapshot. |

The actionable review queue contains `7,746` units, of which `1,820` have a primary locator and `5,926` require discovery or broader evidence search.

## Review batches

Novel and alias-adjudication units are ranked using the existing public-source/locator priority fields and divided into batches of `100`. This rank is an effort-ordering value, not a confidence score.

## Reproduction

```bash
python3 scripts/triage_public_lr_candidates_v1.py
```

Outputs: `candidate_normalization.tsv` contains every normalized unit; `candidate_review_queue.tsv` excludes automatic graph matches; `candidate_triage_summary.json` contains input hashes and counts.
