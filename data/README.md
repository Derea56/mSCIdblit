# mSCIdblit data: tracked releases and what moved to Biowulf

`data/processed/` holds the tracked public release content (release bundles, crosswalks,
evidence bundles, the current mechanism-graph snapshot). Two classes of files were
untracked on 2026-10-27 (SCI D-006, D-007 precondition 3, D-010; mSCIdblit D-009, D-010):

1. Every file of 50 MB or more (22 paths: `gene_catalog.tsv`, `gene_crosswalk.tsv`,
   `mechanism_signaling_route_evidence.tsv.gz`, `source_records.tsv` in eleven release
   directories). All 22 are mirrored and verified on Biowulf. Five current copies stay on
   the laptop as ignored working files (the v1_11 release bundle's three and the
   2026-10-02 v2 crosswalk's two); the 17 superseded copies were deleted locally.
2. The 388 superseded `mechanism_graph_module20_24_v2026_*` snapshots (35.9 GB). They
   were deleted without a mirror: they are regenerable from the database and the curation
   registers. Only `..._v2026_09_25_literature_expansion627` (the snapshot the v1_11
   release and the README name) stays tracked.

Also mirrored (not deleted): the ignored local inputs under `data/raw/evidence/`,
`data/raw/public_database_snapshots/`, `data/processed/module20_24_database_intake_v1/`
and the untracked `work/` tree.

## One setting

`MSCIDBLIT_DATA_ROOT` (read by `scripts/mscidblit_paths.py`) names a directory laid out
like this `data/`; default is this checkout's `data/`. `resolve("processed/<...>")`
returns the local file when present, otherwise the same path under the root. On Biowulf:

```
export MSCIDBLIT_DATA_ROOT=/data/derea/SCI-data/mSCIdblit/data
```

Tests that open a superseded snapshot (`tests/test_mechanism_literature_expansion.py`,
`tests/test_downstream_curation_queue.py`) skip when it is absent and honour the setting.

## Biowulf layout, manifest, checksums

```
/data/derea/SCI-data/mSCIdblit/
  data/processed/<release dir>/...   the 22 large files, intake inputs
  data/raw/...                       ignored evidence and database snapshots
  work/                              working tree snapshot of 2026-10-27
  checksums/mscidblit-local-data-20261027.sha256
```

`data/MANIFEST.tsv` lists every `data/processed` entry with size, file count, git status,
role, producer, policy reference and, for mirrored items, Biowulf path, request id,
checksum file and verification record. `data/checksums/` holds the sha256 list. Ledgers
and the pre-move inventory: `~/Documents/SCI/agent-memory/SCI/phase3-*.tsv` and
`data-inventory-2026-10-27.tsv`; history-only large blobs:
`retired-inputs-history-only-2026-10-27.tsv`.

To work from a restored subset, point the setting at it, e.g.
`export MSCIDBLIT_DATA_ROOT=~/SCI-cache/mSCIdblit/data`. Small files come back with `bw get`; 1 GB or more through Globus into
`~/Globus/NIH-HPC/incoming/<request_id>/`. Working subsets live under
`~/SCI-cache/mSCIdblit/`, not in this tree.
