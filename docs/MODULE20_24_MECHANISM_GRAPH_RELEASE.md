# Module 20B–24B mechanism graph release reference

The current release is documented in
[`RELEASE_v1.9.259.md`](RELEASE_v1.9.259.md). Earlier snapshots, including
v1.9.258, v1.9.149, and the v1.8.x series, are retained as implementation and
historical baseline references.

Current release identifier: `module20_24_mechanism_graph:2026-09-24-wnt3a-canonical-routes-382`

Current bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion382/`.
It contains the machine-readable full-chain audit, generalized evidence-route
layer, public-LR evidence supplement, and mSCS coverage report.

## Current v1.9.259 snapshot

The current bundle contains 11,988 nodes, 14,801 traversable edges, 17,242
linked source rows, 17,406 node-role assignments, 10,960 pathway summaries,
and 96 boundary groups. It retains 341,033 evidence-route records and 7,365
literature-expansion annotations, including 1,355 explicit
`ligand>receptor>intracellular>TF>target_gene_expression` records. The
normalized route artifacts contain 1,311,270 route nodes and 1,287,907 route
edges. This release adds 15 WNT3A routes across FZD2, FZD4, FZD5, FZD7, and
FZD10 branches with MYC, CCND1, and CDKN1A outputs. All route annotations are
evidence-only; missing handoffs remain explicit and no graph edges or database
confidence scores are created.

## Historical evolution through v1.9.258

The v1.9.258 bundle had 11,988 nodes, 14,801 traversable edges, 17,242 linked
source rows, 17,406 node-role assignments, 10,960 pathway summaries, and 96
boundary groups. The full-chain audit reports 141 evidence-backed edge-chain
instances and 95 unique four-node topologies. The route-evidence layer retains
341,018 records across entry, output, intracellular, TF, and combined route
categories; it remains evidence-only so mSCS can evaluate plausibility and
confidence using cell context. This release retains the 313,750
graph-supported compositions across 1,413 exact ligand–receptor edges and
retains 7,350 literature-expansion route annotations across 1,870 ligand labels,
including 5,318 previously exposed source-linked routes, 441 newly promoted
source-linked target-gene route components across 44 ligand labels, and three
BDNF–TrkB–relay–CREB–Arc route alternatives, and 55 alias-composed target-gene
routes across eight ligand aliases. The latest pass adds 42 full-layer alias
routes for Bdnf, Il15, Il2, and Thpo while preserving unasserted receptor-to-relay
handoffs. The prior
relay-promotion pass added 194 full-layer routes across seven ligand labels
by carrying relay identities from existing full routes with identical ligand,
receptor, and TF node identities onto source-linked partial target-gene routes.
The 194 routes retain unresolved edge assertions explicitly and do not replace
their 162 partial source records. The total full-layer target-gene route count
was 675 before the current pass. The exact target-template pass adds 78 more
full-layer routes across 14 ligand labels by carrying relay and TF identities
from routes with identical ligand, receptor, and target-gene node identities.
The total full-layer target-gene route count was 753. The output-template pass
adds 122 more full-layer routes across 11 ligand labels by carrying relay and
TF identities from source-linked full output routes for the same ligand and
receptor. The target-specific handoff remains explicitly unasserted. The total
full-layer target-gene route count was 875. A final split-output pass adds 12
IL9 and IL11 routes by combining separate relay-output and TF-output evidence
for the same ligand–receptor pairs; the relay-to-TF handoff remains unasserted.
The total full-layer target-gene route count was 887. A same-receptor
component pass adds 453 additional full-layer routes across 24 ligand labels,
using source-linked relay and TF components while preserving unresolved
handoffs. The total full-layer target-gene route count is now 1,340. Two
hundred thirty-four missing-both-layer target routes and 11 TF-known routes
still lack a same-receptor template and remain queued for direct literature
curation. GH/GHR–JAK2–STAT5–Cish routes now cover both the GH1 and historical growth-hormone
ligand labels. Six PDGF-BB/PDGFRB receptor-proximal alternatives now connect to
the primary-linked STAT3→FOS target component. Two CSF1/IL-34→CSF1R/c-Fms→MEK/ERK→ELK1→c-FOS evidence routes add ligand-specific output support while preserving the unresolved ERK-to-ELK1 and ELK1-to-c-FOS links. This release adds a Prolactin→PRLR→JAK2→STAT5→Csn2 target-gene route from primary beta-casein reporter evidence while preserving the unresolved STAT5-to-Csn2 link. The prior
1,340 explicit `ligand>receptor>intracellular>TF>target_gene_expression` records
remain, and the new routes preserve unresolved `????` layers rather than
inventing intracellular or TF links. The import is restricted to records
with known ligand and receptor fields, valid current graph references, source
queue/evidence links, and stable primary locators; 2,178 historical records
without an explicit ligand or receptor remain out of this release for later
curation. The routes remain non-causal and do not create graph edges or
confidence scores. Existing IL1B TF-family-supported routes, expanded cytokine/JAK/STAT and
Notch/BMP/RTK routes, receptor aliases, and composite intracellular relays.
IL1B coverage now includes explicit primary-supported NF-kappaB-family target
links for ICAM1/CD54, IL6, and CXCL1 in addition to the existing bounded route
annotations. CSF3/G-CSF now includes SHC1/GRB2-to-STAT3-to-SOCS3 evidence
routes, and TNF includes TNFR1/TRADD and TNFR2/NF-kappaB relay alternatives
to ICAM1/CD54 and IL6. The IL1B pilot covers
the IL1R1/IL1RAP → MYD88 → IRAK4 → IRAK1 → TRAF6 → TAK1 → NF-kappaB branch
with ICAM1, IL6, CCL20, and CXCL1 transcriptional outputs. Exact intracellular
to TF relay edges remain explicitly unasserted; direct TF-to-target edges are
retained where present. EGF now includes a bounded EGFR–SHC1/RAS/ERK–ELK1–EGR1
evidence route with the SHC1-to-ELK1 handoff explicitly unresolved. TGFB1 now
includes bounded TGFBR–SMAD3/4 routes to COL1A2, CTGF/CCN2, JUN, and SERPINE1/PAI-1,
with the SMAD3-to-SMAD3/4 handoff explicitly unresolved. These rows
do not create graph edges, causal assertions,
or database confidence scores. The
normalized route companion tables now expose ordered route nodes and route
edges for all 340,159 routes, including explicit missing-link rows and
separate output-observation edges. They allow shared intermediates such as
MYD88 to be indexed across ligands and outputs for downstream perturbation
analysis in mSCS. The normalized tables are compressed TSV artifacts; Parquet
remains available through the mSCS columnar import.

Historical v1.8.0 release identifier: `module20_24_mechanism_graph:2026-09-16`

Historical v1.8.0 bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16/`

Historical v1.7.0 release identifier: `module20_24_mechanism_graph:2026-09-15`

Historical v1.6.0 release identifier: `module20_24_mechanism_graph:2026-09-10`

## Historical v1.6.0 reference

This is a conservative, register-backed mechanism graph snapshot for mSCIdblit
Modules 20B–24B. It is designed for inspection and simulator import while
preserving the evidence gate: only rows marked `exportable=true` in the
validated edge registers become traversable graph edges.

The v1.6.0 release emitted the required mSCS mechanism-bundle columns and was
validated by running mSCS's `import_mechanism_bundle.py` into a temporary active
release directory. The mSCS checkout was not modified by that verification.

## Release contents

The bundle is at
`data/processed/mechanism_graph_module20_24_v2026_09_10/`.

| Artifact | Purpose |
|---|---|
| `mechanism_nodes.tsv` | mSCS-compatible node table plus curated labels and audit fields; composite labels are preserved. |
| `mechanism_node_roles.tsv` | Explicit many-to-many mSCS role assignments with provenance: ligand, receptor, transcription factor, target gene, and signaling cascade. |
| `mechanism_edges.tsv` | mSCS-compatible directed, typed, evidence-gated pathway edges plus module, context, confidence, and exportability fields. |
| `mechanism_edge_sources.tsv` | mSCS-compatible evidence provenance fields plus evidence-register IDs, source locators, summaries, limitations, and citation notes. |
| `mechanism_pathways.tsv` | Pathway-level edge, node, and evidence counts. |
| `mechanism_boundary_summary.tsv` | Aggregate view of non-exportable edge boundaries. |
| `bundle_metadata.json` | Release policy, counts, module coverage, and accuracy contract. |
| `validation_report.json` | Machine-generated graph integrity report. |

## Release counts

| Module | Register edges | Exported edges | Evidence rows | Non-exportable edges |
|---|---:|---:|---:|---:|
| 20B | 5,906 | 1,145 | 7,630 | 4,761 |
| 21B | 8,171 | 8,089 | 8,120 | 82 |
| 22B | 10,694 | 5,726 | 10,784 | 4,968 |
| 23B | 1,230 | 1,224 | 1,674 | 6 |
| 24B | 151 | 149 | 224 | 2 |
| **Total graph** | — | **16,333** | **17,765 linked source rows** | **9,819** |

The graph contains 10,656 node labels and 8,891 pathway labels. Of the 17,765
linked evidence-source rows, 14,739 retain stable PMID, PMCID, DOI, or HTTP
locators in the release bundle; 1,450 are marked local-only or unresolved and
retain their evidence summaries and limitations without exposing local paths.

The role table contains 14,856 assignments: 10,656 baseline
`signaling_cascade` assignments, 742 `ligand`, 729 `receptor`, 288
`transcription_factor`, and 2,441 `target_gene` assignments. Role assignments are
many-to-many; a node can therefore be both a signaling-cascade participant and
a specialized endpoint. `node_type` remains the legacy single-valued mSCS
field and uses `signaling_effector` for generic relay, complex, and program
labels rather than inventing a new legacy type.

## Accuracy check

Run the exporter and validator from the repository root:

```bash
python3 scripts/export_module20_24_mechanism_graph.py
python3 scripts/validate_module20_24_mechanism_graph.py
```

The validator checks:

- unique node, edge, and source IDs;
- source/target node references;
- evidence-source references for every exported edge;
- pathway summary consistency;
- metadata count consistency; and
- absence of non-exportable edges from the traversable graph;
- role vocabulary, role provenance, role-to-node resolution, and complete
  `signaling_cascade` coverage; and
- canonical role-edge compatibility (`binds_receptor` for ligand-receptor
  edges and the three target-gene relation types for TF-target edges).

The historical v1.6.0 release passed with zero errors; the validator reported the
local-only/unresolved locator count as a warning, not as a graph-integrity
failure.

Validate the mSCS import contract with the mSCS virtual environment (which
provides its optional Parquet dependency):

```bash
rm -rf /private/tmp/mscs_module20_24_import_check
PYTHONPATH=/Users/derea/Documents/SCI/mSCS/src \
  /Users/derea/Documents/SCI/mSCS/.venv/bin/python \
  /Users/derea/Documents/SCI/mSCS/src/mscs/import_mechanism_bundle.py \
  data/processed/mechanism_graph_module20_24_v2026_09_10 \
  --mechanism-dir /private/tmp/mscs_module20_24_import_check --export-tsv
```

The verified import retained 2,787 nodes, 4,345 node-role assignments, 3,167
edges, and 4,393 evidence sources. The bundle is a mechanism snapshot, not a claim that the
register-backed labels are already canonical database entities; the metadata
therefore keeps `canonical_database_materialization=false`.

The database-side role contract is defined in
[`MECHANISM_ROLE_CONTRACT.md`](MECHANISM_ROLE_CONTRACT.md). Apply
`schema/mechanism_roles_layer.sql` after the base schema, populate roles only
from evidence-backed entity mappings (or derive the canonical edge roles with
`scripts/materialize_mechanism_roles.sql`), and run
`scripts/validate_mechanism_roles.sql` before a database-native export.

Regulon modeling is deliberately not inferred into this release. The
database-native, evidence-gated extension is documented in
[`REGULON_MODELING_LAYER.md`](REGULON_MODELING_LAYER.md) and applied through
`schema/regulon_layer.sql` when separately curated TF-target memberships are
ready.

## Interpretation boundaries

- A graph edge is exportable only because the register passed its evidence and
  curation gate; this is not a claim of universal biology or SCI-specific
  applicability.
- Non-exportable, unresolved, low-evidence, and layer-conflicted candidates
  remain summarized as boundaries and are not traversable edges.
- Composite receptor, ligand, pathway, and program labels are preserved rather
  than split into unsupported molecular claims.
- The cross-module synthesis remains an audit-layer interpretation; canonical
  database materialization and source-anchor resolution remain separate release
  gates.

The broader narrative synthesis is in
[`CROSS_MODULE_SYNTHESIS_20_24.md`](CROSS_MODULE_SYNTHESIS_20_24.md), while the
machine-readable graph contract is captured in `bundle_metadata.json`.

The PostgreSQL-materialized companion release is documented in
[`MODULE20_24_DATABASE_GRAPH_RELEASE.md`](MODULE20_24_DATABASE_GRAPH_RELEASE.md).
