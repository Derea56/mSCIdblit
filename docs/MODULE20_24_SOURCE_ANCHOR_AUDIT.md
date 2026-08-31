# Module 20B–24B Source-Anchor Audit

This registry prepares canonical materialization. It does not create
Paper, Observation, or AuthorClaim rows and does not modify canonical SQL.

## Anchor status

| Status | Rows |
|---|---:|
| candidate_external_anchor | 27,762 |
| local_audit_anchor | 4,470 |

## Registry coverage

| Module | Evidence-anchor rows |
|---|---:|
| 20B | 7,353 |
| 21B | 87 |
| 22B | 20,584 |
| 23B | 3,747 |
| 24B | 461 |

## Exportable-evidence anchor posture

| Module | External candidate anchors | Local-only anchors | Unresolved anchors |
|---|---:|---:|---:|
| 20B | 1,996 | 83 | 0 |
| 21B | 87 | 0 | 0 |
| 22B | 2,550 | 0 | 0 |
| 23B | 3,354 | 1 | 0 |
| 24B | 397 | 0 | 0 |

External PMID/PMCID/DOI/URL tokens are candidate anchors only. They must
be resolved to canonical Paper rows and then linked to an observation or
author claim before SignalingEdgeSource materialization.
