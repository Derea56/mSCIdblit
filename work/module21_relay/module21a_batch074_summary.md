# Module 21A batch 074 review summary

## Scope and ordinal note

This batch follows the explicit review-ID range `M20A-CELLCHAT-REMAINING-1243` through `M20A-CELLCHAT-REMAINING-1281`, one row per ID (39 rows). In the current full external-review queue these are physical rows 1243–1281; the request’s “queue rows 1151–1175” ordinal does not correspond to those IDs. The explicit IDs and the named H2-T3/T9 through IGFBP3 families were treated as authoritative, and the mismatch is recorded here for audit.

## Disposition

- 25 `reviewed_relay_candidate`
- 1 `reviewed_binding_only`
- 4 `reviewed_function_only`
- 9 `reviewed_unresolved`
- 0 terminal-TF promotions for the H2, H60, HB-EGF, histamine, IAPP, ICAM, or IGFBP3 rows
- IFNA1/2/4/5/6/7 and IFNL2/3 rows retain canonical STAT1/STAT2/IRF9 handoff annotations only where subtype/receptor evidence supports a relay-level assignment.

## Main additions

- H60a/b/c were supported as mouse NKG2D/KLRK1 ligands. H60a/b/c were linked to the HCST/DAP10 receptor-complex relay with explicit limitations around murine NKG2D isoform/adaptor use. Primary support included PMID 18209064, PMID 19342629, PMID 20432238, PMID 10426994, and PMID 16582911.
- HB-EGF was promoted separately for EGFR and ErbB4. Binding, receptor phosphorylation, PI3K/ERK relay, and chemotaxis/wound-healing outputs were kept distinct (PMID 9135143, PMID 12621152, PMID 21640162).
- Histamine was promoted separately for HRH1–HRH4. The rows retain subtype-specific G-protein/second-messenger branches rather than a generic histamine pathway (PMID 1680603, PMID 6208354, PMID 8961278, PMID 12626656, PMID 17627982, PMCID PMC4706928).
- IAPP was promoted for CALCR-RAMP1 and CALCR-RAMP3, while CALCR-RAMP2 remained binding-only because subtype-specific activation is variable. CALCRL-RAMP1/2/3 were left unresolved because those complexes are the CGRP/adrenomedullin branches, not the canonical CALCR amylin receptor branch (PMID 10623626, PMID 10871296, PMID 18599553, PMID 40828907).
- ICAM1/2 were promoted only for complete beta2-integrin complexes. ICAM1–ITGAL alone was left unresolved because ITGB2 is required for LFA-1; ICAM5–CD209A/F were left unresolved because the primary evidence supports ICAM5–LFA-1 and CD209-family binding to other ICAMs, not these exact pairs.
- Human IFNA1/2/4/5/6/7 rows were promoted at relay level using subtype-specific receptor competition/functional panels plus IFNAR mechanistic studies. Murine IFNA12/13/14/15 were retained as function-only because exact species-matched receptor-binding/proximal assays were not found. IFNL2/3 were promoted for the complete IFNLR1-IL10RB complex (PMID 12483210).
- IGFBP3-TMEM219 was promoted as a direct receptor/function relay in beta-cell models, with colocalization/immunoprecipitation, ecto-receptor blockade, caspase-8, apoptosis, and insulin-secretion evidence (PMID 35115561; PMCID PMC8813914).

## Unresolved boundaries

- H2-T3 evidence is specific to CD8alpha-alpha; no CD8B1 or H2-T9 exact edge was promoted.
- CALCRL-RAMP complexes were not conflated with CALCR-RAMP amylin receptors.
- ITGAL-only and ITGAM-only rows were not treated as complete beta2 integrin receptors.
- No terminal TF was inferred from generic NK-cell, GPCR, integrin, growth-factor, or IGFBP3 functional outputs. IFN terminal-TF annotations are limited to the canonical receptor relay and carry subtype/species caveats in the TSV.

## Validation and files

The TSV validates as 39 rows, 13 columns, unique review IDs, exact ID/pair agreement with the queue, and no missing required evidence fields. No shared registers, Module20A ledgers, frozen manifest, or integration outputs were modified.

Files written:

- `work/module21_relay/module21a_batch074_review.tsv`
- `work/module21_relay/module21a_batch074_summary.md`
