# mSCIdblit release v1.9.327

Release ID: `module20_24_mechanism_graph:2026-09-25-lpa-creb-egr1-queue-545`

This release adds a primary-literature LPA route:
LPA→LPAR1/EDG2→ERK/JNK→CREB→EGR1. Primary vascular smooth-muscle studies
report LPA1- and PKCδ-dependent ERK/JNK signaling, CREB and SRF binding at
the EGR1 promoter, and CREB-dependent LPA-induced EGR1 transcription
(PMID:16497989; PMID:22577133).

The route remains an evidence-layer annotation with explicit missing-link
flags. No graph edges, causal assertions, or confidence scores are created.

The final bundle contains 591,826 signaling route-evidence rows and 25,712
literature-expansion rows. The graph remains unchanged at 11,988 nodes,
14,831 graph edges, and 15,107 edge-source records. The full-sequence
curation queue contains 15,112 candidates across 1,862 ligands, including
9,302 P1 review candidates.

Role-aware coverage is now 150 full target-gene ligands, 110 full
functional-output ligands, 1,545 partial downstream ligands, and 808
ligand–receptor-only ligands. These are evidence-layer summaries, not
confidence scores or causal traversal permissions.

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion545/`
- `scripts/build_primary_lpa_creb_egr1_route.py`
