# mSCIdblit release v1.9.325

Release ID: `module20_24_mechanism_graph:2026-09-25-thrombin-tgfb1-queue-539`

This release adds three primary-literature evidence routes across two
additional ligand contexts: thrombin→PAR1→ERK→Elk-1→EGR1,
TGFβ1→TGFBR1/2→ERK→Elk-1→EGR1, and thrombin→PAR1→ERK→CXCL8/IL-8
functional output. The routes retain explicit missing-link flags and remain
evidence-only; no graph edges, causal assertions, or confidence scores are
created.

Primary support includes thrombin-induced ERK/Elk-1/EGR1 signaling in
fibroblasts (PMID:19432968), thrombin-induced EGR1/MEK-ERK responses in
primary endothelial cells (PMID:12393577), thrombin/PAR1/ERK-dependent IL-8
secretion in primary dermal fibroblasts (PMID:16697690), and
TGFβ-induced MEK-ERK/Elk-1-dependent EGR1 transcription in fibroblasts
(PMID:18772333).

The final bundle contains 591,822 signaling route-evidence rows and 25,708
literature-expansion rows. The graph remains unchanged at 11,988 nodes,
14,831 graph edges, and 15,107 edge-source records. The full-sequence
curation queue contains 15,109 candidates across 1,862 ligands, including
9,302 P1 review candidates.

Role-aware coverage is now 147 full target-gene ligands, 110 full
functional-output ligands, 1,548 partial downstream ligands, and 808
ligand–receptor-only ligands. These are evidence-layer summaries, not
confidence scores or causal traversal permissions.

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion539/`
- `scripts/build_primary_thrombin_tgfb1_routes.py`
