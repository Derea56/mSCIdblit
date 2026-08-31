# Modules 20-24 Local-Model Runbook

This runbook is for filling Modules 20-24 with a local Ollama model while keeping `mSCIdblit` scientifically conservative.

The local model is an extraction assistant only. It may help us search, triage, summarize, and sanity-check. It must not invent edges, species support, receptor complexes, perturbation logic, or database rows.

## Non-Negotiable Rules

- Do not ask the local model to guess missing fields.
- Do not convert review pathway cartoons into direct edges unless the source explicitly supports the edge.
- Do not treat expression of a ligand or receptor as proof of ligand-receptor engagement.
- Do not treat pathway membership as proof of a direct edge.
- Do not collapse mouse and human support into one unlabeled statement.
- Do not insert simulator-facing `SignalingEdge` rows without at least one anchored source path to `paper_id`, `observation_id`, or `claim_id`.
- Use `UNKNOWN` when the paper does not state a field.
- Use `N/A` only when the field is biologically not applicable.

## What The Local Model Should Do

Use the local model for:

- search-query drafting
- abstract triage
- figure/results chunk scouting
- methods metadata extraction
- candidate experiment-row drafting
- row sanity checking against source text

Do not use the local model for:

- final consensus wording
- saturation decisions by itself
- unsupported edge normalization
- unsupervised database insertion

## Most Efficient Module Order

Do the work in this order:

1. Module 20A
2. Module 20B
3. Module 21A
4. Module 21B
5. Module 22A
6. Module 22B
7. Module 23A
8. Module 23B
9. Module 24A
10. Module 24B

Reason:

- Module 20 defines the extracellular handoff layer.
- Module 21 depends on Module 20 receptor definitions.
- Module 22 depends on Module 21 relay outputs.
- Modules 23-24 can reuse Module 20 edge conventions but are lower-priority for the first `mSCS` export.

## Low-Credit Operating Strategy

1. Start from curated ligand-receptor databases before broad literature searching.
2. Use the local model to normalize, deduplicate, and bucket database-derived candidate pairs.
3. Search only for evidence needed to validate or reject retained candidate pairs.
4. Run the local model on one paper, one database row batch, or one source chunk at a time.
5. Draft A-layer tracker rows first.
6. Only after reviewed A-layer rows exist, draft B-layer atomic observations and edge candidates.
7. Stop a search lane after two consecutive targeted evidence passes add no new validated pair class.

## Existing Repo Assets We Should Reuse

- [docs/OLLAMA_CHUNK_EXTRACTION.md](/Users/derea/Documents/SCI/mSCIdblit/docs/OLLAMA_CHUNK_EXTRACTION.md)
- [docs/MODULE20_CONNECTOMEDB_LOCAL_WORKFLOW.md](/Users/derea/Documents/SCI/mSCIdblit/docs/MODULE20_CONNECTOMEDB_LOCAL_WORKFLOW.md)
- [docs/MECHANISM_BUNDLE_EXPORT.md](/Users/derea/Documents/SCI/mSCIdblit/docs/MECHANISM_BUNDLE_EXPORT.md)
- [docs/SCHEMA_DOCUMENTATION.md](/Users/derea/Documents/SCI/mSCIdblit/docs/SCHEMA_DOCUMENTATION.md)
- [modules/Module_17A_TRACKER.md](/Users/derea/Documents/SCI/mSCIdblit/modules/Module_17A_TRACKER.md)
- [modules/Module_17B_TRACKER.md](/Users/derea/Documents/SCI/mSCIdblit/modules/Module_17B_TRACKER.md)
- [modules/Module_18A_TRACKER.md](/Users/derea/Documents/SCI/mSCIdblit/modules/Module_18A_TRACKER.md)
- [modules/Module_19A_TRACKER.md](/Users/derea/Documents/SCI/mSCIdblit/modules/Module_19A_TRACKER.md)
- [scripts/ollama_chunk_extract.py](/Users/derea/Documents/SCI/mSCIdblit/scripts/ollama_chunk_extract.py)
- [scripts/validate_connectomedb_lr_batch.py](/Users/derea/Documents/SCI/mSCIdblit/scripts/validate_connectomedb_lr_batch.py)
- [scripts/export_gtopdb_module20_priority_seeds.py](/Users/derea/Documents/SCI/mSCIdblit/scripts/export_gtopdb_module20_priority_seeds.py)
- [work/module20_db_seed/source_registry.tsv](/Users/derea/Documents/SCI/mSCIdblit/work/module20_db_seed/source_registry.tsv)

## Local Models Available

Current local models:

- `qwen2.5-coder:32b`
- `qwen3.6:latest`

Default recommendation:

- Use `qwen2.5-coder:32b` for `ollama_chunk_extract.py` because the repo already documents it and the prompt format is narrow.
- Use `qwen3.6:latest` only for very short triage or query-drafting prompts when we want a second local opinion.

## Database-First Search Plan

Before searching broadly, build a reusable candidate-pair seed list from curated external resources and only then mine internal modules for missing SCI-specific context.

Priority resource order for Module 20A:

1. ConnectomeDB2025
2. Guide to Pharmacology
3. CellChatDB
4. CellTalkDB
5. Cellinker
6. CellPhoneDB
7. OmniPath overlap checks

### Current Source Intake State

- `ConnectomeDB2025` mouse direct-priority pass is already validated and review-sliced.
- `GuideToPharmacology` endogenous ligand pairings are now downloaded and normalized into Module 20A seed tables, but have not yet gone through the local-model triage loop.
- `CellChatDB.mouse` from the maintained `jinworks/CellChat` package is now extracted and normalized into Module 20A seed tables, with annotation-aware exports for `Secreted Signaling`, `ECM-Receptor`, `Cell-Cell Contact`, and `Non-protein Signaling`.
- `Cellinker` has been checked, but its direct mouse download currently returns `Invalid Request`; keep it registered as blocked rather than treating it as a successful ingest.

### Module 20 Seeds

Start from database-backed extracellular edge families already touched elsewhere:

- IL6, LIF, OSM, CNTF and gp130-family receptors
- TNF/TNFR family
- IL1 family
- chemokines and chemokine receptors
- complement ligands and receptors
- HMGB1-RAGE
- extracellular ATP and purinergic receptors
- IL-33 and its receptor system
- S100A8/S100A9 receptor context
- WNT, Notch, BMP/TGF-beta, EGF/FGF/PDGF/VEGF
- matricellular ligand and receptor pairs already implied by Modules 5, 18, and 19

For each family:

- harvest all candidate pairs from the prioritized LR databases
- retain the database name and version/date checked
- mark whether mouse is directly represented or only human / orthology-supported
- send only unresolved or high-value pairs into review/primary literature follow-up

### Module 21 Seeds

Promote already-observed downstream relay families:

- TLR/MyD88/NF-kappaB and TRIF/TBK1/IRF from Module 17
- cGAS-STING/TBK1/IRF3 and inflammasome intersections from Module 18
- JAK/STAT, MAPK, PI3K-AKT, SMAD, beta-catenin, NICD/RBPJ families

### Module 22 Seeds

Start from TFs already appearing in Modules 17-19:

- STAT3
- IRF3, IRF5, IRF7
- NF-kappaB
- AP-1
- SMADs
- YAP/TAZ/TEAD
- beta-catenin-associated programs

### Module 23 Seeds

- integrins
- focal adhesion / FAK / SRC
- YAP/TAZ/TEAD
- cadherins
- matrix-stiffness and mechanosensing literature
- matricellular ligand edges already encountered in Modules 5, 18, and 19

### Module 24 Seeds

- complement
- coagulation
- kinin
- lipid mediators
- protease-activated receptors
- extracellular protease systems

## Module-Specific Extraction Targets

### Module 20A

The local model should draft candidate paper and experiment rows only when the source supports:

- ligand identity
- receptor identity
- receptor complex or co-receptor requirement
- ligand form
- agonist, antagonist, decoy, inhibitor, or soluble-receptor role
- species support
- cell-type context
- injury or comparator context
- direct-edge versus review-only status
- figure/table/results provenance

### Module 21A

The local model should draft rows only when the source supports:

- receptor branch identity
- adaptor step
- kinase step
- transcription-factor output
- branch-specific perturbation or rescue logic
- species and cell-type context
- pathway-branch specificity

### Module 22A

Draft rows only when the source supports:

- TF identity
- target gene or target program
- direct binding versus broader program association
- receiver cell type
- injury or stimulation context
- phenotype linkage if measured

### Module 23A

Draft rows only when the source supports:

- ECM ligand or matrix feature
- receptor or adhesion system
- mechanotransduction relay
- context such as stiffness, contact, scar, vessel, astrocyte, fibroblast, or OPC state
- downstream TF or program if measured

### Module 24A

Draft rows only when the source supports:

- complement, coagulation, kinin, lipid, or protease ligand identity
- receptor or target system
- protease activation logic if relevant
- inflammatory, vascular, glial, or tissue-state consequence
- context and species support

## Local-Model Prompt Templates

Use short prompts. Do not ask for prose unless we need prose.

### 1. Abstract Triage Prompt

```text
You are helping curate mSCIdblit Module 20A/21A/22A/23A/24A.

Task:
- Read this title and abstract only.
- Decide whether the paper is likely useful for the target module.
- Do not infer results beyond the abstract.

Return exactly:
1. keep_or_skip: KEEP, MAYBE, or SKIP
2. module_fit: one sentence
3. mechanistic_category: one short phrase
4. direct_edge_or_context_only: direct_edge, pathway_context, phenotype_only, or unclear
5. reasons: 3 bullets max
6. missing_fields: short comma-separated list

Rule:
- If the abstract does not explicitly support a direct edge, say so.
```

### 2. Methods Metadata Prompt

```text
Extract only explicit methods metadata from this source chunk.

Return JSON with:
- species
- strain
- sex
- injury_model
- injury_level
- intervention
- cell_type
- assay
- timepoints
- comparator_model
- unknown_fields

Rules:
- Use UNKNOWN when not stated.
- Do not infer SCI metadata for in vitro-only experiments.
- Do not include conclusions or interpretations.
```

### 3. Candidate Experiment Prompt

```text
Read this source chunk and draft only candidate experiment rows.

Return a markdown table with columns:
- candidate_experiment_id
- figure_or_table_ref
- model_context
- sender_ligand_or_upstream_node
- receptor_or_target_node
- downstream_branch_or_tf
- perturbation
- phenotype
- edge_type
- directness
- exact_source_support
- confidence
- needs_manual_check

Rules:
- One row per atomic comparison.
- If a field is not stated, use UNKNOWN.
- If the chunk shows only expression, mark edge_type as expression_only and directness as not_direct.
- Do not write any database IDs.
```

### 4. Row Sanity Prompt

```text
Check the proposed rows against the source chunk.

Return:
- supported_fields
- unsupported_fields
- contradicted_fields
- contamination_warnings
- suggested_edits

Rules:
- Flag any borrowed species, injury, receptor, or pathway information not stated in the chunk.
- Be strict.
```

## Recommended Ollama Commands

### First pass: chunk without model run

```bash
python3 /Users/derea/Documents/SCI/mSCIdblit/scripts/ollama_chunk_extract.py \
  --source-text /ABS/PATH/source_text.txt \
  --paper-id M20A-PXXX \
  --title "Paper title" \
  --doi DOI_OR_UNKNOWN \
  --pmid PMID_OR_UNKNOWN \
  --task figure_candidate_experiments \
  --output-dir /ABS/PATH/extraction_runs/M20A-PXXX
```

### Cheapest useful model run

```bash
python3 /Users/derea/Documents/SCI/mSCIdblit/scripts/ollama_chunk_extract.py \
  --source-text /ABS/PATH/source_text.txt \
  --paper-id M20A-PXXX \
  --title "Paper title" \
  --doi DOI_OR_UNKNOWN \
  --pmid PMID_OR_UNKNOWN \
  --task figure_candidate_experiments \
  --prompt-style compact \
  --chunk-id CHUNK_ID \
  --run-ollama \
  --model qwen2.5-coder:32b \
  --output-dir /ABS/PATH/extraction_runs/M20A-PXXX_chunk1
```

### Sanity-check drafted rows

```bash
python3 /Users/derea/Documents/SCI/mSCIdblit/scripts/ollama_chunk_extract.py \
  --source-text /ABS/PATH/source_text.txt \
  --paper-id M20A-PXXX \
  --title "Paper title" \
  --task row_sanity_check \
  --rows-file /ABS/PATH/proposed_rows.md \
  --run-ollama \
  --model qwen2.5-coder:32b \
  --output-dir /ABS/PATH/extraction_runs/M20A-PXXX_row_check
```

## Completed Module 20A Local Triage

- `2026-08-04`: completed three reproducible, local-only Module 20A seed-triage lanes under `work/module20_db_seed/overnight_runs_v2/`: CellChatDB.mouse Secreted Signaling (`793` rows / `20` chunks), Guide to Pharmacology mouse-priority (`75` rows / `3` chunks), and CellChatDB.mouse ECM-Receptor (`435` rows / `13` chunks).
- `2026-08-04`: audited those completed runs with `scripts/export_module20_seed_triage_review_slices.py` and materialized deterministic curator review slices for each lane plus a consolidated cross-lane slice set under `work/module20_db_seed/overnight_runs_v2/review_slices_consolidated/`.
- Consolidated completed-lane totals are `1303` rows: `612` `boundary_review`, `528` `keep_direct_seed_with_caution`, `151` `keep_direct_seed`, and `12` `defer_lower_priority`; actions are `1091` `review_then_primary`, `115` `primary_first`, and `97` `hold_for_later_family_pass`.
- `scripts/run_module20_seed_triage_batch.py` now normalizes only mechanical TSV drift after validating source-controlled identity, fixed vocabularies, row order, and output shape; raw model output is retained as `*.raw.tsv`. It does not repair biological content.
- One CellChat seed, `CellChat:CCL8_ACKR4`, remains a flagged plain-keep exception. Keep it out of any automatic direct-edge promotion and review its atypical-receptor role against source evidence.

## Human Review Loop

For each paper:

1. Triage abstract.
2. If `KEEP` or `MAYBE`, chunk the full text.
3. Run one compact chunk first.
4. Accept only fields explicitly supported by the source chunk.
5. Add reviewed rows to the A tracker.
6. After enough reviewed A rows accumulate, draft B-layer atomic observations and edge candidates.
7. Do not materialize export-facing graph rows until source anchors are clear.

## When To Advance From A To B

Advance a module from A to B only when:

- the core mechanistic categories for that module are represented
- at least two targeted search rounds add no new category
- major species/context ambiguity is bounded
- the A tracker has enough reviewed experiment rows to support atomic observation splitting

## First Concrete Work Queue

Use this queue before any broad new literature sweep:

1. Module 20A from seed families already cited in Modules 17-19.
2. Module 21A from receptor-to-relay paths already observed in Modules 17-18.
3. Module 22A from TFs already appearing in Modules 17-19.
4. Module 23A from matrix and adhesion edges already implied in Modules 5, 18, and 19.
5. Module 24A from complement, purinergic, DAMP, and protease-adjacent papers already in Module 18.

This reuses existing curation and keeps search volume down.

## Practical Stopping Rule

If a paper only gives:

- expression without perturbation
- pathway membership without an edge
- review summary without primary support
- species-mixed claims without labeling
- phenotype with no mechanistic assignment

then keep it as boundary or context support, or skip it. Do not force it into a direct graph edge.
