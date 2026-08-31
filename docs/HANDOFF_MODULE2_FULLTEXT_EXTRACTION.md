# mSCIdblit Module 2 Handoff

**Date:** 2026-08-03  
**Workspace:** `/Users/derea/Documents/SCI/mSCIdblit`

## Objective

Continue the Module 2 full-text evidence extraction and materialization work. The scientific extraction is substantially complete for the papers with confirmed PMC full text; the immediate remaining task is to repair legacy tracker rows so the SQL export can run and then validate the regenerated materialization.

## Current Status

- Module 2A (biomaterial/scaffold repair evidence): 43-paper corpus.
- 22 confirmed PMC-available papers have been full-text upgraded.
- Those 22 papers have 44 local files under `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module2_fulltext_upgrade/` (one HTML and one text extraction per paper).
- Module 2B (evidence synthesis) currently records 50 observations, 36 author claims, 56 evidence links, 8 boundary records, and 8 consensus-ready statements.
- Tracker and roadmap edits are present in:
  - `/Users/derea/Documents/SCI/mSCIdblit/modules/Module_2A_TRACKER.md`
  - `/Users/derea/Documents/SCI/mSCIdblit/modules/Module_2B_TRACKER.md`
  - `/Users/derea/Documents/SCI/mSCIdblit/modules/ROADMAP.md`
- The helper used to convert downloaded HTML to text is `/Users/derea/Documents/SCI/mSCIdblit/work/html_to_text.py`.
- `git diff --check` passed after the latest edits.

## Full-Text Papers Completed

The completed PMC upgrades are:

`P004 PMC6559945`, `P005 PMC6369008`, `P008 PMC5294639`, `P009 PMC5657723`, `P014 PMC4799710`, `P015 PMC5337930`, `P016 PMC6034707`, `P017 PMC6050906`, `P024 PMC11668012`, `P025 PMC1615967`, `P026 PMC7365325`, `P030 PMC6055812`, `P032 PMC5851469`, `P033 PMC7437585`, `P034 PMC8698735`, `P035 PMC9598945`, `P036 PMC11617199`, `P039 PMC10897856`, `P040 PMC2830720`, `P041 PMC3992004`, `P042 PMC6990792`, `P043 PMC6170848`.

Do not repeat extraction for these papers unless correcting a specific tracker error. Important newly captured boundaries include:

- P032: protoplasmic ECM reduced GFAP and ED1 around the lesion and increased Tuj1-positive lesion area; fibrous ECM did not show the same benefit, and there was no locomotor integration test.
- P034: the fully functionalized scaffold preserved beta-III-tubulin fibers and reduced lesion/PDGF measures, but did not produce an early Iba1/ED1 anti-inflammatory difference and lacked long-term functional testing.
- P035: hAEC-derived neural-like cells in GelMA microchannels improved BBB scores and produced NF-H projections, but maturity of the cells was not proven and severe neuroinflammation/postoperative deaths were reported.
- P036: the 4D-SilMA system combined Ang-(1-7) and NT-3 release with reduced iNOS/GFAP, increased Arg-1/Tuj1, and improved BMS; in vivo cargo attribution remains bundled.
- P039: conductive 2CNT/GelMA plus electrical stimulation gave the strongest structural, electrophysiologic, pain, and BBB recovery; CNTs remained localized to the lesion.
- P040: methods-only in-vitro pH-triggered lysozyme release study; no SCI animal efficacy.
- P041/P042: graft/scaffold studies report myelination or axonal/functional improvement but have limited primary locomotor or cell-tracing evidence.
- P043: seeded and non-seeded scaffolds both improved skilled forelimb function, with no correlation between scaffold axon extent and functional recovery. Treat this as an important negative mechanistic boundary.

## Papers Still Abstract-Only

These IDs are still marked abstract-only/unavailable in the Module 2A full-text table. Do not label them full-text extracted without obtaining and recording a verifiable full text:

`P001`, `P002`, `P003`, `P006`, `P007`, `P010`, `P011`, `P012`, `P013`, `P018`, `P019`, `P020`, `P021`, `P022`, `P023`, `P027`, `P028`, `P029`, `P031`, `P037`, `P038`.

After materialization is repaired, a separate targeted PMC/publisher lookup can be done for these IDs. Preserve abstract-level status when no accessible full text is found.

## Immediate Blocker

The SQL exporter has not completed after the tracker upgrades. Two malformed legacy experiment rows in P005 were repaired, but the next parser error is:

`P008 E001: 14 columns found; 15 expected`

The experiment table header is near line 318 of Module 2A and requires 15 fields:

`Paper ID | Experiment ID | Figure Ref | Species | Strain | Sex | Injury Model | Injury Device | Injury Severity | Vertebral Level | Chronicity (DPI/WPI) | Control Type | Intervention Type | Methods Summary | Experiment Extracted`

More malformed legacy rows may appear after P008 E001. Fix only the row structure and preserve the scientific content. Use `apply_patch` for manual edits.

## Required Next Steps

1. Inspect and repair P008 E001 in `/Users/derea/Documents/SCI/mSCIdblit/modules/Module_2A_TRACKER.md` so it has exactly 15 pipe-delimited fields.
2. Rerun the exporter from `/Users/derea/Documents/SCI/mSCIdblit`:

   ```bash
   python3 scripts/export_module2_full_sql.py
   ```

3. Continue fixing the next reported malformed experiment row until the exporter completes. Do not assume the first error is the only one.
4. Reconcile the regenerated SQL/JSON outputs against the tracker counts: 50 observations, 36 claims, 56 links, 8 boundary records, and 8 consensus rows. Verify source-record and experiment counts rather than copying the old status note.
5. Run the repository’s relevant schema/materialization checks after export. If a check fails, report the exact command and first actionable error.
6. Only after validation, update the Module 2 status notes to say materialization is current.
7. Then, if desired, search for newly accessible full texts for the 21 abstract-only IDs and extract them one at a time using the established schema.

## Useful Checks

Run from `/Users/derea/Documents/SCI/mSCIdblit`:

```bash
git diff --check
rg -n "P008|Experiment ID|Full-text|Total observations|Total author claims|Total evidence links" modules/Module_2A_TRACKER.md modules/Module_2B_TRACKER.md
python3 scripts/export_module2_full_sql.py
```

## Worktree Safety

- The worktree contains unrelated user changes. Do not reset, checkout, clean, or revert them.
- Relevant uncommitted work includes the two Module 2 trackers, the roadmap, and the `module2_fulltext_upgrade` evidence directory.
- Existing processed SQL/JSON materialization is stale relative to the latest tracker edits until the exporter and validation checks succeed. Do not claim it is current or overwrite it with a partial export.
- Keep abstract-only papers abstract-only unless a full text is actually obtained.
- Follow the workspace NIH HPC safety instructions: use Helix or Slurm for intensive filesystem or compute work; never run broad recursive scans on Biowulf login nodes.
