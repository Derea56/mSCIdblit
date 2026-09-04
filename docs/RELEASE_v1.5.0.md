# mSCIdblit v1.5.0 mechanism-graph release

This release freezes an expanded register-backed Module 20B–24B mechanism
graph. It incorporates the Module 21B expansion, the current Module 22B
evidence and promotion registers, and six additional primary-validated 21B
relay rows. The exporter retains only evidence-gated, non-self-loop edges as
traversable graph edges; non-exportable and unresolved records remain in the
boundary summary or source registers.

## Release identity

- Project version: `mSCIdblit v1.5.0`
- Mechanism graph version: `v1.5.0`
- Graph release identifier: `module20_24_mechanism_graph:2026-09-04`
- Release date: `2026-09-04`
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_04/`
- Prior mechanism-graph snapshot: `data/processed/mechanism_graph_module20_24_v2026_09_01/`

This is a register-backed graph release, not a claim that every edge is
SCI-specific or a replacement for canonical PostgreSQL materialization. The
bundle preserves register evidence and excludes local-only locators from the
public locator field while retaining their limitations and evidence summaries.

## Bundle counts

| Measure | v1.4.0 | v1.5.0 | Change |
|---|---:|---:|---:|
| Nodes | 2,787 | 6,667 | +3,880 |
| Traversable edges | 3,161 | 10,410 | +7,249 |
| Evidence-source rows | 4,494 | 11,824 | +7,330 |
| Node-role assignments | 4,340 | 10,546 | +6,206 |
| Pathway summaries | 958 | 3,449 | +2,491 |
| Boundary groups | 16 | 37 | +21 |

| Module | Register edges | Traversable edges | Evidence rows | Non-exportable edges |
|---|---:|---:|---:|---:|
| 20B | 5,906 | 1,145 | 7,630 | 4,761 |
| 21B | 2,646 | 2,626 | 2,595 | 20 |
| 22B | 10,391 | 5,421 | 10,564 | 4,970 |
| 23B | 1,075 | 1,069 | 1,501 | 6 |
| 24B | 151 | 149 | 224 | 2 |

The 20B–22B expansion adds 7,249 traversable edges relative to v1.4.0. The
20B, 21B, and 22B register counts include records retained as boundaries,
including self-loops and non-exportable evidence states; those records are not
inserted into the traversable graph.

## Validation

The graph validator passed with zero errors for unique identifiers, resolved
node and evidence references, pathway summaries, role compatibility,
exportability, and self-loop exclusion. It reports a warning for evidence
sources without stable public locators; those rows remain bounded by their
register evidence summaries and limitations.

The mSCS bundle importer retained all 10,410 graph edges and 11,824
edge-source rows, together with 6,667 nodes and 10,546 node-role assignments,
in an isolated import directory.

Rebuild and validate the release with:

```bash
python3 scripts/export_module20_24_mechanism_graph.py \
  --output-dir data/processed/mechanism_graph_module20_24_v2026_09_04
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_04
```

The source register SHA-256 values used for this snapshot are recorded in
`bundle_metadata.json`. The Module 20B pathway-family layer remains a
conservative grouping annotation and does not assert complete downstream
pathways.
