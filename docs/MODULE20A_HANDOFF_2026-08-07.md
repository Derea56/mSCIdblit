# Module 20A Curation Handoff — 2026-08-07

This is the resume point for the Module 20A database-first ligand-receptor curation work.

## Current state

The external CellChat/LIANA recovery queue is fully reviewed at the row-decision level:

- Queue: `3,529` rows, all `reviewed`
- Overall confidence: `99 high`, `620 medium`, `2,613 low`, `197 uncertain`
- One-row-per-pair species index: `4,522` unique pair keys
- Index extractability: `239` high in at least one species, `724` medium-or-lower, `3,559` uncertain or unassessed
- Source-set conservation: `587` present in both mouse and human sources; `3,918` not established as conserved
- Low-confidence rows remaining: `2,734`

### Current iterative recovery overlay — 2026-08-10

All `2,923` low-confidence rows have now passed through the resumable search
ledger in 15 disjoint iterations. The ledger has `2,923`
`searched_pending_curator` rows and zero `unsearched` or `queued` rows. Worker
reports were literature-triage flags only. The first curator integration pass
has now written authoritative evidence/decision records for `83` accepted rows;
remaining flags still require exact-source, receptor-complex, directness,
species, and SCI-relevance review before promotion.

The first curator integration pass accepted `83` source-anchored worker flags
to overall `medium`. Human-only, mouse-only, and mixed-species support remains
explicit in the decision and pair-species registers. No row was promoted to
`high`, and no `SignalingEdge` was created.

Focused evidence pilot 001 then tested a family-focused, mouse-first search on
20 remaining low rows. Two exact-pair primary-source packets were accepted to
overall `medium`: ARTN-GFRA1/RET with receptor-selectivity caveats and
DLL3-NOTCH1 as a mouse cis-interaction/cis-inhibition record. The other 18
rows remain low with explicit negative, noncognate, species, paralog, topology,
or nomenclature limitations. No high-confidence call or `SignalingEdge` was
created.

### Batched literature acquisition — 2026-08-10

The scalable retrieval pilot was expanded to all `2,838` remaining lows using
114 Europe PMC requests, each containing 25 exact-pair clauses. It returned
`35,676` lead rows for `2,838` pairs: `1,612` pairs had at least one PMID lead
and `1,226` had no PMID lead. A mechanical evidence-signal prefilter routed
`414` leads across `414` pairs for possible local-model or curator review.
The retrieval phase itself made no confidence changes. Four disjoint agent
packets then reviewed all `414` prefiltered candidates. After final curator
reconciliation, `72` exact-pair, source-backed records were promoted to
overall `medium`. A targeted second pass then re-reviewed `105` unresolved or
boundary candidates and promoted `14` additional exact-pair records. A final
19-row continuation promoted `12` more exact-pair records to `medium`; a
44-row manual/boundary continuation then promoted `6` additional exact-pair
records to `medium` and retained `38` low after a narrower final gate. The next
44-row literature continuation promoted `9` more exact-pair records and retained
35 low. The next 44-row continuation promoted `8` more exact-pair records and
retained `36` low. The next 44-row continuation promoted `11` more exact-pair
records and retained `33` low. Continuations 047–050 then promoted `7`, `8`,
`10`, and `13` additional records, respectively; the final 23-row tail
promoted `4` and retained `19` low. Across the disjoint literature
continuations, all `331` remaining source-rich candidates were exhausted. No high-confidence call or
`SignalingEdge` was created. The full lead table, abstracts, query strings,
source locators, no-hit rows, prefilter audit, agent flags, and final
disposition audits are retained under
`work/module20_db_seed/evidence_search_agents/batch_full_002/` and
`work/module20_db_seed/batch_full_002/`.

The Qwen triage runner was validated on three filtered leads with exact TSV
output and no promotion decisions. Full model triage is intentionally not
run unsupervised; only source-backed flags may enter the curator evidence and
decision registers.

- Controller: `scripts/module20a_iterative_low_search.py`
- Ledger: `work/module20_db_seed/evidence_search_agents/iterative/low_search_ledger.tsv`
- Iteration packets: `work/module20_db_seed/evidence_search_agents/iterative/iteration_001/` through `iteration_015/`
- First promotion decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_iterative_promotion_2026-08-10_decision_register.tsv`
- First promotion evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_iterative_promotion_2026-08-10_evidence_register.tsv`
- Promotion-gate audit for all 407 flags: `work/module20_db_seed/evidence_escalation_starter/module20a_iterative_promotion_2026-08-10_audit.tsv`
- Focused pilot manifest and all 20 search outcomes: `work/module20_db_seed/evidence_search_agents/focused_pilot_001/`
- Focused pilot evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_focused_pilot_001_evidence_register.tsv`
- Focused pilot decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_focused_pilot_001_decision_register.tsv`
- Batch 002 all-414 final disposition audit: `work/module20_db_seed/batch_full_002/all_414_final_disposition_audit.tsv`
- Batch 002 final evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_batch002_final_evidence_register.tsv`
- Batch 002 final decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_batch002_final_decision_register.tsv`
- Boundary second-pass audit for all 105 re-reviewed candidates: `work/module20_db_seed/batch_full_002/boundary_second_pass_105/final_curator_review_audit.tsv`
- Boundary second-pass evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_boundary_second_pass_final_evidence_register.tsv`
- Boundary second-pass decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_boundary_second_pass_final_decision_register.tsv`
- Remaining-boundary audit for 19 continuation candidates: `work/module20_db_seed/batch_full_002/boundary_second_pass_remaining_019/final_curator_review_audit.tsv`
- Remaining-boundary evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_remaining_boundary_final_evidence_register.tsv`
- Remaining-boundary decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_remaining_boundary_final_decision_register.tsv`
- Manual-boundary continuation audit: `work/module20_db_seed/batch_full_002/manual_boundary_continuation_044/final_curator_review_audit.tsv`
- Manual-boundary continuation evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_manual_boundary_continuation_final_evidence_register.tsv`
- Manual-boundary continuation decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_manual_boundary_continuation_final_decision_register.tsv`
- Literature-continuation audit: `work/module20_db_seed/batch_full_002/literature_continuation_044/final_curator_review_audit.tsv`
- Literature-continuation evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation_final_evidence_register.tsv`
- Literature-continuation decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation_final_decision_register.tsv`
- Literature-continuation 045 audit: `work/module20_db_seed/batch_full_002/literature_continuation_045/final_curator_review_audit.tsv`
- Literature-continuation 045 evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation045_final_evidence_register.tsv`
- Literature-continuation 045 decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation045_final_decision_register.tsv`
- Literature-continuation 046 audit: `work/module20_db_seed/batch_full_002/literature_continuation_046/final_curator_review_audit.tsv`
- Literature-continuation 046 evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation046_final_evidence_register.tsv`
- Literature-continuation 046 decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation046_final_decision_register.tsv`
- Literature-continuation 047 audit: `work/module20_db_seed/batch_full_002/literature_continuation_047/final_curator_review_audit.tsv`
- Literature-continuation 047 evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation047_final_evidence_register.tsv`
- Literature-continuation 047 decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation047_final_decision_register.tsv`
- Literature-continuation 048 audit: `work/module20_db_seed/batch_full_002/literature_continuation_048/final_curator_review_audit.tsv`
- Literature-continuation 048 evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation048_final_evidence_register.tsv`
- Literature-continuation 048 decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation048_final_decision_register.tsv`
- Literature-continuation 049 audit: `work/module20_db_seed/batch_full_002/literature_continuation_049/final_curator_review_audit.tsv`
- Literature-continuation 049 evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation049_final_evidence_register.tsv`
- Literature-continuation 049 decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation049_final_decision_register.tsv`
- Literature-continuation 050 audit: `work/module20_db_seed/batch_full_002/literature_continuation_050/final_curator_review_audit.tsv`
- Literature-continuation 050 evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation050_final_evidence_register.tsv`
- Literature-continuation 050 decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation050_final_decision_register.tsv`
- Literature-continuation 051 audit: `work/module20_db_seed/batch_full_002/literature_continuation_051/final_curator_review_audit.tsv`
- Literature-continuation 051 evidence register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation051_final_evidence_register.tsv`
- Literature-continuation 051 decision register: `work/module20_db_seed/evidence_escalation_starter/module20a_literature_continuation051_final_decision_register.tsv`
- Literature-continuation exhaustion summary: `work/module20_db_seed/batch_full_002/literature_continuation_exhaustion_summary.tsv`
- Worker reports must follow each iteration's `worker_contract.md`; no worker
  may edit the queue, tracker, evidence registers, or `SignalingEdge` tables.

The queue and index are the integrated Module 20A external curation layer. Module 21A has not been populated from these pairs yet; only reviewed direct edges should be handed downstream.

## Important files

- Final external queue: `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`
- Pair/species confidence index: `work/module20_db_seed/evidence_escalation_router/module20a_pair_species_confidence_index.tsv`
- Queue status summary: `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue_status_summary.tsv`
- Historical evidence and decision registers: `work/module20_db_seed/evidence_escalation_starter/module20a_external*_register.tsv`
- Audited seed-packet supplement: `work/module20_db_seed/evidence_escalation_router/module20a_audited_pair_confidence_supplement.tsv`
- Prioritized low-confidence recovery export: `work/module20_db_seed/evidence_escalation_router/module20a_low_confidence_recovery_priority_1_2_6_7.tsv`
- First low-recovery packet: `work/module20_db_seed/evidence_escalation_starter/module20a_low_recovery_packet01_*`
- Second low-recovery batch: `work/module20_db_seed/evidence_escalation_starter/module20a_low_recovery_batch02_*`
- Agent source-review packets 01–06: `work/module20_db_seed/evidence_escalation_starter/module20a_agent_batch03_packet0[1-6].tsv`
- Agent source-review batch 03 registers: `work/module20_db_seed/evidence_escalation_starter/module20a_agent_source_review_batch03_*`
- Source review batch 04 registers: `work/module20_db_seed/evidence_escalation_starter/module20a_source_review_batch04_*`
- Source review batch 05 registers: `work/module20_db_seed/evidence_escalation_starter/module20a_source_review_batch05_*`
- Agent review batch 06 registers: `work/module20_db_seed/evidence_escalation_starter/module20a_agent_review_batch06_*`
- Iterative low-search controller and ledger: `scripts/module20a_iterative_low_search.py` and `work/module20_db_seed/evidence_search_agents/iterative/`
- Module tracker: `modules/Module_20A_TRACKER.md`

## Completed recent passes

- Recovery batch 19: `1,000` rows, IDs `0801–1800`, integrated through `scripts/curate_module20_external_recovery_batch19.py`.
- Medium review batch 20: all `283` medium rows reviewed; four overall promotions:
  - `MIF -> CD74_CXCR2`
  - `MIF -> CD74_CXCR4`
  - `FAT4 -> DCHS1`
  - `GDF2/BMP9 -> ENG`
- Medium follow-up batch 21: remaining `23` TGFB/TGM2/THBS/THY1/TIMP rows reviewed; none promoted overall, though five received human-specific high confidence.
- Rebuild command: `python3 scripts/build_module20_pair_species_index.py`
- The pair index rebuild now consumes the audited seed-packet supplement above; it updates species confidence for reviewed seed pairs while preserving source/database provenance and does not create simulator-facing edges.
- Low-recovery packet 01 added source-backed decisions for `Amh -> AMHR2_BMPR1A` (medium mouse, complex/context caveat) and `Csf2 -> CSF2RA_CSF2RB` (high mouse, direct receptor-complex reconstitution). `Wnt5a -> Fzd10` was rechecked against its existing negative pair-specific screen and was not duplicated or promoted.
- Low-recovery batch 02 reviewed the next `300` prioritized low rows and added six medium decisions from exact ECM/adhesion primary packets: `Agrn -> Dag1`, `Chad -> ITGA2_ITGB1`, `Col4a3 -> ITGA3_ITGB1`, `Fn1 -> ITGA3_ITGB1`, `Lama1 -> ITGA1_ITGB1`, and `Lama1 -> ITGA2_ITGB1`. The qwen batch-02 triage attempt stalled before producing valid output, so no model-derived decision was accepted; all six promotions were source-bounded curator decisions.
- Agent source-review batch 03 delegated disjoint packets across the remaining prioritized low queue. Packets 01–06 covered `240` rows and returned `27` source candidates. Six exact-pair candidates were integrated at medium confidence: `Fn1 -> ITGAV_ITGB1`, `Fn1 -> ITGAV_ITGB3`, `Fn1 -> ITGAV_ITGB6`, `Ibsp -> ITGAV_ITGB3`, `Ibsp -> ITGAV_ITGB5`, and `Reln -> ITGA3_ITGB1`. Collagen VI/IX candidates stayed low because the cited studies were type-level or heterotrimer-level rather than chain-specific; `Wnt5a -> Fzd10` stayed low after a negative pair-specific binding screen; and `Fn1 -> ITGAV_ITGB8` stayed low because native fibronectin binding was marginal. No `SignalingEdge` rows were created.
- Source review batch 04 added six primary-literature evidence rows and three medium-with-caution decisions: `Npnt complex 1/2 -> ITGA8_ITGB1` are anchored by mouse nephronectin-alpha8beta1 binding/association but retain unresolved Fras/Frem co-ligand composition; `Vwf -> GP complex` is anchored by human vWF binding to platelet GP receptor complexes but retains exact-subunit and mouse-context caveats. No `SignalingEdge` rows were created.

Do not rerun completed batch scripts blindly; they can append duplicate review packets. Use a new batch number for new decisions and preserve prior evidence IDs.

## Recommended next pass: low-confidence recovery

Do not begin by searching all `2,941` low rows uniformly. The low queue is mostly LIANA-only discovery:

- `314` low rows have higher-priority cross-source or CellChat context (`review_priority != 8`) and should be reviewed first.
- `2,627` are priority-8 LIANA-only discovery rows and can remain low until a targeted family packet or exact primary source makes them worth escalation.

The first low-confidence recovery slice is therefore the `314` priority-1/2/6/7 rows, concentrated in review IDs `0001–0800`. Agent packets 01–06 have now covered `240` rows with new primary-source screening; `314` prioritized low rows remain in the queue, with candidates integrated only when the source was exact and sufficiently bounded.

Promotion rules:

- High requires pair-specific direct binding or strong pair-specific functional evidence.
- Human-only or mouse-only evidence updates the corresponding species field but does not automatically promote overall confidence.
- Composite receptors, incomplete integrin notation, co-receptors, decoys, uptake, transactivation, and context-dependent associations should remain medium or low unless the molecular role is explicitly preserved.
- Database consensus and expression alone are not evidence of direct engagement.
- Preserve the distinction between conventional signaling receptors, atypical scavengers, co-receptors, accessory proteins, and uptake receptors.

## Resume checklist

1. Read this handoff, `modules/Module_20A_TRACKER.md`, `docs/SCHEMA_DOCUMENTATION.md`, and `docs/HANDOFF_MODULES_20_24_LOCAL_MODEL.md`.
2. Check the worktree before editing; unrelated existing changes belong to the user and must be preserved.
3. Recompute the queue counts from the TSV rather than relying only on this document.
4. Export the `314` remaining prioritized low rows and divide them into non-overlapping review packets.
5. Integrate new evidence and decisions, rebuild the pair/species index, validate row counts and duplicate IDs, and append the outcome to the tracker.
6. Only after the low-confidence recovery strategy is settled should reviewed direct ligand-receptor edges be routed into Module 21A relay curation.

## Latest low-recovery status

- Packet 01 integrated `2` new evidence records and `2` decisions. Batch 02 integrated `7` evidence records and `6` decisions. Source review batches 03–05 and independently verified agent batch 06 added `24` cautious, source-bounded medium decisions. Queue confidence is now `99/310/2,923/197` for high/medium/low/uncertain.
- The pair index now reports mouse confidence `143 high`, `466 medium`, `3,411 low`, `485 uncertain`; human confidence is `205 high`, `457 medium`, `466 low`, `3,377 uncertain`.
- `Amh -> AMHR2_BMPR1A` remains a reviewed medium mouse complex edge with BMPR1A/ACVR1 redundancy and non-SCI context caveats. `Csf2 -> CSF2RA_CSF2RB` is high for mouse receptor-complex binding/reconstitution but human support is unknown. No `SignalingEdge` rows were created.
- Batches 02–06 remain source-bounded ECM/adhesion or receptor-complex assignments with species/context caveats and are not simulator-facing edges; `296` priority-1/2/6/7 low rows remain.

### 2026-08-11 literature-continuation exhaustion

Batches `052`–`060` reviewed the remaining `354` source-rich candidates. Final
curator review promoted `42` exact, source-backed pairs to medium and retained
`312` low. The current queue is `99` high, `611` medium, `2,622` low, and
`197` uncertain; the pair index is `239` high-in-at-least-one-species, `695`
medium-or-lower, and `3,571` uncertain-or-unassessed. No `SignalingEdge` rows
were created. Per-batch raw flags, audits, evidence registers, decision
registers, and the exhaustion summary remain retained under the Module 20A
work directories.

### Review-reference backtrace 001

The review-reference backtrace covered `129` review-derived candidate rows
from `103` review sources. It traced `9` exact submitted pairs to primary
support and promoted them to medium. It also recorded `234` additional pair
claims from those reviews: `130` primary-source flags representing `110`
unique pair keys, including `74` pair keys not currently in the queue. These
additional claims are discovery-only and remain in
`work/module20_db_seed/evidence_search_agents/review_reference_backtrace_001/`
until pair-specific validation is completed.

Validation of those 74 new keys found `52` exact-primary candidates. Of these,
`45` are candidate-only records awaiting explicit queue intake, `7` are
source-backed boundary cases, and `22` remain low. The candidate intake
register is
`work/module20_db_seed/evidence_search_agents/additional_pair_validation_001/source_backed_candidate_intake_register.tsv`;
the canonical queue remains unchanged for these new keys.

### 2026-08-12 agent batch 007 and no-evidence disposition

Eight disjoint workers completed `200` priority-1/2/6/7 low rows under
`work/module20_db_seed/evidence_search_agents/agent_batch_007/`. Final worker
verdicts were `111` no-evidence, `28` hold-low, `31` manual-review, `14`
reject-pair, and `16` promotion candidates. Curator review promoted `15`
source-backed ECM/adhesion candidates to medium; the `COL6A3-CD44` candidate
was held because the source supports the endotrophin fragment rather than
intact COL6A3. No high-confidence or `SignalingEdge` rows were created.

The canonical queue is now `99` high, `635` medium, `2,598` low, and `197`
uncertain. The pair/species index was rebuilt and contains `4,522` unique
pair rows. The cumulative revisit registry contains `1,229`
`no_evidence_after_search` rows, and the companion non-ligand-receptor
registry contains `263` rows. These registries preserve search limitations and
do not claim biological absence; the canonical queue retains low rows for
compatibility. See `docs/MODULE20A_NO_EVIDENCE.md` and
`scripts/finalize_module20a_agent_batch007.py`.

### 2026-08-13 agent batch 008 and curator-approved integration

Five disjoint workers searched `1,000` previously unreviewed low-confidence
rows in packets of `200` under
`work/module20_db_seed/evidence_search_agents/agent_batch_008/`. Validation
confirmed `1,000` unique report rows. Worker verdicts were `238` promotion
candidates, `426` manual-review, `207` hold-low, `66` no-evidence, and `63`
reject-pair.

Curator approval was stricter than the worker promotion flag: `171` candidates
with non-lead primary locators and no unresolved chain/complex/assignment caveat
were integrated at medium confidence. `67` promotion flags remain in the
batch-008 curator register for manual review. The `66` no-evidence rows were
added to the revisit registry and the `63` reject-pair rows to the companion
non-ligand-receptor registry. No high-confidence or `SignalingEdge` rows were
created.

The canonical queue is now `99` high, `806` medium, `2,427` low, and `197`
uncertain. The pair/species index contains `4,522` unique pair rows. The
cumulative registries contain `1,295` no-evidence rows and `326` non-LR rows.
See `scripts/validate_module20a_agent_batch008.py`,
`scripts/integrate_module20a_agent_batch008.py`, and the retained batch reports
and integration registers under the batch-008 directory.

### 2026-08-13 residual batch 009 completion

The remaining `46` genuinely unreviewed low-confidence rows were searched in a
final residual packet under
`work/module20_db_seed/evidence_search_agents/agent_batch_009/`. The report
validated with `46` unique rows: `13` promotion candidates, `15`
no-evidence, `6` reject-pair, `7` hold-low, and `5` manual-review.

Curator review approved all `13` promotion candidates at medium confidence,
with receptor-complex, co-receptor, clearance, adhesion, processing, and
non-SCI caveats preserved. The `15` no-evidence rows and `6` reject-pair rows
were added to their respective registries. No high-confidence or
`SignalingEdge` rows were created.

All low-confidence rows now have a recorded search or exclusion disposition;
there are `0` unreviewed low rows remaining. The canonical queue is `99` high,
`819` medium, `2,414` low, and `197` uncertain. The cumulative registries
contain `1,310` no-evidence and `332` non-LR rows. The pair/species index still
contains `4,522` unique pair rows.

### 2026-08-13 batches 010–011: all low rows terminally dispositioned

The remaining `772` low rows outside terminal registries were reassessed in
four batch-010 packets (`200/200/200/172`). Validation confirmed `772` unique
reports. Curator review approved `84` exact source-backed candidates at
medium; `159` were no-evidence and `72` were non-LR.

The remaining `457` unresolved rows were adjudicated in three batch-011
packets (`200/200/57`). This produced `84` additional exact source-backed
medium decisions, `163` explicit no-evidence calls, and `46` non-LR calls. The
other `164` boundary calls were recorded as no-evidence for the submitted exact
pair, with family, fragment, complex, and notation limitations retained.

There are now `0` low rows outside a terminal registry or approved evidence
decision. The canonical queue is `99` high, `987` medium, `2,246` low, and
`197` uncertain. Cumulative registries contain `1,796` no-evidence and `450`
non-LR rows; the pair/species index contains `4,522` unique rows. No
high-confidence or `SignalingEdge` rows were created.
