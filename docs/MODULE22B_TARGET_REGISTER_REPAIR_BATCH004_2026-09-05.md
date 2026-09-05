# Module 22B target-register repair batch 004 — 2026-09-05

This batch repairs five malformed rows created by recent standalone target
context additions. Four edge rows had one extra TSV field, which shifted their
species/injury/confidence/export values. The linked evidence records already
support the intended assessments: FOXP3→GPR83 and RELA→DPP4 are medium-high
regulatory-support contexts, while POU2F1→FPR2 and SP1→FPR2 are high direct
promoter-target contexts. The upstream NPY/RELA/FPR2 handoffs remain separate
and no SCI activation is inferred.

One RUNX3→ITGAL evidence row was missing its citation-note field. The missing
field was restored from the row's existing hold-review provenance; its
confidence, evidence layer, and exportability were not changed.

Audit ledger:
`work/module22b_tf_regulon_promotion_audit/module22b_target_register_repair_batch004.tsv`

Canonical SQL materialization is unchanged.
