# mSCIdblit release v1.9.328

Release ID: `module20_24_mechanism_graph:2026-09-25-all-ligand-route-promotion-queue-547`

This release applies the IL1-style evidence-route representation to the next
all-ligand promotion tranche. It adds 928 source-linked literature-expansion
records covering 62 ligands, including IFN-gamma, IL-6, IL-12/IL-23, IL-13,
IL-22, IL-31, IL-3, IL-4, IL-5, CXCL12, interferon-lambda forms, IL-34, TNF,
VIP, CSF1, IL-20, IL-24, IL-36A, IL-18, IL-15, IL-21, HGF, BMP9/GDF2, PGE2,
APRIL, BAFF, WNT5A, GM-CSF and other source-supported ligands.

The tranche contains 648 records with a transcription-factor layer, 916 with
a target-gene layer, and 409 with an explicit intracellular-continuation
layer. The remaining records preserve the supported ligand, receptor, output,
TF, or target layers while retaining unresolved handoffs explicitly. The
records are evidence-layer annotations for mSCS; they do not create graph
edges, causal assertions, or confidence scores.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 591,826 -> 592,754
- Literature-expansion rows: 25,712 -> 26,640
- Full-sequence curation candidates: 15,112 -> 15,117
- Unique ligands in the curation queue: 1,862 (unchanged)
- P1 review candidates: 9,302 -> 9,306

Role-aware coverage remains 150 full target-gene ligands, 110 full
functional-output ligands, 1,545 partial downstream ligands, and 808
ligand-receptor-only ligands. These are evidence-layer summaries, not
confidence scores or causal traversal permissions.

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion547/`
- `scripts/build_all_ligand_full_sequence_promotion_batch.py`
