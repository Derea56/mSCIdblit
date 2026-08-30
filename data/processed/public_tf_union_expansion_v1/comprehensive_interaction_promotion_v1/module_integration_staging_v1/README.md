# Public TF module integration staging

This directory is an additive, review-only module staging layer generated from the comprehensive public-TF review queue and promotion overlay. It does not write canonical TF, Module 22B, SignalingEdge, Regulon, or other database rows.

All reviewed A-E rows are retained. Rows are split one-per-explicit-module assignment; multi-module assignments remain separate, and rows without an explicit module route remain in `catalog_only_evidence.tsv`. The original textual evidence tier is kept unchanged. A/B/C retain ranking aids of 3/2/1; D/E are screening-only with rank 0, `source_exportable=false`, and `module_materialization_allowed=false`. U rows are excluded. Source registry, record, review, species, effect, citation, mechanism, limitation, and raw snapshot fields are copied when present; queue-level provenance is retained for reviewed D/E rows.

See `module_integration_staging_manifest.json` for counts and the explicit no-materialization policy. The deterministic screening overlay is in `module_screening_decisions.tsv`, with the provisional module-owner candidate set in `module_owner_candidate_set.tsv` and its counts in `module_screening_summary.json`. D/E rows are marked `screen_out_low_tier` plus `retain_for_context_only`. Explicitly noncanonical A/B rows are routed to `noncanonical_gene_expression_regulators.tsv` as module-context candidates. The vocabulary is orthogonal: `regulator_role_class` records regulator biology; `evidence_weight_tier` records reviewed evidence strength; `sci_context_status` records SCI relevance; `module_fit_status` records module routing; and `materialization_lane` records the possible destination. The legacy `canonical_tf_eligible` field remains for compatibility but is a role/materialization gate, not an SCI-context result. A/B/C rows with an explicit module route are candidates pending module-owner approval, not approved canonical records.

`mechanism_evidence_type` and `mechanism_evidence_definition` make the
proposed molecular bridge explicit. For example,
`indirect_extracellular_signal_to_target_rna` means an external
ligand/protease/receptor relay is associated with a downstream target-RNA
change; it does not claim that every intermediate step or target-promoter
occupancy was demonstrated. Other values distinguish direct sequence-specific
TF binding, chromatin/cofactor regulation, RNA-level regulation, protein
modification, complex/architecture evidence, and expression/perturbation
association.

The fillable 49-row owner packet is `noncanonical_module_owner_review.tsv`.
Use the controlled decisions and rubric in `noncanonical_module_owner_review_rubric.md`;
all rows start as `pending_review`, and the machine-readable packet summary is
`noncanonical_module_owner_review_summary.json`.

The conservative AI pre-screen is in `noncanonical_module_owner_prescreen.tsv`.
It identifies 27 rows needing additional module/SCI context and 22 rows to
retain as context-only. It does not change the owner decision field, alter
evidence tiers, or authorize materialization.

The mechanism-scope triage is in `noncanonical_module_context_triage.tsv`.
It identifies 35 module-context rows (31 unique pair keys) for focused
module/SCI review and 14 rows (9 unique pair keys) that remain upstream or
protein-level context only. This is still a pre-review recommendation; all
owner decisions remain pending. The former rows are marked
`regulator_role_class=noncanonical_gene_expression_regulator`; the latter are
marked `non_transcriptional_regulator`. Both retain their evidence tier and
carry an independent SCI-context status.

The current adjudication overlay is `noncanonical_module_context_adjudication.tsv`.
All 35 candidates remain `needs_more_context` because the existing records do
not yet satisfy the SCI target-cell/module-context or corroboration gates.
Owner approval remains pending; no noncanonical or canonical materialization
has occurred.

The graded-context registry is `context_evidence_adjudications.tsv`. It contains
3,065 promotion records: 31 A, 30 B, and all 3,004 C records. Context is now ordinal: L0 means no
context evidence, L1 means non-CNS evidence, L2 means CNS evidence, L3 means
spinal-cord-tissue evidence, and L4 means SCI evidence. A component-level SCI
result never upgrades `context_level_exact_pair`.

`context_evidence_scope=not_assessed` identifies rows still awaiting a context
review; `context_evidence_scope=no_qualifying_context_found` identifies a
bounded L0 result. `sci_context_status` and `evidence_weight_tier` remain
separate axes.

The C-tier context pass is resumable for the current evidence packet in
`c_tier_context_review_queue.tsv`: all 3,004 unique
regulator-target-species relationships are retained, including 2,459
module-routed relationships and 545 catalog-only relationships. The queue
retains all module assignments and source-record identifiers and is ranked first
for canonical multi-module relationships, then canonical single-module
relationships, unresolved multi-module and single-module relationships, and
finally catalog-only relationships. All 3,004 C records now have an
adjudication. Round 240 rechecked the 16 records that previously had L0 for
both components, using species-matched HPA, NCBI, MGI, and primary-literature
sources; all 16 gained component context, while their exact pairs remained L0.
The remaining exact-pair L0 values are not component-level no-evidence claims.
They preserve the separation between source-table pair membership and
independent component context. This is not a claim of exhaustive literature
absence and does not change any C tier. Search-round ledgers are preserved as
`c_tier_context_search_round_001.tsv`,
`c_tier_context_search_round_002.tsv`, and
`c_tier_context_search_round_003.tsv`, and
`c_tier_context_search_round_004.tsv`.
The TFLink source citation alone is not treated as context evidence. Round 240
search details are retained in the updated rows of the earlier round ledgers;
the `round_240_` marker identifies the cumulative recheck fields. No canonical
or module materialization was performed.

Round 241 added a provenance-only audit for the 2,994 C-tier records whose
exact-pair context remains L0. Every row matched its species-specific TFLink raw
snapshot, the recorded SHA-256, the regulator and target symbols, organism, and
source metadata. The audit is
`c_tier_exact_pair_source_chain_audit.tsv`; its verified result does not upgrade
context, establish causality, or substitute for direct exact-pair evidence.
Round-241 attachment fields were added to all 2,994 corresponding ledger rows.
Round 242 added two component-only upgrades without changing any exact-pair
level: the mouse target `2610001J05Rik/Smim30` gained L3 spinal-cord tissue
context from Allen Mouse Brain Atlas ISH, and mouse `Actr2` gained L2 CNS
context from Human Protein Atlas mouse-brain evidence. The corresponding
`AHCY -> 2610001J05Rik` and `MFSD11 -> Actr2` exact pairs remain L0 because no
direct pair mechanism or occupancy was verified. These decisions are recorded
in `c_tier_context_search_round_242.tsv` and the cumulative ledger rows.
The Round-242 PubMed exact-pair screen was not completed after transient NCBI
resolver failures; failed requests were not treated as no-evidence outcomes.
Round 243 closed the remaining ledger-coverage gap for 43 C-tier L0 rows that
lacked an explicit literal-symbol exact-pair search record. A bounded PubMed
web screen was recorded for each row; no direct species-matched pair mechanism
or occupancy was found, and all 43 exact-pair levels remain L0. Same-article or
component-only candidates were retained as rejected candidates, not promoted
evidence. The rows and exact search locators are in
`c_tier_context_search_round_243.tsv`.
