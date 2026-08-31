# Module 20–24 database intake v1

Date: 2026-08-26  
Status: assembled in staging; no canonical graph/database writes

## Scope

This intake adds public database records as evidence leads for Modules 20A/B,
21A/B, 23A/B, and 24A/B. Module 22A/B remains covered by the completed public
TF union workflow; TRRUST and DoRothEA are recorded in the registry as already
processed rather than duplicated into this queue.

The source policy is conservative: a database row, pathway membership, network
edge, or PMID identifier is not promotion evidence on its own. A paper must be
checked separately for exact entity or complex, species, assay, branch or
effect, cell/model, and injury context. Directness remains distinct from
pathway, PPI, occupancy, or functional context.

## Imported sources

Release-pinned or locally available sources are recorded with SHA-256 hashes in
`data/processed/module20_24_database_intake_v1/database_source_registry_audit.tsv`.
The imported set is:

- CellChatDB human and mouse LR snapshots
- ConnectomeDB2025 human and mouse LR exports
- Guide to PHARMACOLOGY/GtoPdb 2026.2 detailed endogenous ligand export
- OmniPath causal human and mouse snapshots
- Reactome v97 pathway GMT
- TRRUST human and mouse snapshots, already covered by the TF union review
- DoRothEA human and mouse snapshots, already covered by the TF union review

The registry also records CellPhoneDB, LIANA, CellTalkDB, ICELLNET, SIGNOR,
KEGG, WikiPathways, Pathway Commons, BioGRID, IntAct, CORUM, STRING, JASPAR,
ChIP-Atlas, REMap, ENCODE, Matrisome, and MatrixDB as planned sources. They
are not treated as imported until a release-pinned export is acquired.

These source types have different roles: ConnectomeDB describes manually
curated LR-pair scope and methods at [its documentation site](https://connectomedb.org/docs/about.html);
GtoPdb provides downloadable ligand/target pharmacology data at [its official
download page](https://www.guidetopharmacology.org/download.jsp); Reactome is
used for curated pathway context at [its data-download page](https://reactome.org/download-data/);
and OmniPath is retained as an integrated causal/provenance source at [its
official resource](https://omnipathdb.org/).

## Assembly counts

| Artifact | Count |
|---|---:|
| Registry rows | 30 |
| Imported source snapshots | 12 |
| Planned/missing source rows | 18 |
| Database candidate leads | 28,169 |
| Literature lead rows | 62,144 |
| Unique linked PMIDs requested | 11,978 |
| PMIDs with PubMed metadata/abstract returned | 11,964 |
| Deduplicated module/entity/PMID review candidates | 43,432 |
| Abstract-level high-priority candidates | 8,184 |
| Multi-database review candidates | 17,091 |
| PMIDs reused across multiple modules | 2,466 |
| Leads with no linked literature in the source row | 3,812 |

The module-specific candidate lead counts are:

| Module | Leads | Literature rows | Review candidates |
|---|---:|---:|---:|
| 20A / 20B | 9,879 | 14,113 | 12,463 |
| 21A / 21B | 11,387 | 35,498 | 22,257 |
| 23A / 23B | 4,348 | 6,556 | 4,742 |
| 24A / 24B | 2,555 | 5,977 | 3,970 |
| 22A / 22B | existing TF union | existing TF union | existing TF union |

## Routing rules

- Module 20 receives LR and ligand-target records by default, preserving
  complexes, cofactors, decoys, soluble forms, and species.
- Module 21 receives relay and causal/pathway context. It does not inherit a
  receptor-to-adaptor/kinase/TF claim without separate primary evidence.
- Module 23 receives ECM, adhesion, guidance, and mechanotransduction records.
  Matrix catalog membership and PPI context remain non-direct until reviewed.
- Module 24 receives complement, coagulation, lipid, protease, kinin,
  purinergic, and related boundary records. Cleavage, activation, mediator
  identity, and compartment must be verified separately.
- Each A-layer route has a matching B-layer staging target. No new record was
  written to the frozen B-layer graph/database.

## Evidence and corroboration queues

The full staging artifacts are in
`data/processed/module20_24_database_intake_v1/`:

- `database_candidate_leads.tsv` — all imported database leads
- `database_literature_leads.tsv` — one row per lead–PMID link with retrieved
  PubMed metadata/abstract where available
- `module_*_database_literature_review_queue.tsv` — module-specific deduplicated
  review queues
- `module_*_database_literature_priority_packet.tsv` — bounded priority slices
- `cross_module_paper_corroboration_queue.tsv` — papers used by more than one
  module, requiring independent corroboration before cross-module promotion
- `database_no_linked_literature_leads.tsv` — source rows requiring linked-paper
  acquisition or gap searching

The triage score and `review_high_priority` labels are abstract-level routing
signals only. They do not create canonical Paper, Observation, AuthorClaim, or
SignalingEdgeSource records.

## Module-by-module evidence review pass

Bounded abstract review and corroboration staging now cover all 230 priority
rows. The module table below reports the staged abstract disposition:

| Module | Agent-reviewed rows | Abstract-supported candidates | Full-text holds | Context/no-exact-support |
|---|---:|---:|---:|---:|
| 20A | 80 | 46 | 21 | 13 |
| 21A | 60 | 33 | 12 | 15 |
| 23A | 60 | 26 | 8 | 26 |
| 24A | 30 | 10 | 4 | 16 |

Agent decisions are preserved in `agent_reviews/` and merged into
`database_evidence_decisions_merged.tsv`. Provisional module evidence is
materialized in `agent_evidence_staging.tsv` with
`canonical_eligible=false`.

`module20_24_evidence_summary.tsv` is the module-level routing view. It keeps
the complete database review queue counts alongside the staged decisions and
shows where reviewed rows are handed off: Module 20 binding, Module 21 relay,
Module 23 ECM/adhesion, and Module 24 complement/coagulation/lipid/protease
boundaries.

The cross-module handoff queue records papers whose abstracts suggest more
than one layer. A destination module must independently confirm its claim; a
paper that supports a Module 20 ligand/receptor relationship does not
automatically establish the Module 21 relay, Module 22 TF/program, Module 23
adhesion, or Module 24 boundary consequence.

Ten manually cross-checked records are also in
`manual_cross_module_evidence.tsv`, with 15 retrieved PubMed records. Examples
include CTGF/CCN2–integrin/TrkA with NF-kB/ZEB1 consequences, IL-4/IL-13
JAK/STAT branches with downstream inflammatory genes, OSM–JAK/STAT/CREB
signaling, APOE–TREM2 microglial signaling, C1q-like–BAI3 synaptic adhesion,
and S19-dimer/C5a-receptor mimicry. These remain staging records and are not
canonical promotions.

The explicit corroboration ledger is `manual_corroboration_evidence.tsv`, with
23 manual corroboration rows and 38 locally retrieved PubMed records in
`manual_corroboration_pubmed_records.tsv`. It records exact, partial, and
family-level corroboration separately; family-level support does not satisfy
the exact-pair promotion gate.

For the remaining staged rows with linked second PMIDs,
`agent_review_corroboration_packets.tsv` contains 1,822 primary/secondary
abstract pairings across 127 staged rows. These packets are review inputs only;
they do not by themselves change the underlying disposition or create a
canonical evidence record.

The returned corroboration adjudications are preserved in
`corroboration_agent_decisions.tsv` (230 agent decisions), with five
URL-decoding corrections in `corroboration_reconciliation.tsv` and 23 explicit
local corroborations in `manual_corroboration_evidence.tsv`. The unified
`module20_24_corroboration_adjudication.tsv` contains 258 staging-only
adjudications. Agent-cited PMIDs are materialized in
`agent_corroboration_pubmed_records.tsv`; all decision PMIDs are checked
against retrieved local records by the audit.

## Release gate

`database_intake_audit_manifest.json` reports `status=pass`. It confirms module
routing consistency, unique lead IDs, PMID provenance, imported-source
availability, and an empty frozen-path diff relative to `eeb9960`.

The next phase is full-text review of priority packets, independent
corroboration for reused papers, acquisition of the planned database snapshots,
and targeted gap searches. Only after those decisions are complete should any
reviewed rows be considered for module-specific promotion.
