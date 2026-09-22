# mSCS release coverage report

Release: `module20_24_mechanism_graph:2026-09-22-literature-expansion-276`

This report separates route-evidence coverage from biological confidence. The route layer is evidence-only and non-causal; mSCS applies route plausibility and confidence logic.

## Route categories

| Category | Records |
|---|---:|
| L→R→output | 2,669 |
| L→R→TF→output | 344 |
| L→R→intracellular→output | 2,414 |
| L→R→intracellular→TF→output | 131 |
| L→R→entry→only | 9,307 |

## Audit and public-LR coverage

- Route-evidence records: 16,341
- Graph edges: 14,801
- Graph evidence-source rows: 17,242
- Public-LR candidates covered: 7,737
- Public-LR rows with primary locators and graph matches: 1,115
- Intracellular/TF gap pairs prioritized: 5,954

The prioritized gap table is a workflow queue for evidence harvesting. It does not assign biological confidence or promote causal edges.
