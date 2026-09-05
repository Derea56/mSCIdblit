# Module 20B–24B evidence grade ledger

This is staging/audit output. It does not write canonical database rows.
Rule-based provisional values are derived from explicit register labels
or an exact validated Phase-2 primary-paper route; U grades retain
review-required bases for later paper-level adjudication.

- Evidence records: 20,195
- Phase-2 linked rows available: 0

## Grade counts

| Module | A | B | C | D | E | U |
|---|---:|---:|---:|---:|---:|---:|
| 20B | 44 | 1,382 | 0 | 1,120 | 4,936 | 148 |
| 21B | 6 | 54 | 0 | 0 | 0 | 0 |
| 22B | 0 | 754 | 0 | 4,141 | 4,996 | 889 |
| 23B | 34 | 1,154 | 0 | 0 | 182 | 131 |
| 24B | 24 | 169 | 0 | 0 | 31 | 0 |

## Context counts

| Module | L0 | L1 | L2 | L3 | L4 |
|---|---:|---:|---:|---:|---:|
| 20B | 6,183 | 1,289 | 154 | 4 | 0 |
| 21B | 0 | 44 | 10 | 1 | 5 |
| 22B | 9,158 | 1,543 | 73 | 6 | 0 |
| 23B | 182 | 1,202 | 112 | 0 | 5 |
| 24B | 31 | 167 | 9 | 4 | 13 |

## Use

- `evidence_grade` and `context_level` are independent and must be retained together with the written bases.
- `grading_status=review_required` rows receive rubric grade `U`; the written basis identifies what must be resolved before an A-E call.
- A stable paper anchor, experiment-level source locator, exact claim/observation, and scope match remain required before canonical materialization.
