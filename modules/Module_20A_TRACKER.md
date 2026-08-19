# Module 20A: Ligand-Receptor Interaction Architecture for SCI Cell-Cell Signaling - Corpus Building Tracker

## Overview

This module curates the intercellular edge layer required for `mSCS`: which sender-derived ligands can engage which receiver receptors under mouse SCI-relevant conditions, with explicit species labeling, receptor-complex requirements, agonist/antagonist logic, and context boundaries.

The module is intentionally narrower than whole-pathway curation. Its job is to define the extracellular handoff layer cleanly enough that downstream modules can connect receptor engagement to intracellular relay logic.

**Status**: ACTIVE DATABASE-FIRST LR INTAKE / HIGH PRIORITY FOR `mSCS`.

## Core Questions

- Which ligands are actually plausible sender outputs in SCI-relevant contexts?
- Which receptors or receptor complexes do they bind?
- Are co-receptors, antagonists, decoy receptors, or soluble forms required for interpretation?
- What evidence is mouse primary, human primary, both, or review-supported only?
- Which ligand-receptor pairs are direct edges versus pathway-membership or contextual support only?

## Scope Boundaries

| Boundary ID | Include | Exclude / Route Elsewhere | Notes |
|---|---|---|---|
| M20A-B001 | Direct ligand-receptor and ligand-receptor-complex interactions | Pure intracellular relay logic without extracellular engagement | Relay logic belongs downstream in Module 21. |
| M20A-B002 | Secreted ligands, membrane ligands, matricellular ligands, complement ligands, lipid mediators, and protease-activated receptor agonists when a receptor edge is defined | General expression of a ligand without receptor-binding support | Expression alone is not an edge. |
| M20A-B003 | Receptor complexes, co-receptors, decoy receptors, antagonists, and soluble receptors | Pathway diagrams that imply all listed nodes directly bind each other | Preserve molecular role explicitly. |
| M20A-B004 | Mouse SCI evidence first; human or non-SCI comparator evidence when clearly labeled | Unlabeled cross-species borrowing | Every edge must preserve species support. |
| M20A-B005 | Cell-type or compartment-specific interaction rules when known | Assuming universal binding across all cell states | Context-specific edges remain context-specific. |

## Priority Ligand Families

First-pass curation should prioritize families most likely to matter for astrocyte and multicellular SCI transition modeling:

- IL6-family cytokines and gp130-family receptors
- TNF superfamily
- IL1 family
- interferons
- chemokines
- BMP/TGF-beta ligands and receptors
- EGF/FGF/PDGF/VEGF families
- WNT ligands and frizzled/co-receptor systems
- Notch ligands and receptors
- complement ligands and receptors
- lipid and protease-activated receptor agonists

## Required Extraction Objects

Every retained ligand-receptor record should capture:

- ligand identity
- receptor identity
- receptor complex or co-receptor requirement
- ligand form if relevant, such as soluble, membrane-bound, cleaved, latent, or complexed
- agonist, antagonist, decoy, or inhibitor role
- species support
- cell-type context if explicitly tested
- injury or comparator context
- direct edge versus review-only context
- figure/text provenance

## Database-First Intake Program

The current Module 20A strategy is database-first rather than pathway-first. The rule is:

1. harvest curated ligand-receptor pairs from defensible external resources
2. normalize and deduplicate those pairs into a mouse-first Module 20A intake list
3. sort each pair into direct-evidence, review-backed, database-only, or boundary/caution buckets
4. only after the intake list is reasonably saturated, start family-specific vertical pathway passes in Modules 21A and 22A

This keeps the extracellular handoff layer comprehensive before we spend time on downstream relay detail for only a few familiar pathways.

### Iterative low-confidence evidence recovery

As of `2026-08-10`, all `2,923` low-confidence rows have passed through a
resumable ledger and 15 disjoint literature-search iterations. The ledger has
`2,923` `searched_pending_curator` rows and zero `unsearched` or `queued` rows.
Worker outputs are triage flags until curator-reviewed; exact source locators,
species support, receptor-complex state, directness, and limitations must be
written into authoritative evidence and decision registers before confidence
changes. Rows that remain unsupported after the completed search are retained
explicitly as low rather than silently dropped. See
`scripts/module20a_iterative_low_search.py` and
`work/module20_db_seed/evidence_search_agents/iterative/`.

The first curator integration pass promoted `83` exact-source, direct-binding
or receptor-function candidates to overall `medium`. No high-confidence calls
or `SignalingEdge` rows were created. Species-specific confidence, source
locators, and caveats are retained in the iterative promotion evidence and
decision registers under `work/module20_db_seed/evidence_escalation_starter/`.

Focused evidence pilot 001 tested a family-focused, mouse-first search on 20
remaining low rows. It integrated two exact-pair primary-source packets to
overall `medium`: ARTN-GFRA1/RET with receptor-selectivity caveats and
DLL3-NOTCH1 as a mouse cis-interaction/cis-inhibition record. The other 18
pilot rows remain low with explicit negative, noncognate, species, paralog,
topology, or nomenclature limitations. No high-confidence call or
`SignalingEdge` row was created. The manifest, 20-row search ledger, and
pilot evidence/decision registers are retained under
`work/module20_db_seed/evidence_search_agents/focused_pilot_001/` and
`work/module20_db_seed/evidence_escalation_starter/`.

The scalable literature-acquisition pilot then searched all `2,838` remaining
lows using 114 Europe PMC batched requests. It returned `35,676` lead rows;
`1,612` pairs had at least one PMID lead and `1,226` had no PMID lead. A
mechanical evidence-signal prefilter routed `414` leads across `414` pairs for
possible local-model or curator review. This retrieval phase made no
confidence changes. Four disjoint agent packets then reviewed all 414
candidates. After final curator reconciliation, 72 exact-pair, source-backed
records were promoted to overall `medium`. A targeted second pass then
re-reviewed 105 unresolved or boundary candidates and promoted 14 additional
	exact-pair records. A final 19-row continuation promoted 12 more exact-pair
		records to `medium`; a 44-row manual/boundary continuation promoted 6 more
		exact-pair records and retained 38 low after the final exact-edge gate. The
	next 44-row literature continuation promoted 9 more exact-pair records and
retained 35 low. The next 44-row continuation promoted 8 more exact-pair
records and retained 36 low. The next 44-row continuation promoted 11 more
exact-pair records and retained 33 low. Continuations 047–050 then promoted
7, 8, 10, and 13 additional records; the final 23-row tail promoted 4 and
retained 19 low. All 331 remaining source-rich candidates were exhausted. No
high-confidence call or `SignalingEdge` row was created. The full lead,
no-hit, query, abstract, source-locator, agent-flag, and final-disposition
outputs are retained under
`work/module20_db_seed/evidence_search_agents/batch_full_002/`.

The integrated queue is now `99` high, `569` medium, `2,664` low, and `197`
uncertain. The authoritative batch-002 provenance files are
`work/module20_db_seed/batch_full_002/all_414_final_disposition_audit.tsv`,
`work/module20_db_seed/evidence_escalation_starter/module20a_batch002_final_evidence_register.tsv`,
and
`work/module20_db_seed/evidence_escalation_starter/module20a_batch002_final_decision_register.tsv`.
The refreshed pair/species index has `239` pairs high in at least one species,
`662` medium-or-lower, and `3,604` uncertain or unassessed; `587` pairs are
present in both mouse and human source sets and `3,918` are not established as
conserved from current sources.
The targeted second-pass provenance is recorded in
`work/module20_db_seed/batch_full_002/boundary_second_pass_105/final_curator_review_audit.tsv`,
`work/module20_db_seed/evidence_escalation_starter/module20a_boundary_second_pass_final_evidence_register.tsv`,
and
`work/module20_db_seed/evidence_escalation_starter/module20a_boundary_second_pass_final_decision_register.tsv`.
The remaining-boundary continuation is recorded in
`work/module20_db_seed/batch_full_002/boundary_second_pass_remaining_019/final_curator_review_audit.tsv`,
`work/module20_db_seed/evidence_escalation_starter/module20a_remaining_boundary_final_evidence_register.tsv`,
and
`work/module20_db_seed/evidence_escalation_starter/module20a_remaining_boundary_final_decision_register.tsv`.
The latest 44-row continuation is recorded in
`work/module20_db_seed/batch_full_002/manual_boundary_continuation_044/final_curator_review_audit.tsv`,
`work/module20_db_seed/evidence_escalation_starter/module20a_manual_boundary_continuation_final_evidence_register.tsv`,
and
`work/module20_db_seed/evidence_escalation_starter/module20a_manual_boundary_continuation_final_decision_register.tsv`.
The latest 44-row literature continuation is recorded in
`work/module20_db_seed/batch_full_002/literature_continuation_044/final_curator_review_audit.tsv`,
`work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation_final_evidence_register.tsv`,
and
`work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation_final_decision_register.tsv`.
The latest 44-row literature continuation 045 is recorded in
`work/module20_db_seed/batch_full_002/literature_continuation_045/final_curator_review_audit.tsv`,
`work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation045_final_evidence_register.tsv`,
and
`work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation045_final_decision_register.tsv`.
The latest 44-row literature continuation 046 is recorded in
`work/module20_db_seed/batch_full_002/literature_continuation_046/final_curator_review_audit.tsv`,
`work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation046_final_evidence_register.tsv`,
and
`work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation046_final_decision_register.tsv`.
Literature continuations 047–051 are recorded in their corresponding audit,
evidence, and decision files under
`work/module20_db_seed/batch_full_002/literature_continuation_047/` through
`literature_continuation_051/` and
`work/module20_db_seed/evidence_escalation_starter/`.
The exhaustion summary is recorded in
`work/module20_db_seed/batch_full_002/literature_continuation_exhaustion_summary.tsv`.

### Seed Database Priority

| Resource | Current Version / Date Checked | Species Usefulness For Module 20A | Why It Matters | Current Limitation In This Repo |
|---|---|---|---|---|
| ConnectomeDB2025 | current release dated `2025-09-25`; checked `2026-08-03` | human backbone with explicit mouse files and broad vertebrate homology support | best current backbone for experimentally supported LR-pair harvesting and evidence follow-up queue construction | still needs pair-by-pair source verification before any `SignalingEdge` is trusted |
| Guide to Pharmacology | version `2026.2`, released `2026-06-15`; checked `2026-08-03` | strong receptor pharmacology and endogenous ligand-target pairing support | especially useful for endogenous ligands, receptor families, agonist/antagonist logic, and complex receptor interpretation | not SCI-specific and not a substitute for pair-specific literature review |
| CellChatDB | original literature-supported resource published `2021`; checked `2026-08-03` via current paper/docs | human and mouse; strong on complexes and cofactors | useful for multimeric receptors, co-stimulatory/co-inhibitory modifiers, and pathway-family organization | partially pathway-oriented and may require stricter separation of direct edges from cofactor context |
| CellTalkDB | site last updated `2020-11-24`; checked `2026-08-03` | human and mouse with literature-linked pairs | useful mouse-first comparator source and evidence harvesting aid | older release, so coverage and maintenance are less current |
| Cellinker | platform/paper checked `2026-08-03` | human and mouse, including small molecules and complexes | useful for broad intake expansion and category coverage | broader resource, so direct mechanistic certainty varies by pair and still needs follow-up |
| CellPhoneDB | current docs checked `2026-08-03` | human only | useful for complex-aware LR structure and naming conventions | human-only, so mouse SCI support cannot be assumed |
| OmniPath curated LR view | current docs checked `2026-08-03` | integrative cross-resource filter rather than single-source truth | useful deduplication and cross-database overlap check | integrated resource, so imported pairs still need source-level review in `mSCIdblit` |

### Module 20A Intake Workflow

| Step | Objective | Required Rule |
|---|---|---|
| 1 | Build a master candidate pair list from prioritized LR databases | Keep the external resource name attached to every imported candidate pair |
| 2 | Normalize ligand, receptor, receptor-complex, and species labels | Do not collapse mouse, human, and orthology-projected support into one unlabeled row |
| 3 | Deduplicate overlapping pairs across databases | Retain all contributing source databases in notes instead of silently merging provenance away |
| 4 | Triage each pair into `direct_evidence_queue`, `review_queue`, `database_only_queue`, or `boundary_queue` | Database presence alone is not enough for a simulator-facing edge |
| 5 | Prioritize mouse SCI-relevant and injury-plausible pairs first | Human-only support can seed the queue, but must stay explicitly labeled |
| 6 | Backfill each retained pair with review or primary literature support | Only then can the pair advance toward `SignalingEdge` / `SignalingEdgeSource` curation |

### Evidence Escalation Rule

- External LR databases are seed inventories, not final truth tables.
- A pair can be tracked in Module 20A before it is graph-ready.
- A simulator-facing `SignalingEdge` should be created only after at least one anchored `SignalingEdgeSource` path exists and the pair is still judged to be a true mechanistic edge.
- When a database pair looks plausible but the source support is weak, contradictory, or only expression-based, keep it in Module 20A as boundary or unresolved context rather than forcing it into the graph.

### Local-Model Batch Status

- `2026-08-04`: local triage is complete and structurally validated for CellChatDB.mouse `Secreted Signaling` (`793` rows), Guide to Pharmacology mouse-priority (`75` rows), and CellChatDB.mouse `ECM-Receptor` (`435` rows). Outputs live under `work/module20_db_seed/overnight_runs_v2/`; raw responses are preserved for audit and are not curation evidence.
- `2026-08-04`: those three completed overnight lanes were audited and materialized into deterministic curator review slices using `scripts/export_module20_seed_triage_review_slices.py`. Per-lane outputs now live under each run directory's `review_slices/`, and the combined cross-lane slice set lives under `work/module20_db_seed/overnight_runs_v2/review_slices_consolidated/`.
- Current consolidated completed-lane counts are `1303` rows total: `612` `boundary_review`, `528` `keep_direct_seed_with_caution`, `151` `keep_direct_seed`, and `12` `defer_lower_priority`; actions are `1091` `review_then_primary`, `115` `primary_first`, and `97` `hold_for_later_family_pass`.
- Current consolidated family breadth across those completed overnight lanes is led by `guidance_ecm_family` (`446`), `wnt_notch_family` (`352`), `chemokine_family` (`155`), `tgfb_bmp_family` (`130`), `growth_factor_family` (`116`), and `complement_family` (`93`).
- Do not automatically accept `CellChat:CCL8_ACKR4` as a direct edge: the local model placed it in `keep_direct_seed`, but ACKR-family rows require source-backed atypical/decoy-receptor review before any promotion.

- `2026-08-04`: all `20` ConnectomeDB2025 mouse direct-seed microchunks were run through the local model and saved under `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/outputs/`.
- This completed the generation step for the first database-first intake pass across the current direct-only seed set.
- After parser hardening plus targeted reruns, the current mechanical validation pass using `scripts/validate_connectomedb_lr_batch.py` now recovers `483 / 483` rows into a normalized merged TSV and mechanically repairs `108` rows without inventing fields.
- The rerun queue is now empty for the current ConnectomeDB2025 mouse direct-seed microchunk batch.
- The final holdout, `chunk_05`, required a chunk-specific strict rerun prompt because the broad template repeatedly echoed `boundary_review` into the `next_action` field. That failure mode is now documented by the preserved strict prompt file under `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/prompts/chunk_05_prompt_strict.txt`.
- Treat the validated merged TSV as the current curator-facing triage artifact and treat the rerun queue as unfinished intake rather than silently accepting malformed output.
- `2026-08-04`: the validated merged TSV was further materialized into deterministic curator review slices using `scripts/export_connectomedb_lr_review_slices.py`, with outputs under `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/`.
- Current mechanical triage counts from the exported summary are `304` `keep_direct_seed`, `57` `keep_direct_seed_with_caution`, `118` `boundary_review`, and `4` `defer_lower_priority`; action counts are `369` `review_then_primary`, `70` `primary_first`, and `44` `hold_for_later_family_pass`.
- Current family-level breadth from the exported summary is led by `guidance_ecm_family` (`182`), `wnt_notch_family` (`91`), `growth_factor_family` (`43`), `tgfb_bmp_family` (`43`), `chemokine_family` (`42`), `il_family` (`39`), `tnf_family` (`33`), `complement_family` (`31`), `damp_purinergic_tlr_family` (`26`), and `interferon_family` (`7`).
- The current curator-first queue order is `01_keep_direct_seed_review_then_primary.tsv`, then `02_keep_direct_seed_with_caution_review_then_primary.tsv`, then `04_primary_first.tsv`, then `03_boundary_review.tsv`, then `05_hold_for_later_family_pass.tsv`.
- `2026-08-04`: `GuideToPharmacology` was added as the second real database-seed lane for Module 20A using `scripts/export_gtopdb_module20_priority_seeds.py`. The current normalized GtoPdb exports are under `work/module20_db_seed/gtopdb_module20_priority_seeds/`.
- The first GtoPdb normalization pass retains `1994` mouse-or-human endogenous pairing rows in the all-table export and `480` priority-family rows in the filtered Module 20A export.
- Current GtoPdb priority-family breadth is led by `chemokine_family` (`174`), `complement_family` (`128`), `growth_factor_family` (`80`), `il_family` (`58`), `damp_purinergic_tlr_family` (`46`), `tgfb_bmp_family` (`25`), `tnf_family` (`25`), `interferon_family` (`21`), `wnt_notch_family` (`11`), and `guidance_ecm_family` (`10`).
- Current GtoPdb species balance is strongly human-heavy in the first normalized pass (`405` human target rows, `75` mouse target rows), so this source should be treated mainly as a comparator-expansion lane rather than a mouse-first replacement for ConnectomeDB.
- `2026-08-04`: `CellChatDB.mouse` from the maintained `jinworks/CellChat` package was added as the third real database-seed lane for Module 20A using `scripts/export_cellchatdb_module20_priority_seeds.py`. The normalized exports are under `work/module20_db_seed/cellchatdb_module20_priority_seeds/`.
- The first CellChat normalization pass exports `3379` mouse interaction rows total and retains `1280` priority-family rows after Module 20A family filtering.
- Current CellChat priority annotation breadth is `793` `Secreted Signaling`, `435` `ECM-Receptor`, `50` `Cell-Cell Contact`, and `2` `Non-protein Signaling`.
- Current CellChat priority-family breadth is led by `guidance_ecm_family` (`461`), `wnt_notch_family` (`377`), `tgfb_bmp_family` (`130`), `growth_factor_family` (`118`), `chemokine_family` (`106`), `complement_family` (`52`), `tnf_family` (`29`), `il_family` (`23`), `interferon_family` (`19`), and `damp_purinergic_tlr_family` (`2`).
- Current CellChat directness-note balance is `617` `seed_candidate_complex_or_cofactor_context`, `435` `seed_candidate_ecm_or_adhesion_context`, `176` `seed_candidate_simple`, `50` `seed_candidate_contact_context`, and `2` `seed_candidate_nonprotein_or_mediator_context`, so this source should be treated as a structure-rich seed inventory and not a direct-edge truth table.
- Current CellChat row-version balance is `1241` `CellChatDB v1` rows and `39` `CellChatDB v2` rows inside the priority-family export.
- `Cellinker` remains registered but not ingested because the official direct download currently returns `Invalid Request`; keep that source blocked until a real payload is recovered.
- No `SignalingEdge` or downstream simulator-facing record should be materialized from this batch without pair-level review and source-backed evidence escalation.

- `2026-08-07`: built the consolidated one-row-per-pair index at `work/module20_db_seed/evidence_escalation_router/module20a_pair_species_confidence_index.tsv` using case-insensitive pair-key deduplication. It currently contains `976` unique pair rows from the `1003` router labels after collapsing `27` capitalization-only duplicates.
- Each row carries separate mouse and human confidence tiers, a `high_confidence_species` extraction field, source presence flags, human ortholog-mapping status, and a conservative conservation status.
- `conserved_between_mouse_and_human` is `yes` only when the normalized pair is present in both current mouse-source rows and human-source rows from the full GtoPdb priority export. Mouse-only, mouse-plus-human-ortholog-mapping, and human-only cases are marked `not_established`; absence is explicitly non-evidence.
- The index currently has `71` pairs present in both species source sets, `347` mouse pairs with human ortholog mapping only, and `558` mouse-source-only pairs. These are source-coverage statements, not claims that the pair is biologically absent from the other species.

### CellChat and LIANA comparison

- `2026-08-07`: compared the canonical Module 20A index against the normalized `CellChatDB.mouse` priority-family table and the frozen LIANA mouse consensus resource. Outputs are under `work/module20_db_seed/evidence_escalation_router/module20a_cellchat_liana_*`.
- Comparison uses exact case-insensitive ligand-receptor pair keys. It does not infer aliases, complex decomposition, orthology equivalence, or family-level equivalence.
- Module 20A contains `976` normalized pair keys; CellChat priority contains `1280`; full normalized CellChat contains `3379`; LIANA consensus contains `3989`.
- Exact overlap is `664` with CellChat priority and `602` with LIANA consensus. Module 20A has `212` pairs absent from both comparison sets, while `3529` CellChat-priority-or-LIANA pairs are not currently in Module 20A.
- These differences are discovery queues, not automatic promotions: CellChat includes complex/cofactor/contact/ECM context, and LIANA consensus is a resource union rather than pair-specific evidence.
- `2026-08-07`: audited underscore-delimited multi-component receptor notation in the comparison gaps, including forms such as `Tgfbr1_Tgfbr2`, under `work/module20_db_seed/evidence_escalation_router/module20a_complex_receptor_denotation_*`.
- In the CellChat-priority-or-LIANA missing union, `688 / 3529` external-only pair keys (`19.5%`) use composite receptor notation. Of those, `32` are fully represented by same-ligand component pairs in Module 20A, `80` are partially represented, and `576` have no same-ligand component match.
- Composite notation therefore explains only a bounded subset of the apparent gaps; it should not be used to dismiss the no-match majority without alias and receptor-complex normalization.

### Evidence Escalation Starter Queue

- `2026-08-04`: created a first curator-facing evidence-escalation starter packet under `work/module20_db_seed/evidence_escalation_starter/`.
- The starter TSV currently seeds `7` mouse-priority pairs for the next pass: `S100b -> Ager`, `S100a9 -> Tlr4`, `S100a8 -> Tlr4`, `Cxcl12 -> Cxcr4`, `Ccl21a -> Ccr7`, `Ccl21b -> Ccr7`, and `C3a -> C3ar1`.
- Queue logic is intentionally conservative: favor cross-database convergence or strong overlap with SCI-relevant DAMP/complement axes already curated in Modules `17-19`, but keep all pair-specific directness decisions pending source review.
- Existing local HMGB1-RAGE assets are listed only as receptor-axis orientation anchors for RAGE-adjacent rows; they are not pair-specific proof for `S100b -> Ager`.
- `2026-08-04`: completed a first pair-level evidence audit for those `7` starter rows under `work/module20_db_seed/evidence_escalation_starter/module20a_mouse_direct_seed_evidence_audit.*`.
- Current audit outcome: strongest direct-support packets are `S100a9 -> Tlr4`, `Cxcl12 -> Cxcr4`, and `C3a -> C3ar1`; `S100b -> Ager` and `S100a8 -> Tlr4` remain usable direct seeds but need explicit species/context caution; `Ccl21a -> Ccr7` and especially `Ccl21b -> Ccr7` retain paralog-resolution caution.
- `2026-08-04`: added a machine-readable species-confidence register under `work/module20_db_seed/evidence_escalation_starter/module20a_mouse_direct_seed_confidence_register.tsv`, with `high`/`medium`/`low`/`uncertain` tiers and numeric ranks `3`/`2`/`1`/`0` for downstream thresholding before Module `20B` graph materialization.
- Current mouse-confidence snapshot for the starter set is: `high` for `S100a9 -> Tlr4`, `Cxcl12 -> Cxcr4`, and `C3a -> C3ar1`; `medium` for `S100b -> Ager`, `S100a8 -> Tlr4`, and `Ccl21a -> Ccr7`; `low` for `Ccl21b -> Ccr7`.
- `2026-08-04`: added a row-level evidence provenance register under `work/module20_db_seed/evidence_escalation_starter/module20a_mouse_direct_seed_evidence_register.tsv`, with one row per evidence item preserving source kind, locator, species detail, support kind, source scope, and evidence-item confidence.
- `2026-08-04`: added a receptor-state register under `work/module20_db_seed/evidence_escalation_starter/module20a_receptor_state_register.tsv` so downstream consumers can distinguish `membrane_bound`, `soluble`, `both`, `intracellular_or_noncanonical`, and `unknown` receiver states before Module `20B`.
- Current starter-set receptor-state snapshot is uniformly `membrane_bound` for the `7` audited pairs, while soluble-receptor roles remain a tracked rubric value for future rows that require them.
- `2026-08-04`: added a broader cross-source high-confidence expansion queue under `work/module20_db_seed/evidence_escalation_starter/module20a_cross_source_high_confidence_queue.tsv`.
- That queue currently ranks `14` next-pass pairs because they overlap across `ConnectomeDB2025` and the completed overnight review slices while still landing as `keep_direct_seed` in both sources.
- This expansion queue is intentionally a best-next audit lane, not a promise that every pair will end at `high` confidence; rows should stay `medium` or lower when primary evidence does not justify promotion.
- `2026-08-04`: started the first completed audit mini-batch from that expansion queue under `work/module20_db_seed/evidence_escalation_starter/module20a_cross_source_high_confidence_*`.
- Current audited expansion mini-batch outcome: `Csf1 -> Csf1r`, `Tnfsf11 -> Tnfrsf11a`, `Xcl1 -> Xcr1`, `Tnfsf9 -> Tnfrsf9`, `Cxcl10 -> Cxcr3`, `Ccl11 -> Ccr3`, `Cxcl11 -> Cxcr3`, `Cxcl9 -> Cxcr3`, `Egf -> Egfr`, `Btc -> Egfr`, and `Btla -> Tnfrsf14` now carry logged source packets with `high` mouse confidence.
- `Tnfsf14 -> Tnfrsf14`, `Cxcl13 -> Cxcr5`, and `Tnfsf13 -> Tnfrsf17` remain retained direct pairs, but the currently logged mouse packet is still weaker than the corresponding human or broader direct-support packet, so their mouse confidence should remain below `high` until a cleaner mouse packet is logged.
- `2026-08-04`: opened a second-wave SCI-priority queue under `work/module20_db_seed/evidence_escalation_starter/module20a_second_wave_sci_priority_queue.tsv` centered on DAMP/TLR rows plus a few canonical inflammatory anchors.
- The first completed mini-batch from that second-wave queue now logs `Tnf -> Tnfrsf1a`, `Tnf -> Tnfrsf1b`, `Ccl19 -> Ccr7`, and `Ccl20 -> Ccr6` as `high` mouse-confidence retained direct pairs under `work/module20_db_seed/evidence_escalation_starter/module20a_second_wave_sci_priority_*`.
- `2026-08-04`: extended that second-wave audit packet with harder SCI-relevant DAMP rows: `Hmgb1 -> Tlr2`, `Hmgb1 -> Havcr2`, `Saa1 -> Tlr2`, `S100a9 -> Ager`, `Saa1 -> Tlr4`, `Dcn -> Tlr2`, `S100a8 -> Ager`, and `Lgals9 -> Tlr4`.
- Current second-wave confidence posture should stay explicitly mixed: `Saa1 -> Tlr4` reaches `high` mouse confidence, `Hmgb1 -> Tlr2`, `Hmgb1 -> Havcr2`, `Saa1 -> Tlr2`, `S100a9 -> Ager`, `Dcn -> Tlr2`, and `Lgals9 -> Tlr4` remain retained but below `high`, and `S100a8 -> Ager` remains retained with only `low` species confidence pending a cleaner mouse- or human-matched direct packet.
- `2026-08-04`: opened and completed a small database-citation fast-path trial under `work/module20_db_seed/evidence_escalation_starter/module20a_database_citation_fast_path_trial_*` to test whether database-linked literature plus one strong review can accelerate canonical Module 20A rows without broad independent searching.
- Current fast-path trial rows are `Slit2 -> Robo1`, `Slit2 -> Robo2`, `Vegfc -> Flt4`, and `Lgals9 -> Havcr2`.
- Early result: the fast path is materially quicker for canonical rows with real citation trails, but species-aware confidence still has to stay conservative when the packet is review-heavy or broader than a clean pair-isolated primary source.
- `2026-08-04`: completed a second, larger fast-path batch under `work/module20_db_seed/evidence_escalation_starter/module20a_database_citation_fast_path_batch2_*` to test whether the same workflow still holds on a less cherry-picked canonical set.
- Current batch-2 rows are `Hgf -> Met`, `Pgf -> Flt1`, `Vegfa -> Flt1`, `Vegfb -> Flt1`, `Vegfd -> Flt4`, `Slitrk1 -> Ptprd`, `Slitrk1 -> Ptprs`, `Slitrk2 -> Ptprd`, `Slitrk2 -> Ptprs`, and `C3 -> Cr2`.
- Current batch-2 result: growth-factor rows still clear quickly and mostly strongly; family-structured synaptic adhesion rows clear quickly but usually stay at `medium` confidence; complement rows can clear fast if fragment specificity is kept explicit.
- `2026-08-04`: added an effort-routing layer for the remaining main Module 20A queues using `scripts/route_module20_evidence_effort.py` plus the local rubric `work/module20_db_seed/evidence_escalation_starter/module20a_evidence_effort_routing_rubric.md`.
- Current router outputs live under `work/module20_db_seed/evidence_escalation_router/` and currently classify `1037` queue rows (`1003` unique pair labels) into `145` `fast`, `393` `medium`, and `499` `hard` row-level work tiers.
- Current router behavior is intentionally throughput-oriented rather than perfection-oriented: simple canonical `CellChat` and `GuideToPharmacology` rows can now clear into `fast`, while `ConnectomeDB2025` rows without local citation packets stay mostly `medium`, and atypical receptors, DAMP/TLR rows, and multicomponent receptor rows stay `hard`.
- `2026-08-04`: started consuming the routed `fast` backlog directly with a new timing batch under `work/module20_db_seed/evidence_escalation_starter/module20a_database_citation_fast_path_batch3_*`.
- Current batch-3 rows are `Areg -> Egfr`, `Bdnf -> Ngfr`, `Btc -> Erbb4`, `C3 -> C3ar1`, `C5a -> C5ar1`, `CCL1 -> Ccr8`, `CCL19 -> Ccr7`, `CCL20 -> Ccr6`, `CCL22 -> Ccr4`, and `CCL25 -> Ccr9`.
- `2026-08-04`: added a generated evidence-reuse layer using `scripts/build_module20_evidence_reuse_registry.py`, with reusable packet outputs under `work/module20_db_seed/evidence_escalation_starter/module20a_family_evidence_packets.tsv` and `work/module20_db_seed/evidence_escalation_starter/module20a_citation_reuse_registry.tsv`.
- Current reuse coverage is intentionally narrow and provenance-backed: `5` reusable family packets currently map to `15` routed queue rows, including `12` rows already in the `fast` lane and `3` in the `medium` lane.
- The first reusable packet set covers VEGF or PlGF to FLT-family rows, EGFR or ERBB-family ligand rows, Slit-Robo rows, Slitrk to type-IIa RPTP rows, and complement fragment receptor rows.
- `2026-08-04`: tested the next routed `fast` ten-row batch under `work/module20_db_seed/evidence_escalation_starter/module20a_database_citation_fast_path_batch4_*` as a deliberate no-reuse stress case.
- Current batch-4 rows are `CCL11 -> Ccr5`, `CCL2 -> Ccr5`, `CCL3 -> Ccr5`, `CCL4 -> Ccr5`, `CCL5 -> Ccr3`, `CCL5 -> Ccr5`, `CCL7 -> Ccr1`, `CCL7 -> Ccr2`, `CCL7 -> Ccr3`, and `CCL7 -> Ccr5`.
- Important efficiency finding: `0/10` rows in this batch had reusable packet hits, the local mouse GtoPdb rows were citation-empty for all ten, and the resulting evidence packets remained auditable but mostly low-confidence because support was limited to mouse seed rows plus human comparator PMIDs from the local GtoPdb mirror.
- `2026-08-04`: fixed a router normalization bug in `scripts/route_module20_evidence_effort.py` so audited-pair matching now canonicalizes pair labels instead of missing case-variant duplicates such as `CCL1 Ccr8` versus `Ccl1 Ccr8`.
- `2026-08-04`: tested a larger 30-row routed `fast` batch under `work/module20_db_seed/evidence_escalation_starter/module20a_database_citation_fast_path_batch5_*` after that normalization fix.
- Current batch-5 rows are dominated by citation-poor chemokine and CellChat seed rows: `CCL8 -> Ccr1`, `CCL8 -> Ccr2`, `CCL8 -> Ccr3`, `CCL8 -> Ccr5`, `CX3CL1 -> Cx3cr1`, `CXCL10 -> Ccr3`, `CXCL11 -> Ccr3`, `CXCL16 -> Cxcr6`, `CXCL9 -> Ccr3`, `Ccl17 -> Ccr4`, `Ccl21 -> Ccr7`, `Ccl21d -> Ccr7`, `Ccl21e -> Ccr7`, `Ccl21f -> Ccr7`, `Ccl24 -> Ccr3`, `Ccl26 -> Ccr3`, `Ccl27a -> Ccr3`, `Ccl27b -> Ccr3`, `Ccl28 -> Ccr3`, `Ccl5 -> Ccr1`, `Ccl5 -> Ccr4`, `Ccl6 -> Ccr1`, `Ccl6 -> Ccr2`, `Ccl6 -> Ccr3`, `Ccl8 -> Ccr1`, `Ccl8 -> Ccr2`, `Ccl8 -> Ccr5`, `Ccl9 -> Ccr1`, `Csf3 -> Csf3r`, and `Cx3cl1 -> Cx3cr1`.
- Important timing finding: this 30-row batch completed at about `6.9s/pair`, much faster than the earlier 10-row canonical batches, but the speedup reflects bulk conservative packet logging for sparse-citation rows rather than stronger pair-level validation.
- `2026-08-04`: expanded the reusable packet layer with chemokine-specific canonical and caution packets using `scripts/build_module20_evidence_reuse_registry.py`.
- The new packet set now covers canonical CXCR3 rows, CCR7 cognate-chemokine rows, canonical CXCL12-CXCR4 rows, and caution packets for sparse or nonprincipal CCR3, CCR5, CCR1, and CCR2 chemokine side-pairs.
- `2026-08-04`: exported a whole-fast-lane overview under `work/module20_db_seed/evidence_escalation_router/module20a_fast_lane_overview.*` so we can finish the fast lane first and then return to the medium lane selectively.
- Current whole-fast-lane status is `145` rows total, `145` rows with logged audit packets, `50` rows already flagged as early high-confidence from logged local evidence, `18` rows in a medium-then-targeted bucket, and `85` rows in a low-caution bucket.
- `2026-08-04`: after finishing the fast sweep, exported an all-queue overview under `work/module20_db_seed/evidence_escalation_router/module20a_all_lane_overview.*`.
- Current all-queue split is `73` `high_confidence_early`, `393` `medium_then_targeted`, `77` `low_caution_bucket`, and `494` `hard_followup` rows, which is the real queue-level picture rather than the narrower fast-lane subset.
- `2026-08-04`: started actual medium-lane curation under `work/module20_db_seed/evidence_escalation_starter/module20a_medium_targeted_batch1_*`.
- Current medium-batch-1 rows are `Pdgfa -> Pdgfra`, `Pdgfa -> Pdgfrb`, `Pdgfb -> Pdgfra`, `Pdgfb -> Pdgfrb`, `Pdgfc -> Pdgfra`, `Pdgfd -> Pdgfrb`, `Vegfa -> Kdr`, `Vegfc -> Kdr`, `Vegfd -> Kdr`, and `Ngf -> Ntrk1`.
- Current medium-batch-1 outcome: the PDGF rows now carry logged medium-confidence family-structured packets, the Kdr-facing VEGF rows remain review-led and below promotion, and `Ngf -> Ntrk1` now carries a logged medium-confidence direct packet ready for a later species-specific boost pass.
- `2026-08-04`: extended the medium confidence-boost lane with `work/module20_db_seed/evidence_escalation_starter/module20a_medium_targeted_batch2_*`.
- Current medium-batch-2 rows are `C4a -> C3ar1`, `C4b -> Cr2`, `Inhibin A -> Acvr2a`, `Inhibin B -> Acvr2b`, and `Klk1b4 -> Ntrk1`.
- Current medium-batch-2 outcome: the complement side-pairs now carry explicit low-confidence review-led packets, the inhibin rows now carry medium-confidence family-structured packets with receptor-complex caution, and `Klk1b4 -> Ntrk1` is now explicitly held below promotion because the local source packet points toward `NGF/NTRK1` rather than a clean `Klk1b4/NTRK1` anchor.
- `2026-08-06`: completed medium-targeted batch 7 under `work/module20_db_seed/evidence_escalation_starter/module20a_medium_targeted_batch7_*` for `Fgf17 -> Fgfr1` and `Fgf17 -> Fgfr2`. The original mouse study (PMID `10381577`) supports functional activation of the FGFR1/2 IIIc splice forms in 3T3 fibroblasts; both pairs are retained at medium mouse confidence because the evidence is engineered-cell functional activation rather than clean biophysical binding and is not SCI-specific.
- `2026-08-07`: created the external database review queue under `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`. It contains `3,529` pairs present in CellChat priority and/or LIANA mouse consensus but absent from the pre-review Module 20A index; the first lane was the `21` cross-source simple secreted-signaling rows.
- `2026-08-07`: completed the first external audit batch with `34` evidence rows and `21` decisions under `work/module20_db_seed/evidence_escalation_starter/module20a_external_batch1_*`. The batch resolves `4` pairs as high, `13` as medium, and `4` as low. High mouse-confidence additions are `Ccl2 -> Ccr2`, `Slit1 -> Robo1`, `Slit2 -> Robo1`, and `Wnt5a -> Mcam`.
- Atypical-receptor decisions are role-aware: `ACKR2` and `ACKR4` rows are retained as binding/scavenging interactions rather than being silently treated as conventional G-protein signaling edges. `Gdf15 -> Tgfbr2` is retained only as a medium overall, human-context-specific alternative receptor claim; the canonical `GDF15 -> GFRAL/RET` axis remains separate.
- `2026-08-07`: completed the full external-queue closure pass. All `3,529` queue rows now have row-level decisions: `5` high, `24` medium, and `3,500` low. The low-confidence closure rows carry explicit database-only, citation-unreviewed, LIANA-consensus-only, or unresolved-complex reasons; low is not treated as evidence of absence.
- `2026-08-07`: began targeted primary-source recovery for the external queue. Recovery batches 3–5 added `50` audited decisions covering C1QL-ADGRB3, NTN1/NTN4 guidance receptors, EPGN-EGFR, SLITRK3-PTPRD, MIF receptor complexes, CD23-CR2, complement-fragment/CR3-CR4 edges, AMH receptor complexes, and cited BMP receptor-complex rows.
- `2026-08-07`: recovery batch 6 added `47` medium-confidence FGF-FGFR family packets for CellChat rows carrying an explicit shared literature pointer; LIANA-only lookalikes were not auto-promoted.
- `2026-08-07`: recovery batch 7 added direct packets for NCAM1-FGFR1, vitronectin-uPAR, MMP2-integrin/MMP14 complexes, CNTN1-NOTCH1/2, and APP-DR6. It also documented the likely NTF4-versus-NTN4 nomenclature collision and retained NTN4-NTRK2 at low confidence.
- `2026-08-07`: recovery batch 8 added six audited packets: GDNF-GFRA1/RET and BDNF-NTRK2 were promoted to high; ARTN-GFRA3/RET was promoted to high overall with a human comparator downgrade; ARTN-GFRA1/RET remained low after receptor-selectivity evidence argued against a functional coreceptor assignment; and CCL11/CCL17-ACKR1 were promoted to medium as atypical scavenger/binding edges.
- `2026-08-07`: recovery batch 9 audited the CellChat PMID `22353464` Notch cluster. DLL4-NOTCH4 was promoted to medium from an exact curated binding/function packet; the remaining DLK1, DLL1-NOTCH4, DLL3, DLL4-NOTCH3, and JAG2-NOTCH4 rows received bounded family-level or negative-triage packets and stayed low.
- `2026-08-07`: recovery batch 10 added medium packets for SLITRK4/5/6-PTPRS synaptic adhesion, VCAM1-alphaD-beta2 integrin binding, and cholesterol/DHCR24-RORA/RORC sterol-nuclear-receptor axes. NTN4-UNC5D stayed low because direct binding assays conflict with similarity-based annotation.
- `2026-08-07`: recovery batch 11 added medium packets for six EGF-family receptor-complex rows, promoted IFNB1-IFNAR1/2 and IFNG-IFNGR1/2 to high, and added medium subtype-aware packets for IFNA9, IFNAB, IFNE, and IFNK.
- `2026-08-07`: recovery batch 12 promoted NCAM1 homophilic binding and WNT5A-FZD3 to high, retained NCAM1-L1CAM and WNT5A-FZD6 at medium, and kept NCAM1-NCAM2, NCAM2-L1CAM, and WNT5A-FZD10 low after pair-specific evidence remained unresolved or negative.
- `2026-08-07`: recovery batch 13 added direct RGD-binding packets for the six remaining vitronectin-integrin rows. VTN-ITGAV/ITGB3 was promoted to high; the other five were promoted to medium with receptor-component and integrin-context caveats.
- `2026-08-07`: recovery batch 14 audited the first collagen-I receptor block. COL1A1-ITGA2/ITGB1 was promoted to high; GP6, ITGA10/11/1-ITGB1, and SDC1 were promoted to medium; CD44, ITGA3/9/ITGB1, and ITGAV/ITGB8 stayed low after pair-specific directness remained unresolved.
- `2026-08-07`: recovery batch 15 audited the first laminin receptor block. LAMA1-DAG1 was promoted to high; CD44, ITGA6/ITGB1, ITGA6/ITGB4, and ITGA7/ITGB1 were promoted to medium; exact isoform assignments for ITGA3/ITGB1, ITGA9/ITGB1, ITGAV/ITGB8, and LAMA2-CD44 stayed low.
- `2026-08-07`: parallel recovery batch 16 integrated four disjoint worker packets (`81` decisions) covering collagen-I/II isoform receptors, LAMA2–LAMA4 receptors, thrombospondin/tenascin receptors, and TGFB1/TGFB2 receptor/co-receptor rows. The batch promoted canonical assignments such as LAMA2-DAG1, LAMA2-ITGA6/ITGB1, LAMA3-ITGA3/ITGB1, THBS1-CD36/CD47/integrins, and TGFB1/TGFB2-TGFBR1/TGFBR2; it kept incomplete beta-integrin denotations, indirect transactivation, unsupported ACVR1 composites, and paralog extrapolations low or medium with role caveats.
- `2026-08-07`: credit-controlled recovery batch 17 integrated `160` parallel-worker decisions across COL4A1–COL4A4, LAMA4–LAMB3, tenascin/vitronectin/vWF/C1QL rows, and TGFB3/TGM2/THBS/TIMP rows. Conflicting worker calls were reconciled conservatively; `uncertain` is retained where no pair-specific promotion was justified.
- `2026-08-07`: recovery batch 18 processed the unique portion of the requested 500-row parallel round. It integrated `414` deeper packets; `86` rows overlapped stronger prior recovery batches and were deliberately left unchanged. The new pass primarily resolved canonical FN/Notch/GPCR/adhesion pairs while retaining database-only, shared-subunit, indirect, and unresolved rows at low or uncertain.
- `2026-08-07`: recovery batch 19 completed the next `1,000` queue rows (`M20A-EXT-0801` through `M20A-EXT-1800`) using four disjoint parallel worker packets. It added `1,000` evidence records and `1,000` decisions, with conservative treatment of database-only, shared-subunit, cofactor-dependent, and unresolved-complex rows; canonical coagulation, FGF, and selected growth-factor anchors were promoted where the worker packet supported them.
- After recovery batch 19, all `3,529` queue rows remain row-level reviewed, with `94` high, `283` medium, `2,955` low, and `197` uncertain decisions. The one-row-per-pair index still contains `4,505` unique pair keys. The refreshed index has `233` pairs high in at least one species, `426` medium-or-lower, and `3,846` uncertain or unassessed; `471` pairs are present in both mouse and human source sets, while `4,034` remain not established as conserved from current sources.
- Integration audit after batch 19 found all `3,529` final queue decisions represented in the historical external decision registers (`5,356` records including superseded intermediate decisions; `3,529` unique review IDs), with no queue IDs missing a decision and no decision IDs outside the queue. The queue and pair/species index are therefore the current integrated Module 20A external curation layer; the next pass can focus on promoting the `283` final medium-confidence queue rows.
- `2026-08-07`: completed the four-worker review of all `283` final medium-confidence queue rows in `module20a_external_medium_review_batch20_*`. Four pairs were promoted overall to high: `MIF -> CD74_CXCR2`, `MIF -> CD74_CXCR4`, `FAT4 -> DCHS1`, and `GDF2/BMP9 -> ENG`. Additional human- or mouse-specific high calls were recorded without automatically promoting asymmetric, composite, cofactor-dependent, uptake, or context-limited pairs.
- `2026-08-07`: completed a focused follow-up on the remaining `23` medium rows in the TGFB/TGM2/THBS/THY1/TIMP block (`M20A-EXT-3249` through `M20A-EXT-3304`). None warranted overall high; five received human-specific high confidence while remaining overall medium because of accessory, composite, incomplete-integrin, or context-dependent representations.
- After the medium review, the external queue contains `98` high, `279` medium, `2,955` low, and `197` uncertain decisions. The refreshed pair/species index contains `237` pairs high in at least one species, `422` medium-or-lower, and `3,846` uncertain or unassessed; `473` pairs are present in both mouse and human source sets, while `4,032` remain not established as conserved from current sources.
- `2026-08-07`: low-confidence recovery was intentionally paused for a session handoff. The remaining `2,955` low rows are not uniformly actionable: `328` higher-priority cross-source/CellChat-context rows should be reviewed before the `2,627` priority-8 LIANA-only discovery rows. Resume instructions are recorded in `docs/MODULE20A_HANDOFF_2026-08-07.md`.
- `2026-08-07`: reopened the ConnectomeDB mouse direct-seed curator queue at `work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/priority_queues/01_keep_direct_seed_review_then_primary.tsv`. The queue contains `236` rows; cross-register inspection found `234` already represented in existing evidence packets, so new source escalation was limited to the two uncovered seeds `CDB15:0001286 Rarres2 -> Ccrl2` and `CDB25:0004346 Tafa5 -> Fpr2`.
- `2026-08-07`: completed source-bounded ConnectomeDB direct-seed batch 01 under `work/module20_db_seed/evidence_escalation_starter/module20a_connectomedb_direct_seed_batch01_*`. Both pairs remain medium mouse-confidence candidates. `Rarres2 -> Ccrl2` is explicitly an atypical/non-signaling binding or uptake interaction, and `Tafa5 -> Fpr2` is supported by mouse BMDM antagonist/knockout functional dependence without a purified binding assay. Human confidence remains `uncertain` for both. No `SignalingEdge` rows were created.
- `2026-08-07`: the consolidated completed-overnight `01_keep_direct_seed_review_then_primary.tsv` slice was cross-checked and all `36` rows were already represented in existing evidence packets. A new caution-lane packet then audited `CellChat:IL6_IL6R_IL6ST` and `CellChat:IL33_IL1RL1_IL1RAP` under `work/module20_db_seed/evidence_escalation_starter/module20a_overnight_caution_batch01_*`. `Il6 -> IL6R_IL6ST` remains medium with mouse direct complex support; `Il33 -> IL1RL1_IL1RAP` remains medium overall with high human support but `uncertain` mouse support. Full receptor complexes and the IL-1RAcP coreceptor role are preserved, and no `SignalingEdge` rows were created.
- `2026-08-07`: integrated the four audited packets into the reproducible pair-index build through `work/module20_db_seed/evidence_escalation_router/module20a_audited_pair_confidence_supplement.tsv` and `scripts/build_module20_pair_species_index.py`. The external queue remains `98` high, `279` medium, `2,955` low, and `197` uncertain; the pair index is now `238` high in at least one species, `425` medium-or-lower, and `3,842` uncertain or unassessed. Mouse confidence is `142` high, `458` medium, `3,420` low, `485` uncertain; human confidence is `205` high, `449` medium, `467` low, `3,384` uncertain. No `SignalingEdge` rows were created.
- `2026-08-07`: exported the `328` handoff-priority low rows to `work/module20_db_seed/evidence_escalation_router/module20a_low_confidence_recovery_priority_1_2_6_7.tsv` and integrated low-recovery packet 01. New primary evidence promoted `Amh -> AMHR2_BMPR1A` to medium for mouse complex signaling and `Csf2 -> CSF2RA_CSF2RB` to high for mouse alpha/beta receptor-complex binding/reconstitution; `Wnt5a -> Fzd10` remained low on its existing negative pair-specific screen. The queue is now `99` high, `280` medium, `2,953` low, and `197` uncertain; the index is `239` high in at least one species, `426` medium-or-lower, and `3,840` uncertain or unassessed. No `SignalingEdge` rows were created.
- `2026-08-08`: processed the next `300` prioritized low rows in `module20a_low_recovery_batch02_*`. Exact primary packets promoted six ECM/adhesion candidates to medium: `Agrn -> Dag1`, `Chad -> ITGA2_ITGB1`, `Col4a3 -> ITGA3_ITGB1`, `Fn1 -> ITGA3_ITGB1`, `Lama1 -> ITGA1_ITGB1`, and `Lama1 -> ITGA2_ITGB1`. The qwen triage attempt stalled before valid output and contributed no decisions. The queue is now `99` high, `286` medium, `2,947` low, and `197` uncertain; the index is `239` high in at least one species, `431` medium-or-lower, and `3,835` uncertain or unassessed. No `SignalingEdge` rows were created.
- `2026-08-09`: agent source-review batch 03 completed six disjoint packets covering `240` of the remaining priority-1/2/6/7 low rows. It returned `27` source candidates and integrated six exact-pair primary-literature decisions at medium confidence: `Fn1 -> ITGAV_ITGB1`, `Fn1 -> ITGAV_ITGB3`, `Fn1 -> ITGAV_ITGB6`, `Ibsp -> ITGAV_ITGB3`, `Ibsp -> ITGAV_ITGB5`, and `Reln -> ITGA3_ITGB1`. Type-level/heterotrimer-level collagen VI/IX candidates, the negative `Wnt5a -> Fzd10` screen, and form-limited candidates were retained low. The queue is now `99` high, `292` medium, `2,941` low, and `197` uncertain; the index is `239` high in at least one species, `437` medium-or-lower, and `3,829` uncertain or unassessed. No `SignalingEdge` rows were created.
- `2026-08-10`: source review batch 04 integrated six primary-literature evidence rows and three medium-with-caution decisions. `Npnt complex 1/2 -> ITGA8_ITGB1` are supported by mouse nephronectin-alpha8beta1 binding/association but retain unresolved Fras/Frem co-ligand composition; `Vwf -> GP complex` is supported by human vWF binding to platelet GP receptor complexes but retains exact-subunit and mouse-context caveats. The queue is now `99` high, `295` medium, `2,938` low, and `197` uncertain; the index is `239` high in at least one species, `440` medium-or-lower, and `3,826` uncertain or unassessed. No `SignalingEdge` rows were created.
- `2026-08-10`: source review batch 05 integrated six primary-literature evidence rows and six cautious medium decisions for `Col6a1/2/3 -> ITGA1_ITGB1` and `Col6a1/2/3 -> ITGA2_ITGB1`. PMID `8387021` directly supports native collagen-VI binding to purified alpha1beta1 and alpha2beta1 integrins in human assays; the individual Col6a chain labels remain unresolved representations of the multichain ligand, with mouse and SCI context unknown. The queue is now `99` high, `301` medium, `2,932` low, and `197` uncertain; the index is `239` high in at least one species, `446` medium-or-lower, and `3,820` uncertain or unassessed. No `SignalingEdge` rows were created.
- `2026-08-10`: independently verified agent review batch 06 integrated nine primary-literature evidence rows and nine cautious medium decisions: `Cd47 -> Sirpa`, `Cntn1 -> Ptprz1`, `Cntn3/4/6 -> Ptprg`, `Csf1_Il34 -> Csf1r`, `Dkk1 -> Lrp6`, `Gdf11 -> Acvr2b_Tgfbr1`, and `Lama2 -> ITGA1_ITGB1`. Composite ligand/receptor, inhibitory Wnt-coreceptor, neural adhesion, and receptor-complex caveats remain explicit; unverified or contradictory worker flags were not integrated. The queue is now `99` high, `310` medium, `2,923` low, and `197` uncertain; the index is `239` high in at least one species, `455` medium-or-lower, and `3,811` uncertain or unassessed. No `SignalingEdge` rows were created.

## TLR Pilot Block

The earlier TLR-first work is retained as a pilot curation block, not the top-level Module 20A workflow. It remains useful for stress-testing how database-seeded pairs will later be followed into Modules 21A and 22A.

### TLR Entry Inventory

| TLR Axis | Candidate Signal | Receptor or Complex | Species Tier | Current Support Level | Current State | Key Source PMIDs | Current Take |
|---|---|---|---|---|---|---|---|
| TLR2 | Pam3CSK4 | TLR2/TLR1 | mouse | direct agonist entry | ACCEPTED ENTRY | `28445714`, `17889651` | strongest current Module 20A TLR entry pair because it combines a direct receptor-pair structural anchor with mouse SCI entry and output evidence |
| TLR2 | Pam2CSK4 | canonical TLR2/TLR6 | mouse plus comparator | canonical receptor-pair support with caution | ACCEPTED COMPARATOR ENTRY | `23826682`, `19440307`, `15580661` | first diacyl comparator for testing receptor-pair, kinetic, and output divergence from Pam3CSK4 |
| TLR2 | MALP-2 | TLR2/TLR6 | comparator | strong direct receptor-pair assignment | ACCEPTED COMPARATOR ENTRY | `11431423`, `25077631`, `10569741`, `21124967` | clean TLR2/TLR6 comparator with better direct receptor-pair support than FSL-1 and useful relay/output divergence |
| TLR2 | FSL-1 | likely TLR2/TLR6-class ligand | comparator | strong class-level assignment, less direct structural anchoring | PROVISIONAL COMPARATOR ENTRY | `23271927`, `17316370`, `19440307` | useful for chemokine, IL-1beta, and phagocytosis-related divergence, but receptor-complex certainty is weaker than MALP-2 |
| TLR2 | LTA | TLR2-containing entry with unresolved clean pair specificity | mouse plus human comparator | receptor-supported but purity and pair-specificity remain less clean | BOUNDARY / DIVERGENCE ENTRY | `19440307`, `12011760`, `18468694` | most useful as a divergent-behavior comparator because it shows delayed kinetics and weaker in vivo inflammatory behavior in the mouse acute-inflammation comparison |
| TLR2 | endogenous sterile DAMP(s) after SCI | TLR2 | mouse | axis relevance only | PROVISIONAL ENTRY | `17403033` | TLR2 clearly matters after SCI, but the current queue does not yet resolve a clean endogenous sterile ligand identity |
| TLR4 | LPS | TLR4 | mouse | direct agonist entry | PROVISIONAL ENTRY | `25044014`, `25990044` | strong TLR4 entry logic and downstream branch evidence, but still exogenous-agonist centered |
| TLR4 | endogenous sterile DAMP(s) after SCI | TLR4 | mouse | axis relevance only | PROVISIONAL ENTRY | `17403033`, `25990044`, `38326029` | TLR4 is strongly relevant after SCI, but the current packet does not yet resolve the entry ligand or co-receptor logic cleanly |
| TLR9 | endogenous DNA-context / DAMP context | TLR9 | mouse | receptor-targeted intervention without resolved ligand identity | PROVISIONAL ENTRY | `30953770`, `32098620` | strong mouse TLR9 SCI axis with antagonist and astrocyte-output evidence; exact endogenous ligand remains unresolved |
| TLR3 | poly(I:C) | TLR3 | non-mouse comparator plus partial mouse spinal context | comparator-heavy | BOUNDARY ONLY | `36216458`, `22565312` | useful entry concept, but current packet is not yet strong mouse traumatic-SCI primary evidence |
| TLR1 | post-SCI expression increase | unresolved | mouse | expression only | DEFER | `17403033` | transcript relevance only so far |
| TLR5 | post-SCI expression increase | unresolved | mouse | expression only | DEFER | `17403033` | transcript relevance only so far |
| TLR7 | post-SCI expression increase; viral spinal comparator | unresolved | mouse comparator | sparse / comparator | DEFER | `17403033`, `33679702` | useful spinal comparator context, but weak sterile-SCI entry evidence |
| TLR8 | none convincing yet | unresolved | none | no direct abstract-level support | DEFER | none | no convincing direct mechanistic SCI entry evidence in the current pass |

### TLR1/2 Ligand Vertical Queue

The first completed vertical-comparison block under Module 20A uses Pam3CSK4 as the anchor and asks how other TLR1/2-axis ligands differ at the entry event before spending heavily on downstream pathway detail.

| Comparison | Module 20A Take | Strongest Divergence Point | Caution |
|---|---|---|---|
| Pam3CSK4 vs Pam2CSK4 | Pam3CSK4 is the cleaner TLR2/TLR1 anchor; Pam2CSK4 is the canonical TLR2/TLR6 comparator | receptor-pair framing, comparator output emphasis, and possible kinetic differences | do not overstate Pam2CSK4 as always strictly TLR2/TLR6 because some systems report TLR6-independent signaling features |
| Pam3CSK4 vs MALP-2 | MALP-2 is the cleanest direct TLR2/TLR6 comparator in the current queue | stronger explicit TLR2/TLR6 receptor-pair evidence and distinct Mal/PI3K/Nrf2/HO-1 relay plus chemokine/output profile | current MALP-2 packet is comparator-heavy rather than SCI-specific |
| Pam3CSK4 vs FSL-1 | FSL-1 is a useful TLR2/TLR6-class comparator | stronger CCL2, IL-1beta, and phagocytosis-related output emphasis | receptor-complex certainty in the current packet is weaker than for MALP-2 |
| Pam3CSK4 vs LTA | LTA is most informative as a divergent-behavior comparator rather than a clean entry edge | delayed NF-kappaB / MAPK kinetics and weaker in vivo leukocyte-recruitment behavior in the mouse acute-inflammation comparison | keep stronger caution on purity, context, and exact heterodimer assignment |

### Current TLR1/2 Working Conclusions

- `Pam3CSK4 -> TLR2/TLR1` is the strongest first-pass accepted TLR entry pair because it has both direct receptor-pair support and mouse SCI relevance.
- The first major comparison split is `TLR2/TLR1` versus `TLR2/TLR6`.
- The second major comparison split is ligand-specific behavior within the TLR2/TLR6 family rather than a single uniform “diacyl” program.
- `LTA` should not be treated as equivalent in certainty to the synthetic lipopeptide standards even when it remains biologically informative.
- Endogenous sterile SCI ligands for `TLR2` and `TLR4` remain active discovery gaps and should stay provisional until direct source support is stronger.

## Deliverable Shape

This module should mainly populate:

- `SignalingEntity`
- `SignalingPathwayMember` when receptor family membership matters
- `SignalingEdge` for direct ligand-receptor edges
- `SignalingEdgeSource` for per-edge provenance

## Handoff Goal

By the time Module 20A is first-pass saturated, another model should be able to export a clean ligand-receptor edge table suitable for `mSCS` without using exploratory signaling summaries as a substitute for curation.

## 2026-08-11 continuation status

Literature continuation batches `052`–`060` exhausted the source-rich tail:
`354` candidates reviewed, `42` promoted to medium, and `312` retained low.
After the review-reference backtrace integration, final queue counts are `99`
high, `620` medium, `2,613` low, and `197` uncertain. The pair index is `239`
high in at least one species, `724` medium-or-lower, and `3,559`
uncertain-or-unassessed. No `SignalingEdge` rows
were created. Provenance is in the per-batch audit/evidence/decision files and
`work/module20_db_seed/batch_full_002/literature_continuation_exhaustion_summary.tsv`.

The review-reference backtrace then validated `129` review-derived rows,
promoted `9` exact pairs to medium, and logged `234` additional pair claims
without automatic promotion. Of those claims, `130` have primary-source flags,
`36` match existing queue pairs, and `74` are new pair keys awaiting manual
source validation. See
`work/module20_db_seed/evidence_search_agents/review_reference_backtrace_001/`.

Validation of the 74 new keys found `52` exact-primary claims. The explicit
intake gate accepted `32` ordinary source-backed candidates into the audited
pair-confidence supplement, routed `15` to boundary review, and retained `5`
as low because their primary evidence was chicken- or rat-specific and could
not be normalized to mouse or human. The canonical external queue remains
unchanged for these new keys, and no `SignalingEdge` rows were created.
Provenance is recorded in
`work/module20_db_seed/evidence_search_agents/additional_pair_validation_001/additional_pair_intake_decision_register.tsv`,
`work/module20_db_seed/evidence_escalation_starter/module20a_additional_pair_validation001_evidence_register.tsv`,
and the audited supplement consumed by
`scripts/build_module20_pair_species_index.py`.

## 2026-08-12 agent batch 007 and no-evidence disposition

Eight disjoint workers completed `200` priority-1/2/6/7 low rows under
`work/module20_db_seed/evidence_search_agents/agent_batch_007/`. Final worker
verdicts were `111` no-evidence, `28` hold-low, `31` manual-review, `14`
reject-pair, and `16` promotion candidates. Curator review promoted `15`
source-backed ECM/adhesion candidates to medium; the `COL6A3-CD44` candidate
was held because its source supports the endotrophin fragment rather than
intact COL6A3. No high-confidence or `SignalingEdge` rows were created.

The canonical queue is now `99` high, `635` medium, `2,598` low, and `197`
uncertain. The pair/species index was rebuilt with `4,522` unique pair rows.
The cumulative revisit registry contains `1,229`
`no_evidence_after_search` rows, and the companion non-ligand-receptor
registry contains `263` rows. These are revisit/exclusion dispositions, not
biological absence claims. Batch reports, the curator review register, and
source-backed evidence/decision registers are retained under the batch and
evidence-escalation directories.

## 2026-08-13 agent batch 008 and curator-approved integration

Five disjoint workers searched `1,000` previously unreviewed low-confidence
rows in five packets of `200` under
`work/module20_db_seed/evidence_search_agents/agent_batch_008/`. Validation
confirmed `1,000` unique report rows. Worker verdicts were `238` promotion
candidates, `426` manual-review, `207` hold-low, `66` no-evidence, and `63`
reject-pair.

The curator approved `171` source-backed, non-lead candidates at medium
confidence. `67` worker promotion flags remain manual because the source was a
lead or retained an unresolved chain/complex/assignment caveat. The `66`
no-evidence rows were added to the revisit registry and `63` reject-pair rows
to the non-ligand-receptor registry. No high-confidence or `SignalingEdge`
rows were created.

Current queue counts are `99` high, `806` medium, `2,427` low, and `197`
uncertain. The pair index has `4,522` unique rows; cumulative registries have
`1,295` no-evidence and `326` non-LR rows. Reports, validation, curator
register, evidence register, and decision register are retained under the
batch-008 work directory.

## 2026-08-13 residual batch 009 completion

The remaining `46` genuinely unreviewed low-confidence rows were searched in a
final residual packet under
`work/module20_db_seed/evidence_search_agents/agent_batch_009/`. Validation
confirmed `46` unique rows: `13` promotion candidates, `15` no-evidence, `6`
reject-pair, `7` hold-low, and `5` manual-review.

Curator review approved all `13` promotion candidates at medium confidence,
while preserving receptor-complex, co-receptor, clearance, adhesion,
processing, and non-SCI caveats. The `15` no-evidence rows and `6` reject-pair
rows were added to the corresponding registries. No high-confidence or
`SignalingEdge` rows were created.

There are now `0` unreviewed low rows remaining. Current queue counts are `99`
high, `819` medium, `2,414` low, and `197` uncertain. Cumulative registries
contain `1,310` no-evidence and `332` non-LR rows; the pair index contains
`4,522` unique rows.

## 2026-08-13 batches 010–011: all low rows terminally dispositioned

The remaining `772` low rows outside terminal registries were reassessed in
four batch-010 packets (`200/200/200/172`); `84` exact source-backed candidates
were approved at medium, `159` were no-evidence, and `72` were non-LR.

The final `457` unresolved rows were adjudicated in three batch-011 packets
(`200/200/57`); `84` exact source-backed candidates were approved at medium,
`163` were no-evidence, and `46` were non-LR. The other `164` boundary calls
were recorded as no-evidence for the submitted exact pair, retaining their
family, fragment, complex, and notation limitations.

There are now `0` low rows outside a terminal registry or approved evidence
decision. Current queue counts are `99` high, `987` medium, `2,246` low, and
`197` uncertain. Cumulative registries contain `1,796` no-evidence and `450`
non-LR rows; the pair index contains `4,522` unique rows. No high-confidence or
`SignalingEdge` rows were created.
