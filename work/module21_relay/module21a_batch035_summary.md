# Module 21A batch 035 review summary

## Scope

Reviewed the requested 25 exact priority-8 queue rows and wrote one row per exact pair to `module21a_batch035_review.tsv`.

The local queue contains 26 numeric IDs in the inclusive range `M20A-CELLCHAT-REMAINING-0180` through `-0205` because `-0204` is `Areg Egfr`. That pair was not present in the supplied pair list, so it was excluded to preserve the requested 25-row output. The adrenergic labels `Adra2b`, `Adra2c`, and `Adrb1` are queued locally at `-0177` through `-0179`, outside the requested start ID, and were not included in this batch.

Module20A files, the frozen LR manifest, and shared Module21A registers were not modified.

## Classification

- Exact rows written: 25
- `reviewed_relay_candidate`: 9
- `reviewed_function_only`: 4
- `reviewed_binding_only`: 3
- `reviewed_unresolved`: 9
- Direct terminal TF assignments: 3 rows (`NR3C2`, `SMAD1/5/8`, `AR`)

Promoted receptor-proximal relays include ADR–ADRB2/3, AGT–AT1B, AMH–AMHR2/ACVR1, androstenedione–AR, ANXA1–FPR2, APELA–APLNR, and beta-endorphin–OPRD1. Aldosterone–NR3C2 is retained as a nuclear-receptor relay with NR3C2 itself as the directly activated TF node. ApoA1–CUBAM, APOB–APOBR, APOE–TREM2/TYROBP, and APP–SORL1 are retained as distinct receptor-complex or endocytic functional outputs rather than kinase relays.

## Boundaries and unresolved cases

- PNMT/CYP17A1/HSD17B6 and SLC18A2 are processing or transport components; they were not treated as direct intracellular signaling nodes.
- Family-level FPR2/ALX evidence was not transferred to Fpr-rs3/4/6/7 or FPR3. LXA4–FPR2 signaling was not reassigned to the ANXA1–FPR2_LXA4 composite row.
- ApoA1/ApoA2/ApoB binding to TREM2 was kept separate from ligand-specific TYROBP/SYK relay claims because the retrieved primary assays were binding screens without matching downstream perturbations.
- TREM2 evidence for A-beta, an APP cleavage product, was not used as evidence for full-length APP–TREM2 binding.
- Androsterone–NR1H4, aldosterone–NR3C1, and the exact FPR family rows remain unresolved after exact-pair searches across PubMed/PMC, publisher pages, and pathway context.

## Search boundaries

Searches covered exact gene symbols, receptor-complex notation, ligand synonyms, PubMed/PMC, publisher pages, and pathway context. Primary studies were retained when they directly measured receptor binding, second messengers, receptor-complex function, uptake, perturbation, or cellular output. Reviews and noncognate comparator studies were used only to define limitations and search boundaries. No direct terminal TF was assigned from pathway diagrams or functional association alone.

## File

- `module21a_batch035_review.tsv`
