# Module 20A Takeover Prompt

> **Current handoff:** Read [MODULE20A_HANDOFF_2026-08-07.md](MODULE20A_HANDOFF_2026-08-07.md) first. The historical prompt below describes the original intake setup; the current queue, confidence totals, completed recovery batches, and next low-confidence slice are maintained in that handoff.

Copy the prompt below into a new Codex chat that will continue this work.

```text
Work in the nested repository /Users/derea/Documents/SCI/mSCIdblit. Continue Module 20A database-first ligand-receptor curation from the current checked-in/worktree state.

First use Repowise for repository understanding and code navigation. Query the Module 20A tracker, the local-model runbook, the source registry, and the triage runner before using raw searches. If Repowise is unavailable or low confidence, say so and then use targeted rg/read checks.

Read and follow these canonical local documents before changing anything:
- docs/HANDOFF_MODULES_20_24_LOCAL_MODEL.md
- modules/Module_20A_TRACKER.md
- docs/SCHEMA_DOCUMENTATION.md
- CONTRIBUTING.md
- work/module20_db_seed/source_registry.tsv

Core curation rules:
- External ligand-receptor databases are seed inventories, not truth tables.
- Never invent a ligand-receptor edge, receptor complex, species support, directness, cell context, SCI relevance, or downstream mechanism.
- Do not treat expression, pathway membership, or a review cartoon as evidence of direct engagement.
- Mouse evidence is preferred. Human-only or orthology-supported material must remain explicitly labeled.
- Preserve source/database provenance and ambiguity. Use UNKNOWN when a source does not state a field.
- Do not create simulator-facing SignalingEdge rows until a pair has anchored source-backed evidence and remains a true direct mechanistic edge after review.
- The local Ollama model is extraction/triage assistance only. It must not make final scientific decisions or insert curation rows unsupervised.

Current Module 20A state:
- ConnectomeDB2025 mouse direct-seed pass is validated: 483/483 normalized rows. Start its curator queue at work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/01_keep_direct_seed_review_then_primary.tsv.
- Guide to Pharmacology exported 1,994 mouse-or-human endogenous rows, including 480 priority-family rows; the 75 mouse-priority rows have completed local triage and review-slice export in work/module20_db_seed/overnight_runs_v2/gtopdb_mouse_priority/.
- CellChatDB.mouse exported 1,280 priority-family rows. Local triage and review-slice export are complete for 793 Secreted Signaling rows in work/module20_db_seed/overnight_runs_v2/cellchat_mouse_secreted_signaling/ and 435 ECM-Receptor rows in work/module20_db_seed/overnight_runs_v2/cellchat_mouse_ecm_receptor/.
- A consolidated curator-facing slice set for the three completed overnight lanes now lives under work/module20_db_seed/overnight_runs_v2/review_slices_consolidated/ with 1,303 rows total and an audit flag preserved for CellChat:CCL8_ACKR4.
- All overnight outputs are structurally validated as seven-column TSVs. Raw model responses are retained beside normalized files as *.raw.tsv; rejected retry output is retained separately. Do not delete them.
- The triage runner is scripts/run_module20_seed_triage_batch.py and the reproducible launcher is work/module20_db_seed/run_module20_overnight_triage.sh. The runner now checks source identity, allowed vocabularies, and TSV shape before accepting output.
- One explicit exception needs review: CellChat:CCL8_ACKR4 was labeled keep_direct_seed by the local model. Do not silently promote it. ACKR/atypical/decoy/scavenger receptors generally require boundary_review or keep_direct_seed_with_caution unless primary evidence justifies otherwise.
- Cellinker remains source_fetch_blocked; do not call it ingested or manufacture rows from it.

Recommended next action:
1. Start evidence escalation from the highest-value mouse direct-seed pairs, beginning with ConnectomeDB `01_keep_direct_seed_review_then_primary.tsv` and then the strongest completed overnight review slices.
2. Keep all pair-level decisions auditable in the tracker without writing SignalingEdge records until a pair has anchored source-backed evidence and survives direct-edge review.
3. Route ACKR/decoy/scavenger rows such as CellChat:CCL8_ACKR4 through explicit boundary/caution review before any downstream promotion, then proceed vertically into Module 21A/22A only for reviewed direct edges.

Use qwen2.5-coder:32b for narrow, source-bounded local tasks. Keep prompts small, force exact structured output, and mechanically validate output before treating it as usable. Do not spend model effort on broad unsourced biological synthesis.
```
