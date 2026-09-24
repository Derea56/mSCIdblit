# Module 20B–24B mechanism graph release reference

The current release is documented in
[`RELEASE_v1.9.283.md`](RELEASE_v1.9.283.md). Earlier snapshots, including
v1.9.262, v1.9.261, v1.9.260,
v1.9.259, v1.9.258, v1.9.149, and the v1.8.x series, are retained as implementation and
historical baseline references.

Current release identifier: `module20_24_mechanism_graph:2026-09-24-gap-full-sequences-435`

Current bundle: `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion435/`.

The current snapshot is documented in [`RELEASE_v1.9.283.md`](RELEASE_v1.9.283.md).
It contains the machine-readable full-chain audit, generalized evidence-route
layer, public-LR evidence supplement, and mSCS coverage report.

## Current v1.9.283 snapshot

The current bundle contains 11,988 nodes, 14,831 traversable edges, 15,107
linked source rows, 17,406 node-role assignments, 10,973 pathway summaries,
and 96 boundary groups. It retains 588,201 evidence-route records and 22,087
literature-expansion annotations. The normalized route artifacts contain
2,463,754 route nodes and 2,271,731 route edges. This release adds four
primary-literature evidence routes across three ligand labels and preserves
the all-ligand curation queue at 15,392 deduplicated candidates. The routes
remain evidence-only and are intended for mSCS confidence evaluation; no
causal assertions or database confidence scores are created.

The new tranche mixes a full target-gene route, a full intracellular-to-TF
route ending in a gene-expression output, and a partial ligand–receptor output
route. Shared-source and queue-composed layers remain separately auditable so
mSCS can evaluate their relative plausibility. The component evidence is
preserved and intracellular-to-TF and TF-to-target handoffs remain unasserted
unless an existing graph edge supports them.

## Previous v1.9.282 snapshot

The previous snapshot added 456 all-ligand full-sequence evidence routes across
21 ligand labels and retained 588,197 evidence-route records, 22,083
literature-expansion annotations, and a 15,389-candidate curation queue.

## Previous v1.9.281 snapshot

The previous snapshot added 37 full-output composed routes across three ligand
labels and retained 587,741 evidence-route records, 21,627
literature-expansion annotations, and a 15,388-candidate curation queue.

## Previous v1.9.280 snapshot

The previous snapshot added 72 pairwise-source-overlap composed full-sequence
annotations across 12 ligand labels. It contained 587,704 evidence-route
records, 21,590 literature-expansion annotations, and a 15,388-candidate
curation queue.

## Previous v1.9.279 snapshot

The previous snapshot added 6,655 shared-source composed full-sequence
annotations across 34 ligand labels. It contained 587,632 evidence-route
records, 21,518 literature-expansion annotations, and a 15,359-candidate
curation queue.

## Previous v1.9.278 snapshot

The previous snapshot added 1,602 source-linked partial route annotations
across 731 ligand labels. It contained 580,977 evidence-route records,
14,863 literature-expansion annotations, and a 15,325-candidate curation queue.

## Previous v1.9.277 snapshot

The previous snapshot added 330 source-linked `Il15` alias target-gene routes.
It contained 579,375 evidence-route records and 13,261 literature-expansion
annotations.

The previous six-route tranche covered IL-27/STAT1/STAT3 transcriptional
outputs, IL-17A ACT1/NF-kB-associated DEFB4 and CCL20 outputs,
HBEGF/EGFR/ERK/EGR1/CYP24A1, and PDGFA/PDGFRA/ERK/ELK1/EGR1. In this release,
the alias routes retain unresolved receptor-proximal or intracellular-to-TF
handoffs rather than promoting a composed literature interpretation into a
graph edge.

## Previous v1.9.276 snapshot

The previous snapshot added six bounded primary-literature route annotations
for IL-27, IL-17A, HBEGF, and PDGFA. It contained 12,931
literature-expansion annotations and a 15,321-candidate curation queue.

## Previous v1.9.275 snapshot

The previous snapshot added four bounded primary-literature route annotations
for FGF2, LPA, VEGFA, and norepinephrine. It contained 12,925
literature-expansion annotations and a 15,316-candidate curation queue.

## Previous v1.9.270 snapshot

The previous bundle contained 11,988 nodes, 14,831 traversable edges, 15,107
linked source rows, 17,406 node-role assignments, 10,973 pathway summaries,
and 96 boundary groups. It retained 573,499 evidence-route records and 7,385
literature-expansion annotations. The normalized route artifacts contained
2,394,027 route nodes and 2,216,676 route edges. It added 30 primary-evidence
JAK→STAT pathway-handoff edges and 18,611 graph-supported route compositions
across 58 ligand–receptor edges.

## Previous v1.9.269 snapshot

The current bundle contains 11,988 nodes, 14,801 traversable edges, 17,242
linked source rows, 17,406 node-role assignments, 10,960 pathway summaries,
and 96 boundary groups. It retains 554,888 evidence-route records and 7,385
literature-expansion annotations, including 1,368 explicit
`ligand>receptor>intracellular>TF>target_gene_expression` records. The
normalized route artifacts contain 2,302,921 route nodes and 2,141,150 route
edges. This release adds 213,835 graph-supported route compositions across
206 exact ligand–receptor edges and 174 ligand labels: 198,096 include a
target-gene layer and 15,739 end at a supported output without target-gene
attribution. The routes are evidence-only, require shared pathway or evidence
anchors, and retain the relay-to-TF handoff as unasserted. No graph edges,
causal assertions, or database confidence scores are created.

## Previous v1.9.268 snapshot

The current bundle contains 11,988 nodes, 14,801 traversable edges, 17,242
linked source rows, 17,406 node-role assignments, 10,960 pathway summaries,
and 96 boundary groups. It retains 341,053 evidence-route records and 7,385
literature-expansion annotations, including 1,368 explicit
`ligand>receptor>intracellular>TF>target_gene_expression` records. The
normalized route artifacts contain 1,311,363 route nodes and 1,287,980 route
edges. This release adds four IL-20/STAT3 target-gene routes while preserving
the unresolved intracellular handoffs. It carries
forward the
15 WNT3A routes across FZD2, FZD4, FZD5, FZD7, and
FZD10 branches with MYC, CCND1, and CDKN1A outputs and adds two VIP/VPAC2
routes ending in Per1 and IL6, plus two PACAP/PAC1 routes ending in Bdnf
promoter IV through parallel GNAS and GNAQ/GNA11 receptor-proximal branches.
It also adds two IL-15 routes through parallel JAK1 and JAK3 branches to
STAT5-associated Il17A regulation and two IL-21 routes through JAK1/JAK3 and
STAT3 to IL21 and IL17A. All route annotations are evidence-only; missing
handoffs remain explicit and no graph edges or database confidence scores are
created.

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
