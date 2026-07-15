# Ollama Chunk Extraction Workflow

Use this workflow when a paper is too large or mixed-modal for a single local-model prompt. The goal is to keep Ollama focused on one source packet at a time, then let the curator decide what becomes a database row.

## Why chunk first

The Tamaru 2023 trial showed the failure mode clearly: a long prompt can make the model propagate in vivo SCI metadata into unrelated in vitro and transplantation rows. Smaller chunks reduce that cross-contamination and make review cheaper because each model output can be compared to the exact source text that produced it.

## Standard run

1. Save extracted full text under ignored scratch space, usually `work/module_1a/...`.
2. Generate chunks and prompts without running Ollama. The default task is `extract`, but for most papers start with `triage` or `figure_candidate_experiments`:

   ```bash
   python3 scripts/ollama_chunk_extract.py \
     --source-text work/module_1a/tamaru_2023_pdf_text_clean.txt \
     --paper-id M1A-P003 \
     --title "Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury" \
     --doi 10.1016/j.expneurol.2022.114264 \
     --pmid 36336030 \
     --url https://catalog.lib.kyushu-u.ac.jp/opac_download_md/6787512/med3703.pdf \
     --task figure_candidate_experiments \
     --output-dir work/module_1a/extraction_runs/M1A-P003
   ```

3. Inspect `review_packet.md` and the files in `prompts/`. If a chunk is obviously irrelevant, skip it.
4. Run Ollama only when the chunking looks reasonable. Prefer one compact selected chunk first:

   ```bash
   python3 scripts/ollama_chunk_extract.py \
     --source-text work/module_1a/tamaru_2023_pdf_text_clean.txt \
     --paper-id M1A-P003 \
     --title "Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury" \
     --doi 10.1016/j.expneurol.2022.114264 \
     --pmid 36336030 \
     --url https://catalog.lib.kyushu-u.ac.jp/opac_download_md/6787512/med3703.pdf \
     --output-dir work/module_1a/extraction_runs/M1A-P003_fig2_scout \
     --task figure_candidate_experiments \
     --prompt-style compact \
     --chunk-id figure_02_fig_2 \
     --run-ollama \
     --model qwen2.5-coder:32b
   ```

   Use broader runs only after the compact one-chunk prompt gives useful output:

   ```bash
   python3 scripts/ollama_chunk_extract.py \
     --source-text work/module_1a/tamaru_2023_pdf_text_clean.txt \
     --paper-id M1A-P003 \
     --title "Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury" \
     --doi 10.1016/j.expneurol.2022.114264 \
     --pmid 36336030 \
     --url https://catalog.lib.kyushu-u.ac.jp/opac_download_md/6787512/med3703.pdf \
     --output-dir work/module_1a/extraction_runs/M1A-P003 \
     --task figure_candidate_experiments \
     --run-ollama \
     --model qwen2.5-coder:32b
   ```

5. Review `sanity_report.md` before copying anything into `modules/Module_1A_TRACKER.md` or the database.

## Output files

| File | Purpose |
|---|---|
| `source_clean.txt` | Normalized source text used for chunking |
| `all_chunk_manifest.json` | Machine-readable inventory for all chunks before task filtering |
| `chunk_manifest.json` | Machine-readable inventory for chunks selected by the task |
| `review_packet.md` | Human-readable source packet summary |
| `prompts/*.txt` | Narrow prompts for each chunk |
| `ollama_outputs/*.md` | Raw model outputs when `--run-ollama` is used |
| `sanity_report.md` | Automated warnings and review checklist |

## Token Control

- Use `--chunk-id` to run only one or a few selected chunks.
- Use `--prompt-style compact` for scouting and sanity checks when token cost matters.
- Use standard prompts when the output needs more structure or the compact prompt becomes ambiguous.

## Task modes

| Task | Best use | Output role |
|---|---|---|
| `triage` | Decide whether chunks are worth curator attention | Skip/keep guidance, not rows |
| `methods_metadata` | Index species, injury model, device, timepoints, assays, culture and transplant details | Factual methods map |
| `figure_candidate_experiments` | Scout candidate comparisons from figures/results | Candidate comparison list, not curated rows |
| `row_sanity_check` | Check proposed rows against source chunks | Unsupported fields, contradictions, contamination warnings |
| `extract` | Legacy full candidate extraction | Draft rows requiring manual review |

Use `row_sanity_check` with a file containing proposed tracker/database rows:

```bash
python3 scripts/ollama_chunk_extract.py \
  --source-text work/module_1a/tamaru_2023_pdf_text_clean.txt \
  --paper-id M1A-P003 \
  --title "Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury" \
  --task row_sanity_check \
  --rows-file work/module_1a/proposed_rows/M1A-P003_rows.md \
  --output-dir work/module_1a/extraction_runs/M1A-P003_row_check
```

## Review rules

- Treat Ollama output as extraction assistance, not curated evidence.
- For in vitro chunks, injury device, vertebral level, and injury severity should normally be `N/A`.
- For transplantation into uninjured recipients, do not inherit SCI metadata from donor-cell preparation or another experiment.
- Use `UNKNOWN` when the source chunk omits a field; use `N/A` only when the field is biologically not applicable.
- Commit curated tracker/database changes, not raw PDFs or model scratch output.
