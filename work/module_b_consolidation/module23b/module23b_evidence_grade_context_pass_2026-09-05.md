# Module 23B A–E/U and L0–L5 evidence pass

This is a staging/audit output. It does not modify the Module 23B
registers, promote edges, or write canonical database tables.

The A–E/U grade axis reuses the repository's existing conservative
register-based rules. U means the current register fields do not safely
support an A–E call. The existing repository rubric defines L0–L4; this
pass adds L5 as an audit-only extension for explicit injury-model context
plus an explicitly named SCI receiver cell or lesion compartment.

- Evidence records reviewed: 1,674
- Output: `work/module_b_consolidation/module23b/module23b_evidence_grade_context_pass_2026-09-05.tsv`

## Evidence grade counts

| Grade | Count |
|---|---:|
| A | 34 |
| B | 1,327 |
| C | 0 |
| D | 0 |
| E | 182 |
| U | 131 |

## Context level counts

| Level | Operational meaning | Count |
|---|---|---:|
| L0 | No positive context or negative/bounded record | 182 |
| L1 | Traceable source/species context; no CNS context | 1,221 |
| L2 | CNS/neural system | 123 |
| L3 | Spinal-cord tissue without explicit injury model | 0 |
| L4 | Explicit SCI/injury-model context without receiver-cell match | 75 |
| L5 | Explicit injury model plus SCI receiver cell/lesion compartment | 73 |

## Pass disposition

| Disposition | Count |
|---|---:|
| retain_for_adjudication | 1,361 |
| review_required | 131 |
| boundary_or_nonpromotable | 182 |

No edge promotion or canonical materialization was performed. Grade and
context remain independent axes; the written basis and limitations must
travel with any later promotion review.
