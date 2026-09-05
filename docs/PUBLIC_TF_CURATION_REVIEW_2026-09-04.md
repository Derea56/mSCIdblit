# Public-TF curation review — mSCIdblit modules 20B–24B

Source release: `module20_24_mechanism_graph:v1.1.0`.
Rows reviewed: **4174**; distinct regulator-target pairs: **3591**.
Promotion scope: this audit evaluates the existing v1.1.0 validated overlay and records a bounded review of the unpromoted mouse/direct-binding queue; it makes no new literature promotions.

## Curation outcomes

| Curation tier | Rows |
|---|---:|
| `candidate_only` | 3976 |
| `general_mouse_validated` | 3 |
| `neural_context_validated` | 0 |
| `sci_context_validated` | 0 |
| `unresolved` | 195 |

Candidate-only and unresolved rows are non-traversable. Validated rows are context-gated.
The exportable curation overlay contains **3** context-gated rows representing **2** pairs.
The next review queue contains **112** unpromoted mouse canonical-TF/direct-binding rows from Modules 20B–24B.
The bounded queue adjudication reviewed **112** rows: **0** promoted and **112** retained as candidate-only.

## Context-mode eligibility

| Mode | Eligible rows | Unique pairs |
|---|---:|---:|
| `general_mouse` | 3 | 2 |
| `neural` | 0 | 0 |
| `sci` | 0 | 0 |

## Reconciliation and limitations

Active-graph pair status: exact pair **5**, both nodes present without exact edge **69**, not found **4100**.
Duplicate exact pairs: **533**; pairs duplicated across modules: **444**.
Exact old/new semantic pair matches: **2723**; unresolved old/new pairs: **0 / 2**.

The candidate layer lacks structured tissue and cell-type fields; the ledger preserves unknown values. Graph membership was not used as a likelihood factor or CellChat/LIANA label. No label-adjudication queue was created because dependency metadata were not supplied.
Unavailable citation rows: **0**; missing local inputs: **4**.
Sensitivity smoke benchmark: **not_run** — route_candidates.tsv and route_steps.tsv are absent; identical calibration and evaluation artifacts are unavailable.

The machine-readable ledger, mouse direct-binding review queue, traversable-edge overlay, summary, and old/new semantic crosswalk are stored under `data/processed/public_tf_curation_v2026_09_04/`.
