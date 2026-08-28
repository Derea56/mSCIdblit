# Comprehensive public interaction promotion overlay

This overlay promotes exact regulator-target-species findings from the
reviewed public-TF evidence batches into a broad interaction catalog. It is
separate from the strict canonical TF and Module 22B write path.

The overlay contains 3,065 exportable evidence rows: four strict
sequence-specific TF edges, one broader functional sequence-specific TF edge,
five additional direct-binding/reporter or functional TF-context rows, 27
role-specific noncanonical exact-pair rows, and 3,028 TFLink source-table
binding/association rows. The noncanonical rows include chromatin, cofactor,
RNA, kinase/PTM, receptor/relay, ligand, lipid, ubiquitin, protein-association,
and downstream-expression mechanisms. They retain their mechanism labels and
are not relabeled as canonical TF edges.
Noncanonical rows retain
their mechanism and are routed to the appropriate receptor/relay, ligand,
RNA, chromatin, cofactor, kinase, lipid, ubiquitin, or protein/PTM category;
they are not relabeled as canonical TF edges. Species, model, assay, direction,
primary/corroborating citations, source record IDs, and limitations are copied
from the reviewed pair records.

The promotion is catalog-level only. `canonical_write_performed=false` for all
rows, and no canonical TF, Module 22B, or other database materialization was
performed. Lack of SCI target-cell validation is retained as a context
qualifier rather than used as an exclusion from this comprehensive catalog.

The follow-up queue identifies the next evidence needed to strengthen each
promoted interaction: independent corroboration, orthogonal assay or
perturbation, and/or better target-cell/tissue context. See
`promotion_followup_evidence_queue.tsv` and `promotion_manifest.json`.

`followup_search_log.tsv` records the follow-up search outcomes, including
positive corroboration, cross-species context, same-study hits, and
mechanism-specific near-matches that were deliberately not counted as
independent support.

`followup_promoted_interactions.tsv` is a separate catalog-level promotion
overlay for exact follow-up findings. Its validation is recorded in
`followup_promotion_validation.json`; it does not write canonical TF or
Module 22B records.

`evidence_priority_queue.tsv` is the reproducible search-planning queue for
unpromoted pair groups. It aggregates repeated provenance-aware rows at the
regulator-target-species level while retaining source registries, source record
IDs, review IDs, statuses, citations, and module hints. The queue assigns an
explicit search lane and next action; already promoted pairs are routed to the
separate follow-up queue, while unresolved, near-match, and database-only rows
remain visible but are not active manual-search priorities.

`evidence_search_batch_001.tsv` contains the first 25 active pairs from the
ranked queue. `evidence_priority_summary.json` records the counts and top
active rows for reproducibility. `evidence_search_outcomes.tsv` records
completed searches and prevents those pair groups from reappearing in the next
active packet until they are adjudicated.
