# mSCIdblit v1.6.0 mechanism-graph release

This release freezes the current register-backed Module 20B–24B mechanism
graph from committed `main`. It includes the current Module 21B and Module
22B expansions, the four recently integrated Module 22B SMAD target rows, and
the current Module 23B–24B registers. Only evidence-gated, non-self-loop rows
are traversable graph edges; non-exportable and unresolved records remain in
the boundary summary or source registers.

## Release identity

- Project version: `mSCIdblit v1.6.0`
- Mechanism graph version: `v1.6.0`
- Graph release identifier: `module20_24_mechanism_graph:2026-09-10`
- Release date: `2026-09-10`
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_10/`
- Prior mechanism-graph snapshot: `data/processed/mechanism_graph_module20_24_v2026_09_04/`

This is a register-backed graph release, not a claim that every edge is
SCI-specific or a replacement for canonical PostgreSQL materialization. The
bundle preserves register evidence and excludes local-only locators from the
public locator field while retaining their limitations and evidence summaries.

## Bundle counts

| Measure | v1.5.0 | v1.6.0 | Change |
|---|---:|---:|---:|
| Nodes | 6,667 | 10,656 | +3,989 |
| Traversable edges | 10,410 | 16,333 | +5,923 |
| Evidence-source rows | 11,824 | 17,765 | +5,941 |
| Node-role assignments | 10,546 | 14,856 | +4,310 |
| Pathway summaries | 3,449 | 8,891 | +5,442 |
| Boundary groups | 37 | 98 | +61 |

| Module | Register edges | Traversable edges | Evidence rows | Non-exportable edges |
|---|---:|---:|---:|---:|
| 20B | 5,906 | 1,145 | 7,630 | 4,761 |
| 21B | 8,171 | 8,089 | 8,120 | 82 |
| 22B | 10,694 | 5,726 | 10,784 | 4,968 |
| 23B | 1,230 | 1,224 | 1,674 | 6 |
| 24B | 151 | 149 | 224 | 2 |

The Module 22B source register contained eight duplicated edge identifiers in
two adjacent CTCF/PCDHB batches. The release preparation renumbers the second
batch to `M22B-E010695`–`M22B-E010702` and updates `M22B-EVID-010614` plus its
search-log cross-references. No evidence content was changed; the correction
restores unique edge identity and source linkage required by the graph
validator.

## Validation

The graph validator passed with zero errors for unique identifiers, resolved
node and evidence references, pathway summaries, role compatibility,
exportability, and self-loop exclusion. It reports a warning for evidence
sources without stable public locators; those rows remain bounded by their
register evidence summaries and limitations.

Rebuild and validate the release with:

```bash
python3 scripts/export_module20_24_mechanism_graph.py \
  --output-dir data/processed/mechanism_graph_module20_24_v2026_09_10
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_10
```

The source register SHA-256 values used for this snapshot are recorded in
`bundle_metadata.json`. The Module 20B pathway-family layer remains a
conservative grouping annotation and does not assert complete downstream
pathways. Terminal transcription-factor and SCI-specific receiver claims are
not inferred by the exporter.
